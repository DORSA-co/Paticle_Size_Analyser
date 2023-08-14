# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Assets_rc

class Ui_login_dialog_window(object):
    def setupUi(self, login_dialog_window):
        if not login_dialog_window.objectName():
            login_dialog_window.setObjectName(u"login_dialog_window")
        login_dialog_window.resize(550, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog_window.sizePolicy().hasHeightForWidth())
        login_dialog_window.setSizePolicy(sizePolicy)
        login_dialog_window.setMinimumSize(QSize(550, 430))
        login_dialog_window.setMaximumSize(QSize(550, 430))
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
"")
        self.verticalLayout = QVBoxLayout(login_dialog_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.win_buttons = QFrame(login_dialog_window)
        self.win_buttons.setObjectName(u"win_buttons")
        self.win_buttons.setMaximumSize(QSize(16777215, 30))
        self.win_buttons.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	margin: 0px;\n"
"	min-height: 0px;\n"
"	min-width: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	max-height:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border: 1 solid #ffffff;\n"
"background-color: rgba(31, 32, 85, 100);\n"
" }\n"
"\n"
"#win_buttons{\n"
"\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.win_buttons.setFrameShape(QFrame.StyledPanel)
        self.win_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.win_buttons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.win_buttons)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(16777215, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/assets/Assets/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.win_buttons)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, -1, 60, 25)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(login_dialog_window)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.password_input = QLineEdit(login_dialog_window)
        self.password_input.setObjectName(u"password_input")

        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)

        self.label = QLabel(login_dialog_window)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.username_input = QLineEdit(login_dialog_window)
        self.username_input.setObjectName(u"username_input")

        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.login_error_lbl = QLabel(login_dialog_window)
        self.login_error_lbl.setObjectName(u"login_error_lbl")
        self.login_error_lbl.setMinimumSize(QSize(0, 35))
        self.login_error_lbl.setMaximumSize(QSize(16777215, 45))
        self.login_error_lbl.setStyleSheet(u"color:rgb(255, 99, 94);")

        self.verticalLayout_2.addWidget(self.login_error_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalFrame = QFrame(login_dialog_window)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.login_btn = QPushButton(self.horizontalFrame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #ffffff;\n"
"color: rgb(6, 76, 130);\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(58, 209, 154);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.login_btn)


        self.verticalLayout_2.addWidget(self.horizontalFrame)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(login_dialog_window)

        QMetaObject.connectSlotsByName(login_dialog_window)
    # setupUi

    def retranslateUi(self, login_dialog_window):
        login_dialog_window.setWindowTitle(QCoreApplication.translate("login_dialog_window", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("login_dialog_window", u"Password", None))
        self.password_input.setText(QCoreApplication.translate("login_dialog_window", u"admin", None))
        self.label.setText(QCoreApplication.translate("login_dialog_window", u"Username   ", None))
        self.username_input.setText(QCoreApplication.translate("login_dialog_window", u"admin", None))
        self.login_error_lbl.setText(QCoreApplication.translate("login_dialog_window", u"Error", None))
        self.login_btn.setText(QCoreApplication.translate("login_dialog_window", u"Login", None))
    # retranslateUi

