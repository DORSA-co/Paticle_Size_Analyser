import os
import typing
#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc Assets.qrc -o Assets.py')#PySide
#from PyQt5 import uic
from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import sys
import webbrowser
from functools import partial
import texts
import Assets
#from PySide6.QtChart import QChart, QChartView, QBarSet,QPercentBarSeries
import time
from Charts.BarChart import BarChart
import GUIComponents
import cv2
main_ui_file = 'main_UI.ui'

class GlobalUI():
    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_
    """

    def __init__(self, ui):
        """this function is used to laod ui file and build GUI application
        """
        
        self.ui = ui




        
        # app language
        self.language = 'en'

        # load ui file
        #uic.loadUi(main_ui_file, self)



        self.ui.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        #
        self._old_pos = None
        self.app_close_flag = False

        webbrowser
        # chrome_path_win = "C://Program Files//Google//Chrome//Application//chrome.exe"
        # chrome_path_linux = '/usr/bin/google-chrome %s'
        # if sys.platform.startswith('win'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_win))
        # elif sys.platform.startswith('linux'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_linux))

        # button connector

        self.pages_index = {
            'main'       : 0,
            'report'     : 1,
            'settings'   : 2,
            'calibration': 3,
            'user'       : 4,
            'help'       : 5
        }

        
        self.sidebar_buttons = {
            'main': self.ui.sidebar_main_btn,
            'report': self.ui.sidebar_report_btn,
            'settings': self.ui.sidebar_settings_btn,
            'calibration': self.ui.sidebar_calib_btn,
            'user': self.ui.sidebar_users_btn,
            'help': self.ui.sidebar_help_btn,
        }


        self.header_button_connector()
        self.sidebar_button_connector()

        # startup settings
        self.startup_settings()

        

    

        
    #-------------------------------------------------------------------------------------------


    def startup_settings(self):
        """this function is used to do startup settings on app start
        """
        return

    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        GUIBackend.button_connector( self.ui.minimize_btn, self.minimize_win )
        GUIBackend.button_connector( self.ui.maximize_btn, self.maxmize_minimize )
        GUIBackend.button_connector( self.ui.close_btn, self.close_app )
        # bottom window buttens
        #self.dorsa_url_btn.clicked.connect(partial(lambda: webbrowser.open("https://dorsa-co.ir/")))
        return
    

    def sidebar_button_connector(self):
        for page_name in self.sidebar_buttons.keys():
            GUIBackend.button_connector( self.sidebar_buttons[page_name], self.sidebar_menu_handler(page_name) )
        

        
        
        

    def sidebar_menu_handler(self, pagename):
        def func():
            GUIBackend.set_stack_widget_idx( self.ui.main_pages_stackw, self.pages_index[pagename] )
            for btn in self.sidebar_buttons.values():
                btn.setStyleSheet(GUIComponents.SIDEBAR_BUTTON_STYLE)
            
            self.sidebar_buttons[pagename].setStyleSheet(GUIComponents.SIDEBAR_BUTTON_SELECTED_STYLE)
        return func
    

    def close_app(self):
        """
        this function closes the app
        Inputs: None
        Returns: None
        """
        # create message to confirm close
        res = self.show_alert_window(title=texts.TITLES['close_app'][self.language], message=texts.WARNINGS['app_close_confirm'][self.language], need_confirm=True, level=1)

        if res:
            self.app_close_flag = True

            # close app window and exit the program
            self.ui.close()
            sys.exit()

    def maxmize_minimize(self):
        """
        this function chages the window size of app
        Inputs: None
        Returns: None
        """
        if self.ui.isMaximized():
            self.ui.showNormal()

        else:
            self.ui.showMaximized()

    def minimize_win(self):
        """
        this function minimizes the app to taskbar
        Inputs: None
        Returns: None
        """
        self.ui.showMinimized()
    
    def show_alert_window(self, title, message, need_confirm=False, level=0):
        """this function is used to create a confirm window
        :param title: _description_, defaults to 'Message'
        :type title: str, optional
        :param message: _description_, defaults to 'Message'
        :type message: str, optional
        :return: _description_
        :rtype: _type_
        """

        level = 0 if level<0 or level>2 else level

        # create message box
        alert_window = QtWidgets.QMessageBox()

        # icon
        if level==0:
            alert_window.setIcon(QtWidgets.QMessageBox.Information)
        elif level==1:
            alert_window.setIcon(QtWidgets.QMessageBox.Warning)
        elif level==2:
            alert_window.setIcon(QtWidgets.QMessageBox.Critical)

        # message and title
        alert_window.setText(message)
        alert_window.setWindowTitle(title)
        # buttons
        if not need_confirm:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText(texts.TITLES['ok'][self.language])
        else:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText(texts.TITLES['confirm'][self.language])
            alert_window.button(QtWidgets.QMessageBox.Cancel).setText(texts.TITLES['cancel'][self.language])
        
        alert_window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        # show
        returnValue = alert_window.exec()

        if not need_confirm:
            return True if returnValue == QtWidgets.QMessageBox.Ok else True
        else:
            return True if returnValue == QtWidgets.QMessageBox.Ok else False


    # def mousePressEvent(self, event):
    #     """mouse press event for moving window

    #     :param event: _description_
    #     """

    #     # accept event only on top and side bars and on top bar
    #     if event.button() == QtCore.Qt.LeftButton and not self.isMaximized() and event.pos().y()<=self.header.height():
    #         self._old_pos = event.globalPos()


    # def mouseReleaseEvent(self, event):
    #     """mouse release event for stop moving window

    #     :param event: _description_
    #     """

    #     if event.button() == QtCore.Qt.LeftButton:
    #         self._old_pos = None


    # def mouseMoveEvent(self, event):
    #     """mouse move event for moving window

    #     :param event: _description_
    #     """

    #     if self._old_pos is None:
    #         return

    #     delta = QtCore.QPoint(event.globalPos() - self._old_pos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self._old_pos = event.globalPos()


    
