import cv2
import os
from matplotlib import pyplot as plt

from PagesUI.reportPageUI import reportPageUI
from backend.Processing.Report import Report
from backend.Processing.Particel import Particle
from Database.reportsDB import reportFileHandler
from Database.mainDatabase  import mainDatabase
from backend.Rebuild.rebuidReport import RebuildReport
from backend.Exporter.excelExporter import reportExcelExporter
from Constants import CONSTANTS


class reportPageAPI:
    PARTICLE_PER_PAGE = 48
    PARTICLE_PAGE_COL = 8
    assert PARTICLE_PER_PAGE % PARTICLE_PAGE_COL==0, "Particle Row count should be int"

    def __init__(self, uiHandeler:reportPageUI, database:mainDatabase):
        self.uiHandeler = uiHandeler
        self.database = database

        self.external_back_event_func = None
        self.draw_mode = 'none'
        self.current_particle_idx = -1
        
        self.startup()
        self.uiHandeler.back_button_connector(self.back)
        self.uiHandeler.rebuild_button_connector(self.show_rebuild)
        self.uiHandeler.rebuildDialog.button_connector('rebuild', self.run_rebuild)
        self.uiHandeler.navigator_button_connector(self.particles_navigation)
        self.uiHandeler.particle_click_connector(self.particle_select_event)
        self.uiHandeler.export_button_connector(self.export)
        self.uiHandeler.draw_buttons_connector(self.change_draw_mode)
        

    def startup(self,):
        self.particle_idx = 0
        self.img_id = -1
        self.particles_page = 0
        self.uiHandeler.startup()

    def set_back_event_func(self,func):
        "connect an external function to back button click event"
        self.external_back_event_func = func

    def show_rebuild(self,):
        standards_name = self.database.standards_db.load_standards_name()
        self.uiHandeler.rebuildDialog.set_standards_items(standards_name)
        self.uiHandeler.rebuildDialog.set_current_standard(self.report.standard['name'])
        self.uiHandeler.rebuildDialog.set_grading_parm_items(list(CONSTANTS.Sample.GRADING_PARMS.keys()))
        self.uiHandeler.rebuildDialog.set_current_grading_parm(self.report.grading_parm)
        self.uiHandeler.rebuildDialog.show()

    def run_rebuild(self,):
        """rebuild curent report into new standard
        """
        rebuild_settings = self.uiHandeler.rebuildDialog.get_settings()
        new_standard = self.database.standards_db.load(rebuild_settings['standard_name'])
        name_id = self.report.generate_uniq_id()
        report_record = self.database.reports_db.load_by_name_ids( [name_id] )[0]
        new_report_record, new_report = RebuildReport.rebuild(report_record, 
                                                              self.report, 
                                                              new_standard= new_standard,
                                                              grading_parm= rebuild_settings['grading_parm']

                                                              )
        
        rfh = reportFileHandler(report_record)
        self.database.reports_db.update(new_report_record)
        rfh.save_report(new_report)
        self.set_report(new_report)
        self.uiHandeler.rebuildDialog.go_to_finish()
        #self.uiHandeler.show_confirm_box('result', 'Rebuild Success', ['ok'])
        



    def set_report(self, report:Report):
        """set a report and show it

        Args:
            report (Report): _description_
        """
        self.startup()
        self.report = report
        self.report.Buffer.total_buffer.sort(reverse=True)
        self.particles_count = self.report.get_particles_count()
        self.particle_maximum_page = (self.particles_count // self.PARTICLE_PER_PAGE)
        
        
        args = {'path':self.report.main_path, 'name':self.report.name, 'date':self.report.date, 'time':self.report.time}
        self.report_file_handler = reportFileHandler(args)
        
        self.show_general_information()
        self.show_ranges_statistics()
        self.show_charts()
        self.refresh_particles_page()

        #------------------------------------------------------------
        #min_rs = self.report.Buffer.get_feature('avg_diameter')
        #max_rs = self.report.Buffer.get_feature('avg_diameter')
        #plt.scatter(min_rs, max_rs)
        #plt.show()
    

    
    
    

    def set_master_page(self, page_name:str):
        """set master page

        Args:
            page_name (str): the page name that report page calls from it
        """
        self.master_page = page_name
        

    
    def show_general_information(self,):
        info = {}
        info['name'] = self.report.name
        info['standard'] = self.report.standard['name']
        info['date'] = self.report.date_time.strftime("%Y/%m/%d")
        info['time'] = self.report.date_time.strftime("%H:%M")
        info['username'] = self.report.username
        info['description'] = self.report.description

        statictics =  self.report.get_global_statistics()
        for key, value in statictics.items():
            info[key] = str(value)

        self.uiHandeler.set_general_information(info)

    

    def show_ranges_statistics(self,):
        data = self.report.get_ranges_statistics()
        self.uiHandeler.set_ranges_statistics_tabel(data)


    def show_charts(self,):
        self.uiHandeler.set_grading_chart( values=self.report.Grading.get_hist(), 
                                  ranges= self.report.ranges_string)
        
        self.uiHandeler.set_cumulative_chart_value( *self.report.cumGrading.get_data())

        self.uiHandeler.set_gaussian_chart_value(*self.report.get_gaussian_data(step=0.1))
        

    def back(self, ):
        """this function call when back button clicked
        """
        if self.external_back_event_func is not None:
            self.external_back_event_func(self.master_page)



    def particles_navigation(self, key):
        if key == 'next':
            self.particles_page +=1

        elif key == 'prev':
            self.particles_page -= 1

        self.particles_page = max(0, self.particles_page)
        self.particles_page = min(self.particles_page, self.particle_maximum_page)
        self.refresh_particles_page()

    def refresh_particles_page(self, ):
        self.uiHandeler.handle_navigation_button_enabality(self.particles_page, 0, self.particle_maximum_page)
        self.uiHandeler.show_page_number(self.particles_page + 1, self.particle_maximum_page + 1)
        self.show_particels_img()


    def show_particels_img(self, ):
        imgs = []
        if self.report.settings['save_image']:

            for particle in self.report.Buffer.total_buffer.get_particels()[self.particles_page * self.PARTICLE_PER_PAGE:
                                                               (self.particles_page + 1) * self.PARTICLE_PER_PAGE]:
                p_id = particle.get_id()
                img = self.report_file_handler.load_image(p_id)
                imgs.append(img)

        self.uiHandeler.set_particles_image(imgs,ncol=self.PARTICLE_PAGE_COL, nrow=int(self.PARTICLE_PER_PAGE/self.PARTICLE_PAGE_COL))

    
    def particle_select_event(self, idx:int):
        """this function called when user click on a particle

        Args:
            idx (_type_): a number that shows which particle in table clicked
        """
        idx = self.particles_page * self.PARTICLE_PER_PAGE + idx
        self.current_particle_idx = idx
        self.show_particle_information(self.current_particle_idx)


    def show_particle_information(self, idx:int):
        if idx<0:
            self.uiHandeler.reset_particle_section()
            return
        
        particle = self.report.Buffer.total_buffer.get_particel(idx)
        info = particle.get_info()
        self.uiHandeler.set_particle_information(info)
        #------------------------------------------------
        
        #check if particle is in a diffrent image, load it
        if self.img_id != particle.img_id:
            p_id = particle.get_id()
            particle_img = self.report_file_handler.load_image(p_id)
            
        
        particle_img = self.drawing_on_particle(particle, particle_img)
        self.uiHandeler.set_particle_image(particle_img)
        #------------------------------------------------
        
    def change_draw_mode(self,mode):
        self.draw_mode = mode
        self.show_particle_information(self.current_particle_idx)

    def drawing_on_particle(self, particle:Particle, particle_img):
        if particle_img is None:
            return None
        
        particle_img = cv2.cvtColor(particle_img, cv2.COLOR_GRAY2BGR)

        if self.draw_mode == 'circle':
            center, radius = particle.get_enclosing_circle(transorm_to_single_img=True)
            particle_img = cv2.circle(particle_img, center,radius+2, color=(10,182,235), thickness=2)
        
        elif self.draw_mode == 'cnt':
            cnt = particle.get_contour(transorm_to_single_img=True)
            particle_img = cv2.drawContours(particle_img, [cnt] , 0, color=(209,231,75), thickness=2 )
            
        return particle_img
    

    def export(self,):
        try:
            path = self.database.setting_db.export_db.load()['report_excel']
            if not os.path.exists(path):
                self.uiHandeler.show_confirm_box('Error', 
                                         "Excel format file doesn't exist. Go to setting>>export and set an excel format for report",
                                         buttons=['ok']
                                         )
                return
            
            exporter = reportExcelExporter(path)
            path,_ = self.uiHandeler.open_export_file_dialog()
            if path == '':
                return
            
            wrong_codes = exporter.render(self.report)
            flag,e = exporter.save(path)

            self.uiHandeler.exportDialog.set_wrong_codes(wrong_codes)

            if flag:
                self.uiHandeler.exportDialog.set_massage('Export successfuly')
                self.uiHandeler.exportDialog.set_exception_msg(None)

            else:
                self.uiHandeler.exportDialog.set_massage('Failed to export')
                self.uiHandeler.exportDialog.set_exception_msg(e)
            self.uiHandeler.exportDialog.show()

        except Exception as e:
            self.uiHandeler.exportDialog.set_massage('Some Error Happend')
            self.uiHandeler.exportDialog.set_exception_msg(e)
            self.uiHandeler.exportDialog.show()                


