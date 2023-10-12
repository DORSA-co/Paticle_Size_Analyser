from PagesUI.reportPageUI import reportPageUI
from backend.Processing.Report import Report
from Database.reportsDB import reportFileHandler
from Database.mainDatabase  import mainDatabase
from backend.Rebuild.rebuidReport import RebuildReport

import cv2
class reportPageAPI:
    PARTICLE_PER_PAGE = 48
    PARTICLE_PAGE_COL = 8
    assert PARTICLE_PER_PAGE % PARTICLE_PAGE_COL==0, "Particle Row count should be int"

    def __init__(self, ui:reportPageUI, database:mainDatabase):
        self.ui = ui
        self.database = database
        
        

        self.external_back_event_func = None
        self.particle_idx = 0
        self.img_id = -1
        self.particles_page = 0

        self.ui.back_button_connector(self.back)
        self.ui.rebuild_button_connector(self.show_rebuild)
        self.ui.dialog_rebuild_button_connector(self.run_rebuild)
        self.ui.navigator_button_connector(self.particles_navigation)
        self.ui.particle_click_connector(self.show_particle_information)

    def set_back_event_func(self,func):
        "connect an external function to back button click event"
        self.external_back_event_func = func

    def show_rebuild(self,):
        standards_name = self.database.standards_db.load_standards_name()
        self.ui.set_rebuild_standards(standards_name)
        self.ui.set_rebuild_current_standard(self.report.standard['name'])
        self.ui.show_rebuild_win()

    def run_rebuild(self,):
        """rebuild curent report into new standard
        """
        new_standard_name = self.ui.get_rebuild_standard()
        new_standard = self.database.standards_db.load(new_standard_name)
        name_id = self.report.generate_uniq_id()
        report_record = self.database.reports_db.load_by_name_ids( [name_id] )[0]
        new_report_record, new_report = RebuildReport.rebuild(report_record, self.report, new_standard)
        
        rfh = reportFileHandler(report_record)
        self.database.reports_db.update(new_report_record)
        rfh.save_report(new_report)
        self.set_report(new_report)
        self.ui.close_rebuild_win()
        



    def set_report(self, report:Report):
        """set a report and show it

        Args:
            report (Report): _description_
        """
        self.report = report
        self.report.render()
        self.particles_count = self.report.get_particles_count()
        self.particle_maximum_page = (self.particles_count // self.PARTICLE_PER_PAGE)
        
        
        args = {'path':self.report.main_path, 'name':self.report.name, 'date':self.report.date, 'time':self.report.time}
        self.report_file_handler = reportFileHandler(args)
        
        self.show_general_information()
        self.show_ranges_statistics()
        self.show_charts()
        self.refresh_particles_page()
        self.set_description()
    
    

    
    
    

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

        self.ui.set_general_information(info)

    

    def show_ranges_statistics(self,):
        data = self.report.get_ranges_statistics()
        self.ui.set_ranges_statistics_tabel(data)


    def show_charts(self,):
        self.ui.set_grading_chart( values=self.report.Grading.get_hist(), 
                                  ranges= self.report.ranges_string)
        
        self.ui.set_cumulative_chart_value( *self.report.cumGrading.get_data())

        self.ui.set_gaussian_chart_value(*self.report.get_gaussian_data())
        

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
        self.ui.handle_navigation_button_enabality(self.particles_page, 0, self.particle_maximum_page)
        self.ui.show_page_number(self.particles_page + 1, self.particle_maximum_page + 1)
        self.show_particels_img()


    def show_particels_img(self, ):
        imgs = []
        if self.report.settings['save_image']:

            for particle in self.report.Buffer.get_particels()[self.particles_page * self.PARTICLE_PER_PAGE:
                                                               (self.particles_page + 1) * self.PARTICLE_PER_PAGE]:
                p_id = particle.get_id()
                img = self.report_file_handler.load_image(p_id)
                imgs.append(img)

        self.ui.set_particles_image(imgs,ncol=self.PARTICLE_PAGE_COL, nrow=int(self.PARTICLE_PER_PAGE/self.PARTICLE_PAGE_COL))

    
    def show_particle_information(self, idx:int):
        """this function called when user click on a particle

        Args:
            idx (_type_): a number that shows which particle in table clicked
        """
        idx = self.particles_page * self.PARTICLE_PER_PAGE + idx
        particle = self.report.Buffer.get_particel(idx)
        info = particle.get_info()
        self.ui.set_particle_information(info)
        #------------------------------------------------
        
        #check if particle is in a diffrent image, load it
        if self.img_id != particle.img_id:
            p_id = particle.get_id()
            particle_img = self.report_file_handler.load_image(p_id)
        
        self.ui.set_particle_image(particle_img)
        #------------------------------------------------
        
    def set_description(self, ):
        p1, p2 = reportDescriptions.get_statistic_desc()
        self.ui.set_description('statictics',0, p1)
        self.ui.set_description('statictics',1, p2)
        
        # p = """<p> testttttt</p>"""
        # self.ui.ui.textEdit.setHtml(p)





class reportDescriptions:
    
    @staticmethod
    def get_statistic_desc():
        p1 = ""
        p2 = ""
        
        return p1.replace('\n', ''), p2.replace('\n', '')
