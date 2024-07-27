from __future__ import annotations  #for hint class befor defined
import numpy as np

from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from PagesUI.dialogWindows.samplesDialogUI import samplesDialogUI
from backend.Utils.datetimeUtils import datetimeFormat
from PagesUI.PageUI import commonUI
from PagesUI.dialogWindows.verficationResultDialogUI import verficationResultDialogUI
from uiUtils.IO.Mouse import mouseHandeler
from Constants import CONSTANTS


class validationPageUI:

    def __init__(self, ui) -> None:
        self.statisticalHypothesisTab = statisticalHypothesisTab(ui)
        self.calibrationTab = calibrationTabUI(ui)


class calibrationTabUI(commonUI):

    def __init__(self, ui) -> None:
        
        self.ui = ui
        self.mouseHandeler = mouseHandeler()


        self.check_btn = self.ui.calibrationpage_check_btn
        self.start_calib_btn = self.ui.calibrationpage_calib_btn
        self.calib_type_combobox = self.ui.calibrationpage_calib_type_combobox
        self.calib_itrs_spinbox = self.ui.calibrationpage_calib_itrs_spinbox
        self.liveimage_lbl = self.ui.calibrationpage_liveimage_lbl
        self.calib_tabel = self.ui.calibrationpage_last_calib_tabel
        self.result_box = self.ui.calibrationpage_result_groupbox
        self.progress_bar = self.ui.calibrationpage_process_progressbar
        self.check_message_lbl = self.ui.calibrationpage_check_lbl

        self.result = {
            'accuracy' : self.ui.calibrationpage_accuracy_lbl,
            'precision' : self.ui.calibrationpage_precision_lbl
        }


        self.tabel_headers = ['date', 'time', 'accuracy (mm)', 'type', 'iterations']

        self.image_mouse_evnt_func = None
        
        GUIBackend.set_table_dim(self.calib_tabel, 1, len(self.tabel_headers))
        GUIBackend.set_table_cheaders(self.calib_tabel, self.tabel_headers)
        self.show_calib_result(None)

        #--------------------------------------------------------------------
        #SHOULD CHANGE FOR DEVELOPING
        
        # GUIBackend.set_wgt_visible(self.progress_bar, False)
        #GUIBackend.set_wgt_visible(self.ui.calibration_step2_frame, False)
        #GUIBackend.set_wgt_visible(self.ui.calibration_step1_frame, False)
        GUIBackend.set_wgt_visible(self.ui.calibrationpage_last_calib_tabel, False)
        #--------------------------------------------------------------------

    def startup(self,):
        GUIBackend.set_label_image(self.liveimage_lbl, CONSTANTS.IMAGES.NO_IMAGE)
        self.set_progress_bar(0)
        self.write_check_massage(None)

    def set_progress_bar(self, i):
        GUIBackend.set_progressbar_value(self.progress_bar, i)

    
    
    # def set_passed_step(self, step):
    #     if step == 'none':
    #         GUIBackend.set_enable(self.check_btn, True)
    #         GUIBackend.set_enable(self.start_calib_btn, False )
    

    def connect_image_mouse_event(self, func):
        self.image_mouse_evnt_func = func
        
    def write_check_massage(self, massage:str, status:bool=True):
        if massage is None:
            GUIBackend.set_wgt_visible(self.check_message_lbl, False )
        else:

            GUIBackend.set_label_text(self.check_message_lbl, massage)
            if status:
                GUIBackend.set_style(self.check_message_lbl, "background-color:rgb(58, 209, 154); color:#ffffff;")
            else:
                GUIBackend.set_style(self.check_message_lbl, "background-color:rgb(255, 95, 84); color:#ffffff;")
            
            GUIBackend.set_wgt_visible(self.check_message_lbl, True )
            

        
        

    def check_button_connector(self, func):
        """Connect a function into check button clicled
        """
        GUIBackend.button_connector(self.check_btn, func)

    def start_button_connector(self, func):
        """Connect a function into start button clicled
        """
        GUIBackend.button_connector(self.start_calib_btn, func)

    def get_settings(self,)-> dict:
        """returns calibration settings

        Returns:
            dict: {'type': xxxx, 'iterations':n}
        """
        settings = {}
        settings['type'] = GUIBackend.get_combobox_selected(self.calib_type_combobox)
        settings['iterations'] = GUIBackend.get_input_spinbox_value(self.calib_itrs_spinbox)
        return settings
    
    def set_calib_tabel(self, datas):
        GUIBackend.set_table_row(self.calib_tabel, 0, datas)

    # def write_calib_result(self, old_acc, new_acc):
    #     """show calibration results

    #     Args:
    #         old_acc (_type_): accuracy defor calibration
    #         new_acc (_type_): accuracy after calibration
    #     """
    #     old_acc = str( old_acc ) + " mm"
    #     new_acc = str( new_acc ) + " mm"

    #     GUIBackend.set_label_text(self.new_acc_lbl, new_acc)
    #     GUIBackend.set_label_text(self.old_acc_lbl, old_acc)

    #     #show result
    #     self.show_calib_result(None)
    
    def show_calib_result(self, result:dict):
        """show and hide result box
        """
        if result is None:
            GUIBackend.set_wgt_visible(self.result_box, False)
        else:
            for key , value in result.items():
                GUIBackend.set_label_text( self.result[key], str(value))

            GUIBackend.set_wgt_visible(self.result_box, True)
        

    
    def show_live(self,img):
        pixmap = GUIBackend.set_label_image(self.liveimage_lbl, img)
        GUIBackend.fit_label_to_pixmap(self.liveimage_lbl, pixmap)
        self.mouseHandeler.connect_all(self.liveimage_lbl, self.image_mouse_evnt_func)









