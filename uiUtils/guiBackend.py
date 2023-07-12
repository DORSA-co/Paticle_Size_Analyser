from PySide6 import QtWidgets, QtCore, QtGui 
from functools import partial

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

    def set_spinbox_range(inpt, value_range: tuple[int, int]):
        """set range of spinbox

        Args:
            inpt (QtWidgets.QSpinBox): Qt spinbox object
            value_range (tuple[int, int]): (low_range, highe_range )
        """
        inpt.setRange(*value_range)


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
