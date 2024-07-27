import time

from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtWidgets 
from guiBackend import GUIBackend

CODE_NAME_BUTTON_STYLE ={
    'normal': """ QPushButton{
                  min-width:100px;
                  background-color: rgb(150,150,150);
                }


            QPushButton:hover{
            background-color: rgb(50,50,50);
            }
            """,

    'active':
            """ QPushButton{
                  min-width:100px;
                  background-color: rgb(58, 209, 154);
                }


            QPushButton:hover{
            background-color: rgb(58, 209, 154);
            }
            """

}



TABEL_BUTTON_STYLE = """
    QPushButton{ 
        background-color: rgba(255,255,255,0);
        min-height:0px; min-width:0px; 
        width:auto;
        qproperty-iconSize: 24px;
        } 
    """







REPORT_BUTTON_STYLE = """
QPushButton{
	min-height:30px;
    min-width:30px;
    max-height:30px;
    max-width:30px;
	border-radius:3px;
	color: rgb(255, 255, 255);
	background-color:rgb(54, 193, 142);

}

QPushButton:hover{
	color: rgb(255, 255, 255);
	background-color:rgb(40, 144, 106);
}

"""
TABLE_BUTTON_STYLE = """
QPushButton{
	min-height:30px;
    min-width:100px;
    max-height:30px;
    max-width:100px;
	border-radius:3px;
	color: rgb(255, 255, 255);
	background-color:rgb(54, 193, 142);

}

QPushButton:hover{
	color: rgb(255, 255, 255);
	background-color:rgb(40, 144, 106);
}
"""

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

COMPARE_COMBOBOXE = """
                    QComboBox
{
	min-width:0xp;
	min-height: 18px;
    max-height: 18px;
	font-size: 14px;
    border-color: rgb(150,150,150);
}
        """

TABLE_SPINBOX = """
QSpinBox, QDoubleSpinBox  
{
    min-width:50xp;
    max-width:50px;
	min-height: 0px;
    max-height: 20px;
	font-size: 12px;
}
"""

class editButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(editButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/icons/icons8-edit-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/icons/icons8-edit-hover-table-50.png')
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
        self._icon_normal = QtGui.QIcon(':/assets/icons/icons8-remove-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/icons/icons8-remove-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)



class reportButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(reportButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/icons/icons8-eye-50-green.png')
        self._icon_over = QtGui.QIcon(':/assets/icons/icons8-eye-50-green-hover.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)


class tableButton(QtWidgets.QPushButton):

    def __init__(self, text='', *a, **kw):
        super(tableButton, self).__init__(*a, **kw)
        self.setStyleSheet(TABLE_BUTTON_STYLE)
        self.setText(text)
        
        





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

class compareComboBox(QtWidgets.QComboBox):

    def __init__(self, *a, **kw):
        super(compareComboBox, self).__init__(*a, **kw)

        self.insertItems(0, ['none', '>','>=', '<', '<=', '=='])
        self.setStyleSheet(COMPARE_COMBOBOXE)



class Input(QtWidgets.QLineEdit):

    def __init__(self, *a, **kw):
        super(Input, self).__init__(*a, **kw)

        

    def set_size(self, w, h):
        self.setStyleSheet(f"""QLineEdit 
                                {{
                               width :{w}px;
                               height :{h}px;

                               min-width :{w}px;
                               min-height :{h}px;

                               max-width :{w}px;
                               max-height :{h}px;
                               }}""")


class doubleSpinBoxTable(QtWidgets.QDoubleSpinBox):

    def __init__(self, *a, **kw):
        super(doubleSpinBoxTable, self).__init__(*a, **kw)
        self.setStyleSheet(TABLE_SPINBOX)
        self.setButtonSymbols(QtWidgets.QSpinBox.NoButtons)
        

class LabelTable(QtWidgets.QLabel):
    clicked = QtCore.Signal()
    def __init__(self, *a, **kw):
        super(LabelTable, self).__init__(*a, **kw)
        self.setScaledContents(True)

    def mousePressEvent(self, event:QtCore.QEvent):        
        if event.type() == QtCore.QEvent.MouseButtonPress:
                self.clicked.emit()
  

    
    def set_size(self, h,w):
        GUIBackend.set_max_size(self, h, w)
        GUIBackend.set_min_size(self, h, w)


class inputTable(QtWidgets.QLineEdit):
    def __init__(self, *a, **kw):
        super(inputTable, self).__init__(*a, **kw)



        


class confirmMessageBox:
    def __init__(self, title, text, buttons, min_height=300, min_width=400, parent=None ):
        self.STANDARD_BUTTONS = {
            'yes': QtWidgets.QMessageBox.Yes,
            'no': QtWidgets.QMessageBox.No,
            'cancel': QtWidgets.QMessageBox.Cancel,
            'save': QtWidgets.QMessageBox.Save,
            'ok': QtWidgets.QMessageBox.Ok,
            'ignore': QtWidgets.QMessageBox.Ignore,
            

        }

        self.icon = QtGui.QIcon(':/assets/icons/icons8-question-blue-50.png')
        self.buttons = buttons

        text = text + " " * 100 + "\n"

        self.msg = QtWidgets.QMessageBox( text=text, parent=parent)
        self.msg.setWindowTitle(title)
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)
        self.msg.setWindowIcon(self.icon)
        #self.msg.setMinimumHeight(min_height)
        #self.msg.setStyleSheet("QLabel{ min-width:" + str(min_width) + " px; }" )
        #self.msg.setMinimumWidth(min_width)

        
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

    def render(self) -> str:
        retval = self.msg.exec_()
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name


class timerBuilder:

    def __init__(self, t, event_func) -> None:
        self.event_func = event_func
        self.t = t
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect( self.event_func)


    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect( self.event_func)
        self.timer.start(self.t)
    

    def stop(self, ):
        self.timer.stop()
        self.timer.deleteLater()



    
def single_timer_runner( t, func):
    """runs a function after a delay time

    Args:
        t (_type_): delay time in ms`
        func (_type_): function event after time finished
    """
    timer = QtCore.QTimer()
    timer.singleShot(t, func)
    
    


class singleAnimation:

    def __init__(self, obj ,atribute, time, key1, key2) -> None:
        
        self.key1 = key1
        self.key2 = key2
        self.time = time
        self.toggle_flag = True
        self.animation = QtCore.QPropertyAnimation(obj, atribute)
        self.animation.setDuration(time)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
    
    def reset(self,):
        self.animation.setDuration(1)
        self.animation.setStartValue(self.key1)
        self.animation.setEndValue(self.key1)
        self.animation.start()
        self.animation.setDuration(self.time)
        
    
    def forward( self ):
        self.toggle_flag = False
        self.animation.setStartValue(self.key1)
        self.animation.setEndValue(self.key2)
        self.animation.start()
        
    
    def backward(self):
        self.toggle_flag = True
        self.animation.setStartValue(self.key2)
        self.animation.setEndValue(self.key1)
        self.animation.start()
        


    def single_forward(self):
        if self.toggle_flag:
            self.forward()
            
        
    
    def single_backward(self,):
        if not self.toggle_flag:
            self.backward()
    
    
    def toggle(self,):
        if self.toggle_flag:
            self.forward()
        else:
            self.backward()



class gifPlayer:

    def __init__(self, label: QtWidgets.QLabel, gif_path: str) -> None:
        self.movie = QtGui.QMovie(gif_path)
        self.label = label
        self.label.setMovie(self.movie)

        self.max_w = self.label.maximumWidth()
        self.max_h = self.label.maximumHeight()
    
    def set_maxsize(self, max_h, max_w):
        if max_w is not None:
            self.max_w = max_w
        
        if max_h is not None:
            self.max_h = max_h


	# Start Animation
    def start_animation(self):
        self.movie.start()

    def show_and_start_animation(self,):
        self.label.setMaximumHeight(self.max_h)
        self.label.setMaximumWidth(self.max_w)

        self.start_animation()

	# Stop Animation(According to need)
    def stop_animation(self):
        pass
        #self.movie.startTimer()

    def hide_and_stop_animation(self,):
        self.label.setMaximumHeight(0)
        self.label.setMaximumWidth(0)

        self.stop_animation()
        
    
       
                

def selectDirectoryDialog():
    path = QtWidgets.QFileDialog.getExistingDirectory()
    return path

def selectSaveFile(file_name:str = 'All', file_extention:str='.*'):
    """opens a dialog file to select a file to save

    Args:
        file_name (str): an ideal name of file like 'Excel' 
        file_extention (str): file extention like '.xlsx'

    Returns:
        _type_: selected path
    """
    filter = f'{file_name} (*{file_extention})'
    path = QtWidgets.QFileDialog.getSaveFileName(filter=filter)
    return path


def selectFileDialog(file_name:str = 'All', file_extention:str='.*'):
    """opens a dialog file to select a file to save

    Args:
        file_name (str): an ideal name of file like 'Excel' 
        file_extention (str): file extention like '.xlsx'

    Returns:
        _type_: selected path
    """
    filter = f'{file_name} (*{file_extention})'
    path = QtWidgets.QFileDialog.getOpenFileName(filter=filter)
    return path




class overlayMassage(QtWidgets.QWidget):
    def __init__(self, 
                 text,
                 fill_overlay_color:tuple=(30, 30, 30, 200),
                 popup_bg:tuple=(0,0,0,0),
                 popup_card_size = (120,300),
                 font_size = 48,
                 text_color:tuple = (220,220,220), 
                 parent=None):
        
        super(overlayMassage, self).__init__()

        self.text = text
        self.popup_bg = QtGui.QColor(*popup_bg)
        self.overlay_color = fill_overlay_color
        self.fill_overlay_color = QtGui.QColor(*fill_overlay_color)
        self.popup_fillColor = QtGui.QColor(*popup_bg)
        self.popup_card_size = popup_card_size
        self.font_size = font_size
        self.text_color = text_color

        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




    def paintEvent(self, event):
        # This method is, in practice, drawing the contents of
        # your window.

        # get current window size
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setBrush(self.fill_overlay_color)
        qp.drawRect(0, 0, s.width(), s.height())

        # drawpopup
        qp.setBrush(self.popup_bg)
        qp.setPen(self.popup_bg)
        popup_width = self.popup_card_size[0]
        popup_height = self.popup_card_size[1]
        ow = int(s.width()/2-popup_width/2)
        oh = int(s.height()/2-popup_height/2)
        qp.drawRoundedRect(ow, oh, popup_width, popup_height, 5, 5)

        font = QtGui.QFont()
        font.setPixelSize(self.font_size)
        font.setBold(True)
        qp.setFont(font)
        qp.setPen(QtGui.QColor(*self.text_color))
        tolw, tolh = 80, -5
        qp.drawText(ow + int(popup_width/2) - tolw, oh + int(popup_height/2) - tolh, self.text)

        qp.end()


    def show(self,):
        self.showMaximized()