class statisticalHypothesisTab(commonUI):
    
    
    MAX_TEST_COUNT = 10
    
    
    def __init__(self, ui) -> None:
        super(statisticalHypothesisTab, self).__init__()

        self.ui = ui
        self.sampleLoader = samplesDialogUI(button_name='load')
        self.resultDialog = verficationResultDialogUI()

        self.standards_combobox = self.ui.validationpage_hypotest_standards_combobox
        self.test_count_spinbox = self.ui.validationpage_hypotest_test_count_spinbox
        self.calculate_button = self.ui.validationpage_hypotest_calculate_btn
        self.sections_layout = self.ui.validationpage_hypotest_sections_layout
        self.verification_type_combobox = self.ui.validationpage_verify_type

        self.test_sections =[]
        for i in range(self.MAX_TEST_COUNT):
            self.test_sections.append(testSectionUI(i))
            self.test_sections[i].append_to_layout(self.sections_layout)
            

        
        GUIBackend.spinbox_connector(self.test_count_spinbox, self.test_count_event)

        self.show_test_sections(0)

    
    def test_count_event(self,):
        n = self.get_test_count()
        self.show_test_sections(n)

    
    def get_test_section(self, idx:int)-> testSectionUI:
        """returns (test section) object idx'th in the list

        Args:
            idx (int): section index

        Returns:
            testSectionUI: 
        """
        return self.test_sections[idx]



    def set_standards_list(self, standards_name:list[str]):
        GUIBackend.set_combobox_items(self.standards_combobox, standards_name)

    def get_selected_standard(self) -> str:
        return GUIBackend.get_combobox_selected(self.standards_combobox)

    def get_test_count(self, ) -> int:
        """returns test count from corspond spinbox

        Returns:
            int: number of test that user determind
        """
        return GUIBackend.get_input_spinbox_value(self.test_count_spinbox)
    
    def set_verification_type_items(self, types:list[str]):
        GUIBackend.set_combobox_items(self.verification_type_combobox,
                                      types 
        )
    
    def get_verfication_type(self)-> str:
        return GUIBackend.get_combobox_selected(self.verification_type_combobox).lower()

    def calculate_button_connector(self, func):
        GUIBackend.button_connector(self.calculate_button, func)


    def show_test_sections(self,n:int):
        """show only fist n'th test section in UI

        Args:
            n (_type_): number of test section to show
        """
        for i in range(self.MAX_TEST_COUNT):
            if i<n:
                self.test_sections[i].set_visibility(True)
            else:

                self.test_sections[i].set_visibility(False)
                self.test_sections[i].clear()
        

    def get_sieve_inputs(self) -> list[np.ndarray]:
        sieve_percents = []
        n = self.get_test_count()
        for i in range(n):
            test_section = self.get_test_section(i)
            percents = test_section.get_sieve_percents()
            sieve_percents.append(percents)
        return sieve_percents


