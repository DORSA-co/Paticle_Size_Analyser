from appUI import mainUI
from appAPI import main_API
from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import sys
import os

#----------------------Compile Resource File-----------------------
#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc uiFiles/Assets/Assets.qrc -o uiFiles/Assets/Assets.py')#PySide
os.environ['PYSIDE_DESIGNER_PLUGINS'] = "."
#----------------------Add Lib Files to path-----------------------
from uiFiles.Assets import Assets

main_ui_file = 'uiFiles/main_UI.ui'
login_ui_file = 'uiFiles/login.ui'
sample_info_ui_file = 'uiFiles/sample_info.ui'
edit_user_ui_file = 'uiFiles/edit_user.ui'
auto_rebuild_ui_file = 'uiFiles/rebuild.ui'
single_rebuild_manual_ui_file = 'uiFiles/single_rebuild_manual.ui'
db_init_ui_file = 'uiFiles/db_init.ui'


if __name__ == '__main__':
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    #load .ui files
    window = loader.load(main_ui_file, None)
    login_ui = loader.load(login_ui_file, None)
    sample_info = loader.load(sample_info_ui_file, None)
    edit_user = loader.load(edit_user_ui_file, None)
    auto_rebuild_ui = loader.load(auto_rebuild_ui_file, None)
    single_rebuild_manual_ui = loader.load(single_rebuild_manual_ui_file, None)
    db_init_ui = loader.load(db_init_ui_file, None)

    main_ui = mainUI(window, login_ui,
                             sample_info,
                             edit_user,
                             auto_rebuild_ui,
                             single_rebuild_manual_ui,
                             db_init_ui)

    
    api = main_API(main_ui)
    #main_ui.usersPage.loginUserBox.show_login()
   
    #window.showMaximized()
    app.exec()

  
    