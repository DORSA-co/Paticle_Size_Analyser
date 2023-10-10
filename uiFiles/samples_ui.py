# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'samples.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Assets_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(764, 751)
        Dialog.setMinimumSize(QSize(600, 0))
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-settings-50.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	color: #ffffff;\n"
"	background-color:rgb(6, 76, 130);\n"
"	min-height: 35px;\n"
"	border-radius: 5px;\n"
"	min-width:200px;\n"
"	font-size:12px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color:rgb(22, 38, 76);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: #808080;\n"
"	background-color:rgb(210, 210, 210);\n"
"\n"
"}\n"
"\n"
"/*********************************************/\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
""
                        "\n"
"\n"
"/*********************************************/\n"
"\n"
"\n"
"\n"
"/*********************************************/\n"
"QComboBox\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border:2px solid rgb(210, 210, 210);\n"
"	color:(210, 210, 210);\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-arrow-48.png);\n"
"	width: 15px;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 background-color: rgb(6, 76, 130);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled \n"
"{\n"
"	 background-color: rgb(210, 210, 210);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"    selection-background-color: rgb(6, 76, 130);\n"
"	selection-color: rgb(6, 76, 130"
                        ");\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"	height:30px;\n"
"}\n"
"\n"
"/*********************************************/\n"
"\n"
"QDateEdit\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QDateEdit:disabled ,\n"
"QDateEdit:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"\n"
"\n"
"QDateEdit::up-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::down-arrow \n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-downtriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button\n"
"{\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: "
                        "30px;\n"
"}\n"
"\n"
"\n"
"QDateEdit::up-button:disabled ,\n"
"QDateEdit::down-button:disabled\n"
"    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"	background: rgb(241, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"\n"
"/*********************************************/\n"
"\n"
"QSpinBox, QDoubleSpinBox  \n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox:enabled, QDoubleSpinBox:enabled{\n"
"color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"	color:(210, 210, 210);\n"
"}\n"
"\n"
"QSpinBox:focus , QDoubleSpinBox:focus\n"
"{\n"
"	background-color:red;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8"
                        "-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-downtriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button   {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: 30px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus{\n"
"	background: rgb(241, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"\n"
"\n"
"/*******************************************/\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: "
                        "25px;\n"
"	border:2px solid rgb(6, 76, 130);\n"
"	border-radius: 3px;\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image:url(:/assets/Assets/icons/icons8-check-50.png);\n"
"	background-color:rgb(6, 76, 130);\n"
"}\n"
"\n"
"/*******************************************/\n"
"QLineEdit\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"/*******************************************/\n"
"\n"
"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"	background-color:rgb(43, 43, 43);\n"
"	color:#ffffff;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"	height: 32;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(8, 103, 176);\n"
"    width: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/*******************************************/\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(6, 76, 130);\n"
"	font-weight:"
                        " bold;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	border-left: 1px solid rgb(199, 199, 199);\n"
"	border-right: 1px solid rgb(199, 199, 199);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	height:40px;\n"
"	width: 150px;\n"
"	background-color: rgb(93, 93, 93);\n"
"	color: rgb(255,255,255);\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid rgb(6, 76, 130);\n"
"\n"
"\n"
"}\n"
"QTabWidget{\n"
"background-color: rgb(48, 48, 48)\n"
"}\n"
"/*******************************************/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QGroupBox{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 1px solid black;\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: white;\n"
"	background: #0078D7;\n"
"	selection-background-color: black;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
""
                        "QTimeEdit:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"	color: white;\n"
"	background: #0078D7;\n"
"	selection-background-color: black;\n"
"}\n"
"\n"
"QListView::item{\n"
"	height: 30px;\n"
"}\n"
"")
        Dialog.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.samples_table = QTableWidget(Dialog)
        if (self.samples_table.columnCount() < 7):
            self.samples_table.setColumnCount(7)
        if (self.samples_table.rowCount() < 6):
            self.samples_table.setRowCount(6)
        self.samples_table.setObjectName(u"samples_table")
        self.samples_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.samples_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.samples_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.samples_table.setRowCount(6)
        self.samples_table.setColumnCount(7)
        self.samples_table.verticalHeader().setVisible(False)
        self.samples_table.verticalHeader().setDefaultSectionSize(35)

        self.verticalLayout_2.addWidget(self.samples_table, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Samples", None))
    # retranslateUi