class GUIBackend:


    #----------------------------------------------------------------
    @staticmethod
    def is_spinbox(wgt):
        """check an object is spinBox or Not
        """
        return isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox)

    #----------------------------------------------------------------
    @staticmethod
    def set_wgt_visible( wgt:QtWidgets.QWidget, status:bool):
        """changes visibility of a given Qt widget

        Args:
            wgt (QtWidgets.QWidget): a Qt widget like QPushButton
            status (bool): True of visible and False for hide
        """
        wgt.setVisible(status)

    

    @staticmethod
    def set_disable( wdgt: QtWidgets ):
        """disables a PyQt widget

        Args:
            wdgt (QtWidgets): PyQt widget object
        """
        wdgt.setDisabled(True)


    @staticmethod
    def set_enable( wdgt: QtWidgets ):
        """enables a PyQt widget

        Args:
            wdgt (QtWidgets): PyQt widget object
        """
        wdgt.setDisabled(False)

    
    @staticmethod
    def set_disable_enable( wdgt: QtWidgets, status ):
        """enable or disables a PyQt widget

        Args:
            wdgt (QtWidgets): PyQt widget object
            status: enable if True, and disable if False 
        """
        wdgt.setDisabled(status)


    def add_widget( parent:QtWidgets.QLayout, widget):
        """insert a new widget into parent widget

        Args:
            parent (QtWidgets.QLayout): parent widget that is a QLayout
            widget (_type_): Qt widget that you want insert into parent
        """
        parent.addWidget(widget)

    @staticmethod
    def set_style( btn: QtWidgets.QPushButton, style:str):
        """set style to an object

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            style (tuple): string Qt style sheet
        """
        btn.setStyleSheet(style)

    
    #--------------------------------- GLOBAL GET ALL INPUT TyPE ---------------------------------
    @staticmethod
    def get_input(wgt):
        """get value of all inputs widget like ComboBox, SpinBox and LineEdit

        Args:
            wgt (_type_): Qt input Widgt

        Returns:
            _type_: value of input
        """
        if isinstance(wgt, QtWidgets.QComboBox):
            return GUIBackend.get_combobox_selected(wgt)
        
        if isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox):
            return GUIBackend.get_input_spinbox_value(wgt)
        
        if isinstance(wgt, QtWidgets.QLineEdit):
            return GUIBackend.get_input_text(wgt)
    


    @staticmethod
    def set_input(wgt, value):
        """set value to a input widget in any type like ComboBox, SpinBox and LineEdit

        Args:
            wgt (_type_): Qt input Widgt
            value (_type_): input value to set


        """
        if isinstance(wgt, QtWidgets.QComboBox):
            return GUIBackend.set_combobox_current_item(wgt, value)
        
        if isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox):
            return GUIBackend.set_spinbox_value(wgt, value)
        
        if isinstance(wgt, QtWidgets.QLineEdit):
            return GUIBackend.set_input_text(wgt, value)



    #--------------------------------- GLOBAL BUTTON FUNCTIONs ---------------------------------
    @staticmethod
    def button_connector( btn: QtWidgets.QPushButton, func):
        """Connects a PyQt Button clicked event into a function

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            func (_type_): function that execute when event happend
        """
        btn.clicked.connect(partial( func ))

    @staticmethod
    def button_disable( btn: QtWidgets.QPushButton ):
        """disables a PyQt Button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
        """
        btn.setDisabled(True)


    @staticmethod
    def button_enable( btn: QtWidgets.QPushButton ):
        """enables a PyQt Button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
        """
        btn.setDisabled(False)

    @staticmethod
    def button_background( btn: QtWidgets.QPushButton, color):
        """changes background color of button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            color (tuple): color of background in format of 'rgb' or 'rgba'
        """
        #convert rgb to rgba
        if len(color) == 3:
            color+= (255,)

        btn.setStyleSheet(f'background-color: rgba{color}')


    @staticmethod
    def set_button_icon( btn: QtWidgets.QPushButton, path):
        """sets icon of PyQt button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            path (_type_): path of icon's file or url of recource's icon
        """
        #load from resources
        if path[0] == ':':
            icon = QtGui.QIcon( path )
        
        #load from file
        else:
            pixmap = QtGui.QPixmap(path)
            icon = QtGui.QIcon( pixmap )
        
        btn.setIcon(icon)
    
    #--------------------------------- GLOBAL ComboBox FUNCTIONs ---------------------------------
    @staticmethod
    def get_combobox_selected( combo: QtWidgets.QComboBox)->str :
        """returns curent combobox text

        Args:
            combo (QtWidgets.QComboBox): Qt comboBox object

        Returns:
            str: current text
        """
        return combo.currentText()
    
    @staticmethod
    def set_combobox_items(combo: QtWidgets.QComboBox, items:list[str]):
        """clear and set items into combobox

        Args:
            combo (QtWidgets.QComboBox): Qt comboBox object
            items (list[str]): list of string items
        """
        combo.clear()
        combo.insertItems(0, items)

    @staticmethod
    def add_combobox_item( combo: QtWidgets.QComboBox, item: str):
        """add new item into combobox

        Args:
            combo (QtWidgets.QComboBox): Qt comboBox object
            item (str): string item
        """
        combo.insertItems(0, item)

    
    @staticmethod
    def set_combobox_current_item( combo: QtWidgets.QComboBox, item: str):
        """set cobobox selected item to a custom item

        Args:
            combo (QtWidgets.QComboBox): Qt comboBox object
            item (str): string item
        """
        combo.setCurrentText(item)

    #--------------------------------- GLOBAL CheckBox FUNCTIONs ---------------------------------
    @staticmethod
    def get_checkbox_value(chbox: QtWidgets.QCheckBox) -> bool:
        """returns state of Qt checkbox

        Args:
            chbox (QtWidgets.QCheckBox): Qt CheckBox object

        Returns:
            bool: return True if checked. else return False
        """
        return chbox.isChecked()
    
    @staticmethod
    def checkbox_connector(chbox: QtWidgets.QCheckBox, func):
        """connects a function to event of Qt checkbox change state

        Args:
            chbox (QtWidgets.QCheckBox): Qt CheckBox object
            func (_type_): name of funtion
        """
        chbox.stateChanged.connect(partial( func ))

    #--------------------------------- GLOBAL Label FUNCTIONs ---------------------------------
    @staticmethod
    def set_label_text(lbl: QtWidgets.QLabel, text:str):
        """sets a text into the given Qt Label

        Args:
            lbl (QtWidgets.QLabel): Qt label object
            text (str): text that you want show in label
        """
        lbl.setText(text)

    
    @staticmethod
    def set_label_image(lbl: QtWidgets.QLabel, image):
        qformat =QtGui.QImage.Format_Indexed8
        if len(image.shape)==3:
            if image.shape[2] ==4:
                qformat=QtGui.QImage.Format_RGBA8888
            else:
                qformat=QtGui.QImage.Format_RGB888
            img = QtGui.QImage(image.data,
                image.shape[1],
                image.shape[0], 
                image.strides[0], # <--- +++
                qformat)
            img = img.rgbSwapped()
            lbl.setPixmap(QtGui.QPixmap.fromImage(img))
            lbl.setAlignment(QtCore.Qt.AlignCenter)
    #--------------------------------- GLOBAL Input FUNCTIONs ---------------------------------
    @staticmethod
    def get_input_spinbox_value( inpt: QtWidgets.QSpinBox)-> float:
        """return value of a given spinbox

        Args:
            inpt (QtWidgets.QSpinBox): Qt spinbox object

        Returns:
            float: value of spinbox
        """
        return inpt.value()
    
    def set_spinbox_value(inpt: QtWidgets.QSpinBox, value):
        """set a value into spinbox

        Args:
            inpt (QtWidgets.QSpinBox): Qt spinbox object
            value (_type_): custom value
        """
        inpt.setValue(value)

    def spinbox_connector(inpt: QtWidgets.QSpinBox, func):
        """connect a function to change value event

        Args:
            inpt (QtWidgets.QSpinBox): Qt spinbox object
            func (): 
        """
        inpt.valueChanged.connect(func)


    #--------------------------------- GLOBAL QLine edit FUNCTIONs ---------------------------------    
    def get_input_text(inpt:QtWidgets.QLineEdit)-> str:
        """returns text of an input box

        Args:
            inpt (QtWidgets.QLineEdit): Qt Line edit object

        Returns:
            str: text of input
        """
        return inpt.text()

    def set_input_text(inpt:QtWidgets.QLineEdit, txt:str):
        """returns text of an input box

        Args:
            inpt (QtWidgets.QLineEdit): Qt Line edit object
            txt (str): 

        """
        inpt.setText(txt)

    #--------------------------------- GLOBAL table FUNCTIONs ---------------------------------
    @staticmethod
    def set_table_dim(table: QtWidgets.QTableWidget, row:int , col:int):
        """sets number of column and row of given Qt table
        if pass 'None' into row or col, it dosen't changed

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            row (int): numbr fo row
            col (int): number of col
        """
        if col is not None:
            table.setColumnCount(col)
        
        if row is not None:
            table.setRowCount(row)

    
    def clear_table(table: QtWidgets.QTableWidget, clear_header=False):
        """_summary_

        Args:
            table (QtWidgets.QTableWidget): _description_
            clear_header (bool, optional): _description_. Defaults to False.
        """
        while (table.rowCount() > 0):
            table.removeRow(table.rowCount()-1);

    
    @staticmethod
    def add_table_row(table: QtWidgets.QTableWidget, row_position=None):
        """add a row in custom position into given Qt tabel

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            row_position (_type_, optional): position of new row. if None, row whould be added at the end. Defaults to None.
        """
        if not row_position:
            row_position = table.rowCount()
        table.insertRow(row_position)


    @staticmethod
    def set_table_cheaders(table: QtWidgets.QTableWidget, headers:list[str]):
        """sets headers of given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            headers (list[str]): list of headers. like headers = ['title1', 'title2',...]
        """
        table.setHorizontalHeaderLabels(headers)


    @staticmethod
    def set_table_cell_color(table: QtWidgets.QTableWidget, index:tuple, color=None, bg_color=None):
        """changes text color and background color of custom cell of a given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            index (tuple): position of cell (row_idx, col_idx)
            color (_type_, optional): color of text. if pass None, color doesn't change. Defaults to None.
            bg_color (_type_, optional): background color of cell. if pass None, color doesn't change. Defaults to None.
        """
        if bg_color is not None:
            table.item(*index).setBackground(QtGui.QColor(*bg_color))

        if color is not None:
            table.item(*index).setForeground(QtGui.QBrush(QtGui.QColor(*color)))
        
    @staticmethod
    def set_table_cell_widget(table: QtWidgets.QTableWidget, idx: tuple, widget):
        """insert a Qt widget (like QPushButton) into a custom cell of given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            idx (tuple): position of cell (row_idx, col_idx)
            widget (_type_): Qt widget that you want insert into cell of table
        """
        table.setCellWidget(*idx, widget)

    @staticmethod
    def set_table_cell_value(table: QtWidgets.QTableWidget,index:tuple, value):
        """sets a text or number into custom cell of given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            index (tuple): position of cell (row_idx, col_idx)
            value (_type_): a text or number  that you want set into cell of table
        """
        item = QtWidgets.QTableWidgetItem(str(value))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        table.setItem(*index, item )

    
    
    @staticmethod
    def set_table_row(table: QtWidgets.QTableWidget, row:int, values:list):
        """sets a row data into specific row of a given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            row (int): index of row that you want insert data into it
            values (list): list of text or number
        """
        for i,value in enumerate(values):
            GUIBackend.set_table_cell_value(table,(row,i), value)
    
    @staticmethod
    def set_table_datas(table: QtWidgets.QTableWidget, datas:list[list]):
        """sets given data into specific row of a given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            datas (list[list]): data of table. like [ ['ali','184'], ['hamid', '193']]
        """
        for row, row_datas in enumerate(datas):
            GUIBackend.set_table_row(table, row, row_datas)        



    #--------------------------------- GLOBAL StackWidget FUNCTIONs ---------------------------------
    @staticmethod
    def set_stack_widget_idx(stw: QtWidgets.QStackedWidget, idx ):
        """change current index of given Qt stack widget

        Args:
            stw (QtWidgets.QStackedWidget): Qt stack widget object
            idx (_type_): custom index to set as current index
        """
        stw.setCurrentIndex(idx)



