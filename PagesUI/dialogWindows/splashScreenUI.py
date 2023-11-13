from PySide6.QtWidgets import QSplashScreen
from uiUtils.guiBackend import GUIBackend
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore

class loadingSplashScreen(QSplashScreen):
    ui_path = 'uiFiles\\splash_ui.ui'

    def __init__(self,):
        #super(loadingSplashScreen, self).__init__()
        self.ui = GUIBackend.load_ui(self.ui_path)
        GUIBackend.set_win_frameless(self.ui)
        self.ui.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.SplashScreen))
        
        
        
        #self.progress_bar

        #self.set_progressbar(0)
    
    def set_progressbar(self, x):
        x = int(x)
        GUIBackend.set_progressbar_value(self.ui.progress_bar,x)