# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QSpacerItem,
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

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 20)
        self.title_lbl = QLabel(rebuild_win)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setStyleSheet(u"font-size:22px;")
        self.title_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_lbl)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.description_lbl = QLabel(rebuild_win)
        self.description_lbl.setObjectName(u"description_lbl")
        self.description_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.description_lbl)

        self.progressbar = QProgressBar(rebuild_win)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressbar)

        self.progress_frame = QFrame(rebuild_win)
        self.progress_frame.setObjectName(u"progress_frame")
        self.horizontalLayout = QHBoxLayout(self.progress_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, -1, -1)
        self.complete_count_lbl = QLabel(self.progress_frame)
        self.complete_count_lbl.setObjectName(u"complete_count_lbl")

        self.horizontalLayout.addWidget(self.complete_count_lbl)

        self.label_2 = QLabel(self.progress_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.total_count_lbl = QLabel(self.progress_frame)
        self.total_count_lbl.setObjectName(u"total_count_lbl")

        self.horizontalLayout.addWidget(self.total_count_lbl)

        self.progress_operetion_lbl = QLabel(self.progress_frame)
        self.progress_operetion_lbl.setObjectName(u"progress_operetion_lbl")

        self.horizontalLayout.addWidget(self.progress_operetion_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.progress_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(rebuild_win)

        QMetaObject.connectSlotsByName(rebuild_win)
    # setupUi

    def retranslateUi(self, rebuild_win):
        rebuild_win.setWindowTitle(QCoreApplication.translate("rebuild_win", u"Edit User", None))
        self.title_lbl.setText(QCoreApplication.translate("rebuild_win", u"title", None))
        self.description_lbl.setText(QCoreApplication.translate("rebuild_win", u"bla bla bla", None))
        self.complete_count_lbl.setText(QCoreApplication.translate("rebuild_win", u"-", None))
        self.label_2.setText(QCoreApplication.translate("rebuild_win", u"/", None))
        self.total_count_lbl.setText(QCoreApplication.translate("rebuild_win", u"-", None))
        self.progress_operetion_lbl.setText(QCoreApplication.translate("rebuild_win", u"removed", None))
    # retranslateUi

