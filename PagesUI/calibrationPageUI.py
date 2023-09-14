from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents

class validationPageUI:

    def __init__(self, ui) -> None:
        self.statisticalHypothesisTab = statisticalHypothesisTab(ui)



class calibrationPageUI:

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
    sample_section_path = 'uiFiles\\untitled.ui'
    MAX_TEST_COUNT = 10
    def __init__(self, ui) -> None:
        self.ui = ui

        self.standards_combobox = self.ui.validationpage_hypotest_standards_combobox
        self.test_count_spinbox = self.ui.validationpage_hypotest_test_count_spinbox
        self.calculate_button = self.ui.validationpage_hypotest_calculate_btn

        self.samples_test_section =[]
        for i in range(self.MAX_TEST_COUNT): 
            self.samples_test_section.append(
                        GUIBackend.load_ui(self.sample_section_path)
                        )
            
            GUIBackend.add_widget(self.ui.verticalLayout_50, self.samples_test_section[i] )

        self.init_tests_tables()
    


    def set_standards_list(self, standards_name:list[str]):
        GUIBackend.set_combobox_items(standards_name)


    def get_setting(self, ) -> dict:
        res = {}
        res['test_count'] = GUIBackend.get_input_spinbox_value(self.test_count_spinbox)
        res['standard'] = GUIBackend.get_combobox_selected(self.standards_combobox)
        return res
    
    def calculate_button_connector(self, func):
        GUIBackend.button_connector(self.calculate_button, func)

        
    def init_tests_tables(self,):
        n = 5
        standard_ranges = [[0,6], [6,8], [8,10],[10,12],[12,14]]

        standard_ranges_str = list(map( lambda x: f'{x[0]}mm - {x[1]}mm', standard_ranges ))
        table_headers = ['-'] + standard_ranges_str

        self.show_test_sections(n)
        for i in range(n):
            table = self.samples_test_section[i].table
            
            GUIBackend.set_table_dim(table, row=2, col=len(table_headers))
            GUIBackend.set_table_cheaders(table, table_headers)

            for col in range(1, len(table_headers)):
                inpt = GUIComponents.doubleSpinBoxTable()
                GUIBackend.set_table_cell_widget( table, (1, col), inpt, layout=True )

            
            for row, text in enumerate( ['dorsa PSA', 'alak']):
                GUIBackend.set_table_cell_value(table,(row,0), text )
                GUIBackend.set_table_cell_color( table,(row,0), color=(255,255,255), bg_color=(90, 117, 127))


    def show_test_sections(self,n:int):
        """show only fist n'th test section in UI

        Args:
            n (_type_): number of test section to show
        """
        for i in range(self.MAX_TEST_COUNT):
            visiblity = False
            if i<n:
                visiblity = True
            GUIBackend.set_wgt_visible(self.samples_test_section[i], visiblity)
        
