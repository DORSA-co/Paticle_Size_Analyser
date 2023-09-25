# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import Assets_rc

class Ui_login_dialog_window(object):
    def setupUi(self, login_dialog_window):
        if not login_dialog_window.objectName():
            login_dialog_window.setObjectName(u"login_dialog_window")
        login_dialog_window.resize(550, 442)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog_window.sizePolicy().hasHeightForWidth())
        login_dialog_window.setSizePolicy(sizePolicy)
        login_dialog_window.setMinimumSize(QSize(550, 400))
        login_dialog_window.setMaximumSize(QSize(550, 442))
        login_dialog_window.setStyleSheet(u"*{\n"
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
"#login_dialog_window{\n"
"	background-color: rgb(6, 76, 130);\n"
"	\n"
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
"	color: rgb(50,50,50);\n"
"color: #ffffff;\n"
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
"/***************************************"
                        "****/\n"
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
"	 background-color: rgb(238, 134, 44);\n"
"	 min-width: 30p"
                        "x;\n"
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
"\n"
"")
        self.verticalLayout = QVBoxLayout(login_dialog_window)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 40, 60, 40)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.username_input = QLineEdit(login_dialog_window)
        self.username_input.setObjectName(u"username_input")

        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)

        self.role_combobox = QComboBox(login_dialog_window)
        self.role_combobox.setObjectName(u"role_combobox")

        self.gridLayout.addWidget(self.role_combobox, 2, 1, 1, 1)

        self.label_2 = QLabel(login_dialog_window)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(login_dialog_window)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(login_dialog_window)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.password_input = QLineEdit(login_dialog_window)
        self.password_input.setObjectName(u"password_input")

        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.error_lbl = QLabel(login_dialog_window)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"color:rgb(255, 99, 94);")

        self.verticalLayout.addWidget(self.error_lbl)

        self.horizontalFrame = QFrame(login_dialog_window)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.save_btn = QPushButton(self.horizontalFrame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(58, 209, 154);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(49, 177, 130);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.horizontalFrame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:rgb(255, 99, 94);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(208, 79, 77);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.retranslateUi(login_dialog_window)

        QMetaObject.connectSlotsByName(login_dialog_window)
    # setupUi

    def retranslateUi(self, login_dialog_window):
        login_dialog_window.setWindowTitle(QCoreApplication.translate("login_dialog_window", u"Edit User", None))
        self.label_2.setText(QCoreApplication.translate("login_dialog_window", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("login_dialog_window", u"Role", None))
        self.label.setText(QCoreApplication.translate("login_dialog_window", u"Username", None))
        self.error_lbl.setText(QCoreApplication.translate("login_dialog_window", u"Error", None))
        self.save_btn.setText(QCoreApplication.translate("login_dialog_window", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("login_dialog_window", u"Cancel", None))
    # retranslateUi

