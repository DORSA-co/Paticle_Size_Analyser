from PySide6.QtCore import *
from PySide6 import QtWidgets, QtGui
from matplotlib.widgets import Widget
import numpy as np




EVENTS_TYPE={
    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release',
    QEvent.Type.MouseButtonDblClick: 'mouse_dclick',
}


BUTTONS = {

    Qt.LeftButton:'left_btn',
    Qt.RightButton:'right_btn'
}

class MouseEvent:

    def __init__(self, e:QtGui.QMouseEvent) -> None:
        self.x = e.x()
        self.y = e.y()
        self.button = e.button()
        self.type = e.type()
    
    def get_postion(self):
        return np.array([self.x, self.y])
    
    def is_move(self,) -> bool:
        return self.type == QEvent.Type.MouseMove

    def is_click(self,) -> bool:
        return self.type == QEvent.Type.MouseButtonPress
    
    def is_dclick(self,) -> bool:
        return self.type == QEvent.Type.MouseButtonDblClick
    
    def is_release(self,) -> bool:
        return self.type == QEvent.Type.MouseButtonRelease
    
    def is_left_btn(self) -> bool:
        return self.button == Qt.LeftButton
    
    def is_right_btn(self) -> bool:
        return self.button == Qt.RightButton
    

class mouseHandeler(QObject):

    def __init__(self):
        super(mouseHandeler,self).__init__()
        self.events = {}
    

    def __generate_event_func(self, function):
        def _event_( e:QtGui.QMouseEvent):
            function(MouseEvent(e))
            
        return _event_
    

    def connet_dbclick(self, widget:QtWidgets.QWidget, function):
        widget.mouseDoubleClickEvent = self.__generate_event_func( function)

    def connect_click(self, widget:QtWidgets.QWidget, function ):
        widget.mousePressEvent =self.__generate_event_func(function)

    def connect_move(self, widget:QtWidgets.QWidget, function ):
        widget.mouseMoveEvent =self.__generate_event_func(function)

    def connect_release(self, widget:QtWidgets.QWidget, function ):
        widget.mouseReleaseEvent =self.__generate_event_func(function)

    def connect_all(self, widget:QtWidgets.QWidget, function ):
        self.connet_dbclick(widget , function)
        self.connect_click(widget , function)
        self.connect_move(widget , function)
        self.connect_release(widget , function)
        