class mainPage:
    
    def __init__(self, ui):
        self.ui = ui
        
        self.warning_btns = {
            'camera_connection': {
                'btn':self.ui.mainpage_camera_connection_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-connection-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-connection-red-50.png'
                },
            'camera_grabbing': {
                'btn': self.ui.mainpage_camera_grabbing_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-camera-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-camera-red-50.png'
                },

            'illumination': {
                'btn': self.ui.mainpage_illumination_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-headlight-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-headlight-red-50.png'
            },
                             
            'tempreture': {
                'btn': self.ui.mainpage_tempreture_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-thermometer-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-thermometer-red-50.png'
            }
        }
        
        self.informations = {
            'ovality': self.ui.mainpage_mean_oval_lbl,
            'avrage': self.ui.mainpage_avrage_lbl,
            'std': self.ui.mainpage_std_lbl,
            'fps': self.ui.mainpage_fps_lbl

        }

        self.player_btns = {
            'start': self.ui.mainpage_start_btn,
            'stop' : self.ui.mainpage_stop_btn,
            'fast_start': self.ui.mainpage_faststart_btn
        }


        self.grading_chart = BarChart(
                    chart_title = None,
                    chart_title_color = '#404040',
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = '#ffffff',
                    bar_color = '#4caf50',
                    axis_color = '#404040',
                    axis_grid=True,
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = True,
                    bar_width = 1,
                )
        
        categoris = ['a', 'b', 'c', 'd', 'e', 'f']
        values = [5, 10, 20, 40, 60, 80]
        self.grading_chart.update_chart(axisX_ranges=categoris, axisY_values=values)

        
        

        self.current_status = 'stop'
        self.statistics_table = self.ui.mainpage_statistics_table
        self.warning_msg_lbl = self.ui.mainpage_warning_massage_lbl
        
        GUIBackend.add_widget( self.ui.mainpage_grading_chart_frame, self.grading_chart )
        #GUIBackend.add_widget( self.ui.mainpage_second_chart_frame, self.second_chart )


        #Startup operations-----------------
        self.__player_buttons_connect_internal__()
        GUIBackend.set_wgt_visible(self.warning_msg_lbl, False)

        
        
        # self.ui.mainpage_right_frame.addWidget(self.chart1)



    
    def __player_buttons_status__(self,state:str):
        """manage enable and disable, player buttons in diffent state.
        THIS FUNCTION ONLY IS USED IN CLASS

        Args:
            state (str): state of playing. it could be one of 'start' , 'fast_start' and 'stop'
        """
        def func():

            if state in ['start', 'fast_start']:
                GUIBackend.button_disable(self.player_btns['start'])
                GUIBackend.button_disable(self.player_btns['fast_start'])
                GUIBackend.button_enable(self.player_btns['stop'])
                self.current_status = 'start'
            
            else:
                GUIBackend.button_enable(self.player_btns['start'])
                GUIBackend.button_enable(self.player_btns['fast_start'])
                GUIBackend.button_disable(self.player_btns['stop'])
                self.current_status = 'stop'
        return func
        

    def player_buttons_connect(self,name:str,  func):
        """connect click event of start or fast_start or stop button into a function

        Args:
            name (str): name of button. it could be one of the 'start', 'fast_start' and 'stop' 
            func (_type_): event function for click
        """
        GUIBackend.button_connector( self.player_btns[ name ], func)

    
    def __player_buttons_connect_internal__(self):
        """connect player buttons into player_buttons_status for manage enble and disable buttons
        THIS FUNCTION ONLY IS USED IN CLASS
        """
        for state, btn in self.player_btns.items():
            GUIBackend.button_connector(btn, self.__player_buttons_status__(state) )


    def set_warning_buttons_status(self, name: str, status: bool):
        """change situation of warning buttons and set them in ok (green) or warning (red) state

        Args:
            name (str): name of warning that could be one of ['camera_connection', 'camera_grabbing', 'illumination', 'tempreture']
            status (bool): 'True' for ok and 'False' for warning
        """
        assert name in self.warning_btns.keys(), f" {name} warning doesn't exist. it could be only ['camera_connection', 'camera_grabbing', 'illumination', 'tempreture']"
        if status:
            GUIBackend.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['ok-icon'])
        else:
            GUIBackend.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['warning-icon'])
            
    
    def report_btn_connector(self, func):
        """connect a function to clicked event of report button

        Args:
            func (_type_): function
        """
        GUIBackend.button_connector(self.ui.mainpage_stop_btn, func)

    def toolbox_connector(self, func):
        """connect a function to change event of toolbox checkboxes of main page

        Args:
            func (_type_): this function should be have one argumant. the value of this argument would be 'live-view' or 'drawing'.
        """
        GUIBackend.checkbox_connector(self.ui.mainpage_liveview_checkbox, func('live-view'))
        GUIBackend.checkbox_connector(self.ui.mainpage_drawing_checkbox, func('drawing'))
    

    def set_information(self, data:dict):
        """set data into information box of main page

        Args:
            data (dict): data is a dictionary that it keys are name of info and values are value of that infos.
            allowable are 'ovality', 'avrage', 'std', 'fps'
        """
        for name, value in data.items():
            GUIBackend.set_label_text( self.informations[name],
                                    str(value) 
                                    )
            
        self.set_statistics_table_datas()
    
    def set_statistics_table_datas(self, datas: list[list]):
        """set data into statistics table of mainpage. 

        Args:
            datas (list[list]): list of row list. first item in each row sould be name of row. 
            - for e.g [ ['avrage', 12, 13.5, ...], ['std', 0.5, 0.76, ...]]
        """
        cols_count = len(datas[0])
        #set cols count
        GUIBackend.set_table_dim(self.statistics_table, None, col=cols_count)
        #insert datas into table
        GUIBackend.set_table_datas(self.statistics_table, datas)

        #set first column ( row headers) color diffrence
        for row in range(len(datas)):
            GUIBackend.set_table_cell_color(self.statistics_table, (row,0), bg_color=(6, 76, 130), color=(255,255,255))

    def set_statistics_table_headers(self, headers:list[str]):
        """set heaaders of statistics table in mainpage. these are ranges of particles

        Args:
            headers (list[str]): list of headers like: [ '<6mm', '6mm-8mm' ,...]
        """
        #first columns should be empty for rows header
        headers = [''] + headers
        GUIBackend.set_table_cheaders(self.statistics_table, headers)

    def set_warning_massage(self, text):
        text = "Warning: " + text
        self.warning_msg_lbl.setText(text)
        GUIBackend.set_wgt_visible(self.warning_msg_lbl, True)
      
        # self.worker = timerThread()
        # self.thread = QThread()

        # #self.worker.progress.connect(self.update_progress)
        # #self.worker.completed.connect(self.complete)
        # self.worker.moveToThread(self.thread)
        # self.thread.started.connect(self.worker.wait('test', 5, 0.5))

        # self.thread.start()
        # print("DDDD")

        # self.thread = QThread()
        # # Step 3: Create a worker object
        # self.worker = timerThread()
        # self.worker.add('test')
        # # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # self.thread.started.connect(self.worker.wait)
        # self.worker.completed.connect(self.thread.quit)
        # self.worker.completed.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # # Step 6: Start the thread
        # self.thread.start()



