import os
import sys
sys.path.append( os.getcwd() + "/uiUtils" )
from guiBackend import GUIBackend



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
