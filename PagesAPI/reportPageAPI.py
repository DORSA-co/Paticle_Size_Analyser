from PagesUI.reportPageUI import reportPageUI
from backend.Processing.Report import Report
from Database.reportsDB import reportFileHandler
import cv2
class reportPageAPI:
    
    def __init__(self, ui:reportPageUI):
        self.ui = ui

        self.ui.back_button_connector(self.back)
        self.ui.navigator_button_connector(self.particle_navigation)
        self.external_back_event_func = None
        self.particle_idx = 0
        self.img_id = None
        

    
    def particle_navigation(self, key):
        if key == 'next':
            self.particle_idx+=1

        elif key == 'prev':
            self.particle_idx-=1

        self.particle_idx = max(0, self.particle_idx)
        self.particle_idx = min(self.particles_count, self.particle_idx)

        self.show_particle_information()

    
    def show_particle_information(self,):
        particle = self.report.Buffer.get_particel(self.particle_idx)
        info = particle.get_info()
        self.ui.set_particle_information(info)
        #------------------------------------------------
        (x1,y1), (x2,y2) = particle.get_roi(20)
        
        #check if particle is in a diffrent image, load it
        if self.img_id != particle.img_id:
            self.img_id = particle.img_id
            self.img = self.report_file_handler.load_image(self.img_id)
        
        particle_img = self.img[y1:y2, x1:x2]
        self.ui.set_particle_image(particle_img)
        #------------------------------------------------


        
        
        
        

    def set_back_event_func(self,func):
        "connect an external function to back button click event"
        self.external_back_event_func = func
        
    def set_report(self, report:Report):
        """set a report and show it

        Args:
            report (Report): _description_
        """
        self.report = report
        self.report.render()
        self.particles_count = len(self.report.Buffer.particels)
        self.report_file_handler = reportFileHandler(self.report.main_path,
                                                     self.report.name,
                                                     self.report.date)
        
        self.show_general_information()
        self.show_ranges_statistics()
        self.show_charts()
        self.show_particle_information()

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
        info['date'] = self.report.date.strftime("%Y/%m/%d")
        info['time'] = self.report.date.strftime("%H:%M")
        info['username'] = self.report.username

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

    def back(self, ):
        """this function call when back button clicked
        """
        if self.external_back_event_func is not None:
            self.external_back_event_func(self.master_page)
