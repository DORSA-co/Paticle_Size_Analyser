# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Assets_rc

class Ui_sampleTest(object):
    def setupUi(self, sampleTest):
        if not sampleTest.objectName():
            sampleTest.setObjectName(u"sampleTest")
        sampleTest.setEnabled(True)
        sampleTest.resize(1013, 160)
        sampleTest.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	\n"
"\n"
"}\n"
"\n"
"#sampleTest{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
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
"    background-color: rgb(90, 117, 127);\n"
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
"QHeaderView::s"
                        "ection:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"QLabel{\n"
"	color: #404040;\n"
"\n"
"}\n"
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
" "
                        "   border: none;\n"
"    selection-background-color: rgb(6, 76, 130);\n"
"	selection-color: rgb(6, 76, 130);\n"
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
"QDateEdit::d"
                        "own-button\n"
"{\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: 30px;\n"
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
""
                        "\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-uptriangle-48.png);\n"
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
"/****************"
                        "***************************/\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
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
"/*****************************"
                        "**************/\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(6, 76, 130);\n"
"	font-weight: bold;\n"
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
"	backgrou"
                        "nd: #e4f0fa;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
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
        self.horizontalLayout = QHBoxLayout(sampleTest)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.pushButton = QPushButton(sampleTest)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color:rgb(90, 117, 127);")
        icon = QIcon()
        icon.addFile(u":/assets/Assets/icons/icons8-download-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(sampleTest)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.sample_name_lbl = QLabel(sampleTest)
        self.sample_name_lbl.setObjectName(u"sample_name_lbl")

        self.gridLayout_2.addWidget(self.sample_name_lbl, 0, 1, 1, 1)

        self.label = QLabel(sampleTest)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.date_lbl = QLabel(sampleTest)
        self.date_lbl.setObjectName(u"date_lbl")

        self.gridLayout_2.addWidget(self.date_lbl, 1, 1, 1, 1)

        self.label_5 = QLabel(sampleTest)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.time_lbl = QLabel(sampleTest)
        self.time_lbl.setObjectName(u"time_lbl")

        self.gridLayout_2.addWidget(self.time_lbl, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(sampleTest)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(15, 0))
        self.line.setStyleSheet(u"color: #a0a0a0;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.table = QTableWidget(sampleTest)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        if (self.table.rowCount() < 2):
            self.table.setRowCount(2)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(0, 140))
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setRowCount(2)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(48)

        self.horizontalLayout.addWidget(self.table)


        self.retranslateUi(sampleTest)

        QMetaObject.connectSlotsByName(sampleTest)
    # setupUi

    def retranslateUi(self, sampleTest):
        sampleTest.setWindowTitle(QCoreApplication.translate("sampleTest", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("sampleTest", u"Load Sample", None))
        self.label_3.setText(QCoreApplication.translate("sampleTest", u"Date", None))
        self.sample_name_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sampleTest", u"Sample Name:", None))
        self.date_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("sampleTest", u"Time", None))
        self.time_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
    # retranslateUi