class CalibrationPage:

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


class RegisterUserTab:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.register_error_lbl = self.ui.userspage_register_error_lbl
        self.register_btn = self.ui.userspage_add_user_btn

        self.register_users_field = {
            'username' : self.ui.userpage_username_inpt,
            'password' : self.ui.userpage_password_inpt,
            'password_confirm': self.ui.userpage_confirm_password_inpt,
            'role': self.ui.userpage_user_role_combobox
        }

    def register_button_connector(self, func):
        """connect function into register button clicked event
        """
        GUIBackend.button_connector(self.register_btn, func)
    
    def get_register_fields(self)-> dict:
        """returns register fields in dictionary type

        Returns:
            dict: infos in format {
            'username':xxxx,
            'password':xxxx,
            'password_confirm':xxxx,
            'role':xxxx,}
        """
        infos = {}
        for name, field in self.register_users_field.items():
            infos[name] = GUIBackend.get_input(field)
        return infos
    
    def write_register_error(self, txt:str):
        """Write Errors message in Register

        Args:
            txt (str): error message
        """
        GUIBackend.set_label_text(self.register_error_lbl, txt)



class AllUserTab:

    def __init__(self, ui) -> None:
        self.ui = ui
        self.users_table = self.ui.userpage_all_users_table
        self.__table_external_event_function__ = None

        self.users_table_headers = ['username', 'password', 'role', 'edit', 'delete']
        GUIBackend.set_table_dim(self.users_table, row=10, col=len(self.users_table_headers))
        GUIBackend.set_table_cheaders(self.users_table, self.users_table_headers)


    def table_external_event_connector(self, func):
        """connect edit and delete button of each record in users tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, user info dic, 'edit' or 'delete' flag, button )
        """
        self.__table_external_event_function__ = func
    
    def table_event_connector(self,idx, user_info, status, btn):
        """this function exec when edit or delete button clicked on defined ranges table

        Args:
            idx (_type_): row index that its button clicked
            user_info (_type_): user info dictionary in format {'username':****, 'password':****', 'role':****}
            status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
            btn (_type_): button object that clicked
        """
        def func():
            #
            # Write Internal Code Here
            #
            self.__table_external_event_function__(idx, user_info, status, btn)
        return func

    def set_users_table(self,users:list[dict]):
        """insert users info into table
        Args:
            datas (list[list]): list of users info
        """
        assert self.__table_external_event_function__ is not None, "ERROR: First determine an event Function for edit and delete button by 'AllUserTab.table_event_connector' method "
        
        #set row count
        users_count = len(users)
        GUIBackend.set_table_dim(self.users_table, row=users_count, col=None)
        info_count = len(users[0])

        for row, user in enumerate(users):
            for info_name in user.keys():
                col = self.users_table_headers.index(info_name)
                GUIBackend.set_table_cell_value(self.users_table, (row, col), value=user[info_name])

            #define edit and delete button
            edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()

            #connect buttons to event function 
            GUIBackend.button_connector( edit_btn, self.table_event_connector(row, user, 'edit',  edit_btn) )
            GUIBackend.button_connector( del_btn, self.table_event_connector(row, user, 'delete',  del_btn ) )

            #insert buttons into table
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count), edit_btn)
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count+1), del_btn)




