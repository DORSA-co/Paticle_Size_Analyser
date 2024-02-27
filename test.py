

import sys
sys.path.append('uiFiles//Assets')

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from uiFiles.main_UI_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())




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