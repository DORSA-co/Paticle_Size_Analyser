from functools import partial
from datetime import datetime, date
import sys

import cv2 
from PySide6.QtGui import QMovie
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
#from PyQt5 import uic

from Constants import CONSTANTS





class GUIBackend:


    @staticmethod
    def load_ui(path, parent=None, byQt=False):
        if not byQt:
            loader = QUiLoader()
            window = loader.load(path, parent)
        else:
            pass
            #window = uic.loadUi(path)
        return window

    @staticmethod
    def set_signal_connection(wgt:QtWidgets.QWidget, connection:bool):
        wgt.blockSignals(not(connection))


    @staticmethod
    def set_max_size(wgt:QtWidgets.QWidget, h=None, w=None):
        if w is not None:
            wgt.setMaximumWidth(w)
        
        if h is not None:
            wgt.setMaximumHeight(h)


    @staticmethod
    def set_min_size(wgt:QtWidgets.QWidget, h=None, w=None):
        if w is not None:
            wgt.setMinimumWidth(w)
        
        if h is not None:
            wgt.setMinimumHeight(h)


    @staticmethod
    def set_win_frameless(ui):
        ui.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

    @staticmethod
    def move(ui:QtWidgets.QMainWindow, pos:tuple[int]):
        point = QtCore.QPoint(*pos)
        ui.move(point)

    @staticmethod
    def relative_move(ui:QtWidgets.QMainWindow, diff_pos:tuple[int]):
        diff_pos = QtCore.QPoint(*diff_pos)
        new_pos = ui.pos() + diff_pos
        ui.move(new_pos)



    @staticmethod
    def close_app(ui:QtWidgets.QMainWindow ):
        # close app window and exit the program
        ui.close()
        sys.exit()

    @staticmethod
    def maxmize_minimize(ui:QtWidgets.QMainWindow):
        """
        this function chages the window size of app
        Inputs: None
        Returns: None
        """
        if ui.isMaximized():
            ui.showNormal()
        else:
            ui.showMaximized()

    def is_maximize(ui:QtWidgets.QMainWindow):
        return ui.isMaximized()
    
    def show_normal(ui:QtWidgets.QMainWindow):
        ui.showNormal()

    def show_maximize(ui:QtWidgets.QMainWindow):
        ui.showMaximized()
    
    @staticmethod
    def adjustsize( wgt: QtWidgets.QWidget):
        """adjust size of Qwidget . for example if you hide some widgets, you 
            can adjust window to resize

        Args:
            wgt (QtWidgets.QWidget): _description_
        """
        wgt.adjustSize()


    @staticmethod
    def minimize_win(ui):
        """
        this function minimizes the app to taskbar
        Inputs: None
        Returns: None
        """
        ui.showMinimized()

    
    @staticmethod
    def set_relation_size(wgt: QtWidgets.QWidget, rw, rh):
        h = int( CONSTANTS.screen.H * rh )
        w = int( CONSTANTS.screen.W * rw )
        GUIBackend.set_max_size(wgt, h, w)
        GUIBackend.set_min_size(wgt, h, w)
    #----------------------------------------------------------------

    @staticmethod
    def emit_signal(signal:QtCore.Signal):
        signal.emit()

    @staticmethod
    def show_window( ui, always_on_top=False):
        if always_on_top:
            ui.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        ui.show()

    @staticmethod
    def close_window( ui:QtWidgets.QDialog):
        ui.close()

    @staticmethod
    def hide_window( ui:QtWidgets.QDialog):
        ui.hide()
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
    def set_disable_enable( wdgt: QtWidgets.QWidget, status ):
        """enable or disables a PyQt widget

        Args:
            wdgt (QtWidgets): PyQt widget object
            status: enable if True, and disable if False 
        """
        wdgt.setEnabled(status)

    @staticmethod
    def cursor_changer(cursor_shape:str):
        dict_cur = {
            'wait': Qt.CursorShape.WaitCursor,
        }
        if cursor_shape is None:
            QApplication.restoreOverrideCursor()
        else:
            QApplication.setOverrideCursor(dict_cur[cursor_shape])



    def add_widget( parent:QtWidgets.QFrame, widget):
        """insert a new widget into parent widget

        Args:
            parent (QtWidgets.QLayout): parent widget that is a QLayout
            widget (_type_): Qt widget that you want insert into parent
        """
        if isinstance(parent, QtWidgets.QVBoxLayout) or isinstance(parent, QtWidgets.QHBoxLayout)  :
            parent.addWidget(widget)
        else:
            pass

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
        
        elif isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox):
            return GUIBackend.get_input_spinbox_value(wgt)
        
        elif isinstance(wgt, QtWidgets.QLineEdit):
            return GUIBackend.get_input_text(wgt)

        elif isinstance(wgt, QtWidgets.QCheckBox):
            return GUIBackend.get_checkbox_value(wgt)

        else:
            assert False, f"get_input method doesn't support {wgt} object"

    @staticmethod
    def set_input(wgt, value):
        """set value to a input widget in any type like ComboBox, SpinBox and LineEdit

        Args:
            wgt (_type_): Qt input Widgt
            value (_type_): input value to set


        """
        if isinstance(wgt, QtWidgets.QComboBox):
            GUIBackend.set_combobox_current_item(wgt, value)
        
        elif isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox):
            GUIBackend.set_spinbox_value(wgt, value)
        
        elif isinstance(wgt, QtWidgets.QLineEdit):
            GUIBackend.set_input_text(wgt, value)
        
        elif isinstance(wgt, QtWidgets.QCheckBox):
            GUIBackend.set_checkbox_value(wgt, value)

        else:
            assert False, f"set_input method doesn't support {wgt} object"


    @staticmethod
    def connector(wgt, func):
        """
        """
        if isinstance(wgt, QtWidgets.QComboBox):
            return GUIBackend.combobox_changeg_connector(wgt, func)
        
        elif isinstance(wgt, QtWidgets.QSpinBox) or isinstance(wgt, QtWidgets.QDoubleSpinBox):
            return GUIBackend.spinbox_connector(wgt, func)
        
        elif isinstance(wgt, QtWidgets.QLineEdit):
            return GUIBackend.input_text_connector(wgt, func)

        elif isinstance(wgt, QtWidgets.QCheckBox):
            return GUIBackend.checkbox_connector(wgt, lambda x: func())
        
        else:
            assert False, f"connector method doesn't support {wgt} object"


    #--------------------------------- GLOBAL BUTTON FUNCTIONs ---------------------------------
    @staticmethod
    def event_argumant_passer(func, args):
        def event_func():
            func(*args)
        return event_func
    
    @staticmethod
    def button_connector( btn: QtWidgets.QPushButton, func):
        """Connects a PyQt Button clicked event into a function

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            func (_type_): function that execute when event happend
        """
        btn.clicked.connect(partial( func ))

    
    def button_connector_argument_pass(btn: QtWidgets.QPushButton, func, args):
        """Connects a PyQt Button clicked event into a function and pass args to it
        """
        event_func = GUIBackend.event_argumant_passer(func, args)

        btn.clicked.connect(partial( event_func  ))



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
        txt = btn.styleSheet()
        #convert rgb to rgba
        if len(color) == 3:
            color+= (255,)

        btn.setStyleSheet(f'background-color: rgba{color}')

    @staticmethod
    def set_button_text( btn: QtWidgets.QPushButton , txt:str):
        """changes text of button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
        """
        btn.setText(txt)

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
        #GUIBackend.set_signal_connection(combo,False)
        combo.clear()
        combo.insertItems(0, items)
        #GUIBackend.set_signal_connection(combo,True)

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


    @staticmethod
    def combobox_changeg_connector( combo: QtWidgets.QComboBox, func):
        """connect combobox change selected item selected event

        Args:
            combo (QtWidgets.QComboBox): Qt comboBox object
            func : python function
        """
        combo.currentTextChanged.connect(func)

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
    def set_checkbox_value(chbox: QtWidgets.QCheckBox, value: bool):
        """set state of Qt checkbox

        Args:
            chbox (QtWidgets.QCheckBox): Qt CheckBox object
            value (bool): checked if True

        
        """
        return chbox.setChecked(value)
    
    
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
    def set_label_image(lbl: QtWidgets.QLabel, image) -> QtGui.QPixmap:

        if isinstance(image, str):
            image = cv2.imread(image)        

        #resie image to fix in label
        img_h, img_w = image.shape[:2]
        lbl_h, lbl_w = lbl.height(), lbl.width()
        
        scale = min(lbl_h/img_h, lbl_w/img_w)
        image = cv2.resize(image, None, fx= scale, fy=scale)

        #color image
        if len(image.shape)==3:
            #alpha channel image
            if image.shape[2] ==4:
                qformat=QtGui.QImage.Format_RGBA8888
            else:
                qformat=QtGui.QImage.Format_RGB888          

        #grayscale image
        if len(image.shape) == 2:
            qformat=QtGui.QImage.Format_Grayscale8

        img = QtGui.QImage(image.data,
            image.shape[1],
            image.shape[0], 
            image.strides[0], # <--- +++
            qformat)
        
        img = img.rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(img)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(QtCore.Qt.AlignCenter)
        return pixmap
    
    @staticmethod
    def fit_label_to_pixmap(lbl: QtWidgets.QLabel, pixmap:QtGui.QPixmap):
        lbl.setFixedSize(pixmap.size())

    
    def set_label_scale(lbl: QtWidgets.QLabel, active:bool):
        lbl.setScaledContents(active)
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

    def set_spinbox_range(inpt, value_range: tuple[int, int]):
        """set range of spinbox

        Args:
            inpt (QtWidgets.QSpinBox): Qt spinbox object
            value_range (tuple[int, int]): (low_range, highe_range )
        """
        inpt.setRange(*value_range)



    def get_textarea_text(inpt:QtWidgets.QTextEdit) -> str:
        return inpt.toPlainText()
    
    def set_textarea_text(inpt:QtWidgets.QTextEdit, txt) -> str:
        return inpt.setPlainText(txt)


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

    def set_input_password(inpt:QtWidgets.QLineEdit):
        """make a input, password format that show charater by *

        Args:
            inpt (QtWidgets.QLineEdit): _description_
        """
        inpt.setEchoMode(QtWidgets.QLineEdit.Password)


    def input_text_connector(inpt:QtWidgets.QLineEdit, func):
        inpt.textChanged.connect(func)
    

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


    @staticmethod
    def get_table_dim(table: QtWidgets.QTableWidget,) -> tuple[int,int]:
        """
        """
        return table.rowCount(), table.columnCount()
        

    def set_cell_width_content_adjust(table: QtWidgets.QTableWidget, indexes:list[int] = None):
        """adjust cell width based on its content

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            indexes (list[int]): columns indexes that you want adjust. if None, all columns size policy whould be change
        """
        headers = table.horizontalHeader()
        hcount = headers.count()

        if indexes is None:
            indexes = range(hcount)

        for i in indexes:
            headers.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents )
    
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
    def set_table_cell_widget(table: QtWidgets.QTableWidget, index: tuple, widget, layout=False):
        """insert a Qt widget (like QPushButton) into a custom cell of given Qt table

        Args:
            table (QtWidgets.QTableWidget): Qt tableWidget object
            idx (tuple): position of cell (row_idx, col_idx)
            widget (_type_): Qt widget that you want insert into cell of table
        """
        if layout:
            #container = QtWidgets.QWidget()
            container = QtWidgets.QFrame()
            layouth = QtWidgets.QHBoxLayout(container)
            layouth.addWidget(widget)
            layouth.setContentsMargins(2,2,2,2)
            table.setCellWidget(*index, container)
        else:
            table.setCellWidget(*index, widget)
            
        
        #item = QtWidgets.QTableWidgetItem(widget)
        #table.setItem(*index, item )

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


    @staticmethod
    def get_table_cell_value(table: QtWidgets.QTableWidget,index:tuple):
        """
        """
        return table.itemAt(*index).text()
    
    @staticmethod
    def get_table_cell_widget(table: QtWidgets.QTableWidget,index:tuple):
        """
        """
        return table.itemAt(*index).text()

    #--------------------------------- GLOBAL StackWidget FUNCTIONs ---------------------------------
    @staticmethod
    def set_stack_widget_idx(stw: QtWidgets.QStackedWidget, idx ):
        """change current index of given Qt stack widget

        Args:
            stw (QtWidgets.QStackedWidget): Qt stack widget object
            idx (_type_): custom index to set as current index
        """
        stw.setCurrentIndex(idx)

    @staticmethod
    def get_stack_widget_idx(stw: QtWidgets.QStackedWidget ) -> int:
        """get current index of given Qt stack widget

        Args:
            stw (QtWidgets.QStackedWidget): Qt stack widget object
        
        Returns:
            int: current index
        """
        return stw.currentIndex()
    

    @staticmethod
    def get_stack_widget_count(stw: QtWidgets.QStackedWidget ) -> int:

        return stw.count()
    
    #--------------------------------- GLOBAL GroupBox FUNCTIONs ---------------------------------
    @staticmethod
    def groupbox_checkbox_connector(gp: QtWidgets.QGroupBox, func):
        """connect a function to groubox toggle

        Args:
            gp (QtWidgets.QGroupBox): Qt GroupBox Widget Object
            func (_type_): python function
        """
        gp.toggled.connect(func)


    @staticmethod
    def is_groupbox_checked(gp: QtWidgets.QGroupBox) -> bool:
        """returns True when a groupbox's checkbox is checked

        Args:
            gp (QtWidgets.QGroupBox): Qt GroupBox Widget Object
        
        Returns:
            (bool) : True if checked and False if not
        """
        return gp.isChecked()
    


    @staticmethod
    def set_groupbox_checkbox(gp: QtWidgets.QGroupBox, state) :
        return gp.setChecked(state)


    
    def set_groupbox_title(gp: QtWidgets.QGroupBox, title):

        gp.setTitle(title)

    #--------------------------------- GLOBAL Frame FUNCTIONs ---------------------------------
    @staticmethod
    def set_frame_max_size( frame: QtWidgets.QFrame, w:int, h:int):
        """set maximum width and height of a frame.

        Args:
            frame (QtWidgets.QFrame): Qt Frame Widget Object
            w (int): maximum width. ignore if be None
            h (int): maximum height. ignore if be None
        """
        if h is not None:
            frame.setMaximumHeight(h)
        if w is not None:
            frame.setMaximumWidth(w)

    @staticmethod
    def set_frame_min_size( frame: QtWidgets.QFrame, w:int, h:int):
        """set maximum width and height of a frame.

        Args:
            frame (QtWidgets.QFrame): Qt Frame Widget Object
            w (int): maximum width. ignore if be None
            h (int): maximum height. ignore if be None
        """
        if h is not None:
            frame.setMinimumHeight(h)
        if w is not None:
            frame.setMinimumWidth(w)

    
    #--------------------------------- GLOBAL DateEdit FUNCTIONs ---------------------------------
    def get_date_input( obj: QtWidgets.QDateEdit) -> datetime:
        """returns date of QDateEdit

        Args:
            obj (QtWidgets.QDateEdit): Qt DateEdit Widget Object

        Returns:
            datetime: value in format if python datetime
        """
        return obj.date().toPython()
        #return datetime.combine( obj.date().toPython(), datetime.min.time() )

    
    def set_date_input( obj: QtWidgets.QDateEdit, date:date) -> datetime:
        """returns date of QDateEdit
        """

        date = QtCore.QDate(date.year, date.month, date.day)
        return obj.setDate(date)
    

    def date_input_connector( obj: QtWidgets.QDateEdit, func):
        obj.dateChanged.connect(lambda: func())
    
    def get_date_input_range(obj: QtWidgets.QDateEdit)-> tuple[datetime]:
        return obj.minimumDate().toPython(), obj.maximumDate().toPython()
    
    def set_date_input_range(obj: QtWidgets.QDateEdit,
                             min_date:datetime=None, 
                             max_date:datetime=None):
        if min_date is not None:
            min_date = QtCore.QDate(min_date.year, min_date.month, min_date.day)
            obj.setMinimumDate(min_date)
        
        if max_date is not None:
            max_date = QtCore.QDate(max_date.year, max_date.month, max_date.day)
            obj.setMaximumDate(max_date)
    

    #--------------------------------- GLOBAL Tabs FUNCTIONs ---------------------------------
    @staticmethod 
    def set_enable_tab( tab: QtWidgets.QTabWidget, idx, status):
        tab.setTabEnabled(idx, status)


    @staticmethod 
    def set_visible_tab( tab: QtWidgets.QTabWidget, idx, status):
        tab.setTabVisible(idx, status)

    
    @staticmethod
    def set_current_tab( tab:QtWidgets.QTabWidget, idx):
        tab.setCurrentIndex(idx)

    @staticmethod
    def hide_tab_header(tab:QtWidgets.QTableWidget, status):
        if status:
            tab.setStyleSheet(tab.styleSheet() + "QTabBar::tab{max-height:0px;}")
        else:
            tab.setStyleSheet(tab.styleSheet() + "QTabBar::tab{max-height:1000px;}")


    #------------------------------------------------------------------------------------------
    @staticmethod
    def set_progressbar_value(progressbar:QtWidgets.QProgressBar, value):
        progressbar.setValue(int(value))