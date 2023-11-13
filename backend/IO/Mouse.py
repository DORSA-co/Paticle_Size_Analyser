from tkinter import W
from PySide6.QtCore import *
from PySide6 import QtWidgets, QtGui
from matplotlib.widgets import Widget





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
    
    def get_postion(self):
        return self.x, self.y

class Mouse(QObject):

    def __init__(self):
        super(Mouse,self).__init__()
        self.events = {}
    

    def __generate_event_func(self, function):
        def _event_( e:QtGui.QMouseEvent):
            print('hello')
            function(MouseEvent(e))
            
        return _event_
    

    def connet_dbclick(self, widget:QtWidgets.QWidget, function):
        widget.mouseDoubleClickEvent = self.__generate_event_func( function)

    def connect_click(self, widget:QtWidgets.QWidget, function ):
        widget.mousePressEvent =self.__generate_event_func(function)

    def connect_all(self, widget:QtWidgets.QWidget, function ):
        self.connet_dbclick(widget , function)
        self.connect_click(widget , function)
        