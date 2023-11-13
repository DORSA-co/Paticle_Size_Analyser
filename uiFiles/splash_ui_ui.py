# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)
import Assets_rc
import Assets_rc

class Ui_splash_dialog_window(object):
    def setupUi(self, splash_dialog_window):
        if not splash_dialog_window.objectName():
            splash_dialog_window.setObjectName(u"splash_dialog_window")
        splash_dialog_window.resize(920, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(splash_dialog_window.sizePolicy().hasHeightForWidth())
        splash_dialog_window.setSizePolicy(sizePolicy)
        splash_dialog_window.setMinimumSize(QSize(920, 550))
        splash_dialog_window.setMaximumSize(QSize(920, 550))
        splash_dialog_window.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	font-size: 14px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#splash_dialog_window{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 20, 34, 255), stop:1 rgba(12, 80, 139, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	min-height: 40px;\n"
"	border-radius: 5px;\n"
"\n"
"	\n"
"}\n"
"/*\n"
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
"*/\n"
"\n"
"/*********************************************/\n"
"QLabel{\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
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
""
                        "}\n"
"\n"
"\n"
"\n"
"/*******************************************/\n"
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
"	color: rgb(6, 76, 130);\n"
"	background: #ffffff;\n"
"	selection-background-color: rgb(255, 204, 75);\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(splash_dialog_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(splash_dialog_window)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(650, 250))
        self.label.setPixmap(QPixmap(u":/assets/images/dorsa.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(splash_dialog_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(650, 100))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 42px;")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, 25, 25, 25)
        self.progress_bar = QProgressBar(splash_dialog_window)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"    border: solid;\n"
"	border-width: 2px;\n"
"    border-color: #ffffff;\n"
"	background-color:rgba(60, 60, 60,0);\n"
"	color:#ffffff;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"	height: 32;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:100 rgba(225, 225, 225, 255));\n"
"    width: 20px;\n"
"\n"
"\n"
"}\n"
"")
        self.progress_bar.setValue(20)
        self.progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.progress_bar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(splash_dialog_window)

        QMetaObject.connectSlotsByName(splash_dialog_window)
    # setupUi

    def retranslateUi(self, splash_dialog_window):
        splash_dialog_window.setWindowTitle(QCoreApplication.translate("splash_dialog_window", u"PSA Lodaing", None))
#if QT_CONFIG(accessibility)
        splash_dialog_window.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("splash_dialog_window", u"PSA-Alpha", None))
    # retranslateUi

