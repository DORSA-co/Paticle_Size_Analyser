# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_result.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import Assets_rc

class Ui_rebuild_win(object):
    def setupUi(self, rebuild_win):
        if not rebuild_win.objectName():
            rebuild_win.setObjectName(u"rebuild_win")
        rebuild_win.resize(700, 596)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rebuild_win.sizePolicy().hasHeightForWidth())
        rebuild_win.setSizePolicy(sizePolicy)
        rebuild_win.setMinimumSize(QSize(700, 200))
        rebuild_win.setMaximumSize(QSize(700, 1200))
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-compare-50.png", QSize(), QIcon.Normal, QIcon.Off)
        rebuild_win.setWindowIcon(icon)
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
"	border: 5px solid rgb(77, 77, 77);\n"
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
"margin: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border: 2px solid #404040;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 20)
        self.label_2 = QLabel(rebuild_win)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size:22px;\n"
"font-weight: bold;\n"
"color:rgb(12, 80, 139);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.message_lbl = QLabel(rebuild_win)
        self.message_lbl.setObjectName(u"message_lbl")
        self.message_lbl.setStyleSheet(u"margin: 10px 0px 0px 20px;")
        self.message_lbl.setAlignment(Qt.AlignCenter)
        self.message_lbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.message_lbl, 0, Qt.AlignLeft)

        self.wrong_codes_frame = QFrame(rebuild_win)
        self.wrong_codes_frame.setObjectName(u"wrong_codes_frame")
        self.verticalLayout_3 = QVBoxLayout(self.wrong_codes_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.wrong_code_title = QLabel(self.wrong_codes_frame)
        self.wrong_code_title.setObjectName(u"wrong_code_title")
        self.wrong_code_title.setFont(font)
        self.wrong_code_title.setStyleSheet(u"font-size:22px;\n"
"font-weight: bold;")

        self.verticalLayout_3.addWidget(self.wrong_code_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.wrong_codes_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.wrong_count_lbl = QLabel(self.wrong_codes_frame)
        self.wrong_count_lbl.setObjectName(u"wrong_count_lbl")

        self.horizontalLayout_3.addWidget(self.wrong_count_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.wrong_codes_text_edit = QTextEdit(self.wrong_codes_frame)
        self.wrong_codes_text_edit.setObjectName(u"wrong_codes_text_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wrong_codes_text_edit.sizePolicy().hasHeightForWidth())
        self.wrong_codes_text_edit.setSizePolicy(sizePolicy1)
        self.wrong_codes_text_edit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.wrong_codes_text_edit)


        self.verticalLayout_2.addWidget(self.wrong_codes_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.exception_frame = QFrame(rebuild_win)
        self.exception_frame.setObjectName(u"exception_frame")
        self.verticalLayout_4 = QVBoxLayout(self.exception_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.exception_title = QLabel(self.exception_frame)
        self.exception_title.setObjectName(u"exception_title")
        self.exception_title.setFont(font)
        self.exception_title.setStyleSheet(u"font-size:22px;\n"
"font-weight: bold;")

        self.verticalLayout_4.addWidget(self.exception_title)

        self.exception_error = QTextEdit(self.exception_frame)
        self.exception_error.setObjectName(u"exception_error")
        sizePolicy1.setHeightForWidth(self.exception_error.sizePolicy().hasHeightForWidth())
        self.exception_error.setSizePolicy(sizePolicy1)
        self.exception_error.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.exception_error)


        self.verticalLayout_2.addWidget(self.exception_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_btn = QPushButton(rebuild_win)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setEnabled(True)
        self.ok_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"color:#ffffff;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.ok_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(rebuild_win)
        self.ok_btn.clicked.connect(rebuild_win.close)
        self.close_btn.clicked["bool"].connect(rebuild_win.close)

        QMetaObject.connectSlotsByName(rebuild_win)
    # setupUi

    def retranslateUi(self, rebuild_win):
        rebuild_win.setWindowTitle(QCoreApplication.translate("rebuild_win", u"Export", None))
        self.close_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("rebuild_win", u"Export", None))
        self.message_lbl.setText(QCoreApplication.translate("rebuild_win", u"massage", None))
        self.wrong_code_title.setText(QCoreApplication.translate("rebuild_win", u"invalid codes", None))
        self.label.setText(QCoreApplication.translate("rebuild_win", u"number of undefined codes:", None))
        self.wrong_count_lbl.setText(QCoreApplication.translate("rebuild_win", u"0", None))
        self.exception_title.setText(QCoreApplication.translate("rebuild_win", u"Exception", None))
        self.ok_btn.setText(QCoreApplication.translate("rebuild_win", u"Ok", None))
#if QT_CONFIG(shortcut)
        self.ok_btn.setShortcut(QCoreApplication.translate("rebuild_win", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

