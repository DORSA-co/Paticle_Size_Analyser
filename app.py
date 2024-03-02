from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import sys
import os

#----------------------Compile Resource File-----------------------
#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc uiFiles/Assets/Assets.qrc -o uiFiles/Assets/Assets.py')#PySide
os.system('CMD /C pyside6-uic uiFiles/main_UI.ui -o uiFiles/main_UI_ui.py')
os.environ['PYSIDE_DESIGNER_PLUGINS'] = "."
sys.path.append('uiFiles//Assets')
#----------------------Add Lib Files to path-----------------------
from uiFiles.Assets import Assets

from appUI import mainUI
from appAPI import main_API
from Constants import CONSTANTS


main_ui_file = 'uiFiles/main_UI.ui'
login_ui_file = 'uiFiles/login.ui'
sample_info_ui_file = 'uiFiles/sample_info.ui'
edit_user_ui_file = 'uiFiles/edit_user.ui'
db_init_ui_file = 'uiFiles/db_init.ui'



if __name__ == '__main__':
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    
    screen = app.screens()[0]
    CONSTANTS.screen.H = screen.virtualSize().height()
    CONSTANTS.screen.W = screen.virtualSize().width()
    
    #load .ui files
    login_ui = loader.load(login_ui_file, None)
    edit_user = loader.load(edit_user_ui_file, None)
    db_init_ui = loader.load(db_init_ui_file, None)

    main_ui = mainUI( 
                     login_ui,
                     edit_user,
                     db_init_ui)

    
    api = main_API(main_ui)
    app.exec()

  
    