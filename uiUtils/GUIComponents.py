from PySide6 import QtWidgets, QtCore, QtGui 
import Assets


TABEL_BUTTON_STYLE = """
    QPushButton{ 
        background-color: rgba(255,255,255,0);
        min-height:0px; min-width:0px; 
        width:auto;
        qproperty-iconSize: 24px;
        } 
    """

SIDEBAR_BUTTON_SELECTED_STYLE = """
QPushButton{
	color: #ffffff;
	min-height: 40px;
	text-align: left;
    margin-left:15px;
	icon-size:25px;
	background-color:rgba(0,0,0,0);

    color:rgb(255, 205, 5);
    font-size:14px;
    font-weight:bold;
    }

"""


SIDEBAR_BUTTON_STYLE = """
QPushButton{
	color: #ffffff;
	min-height: 40px;
	text-align: left;
    margin-left:15px;
	icon-size:25px;
	background-color:rgba(0,0,0,0);
    }

    QPushButton:hover{
    font-size:14px; 
    font-weight:bold;
}
"""




class editButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(editButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/Assets/icons/icons8-edit-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/Assets/icons/icons8-edit-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(editButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(editButton, self).enterEvent(event)



class deleteButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(deleteButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/Assets/icons/icons8-remove-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/Assets/icons/icons8-remove-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)



class tabelCheckbox(QtWidgets.QCheckBox):

    def __init__(self, *a, **kw):
        super(tabelCheckbox, self).__init__(*a, **kw)
        

    def set_size(self, w, h):
        self.setStyleSheet(f"""QCheckBox::indicator 
                                {{
                               width :{w}px;
                               height :{h}px;
                               }}""")

        #self.setMaximumWidth(h+5)
        #self.setMaximumWidth(w+5)


CONFIRMBOX_STYLESHEET = """
   QMessageBox{ 
        background-color: #ffffff;

    }
    
    QPushButton{
        border: none;
        font-weight: bold;
        color: #ffffff;
        background-color:rgb(6, 76, 130);
        min-height: 25px;
        border-radius: 5px;
        min-width:100px;
        font-size:12px;
	
        }

    QPushButton:hover{
	    background-color:rgb(22, 38, 76);
    }
"""

class confirmMessageBox:
    def __init__(self, title, text, buttons, min_height=400, min_width=700 ):
        self.STANDARD_BUTTONS = {
            'yes': QtWidgets.QMessageBox.Yes,
            'no': QtWidgets.QMessageBox.No,
            'cancel': QtWidgets.QMessageBox.Cancel,
            'save': QtWidgets.QMessageBox.Save,
        }

        self.icon = QtGui.QIcon(':/assets/Assets/icons/icons8-question-blue-50.png')
        self.buttons = buttons

        self.msg = QtWidgets.QMessageBox( text=text)
        self.msg.setWindowTitle(title)
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)
        self.msg.setWindowIcon(self.icon)
        self.msg.setMinimumHeight(min_height)
        self.msg.setMinimumWidth(min_width)

        
        #---------------------------------------------------
        selected_buttons_obj = []
        for btn_name in buttons:
            btn = self.STANDARD_BUTTONS[btn_name]
            if isinstance(selected_buttons_obj, list):
                selected_buttons_obj = btn
            else:
                selected_buttons_obj = selected_buttons_obj | btn
        self.msg.setStandardButtons(selected_buttons_obj)
        #---------------------------------------------------

    def render(self):
        retval = self.msg.exec_()
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name


def signal():
    return QtCore.Signal()

if __name__ == '__main__':
    pass
# msg = QMessageBox()
# msg.setIcon(QMessageBox.Information)
# msg.setText("This is a message box")
# msg.setInformativeText("This is additional information")
# msg.setWindowTitle("MessageBox demo")
# msg.setDetailedText("The details are as follows:")