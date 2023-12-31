# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compare_info.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import Assets_rc

class Ui_dialog_window(object):
    def setupUi(self, dialog_window):
        if not dialog_window.objectName():
            dialog_window.setObjectName(u"dialog_window")
        dialog_window.resize(550, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_window.sizePolicy().hasHeightForWidth())
        dialog_window.setSizePolicy(sizePolicy)
        dialog_window.setMinimumSize(QSize(550, 430))
        dialog_window.setMaximumSize(QSize(550, 430))
        dialog_window.setStyleSheet(u"*{\n"
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
"#dialog_window{\n"
"	background-color: #ffffff;\n"
"	background-color: rgb(6, 76, 130);\n"
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
"}\n"
"\n"
"\n"
"\n"
"/*******************************************/\n"
""
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
"	image: url(:/assets/icons/icons8-arrow-48.png);\n"
"	width: 15px;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 background-color:rgb(217, 82, 48);\n"
"	 min-width: 30px;\n"
"}\n"
""
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
"}")
        self.verticalLayout = QVBoxLayout(dialog_window)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 80, 60, 80)
        self.error_lbl_2 = QLabel(dialog_window)
        self.error_lbl_2.setObjectName(u"error_lbl_2")
        self.error_lbl_2.setMaximumSize(QSize(16777215, 30))
        self.error_lbl_2.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.error_lbl_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.standards_name_combobox = QComboBox(dialog_window)
        self.standards_name_combobox.setObjectName(u"standards_name_combobox")

        self.gridLayout.addWidget(self.standards_name_combobox, 0, 1, 1, 1)

        self.label_2 = QLabel(dialog_window)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalFrame = QFrame(dialog_window)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #ffffff;\n"
"color: rgb(6, 76, 130);\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.run_btn = QPushButton(self.horizontalFrame)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"background-color: rgb(58, 209, 154);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.run_btn)

        self.cancel_btn = QPushButton(self.horizontalFrame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 95, 84);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.retranslateUi(dialog_window)

        QMetaObject.connectSlotsByName(dialog_window)
    # setupUi

    def retranslateUi(self, dialog_window):
        dialog_window.setWindowTitle(QCoreApplication.translate("dialog_window", u"Dialog", None))
        self.error_lbl_2.setText(QCoreApplication.translate("dialog_window", u"Select a Standard for compare", None))
        self.label_2.setText(QCoreApplication.translate("dialog_window", u"Standard", None))
        self.run_btn.setText(QCoreApplication.translate("dialog_window", u"Run", None))
        self.cancel_btn.setText(QCoreApplication.translate("dialog_window", u"Cancel", None))
    # retranslateUi

