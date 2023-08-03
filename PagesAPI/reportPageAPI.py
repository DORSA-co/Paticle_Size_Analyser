from PagesUI.reportPageUI import reportPageUI
from backend.Processing.Report import Report


class reportPageAPI:
    
    def __init__(self, ui:reportPageUI):
        self.ui = ui

        self.ui.back_button_connector(self.back)
        self.external_back_event_func = None
    

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
        
        self.show_general_information()
        self.show_ranges_statistics()
        self.show_charts()

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