#-----------------------------------------------------------------------------------------------
class testSectionUI:
    sample_section_path = 'uiFiles\\test.ui'
    def __init__(self, idx) -> None:
    
        self.wgt_ui = GUIBackend.load_ui(self.sample_section_path)
        self.idx = idx
        
        self.sample_infoes = {
            'name': self.wgt_ui.sample_name_lbl,
            'date': self.wgt_ui.sample_date_lbl,
            'time': self.wgt_ui.sample_time_lbl
        }
        self.load_btn = self.wgt_ui.load_btn
        self.table = self.wgt_ui.table
        self.error_lbl = self.wgt_ui.error_lbl
        self.warning_lamp = self.wgt_ui.warning_lamp
        self.sum_percents_lbl = self.wgt_ui.sum_percents_lbl

        self.table_inputs = []
        self.table_rows_header = ['Dorsa-PSA', 'Sieve']

        GUIBackend.set_table_dim(self.table, row=2, col=None)
        #setup row headers. this setup is fix
        for row, text in enumerate(self.table_rows_header):
            GUIBackend.set_table_cell_value(self.table,(row,0), text )
            # GUIBackend.set_table_cell_color( self.table,(row,0), color=(255,255,255), bg_color=(90, 117, 127))

        self.write_error(None)

    def load_button_connector(self, func):
        GUIBackend.button_connector_argument_pass(self.load_btn,
                                                      func, (self.idx,))

    
    def set_sample_info(self, sample:dict):
        """shows sample information in specific test section

        Args:
            section_idx (int): index of test section
            sample (dict): sample infoes
        """
        if not isinstance(sample['date'], str):
            sample['date'] = datetimeFormat.date_to_str(sample['date'])
        
        if not isinstance(sample['time'], str):
            sample['time'] = datetimeFormat.time_to_str(sample['time'])
        
        for name, obj in self.sample_infoes.items():
            GUIBackend.set_label_text( obj, sample.get(name, '') )

    
    def setup_table(self, standard_ranges:list[list]):
        """setup Primary setting of table base on standard_ranges

        Args:
            standard_ranges (_type_): standard ranges
        """
        #conver standard range into string formant
        standard_ranges_str = list(map( lambda x: f'{x[0]}mm - {x[1]}mm', standard_ranges ))
        #first column is for headers of rows
        self.table_headers = ['-'] + standard_ranges_str

        #set table column corespond to ranges count
        GUIBackend.set_table_dim(self.table, row=None, col=len(self.table_headers))
        GUIBackend.set_table_cheaders(self.table, self.table_headers)
        GUIBackend.set_cell_width_content_adjust(self.table, None)

        #append input filelds in columns of range in table
        self.table_inputs.clear()
        for col in range(1, len(self.table_headers)):
            inpt = GUIComponents.doubleSpinBoxTable()
            
            GUIBackend.input_text_connector(inpt, self.__percent_inputs_event__)
            GUIBackend.set_table_cell_widget( self.table, (1, col), inpt, layout=True )
            self.table_inputs.append(inpt)

            GUIBackend.set_table_cell_value( self.table, (0, col), '' )


    
    def set_grading_result(self, hist:list[float]):
        """shows sample grading result into table

        Args:
            hist (list[float]): sample grading result
        """
        for i, value in enumerate(hist):
            value = str(value) + ' %'
            GUIBackend.set_table_cell_value(self.table, (0, i+1) , value  )

    
    def clear(self,):
        """clear section info
        """
        self.set_sample_info({'name':'-','date':'-','time':'-'})
        GUIBackend.set_table_dim(self.table, row=2, col=1)
        

        

    def set_sample(self, sample:dict, standard_range:list[list]):
        """setup table corespond to standard and set sample information
          into table and information section

        Args:
            sample (dict): sample information dict. it can be also sample database record
            standard_range (list[list]): list of range
        """
        self.setup_table( standard_range )
        self.set_sample_info(sample)
        self.set_grading_result(sample['grading_result'])

    def write_error(self, txt: str):
        if txt is None:
            GUIBackend.set_wgt_visible(self.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.error_lbl, True)
            GUIBackend.set_label_text(self.error_lbl, txt)
        


    def set_visibility(self, status:bool):
        """if True, section whould be visible in UI

        Args:
            status (bool): _description_
        """
        GUIBackend.set_wgt_visible(self.wgt_ui, status)

    
    def append_to_layout(self, layout):
        GUIBackend.add_widget(layout, self.wgt_ui)
    
    def __percent_inputs_event__(self,):
        res = self.get_sieve_percents()
        percents_sum =  np.round(res.sum(),2)
        GUIBackend.set_label_text(self.sum_percents_lbl, f'{percents_sum} %')
        if percents_sum == 100:
            GUIBackend.set_style(self.warning_lamp, 'background-color:rgb(58, 209, 154);') #green color
    
        else:
            GUIBackend.set_style(self.warning_lamp, 'background-color:rgb(197, 63, 59);') #red color
            

    def get_sieve_percents(self,):
        res = []
        for inpt in self.table_inputs:
            value = GUIBackend.get_input(inpt)
            res.append(value)

        return np.array(res)