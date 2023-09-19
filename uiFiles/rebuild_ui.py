# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rebuild.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import Assets_rc

class Ui_rebuild_win(object):
    def setupUi(self, rebuild_win):
        if not rebuild_win.objectName():
            rebuild_win.setObjectName(u"rebuild_win")
        rebuild_win.resize(700, 226)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rebuild_win.sizePolicy().hasHeightForWidth())
        rebuild_win.setSizePolicy(sizePolicy)
        rebuild_win.setMinimumSize(QSize(700, 200))
        rebuild_win.setMaximumSize(QSize(700, 300))
        rebuild_win.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	font-size: 14px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#rebuild_win{\n"
"	background-color: #ffffff;\n"
"	border: 2px solid rgb(77, 77, 77);\n"
"	border-radius: 10px;\n"
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
"color: #404040;\n"
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
"/************"
                        "*******************************/\n"
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
"	image: url(:/assets/Assets/icons/icons8-arrow-48.png);\n"
"	width: 15px;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 background-color: rgb(2"
                        "38, 134, 44);\n"
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
        self.verticalLayout = QVBoxLayout(rebuild_win)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(rebuild_win)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	padding:3px;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border: 2px solid #404040;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/Assets/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 20)
        self.label = QLabel(rebuild_win)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.converting_progressbar = QProgressBar(rebuild_win)
        self.converting_progressbar.setObjectName(u"converting_progressbar")
        self.converting_progressbar.setValue(0)

        self.verticalLayout_2.addWidget(self.converting_progressbar)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rebuild_btn = QPushButton(rebuild_win)
        self.rebuild_btn.setObjectName(u"rebuild_btn")
        self.rebuild_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.rebuild_btn)

        self.close_btn22 = QPushButton(rebuild_win)
        self.close_btn22.setObjectName(u"close_btn22")
        self.close_btn22.setEnabled(False)
        self.close_btn22.setStyleSheet(u"QPushButton{\n"
"max-width: 200px;\n"
"background-color: rgb(197, 63, 59);\n"
"color:#ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: rgb(220, 220, 220);\n"
"color:#909090;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(152, 46, 44);\n"
"color:#ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.close_btn22)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(rebuild_win)

        QMetaObject.connectSlotsByName(rebuild_win)
    # setupUi

    def retranslateUi(self, rebuild_win):
        rebuild_win.setWindowTitle(QCoreApplication.translate("rebuild_win", u"Edit User", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("rebuild_win", u"You edit some standards, You should rebuild your database ", None))
        self.rebuild_btn.setText(QCoreApplication.translate("rebuild_win", u"Rebuild", None))
        self.close_btn22.setText(QCoreApplication.translate("rebuild_win", u"Close", None))
    # retranslateUi

