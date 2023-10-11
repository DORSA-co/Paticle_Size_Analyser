# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verfication_result.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import Assets_rc

class Ui_sampleTest(object):
    def setupUi(self, sampleTest):
        if not sampleTest.objectName():
            sampleTest.setObjectName(u"sampleTest")
        sampleTest.setEnabled(True)
        sampleTest.resize(450, 300)
        sampleTest.setMinimumSize(QSize(450, 300))
        sampleTest.setMaximumSize(QSize(450, 350))
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
"\n"
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
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"Q"
                        "TabBar::tab:!selected {\n"
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
"QTimeEdit:hover{\n"
"	background: #e4f0fa;"
                        "\n"
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
        self.verticalLayout_3 = QVBoxLayout(sampleTest)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 40, 25, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.label = QLabel(sampleTest)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 18px;\n"
"font-weight:bold;")

        self.horizontalLayout.addWidget(self.label)

        self.passed = QFrame(sampleTest)
        self.passed.setObjectName(u"passed")
        self.horizontalLayout_2 = QHBoxLayout(self.passed)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sample_date_lbl_2 = QLabel(self.passed)
        self.sample_date_lbl_2.setObjectName(u"sample_date_lbl_2")
        self.sample_date_lbl_2.setStyleSheet(u"color:rgb(41, 147, 108);\n"
"font-weight: bold;\n"
"font-size:16px;")

        self.horizontalLayout_2.addWidget(self.sample_date_lbl_2)


        self.horizontalLayout.addWidget(self.passed)

        self.not_passed = QFrame(sampleTest)
        self.not_passed.setObjectName(u"not_passed")
        self.horizontalLayout_4 = QHBoxLayout(self.not_passed)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sample_date_lbl_3 = QLabel(self.not_passed)
        self.sample_date_lbl_3.setObjectName(u"sample_date_lbl_3")
        self.sample_date_lbl_3.setStyleSheet(u"color:rgb(152, 46, 44);\n"
"font-weight: bold;\n"
"font-size:16px;")

        self.horizontalLayout_4.addWidget(self.sample_date_lbl_3)


        self.horizontalLayout.addWidget(self.not_passed)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pages = QStackedWidget(sampleTest)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"#type1,\n"
"#type2\n"
"{\n"
"	background-color: rgba(0,0,0,0);\n"
"	padding:0px;\n"
"	margin:0px;\n"
"}\n"
"")
        self.type1 = QWidget()
        self.type1.setObjectName(u"type1")
        self.verticalLayout_2 = QVBoxLayout(self.type1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_2 = QFrame(self.type1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.error_lbl_2 = QLabel(self.type1)
        self.error_lbl_2.setObjectName(u"error_lbl_2")

        self.gridLayout.addWidget(self.error_lbl_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.type1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.error_lbl = QLabel(self.type1)
        self.error_lbl.setObjectName(u"error_lbl")

        self.gridLayout.addWidget(self.error_lbl, 0, 1, 1, 1)

        self.sieve_std_lbl = QLabel(self.type1)
        self.sieve_std_lbl.setObjectName(u"sieve_std_lbl")

        self.gridLayout.addWidget(self.sieve_std_lbl, 1, 1, 1, 1)

        self.sieve_std_lbl_2 = QLabel(self.type1)
        self.sieve_std_lbl_2.setObjectName(u"sieve_std_lbl_2")

        self.gridLayout.addWidget(self.sieve_std_lbl_2, 1, 2, 1, 1)

        self.label_5 = QLabel(self.type1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pages.addWidget(self.type1)
        self.type2 = QWidget()
        self.type2.setObjectName(u"type2")
        self.pages.addWidget(self.type2)

        self.verticalLayout_3.addWidget(self.pages)

        self.description_lbl = QLabel(sampleTest)
        self.description_lbl.setObjectName(u"description_lbl")
        self.description_lbl.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.description_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.ok = QPushButton(sampleTest)
        self.ok.setObjectName(u"ok")
        self.ok.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(150, 150, 150);\n"
"max-width: 100px;\n"
"min-width:100px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(100, 100, 100);\n"
"max-width: 100px;\n"
"min-width:100px;\n"
"}")

        self.verticalLayout_3.addWidget(self.ok, 0, Qt.AlignHCenter)

        self.line = QFrame(sampleTest)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(15, 0))
        self.line.setStyleSheet(u"color: #a0a0a0;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.verticalLayout_3.addWidget(self.line)


        self.retranslateUi(sampleTest)
        self.ok.clicked.connect(sampleTest.close)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(sampleTest)
    # setupUi

    def retranslateUi(self, sampleTest):
        sampleTest.setWindowTitle(QCoreApplication.translate("sampleTest", u"Form", None))
        self.label.setText(QCoreApplication.translate("sampleTest", u"Test Result:", None))
        self.sample_date_lbl_2.setText(QCoreApplication.translate("sampleTest", u"Passed", None))
        self.sample_date_lbl_3.setText(QCoreApplication.translate("sampleTest", u"Not Passed", None))
        self.error_lbl_2.setText(QCoreApplication.translate("sampleTest", u"%", None))
        self.label_3.setText(QCoreApplication.translate("sampleTest", u"Error of System and Sieve ", None))
        self.error_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.sieve_std_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.sieve_std_lbl_2.setText(QCoreApplication.translate("sampleTest", u"%", None))
        self.label_5.setText(QCoreApplication.translate("sampleTest", u"Avrage of Sieved STD", None))
        self.description_lbl.setText(QCoreApplication.translate("sampleTest", u"Desc", None))
        self.ok.setText(QCoreApplication.translate("sampleTest", u"ok", None))
    # retranslateUi

