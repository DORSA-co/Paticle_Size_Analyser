# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
        sampleTest.resize(860, 160)
        sampleTest.setMinimumSize(QSize(0, 150))
        sampleTest.setMaximumSize(QSize(16777215, 200))
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
        self.horizontalLayout = QHBoxLayout(sampleTest)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.load_btn = QPushButton(sampleTest)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color:rgb(90, 117, 127);\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgb(76, 99, 107);\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-download-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_btn.setIcon(icon)

        self.verticalLayout.addWidget(self.load_btn)

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

        self.sample_date_lbl = QLabel(sampleTest)
        self.sample_date_lbl.setObjectName(u"sample_date_lbl")

        self.gridLayout_2.addWidget(self.sample_date_lbl, 1, 1, 1, 1)

        self.label_5 = QLabel(sampleTest)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 14px;\n"
"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.sample_time_lbl = QLabel(sampleTest)
        self.sample_time_lbl.setObjectName(u"sample_time_lbl")

        self.gridLayout_2.addWidget(self.sample_time_lbl, 2, 1, 1, 1)


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
        self.table.setMinimumSize(QSize(0, 150))
        self.table.setMaximumSize(QSize(16777215, 16777215))
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
        self.load_btn.setText(QCoreApplication.translate("sampleTest", u"Load Sample", None))
        self.label_3.setText(QCoreApplication.translate("sampleTest", u"Date", None))
        self.sample_name_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sampleTest", u"Sample Name:", None))
        self.sample_date_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("sampleTest", u"Time", None))
        self.sample_time_lbl.setText(QCoreApplication.translate("sampleTest", u"TextLabel", None))
    # retranslateUi

