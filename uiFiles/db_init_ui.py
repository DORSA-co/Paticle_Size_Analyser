# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_init.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
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
"	background-color: rgb(50,50,50);\n"
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
"/*"
                        "******************************************/\n"
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
"background-color: rgb(20, 20, 20);\n"
"}")
        self.win_buttons.setFrameShape(QFrame.StyledPanel)
        self.win_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.win_buttons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.win_buttons)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(16777215, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/assets/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.win_buttons)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 40, 50, 25)
        self.pages = QStackedWidget(login_dialog_window)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"#page1,\n"
"#page2,\n"
"#page3\n"
"{\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page1)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.master_password_inpt = QLineEdit(self.page1)
        self.master_password_inpt.setObjectName(u"master_password_inpt")

        self.verticalLayout_3.addWidget(self.master_password_inpt)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.line = QFrame(self.page1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.label_7 = QLabel(self.page1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 50))
        self.label_7.setPixmap(QPixmap(u":/assets/icons/icons8-support-64.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.page1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 191, 0);")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_4 = QVBoxLayout(self.page2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 11, -1, -1)
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.widget_4 = QWidget(self.page2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_24 = QGridLayout(self.widget_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_35 = QLabel(self.widget_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_35, 0, 0, 1, 1)

        self.db_password_inpt = QLineEdit(self.widget_4)
        self.db_password_inpt.setObjectName(u"db_password_inpt")

        self.gridLayout_24.addWidget(self.db_password_inpt, 1, 1, 1, 1)

        self.db_username_inpt = QLineEdit(self.widget_4)
        self.db_username_inpt.setObjectName(u"db_username_inpt")

        self.gridLayout_24.addWidget(self.db_username_inpt, 0, 1, 1, 1)

        self.label_98 = QLabel(self.widget_4)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_98, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.label_3 = QLabel(self.page2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 191, 0);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 14, -1, -1)
        self.label_102 = QLabel(self.page2)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_102, 0, 0, 1, 1)

        self.db_host_inpt = QLineEdit(self.page2)
        self.db_host_inpt.setObjectName(u"db_host_inpt")

        self.gridLayout.addWidget(self.db_host_inpt, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pages.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_5 = QVBoxLayout(self.page3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.page3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/assets/icons/icons8-check-150.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_4 = QLabel(self.page3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")
        self.label_4.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.pages.addWidget(self.page3)

        self.verticalLayout_2.addWidget(self.pages)

        self.error_lbl = QLabel(login_dialog_window)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"background-color: rgb(197, 63, 59);\n"
"padding: 5px;")
        self.error_lbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.error_lbl)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.prev_btn = QPushButton(login_dialog_window)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color:#ffffff;\n"
"	background-color: rgb(19, 165, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.prev_btn)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.next_btn = QPushButton(login_dialog_window)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color:#ffffff;\n"
"	background-color: rgb(19, 165, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.next_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(login_dialog_window)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(login_dialog_window)
    # setupUi

    def retranslateUi(self, login_dialog_window):
        login_dialog_window.setWindowTitle(QCoreApplication.translate("login_dialog_window", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("login_dialog_window", u"Input your master password", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("login_dialog_window", u"If you forget your master password, please contact to Dorsa support", None))
        self.label_2.setText(QCoreApplication.translate("login_dialog_window", u"Please insert database information", None))
        self.label_35.setText(QCoreApplication.translate("login_dialog_window", u"Username:", None))
        self.label_98.setText(QCoreApplication.translate("login_dialog_window", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("login_dialog_window", u"Warning: almost you don't need to change host", None))
        self.label_102.setText(QCoreApplication.translate("login_dialog_window", u"Host:", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("login_dialog_window", u"Database Initial successfully. click on finish and run the software again", None))
        self.error_lbl.setText("")
        self.prev_btn.setText(QCoreApplication.translate("login_dialog_window", u"Previous", None))
        self.next_btn.setText(QCoreApplication.translate("login_dialog_window", u"Next", None))
    # retranslateUi