class cameraSettingTab:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.devices_combobox = self.ui.settingpage_camera_device_combobox
        self.fps_spinbox = self.ui.settingpage_camera_fps_spinbox
        self.camera_start_btn = self.ui.settingpage_camera_start_btn
        self.save_btn = self.ui.settingpage_camera_save_btn
        self.restor_btn = self.ui.settingpage_camera_restore_btn
        self.__is_start__ = False
        self.__connection_event_function__ = None
        self.__change_setting_event_function__ = None


        
        self.settings = {
            #features that can't be changed in grabbing
            'width': self.ui.settingpage_camera_width_spinbox,
            'height': self.ui.settingpage_camera_height_spinbox,
            'gain': self.ui.settingpage_camera_gain_spinbox,
            'exposure': self.ui.settingpage_camera_exposure_spinbox
            }

        self.start_stop_icon = {
            True: ":/assets/Assets/icons/stop50.png",
            False: ":/assets/Assets/icons/play-48.png"
        }

        self.fields_enable_status = {
            True: ['gain', 'exposure'],
            False: ['width','height' ]
        }

        GUIBackend.button_connector(self.camera_start_btn, self.__internal_start_event__)
        self.__mange_fields_enable__()
        self.__settings_change_connector__()
    

    def start_stop_event_connector(self, func):
        """connect a function to start and stop button vlick event

        Args:
            func (_type_): a function with one argument that would be True in start and False in Stop
        """
        self.__connection_event_function__ = func

    def change_setting_event_connector(self, func):
        """connect a function to change setting event

        Args:
            func (_type_): a function with one argument that whould be a dictionary whit key setting name and its value
        """
        self.__change_setting_event_function__ = func

    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)

    def restor_button_connector(self, func):
        GUIBackend.button_connector(self.restor_btn, func)

    def __settings_change_connector__(self,):
        """connect all input fields of setting into an internal function
        """
        for key, field in self.settings.items():
            if GUIBackend.is_spinbox(field):
                GUIBackend.spinbox_connector(field, self.__internal_change_setting_event__(key))


    
    def __internal_change_setting_event__(self, setting_name):
        """got setting that changed and pass it to external function self.__change_setting_event_function__ as an event
        this function connected to change setting input fields and calledc automaticly

        Args:
            setting_name (_type_): name of setting that changed.
        """
        def func():
            #assert self.change_setting_event_connector is not None, "No Function Event determind. use cameraSettingTab.change_setting_event_connector method to do it"
            value = GUIBackend.get_input(self.settings[setting_name])
            arg = {setting_name:value}
            if self.__change_setting_event_function__ is not None:
                self.__change_setting_event_function__(arg)
        return func


    
    def __internal_start_event__(self,):
        """this function called when the start button clicked. this function calls manage disable and enable fields and call external function
        """
        #change flag. (True for grabbing)
        self.__is_start__ = not(self.__is_start__)
        #change button icon
        GUIBackend.set_button_icon(self.camera_start_btn, self.start_stop_icon[self.__is_start__])
        #enable and disable setting fields
        self.__mange_fields_enable__()
        #call exteral function as event
        if self.__connection_event_function__ is not None:
            self.__connection_event_function__(self.__is_start__)


    def __mange_fields_enable__(self):
        """mange which fields be enable when change start, stop
        """
        #enable fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[self.__is_start__]:
            GUIBackend.set_enable(self.settings[fields_name])

        #disable other fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[not(self.__is_start__)]:
            GUIBackend.set_disable(self.settings[fields_name])

        GUIBackend.set_disable_enable( self.devices_combobox, self.__is_start__ )

    
    def set_camera_devices(self, devices:list):
        """set camera divices comboBox items

        Args:
            devices (list): list of camera devices
        """
        GUIBackend.set_combobox_items(self.devices_combobox, devices)


    def get_camera_device(self,):
        """returns camera diveces that selected in combobox
        """
        return GUIBackend.get_combobox_selected(self.devices_combobox)
    
    
    def get_fps(self):
        return GUIBackend.get_input_spinbox_value(self.fps_spinbox)
    
    def get_settings(self)-> dict:
        """return settings in dictionary format

        Returns:
            dict: a dictionary like {'gain': 50 ,...}
        """
        res = {}
        for sname, sfield in self.settings.items():
            res[sname] = GUIBackend.get_input(sfield)
        
        return res

    def set_settings(self, settings:dict):
        """set defualt values to input's fields of settings

        Args:
            settings (dict): settings paramaeters. this is a dictionary like {'gain': 50 ,...}
        """
        for key , value in settings.items():
            GUIBackend.set_input( self.settings[key], value )



        

