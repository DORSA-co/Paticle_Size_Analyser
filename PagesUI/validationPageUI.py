from __future__ import annotations  #for hint class befor defined


from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from PagesUI.dialogWindows.samplesDialogUI import samplesDialogUI
from backend.Utils.datetimeUtils import datetimeFormat


class validationPageUI:

    def __init__(self, ui) -> None:
        self.statisticalHypothesisTab = statisticalHypothesisTab(ui)
        self.calibrationTab = calibrationTabUI(ui)


class calibrationTabUI:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.check_btn = self.ui.calibrationpage_check_btn
        self.start_calib_btn = self.ui.calibrationpage_calib_btn
        self.calib_type_combobox = self.ui.calibrationpage_calib_type_combobox
        self.calib_itrs_spinbox = self.ui.calibrationpage_calib_itrs_spinbox
        self.liveimage_lbl = self.ui.calibrationpage_liveimage_lbl
        self.calib_tabel = self.ui.calibrationpage_last_calib_tabel
        self.new_acc_lbl = self.ui.calibrationpage_new_acc_lbl
        self.old_acc_lbl = self.ui.calibrationpage_prev_acc_lbl
        self.result_box = self.ui.calibrationpage_result_groupbox

        self.tabel_headers = ['date', 'time', 'accuracy (mm)', 'type', 'iterations']
        
        GUIBackend.set_table_dim(self.calib_tabel, 1, len(self.tabel_headers))
        GUIBackend.set_table_cheaders(self.calib_tabel, self.tabel_headers)
        self.show_calib_result(False)

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

    def write_calib_result(self, old_acc, new_acc):
        """show calibration results

        Args:
            old_acc (_type_): accuracy defor calibration
            new_acc (_type_): accuracy after calibration
        """
        old_acc = str( old_acc ) + " mm"
        new_acc = str( new_acc ) + " mm"

        GUIBackend.set_label_text(self.new_acc_lbl, new_acc)
        GUIBackend.set_label_text(self.old_acc_lbl, old_acc)

        #show result
        self.show_calib_result(True)
    
    def show_calib_result(self, status:bool):
        """show and hide result box
        """
        GUIBackend.set_wgt_visible(self.result_box, status)

    
    def show_live(self,img):
        pass









class statisticalHypothesisTab:
    
    
    MAX_TEST_COUNT = 10
    
    def __init__(self, ui) -> None:
        self.ui = ui
        self.sampleLoader = samplesDialogUI(button_name='load')

        self.standards_combobox = self.ui.validationpage_hypotest_standards_combobox
        self.test_count_spinbox = self.ui.validationpage_hypotest_test_count_spinbox
        self.calculate_button = self.ui.validationpage_hypotest_calculate_btn
        self.sections_layout = self.ui.validationpage_hypotest_sections_layout

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


    def get_test_count(self, ) -> int:
        """returns test count from corspond spinbox

        Returns:
            int: number of test that user determind
        """
        return GUIBackend.get_input_spinbox_value(self.test_count_spinbox)
    

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
        




#-----------------------------------------------------------------------------------------------
class testSectionUI:
    sample_section_path = 'uiFiles\\untitled.ui'
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

        self.table_inputs = []
        self.table_rows_header = ['Dorsa-PSA', 'Sieve']

        GUIBackend.set_table_dim(self.table, row=2, col=None)
        #setup row headers. this setup is fix
        for row, text in enumerate(self.table_rows_header):
            GUIBackend.set_table_cell_value(self.table,(row,0), text )
            GUIBackend.set_table_cell_color( self.table,(row,0), color=(255,255,255), bg_color=(90, 117, 127))
    

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
        


    def set_visibility(self, status:bool):
        """if True, section whould be visible in UI

        Args:
            status (bool): _description_
        """
        GUIBackend.set_wgt_visible(self.wgt_ui, status)

    
    def append_to_layout(self, layout):
        GUIBackend.add_widget(layout, self.wgt_ui)
        