class gradingSettingTab:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.ranges_input = {
            'lower': self.ui.settingpage_grading_low_limit_spinbox,
            'upper': self.ui.settingpage_grading_up_limit_spinbox
        }

        self.ranges_table = self.ui.settingpage_grading_ranges_table
        self.standards_table = self.ui.settingpage_grading_standards_table
        self.range_name_input = self.ui.settingpage_grading_name_inpt
        self.ranges_table_event_function = None


        self.ranges_table_headers = ['no', 'low (mm)', 'high (mm)', 'edit', 'delete']
        GUIBackend.set_table_dim(self.ranges_table, 1 , len(self.ranges_table_headers))
        GUIBackend.set_table_cheaders(self.ranges_table, headers=self.ranges_table_headers)
        GUIBackend.button_connector(self.ui.settingpage_grading_cancel_btn, self.__clear_settings__)


    def __clear_settings__(self):
        #clear 
        for wdgt in self.ranges_input.values():
            GUIBackend.set_spinbox_value(wdgt, 0)

        GUIBackend.set_input_text(self.range_name_input,"")
        #clear tabel
        GUIBackend.clear_table( self.ranges_table )
        #insert an empty row for better ui
        GUIBackend.set_table_dim(self.ranges_table, 1 , len(self.ranges_table_headers))
    

    def add_range_button_connector(self, func):
        """connect add new range button into a function

        Args:
            func (_type_): clicked event function
        """
        data = {}
        for key in self.ranges_input.keys():
            data[key] = self.ui.get_input_spinbox_value( 
                self.ranges_input[key]
             )
        
        GUIBackend.button_connector( self.ui.settingpage_grading_add_range_btn, func(data) )
        
    
    def external_ranges_table_connector(self, func):
        """connect edit and delete button of each record in defined ranges tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, row data, 'edit' or 'delete' flag, button )
        """
        self.ranges_table_external_event_function = func

    
    def ranges_table_event(self, idx, data, status, btn):
        """this function exec when edit or delete button clicked on defined ranges table

        Args:
            idx (_type_): row index that its button clicked
            data (_type_): row datas that its button clicked
            status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
            btn (_type_): button object that clicked
        """
        def func():
            #
            # Write Internal Code Here
            #
            self.ranges_table_external_event_function(idx, data, status, btn)
        return func


    
    def set_ranges_table_data(self, datas:list[list]):
        """insert ranges tnto defined ranges table
        Args:
            datas (list[list]): list of row lits datas
        """
        assert self.ranges_table_external_event_function is not None, "ERROR: First determine an event Function for edit and delete button by 'gradingSettingPage.external_ranges_table_connector' method "
        
        #set row count
        records_count = len(datas)
        GUIBackend.set_table_dim(self.ranges_table, row=records_count, col=None)
        
        for i, row_data in enumerate(datas):
            GUIBackend.set_table_row(self.ranges_table, row=i, values=row_data)

            #define edit and delete button
            edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()


            #connect buttons to event function 
            GUIBackend.button_connector( edit_btn, self.ranges_table_event(i, datas[i], 'edit',  edit_btn) )
            GUIBackend.button_connector( del_btn, self.ranges_table_event(i, datas[i], 'delete',  del_btn ) )

            #insert buttons into table
            item_count = len(row_data)
            GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count), edit_btn)
            GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count+1), del_btn)



    def set_standards_table_data(self, datas:list[list]):
       pass


# class timerThread(QObject):
#     completed =  pyqtSignal()

#     def __init__(self,) -> None:
#         super().__init__()
#         self.ts = {}
#         self.on_threads_flag = {}

#     def wait(self,name, wait_time, step=1):
#         #set value into ts and flag 
#         self.on_threads_flag[name] = True
#         self.ts[name] = 0

#         #wait untile timer is lower than wait_time
#         while self.ts[name] < wait_time:
#             time.sleep(step)
#             self.ts[name] += step
#             print( self.ts[name] )

#         self.on_threads_flag[name] = False
#         self.completed.emit()


#     def is_thread_running(self, name):
#         return self.on_threads_flag[name]
    
#     def reset_wait_timer(self, name):
#         self.ts[name] = 0

#     def add(self, name):
#         self.ts[name] = 0
#         self.on_threads_flag[name] = False

        
if __name__ == '__main__':

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load(main_ui_file, None)
    global_ui = GlobalUI(window)
    main_page = mainPage(window)
    grading_setting_page = gradingSettingTab(window)
    calib_page = CalibrationPage(window)
    all_users_tab = AllUserTab(window)
    camera_setting_tab = cameraSettingTab(window)

    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    #------------------------------------------------------------
    main_page.set_warning_buttons_status('camera_connection', False)
    main_page.set_warning_buttons_status('camera_grabbing', False)
    main_page.set_warning_buttons_status('illumination', False)
    main_page.set_warning_buttons_status('tempreture', False)



    main_page.set_statistics_table_headers(['<6mm', '6mm-8mm', '8mm-10mm', '10mm-12.5mm'])
    main_page.set_statistics_table_datas(datas=[['Avrage', 1,2,3,4],
                                          ['STD', 5,1,5,4],
                                          ['ovality', 5,1,5,4],
                                          ['Variance', 5,1,5,4],
                                          ])
    
    
    #------------------------------------------------------------
    # #main_page.player_buttons_connect('start', lambda :main_page.set_warning_massage('dama balast'))
    def test_func(idx, data, status, btn):
            print(idx, data, status)
    
    grading_setting_page.external_ranges_table_connector(test_func)
    grading_setting_page.set_ranges_table_data([[1,4,6],[2,6,8]])
    #------------------------------------------------------------

    calib_page.set_calib_tabel(['2022/12/01','18:30', '0.1', 'mean', '5'])
    calib_page.write_calib_result(0.2, 0.1)
    settings = calib_page.get_settings()
    print(settings)

    #------------------------------------------------------------
    def test_users_func(idx, users, status, btn):
        print(users, status)

    all_users_tab.table_external_event_connector(test_users_func)
    
    all_users_tab.set_users_table([{'username':'amir', 'password':'******', 'role': 'user'},
                                    {'username':'its.big', 'password':'********', 'role': 'admin'}])
    #------------------------------------------------------------
    
    #------------------------------------------------------------
    def test_change_cam_setting(arg):
        print(arg)
    camera_setting_tab.change_setting_event_connector(test_change_cam_setting)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    window.show()
    

    app.exec()

    