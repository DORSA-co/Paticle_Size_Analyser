# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Assets_rc

class Ui_NodeSetting(object):
    def setupUi(self, NodeSetting):
        if not NodeSetting.objectName():
            NodeSetting.setObjectName(u"NodeSetting")
        NodeSetting.resize(984, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NodeSetting.sizePolicy().hasHeightForWidth())
        NodeSetting.setSizePolicy(sizePolicy)
        NodeSetting.setMinimumSize(QSize(0, 160))
        NodeSetting.setMaximumSize(QSize(16777215, 163))
        NodeSetting.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	\n"
"\n"
"}\n"
"\n"
"#NodeSetting{\n"
"	background-color:transparent;\n"
"\n"
"}\n"
"\n"
"QLabel[styleClass=\"title\"]{\n"
"	font-weight:bold;\n"
"}\n"
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
"    background-color: rgb(6, 76, 130);\n"
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
"    borde"
                        "r-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"\n"
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
"	 background-color: rgb(6, 76, 130);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled \n"
"{\n"
"	 background-color: rgb(210, 210, 210);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemVie"
                        "w {\n"
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
"/*********************************************/\n"
"\n"
"QDateEdit\n"
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
"QDateEdit:disabled ,\n"
"QDateEdit:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"\n"
"\n"
"QDateEdit::up-arrow\n"
"{   \n"
"	image: url(:/assets/icons/icons8-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::down-arrow \n"
"{   \n"
"	image: url(:/assets/icons/icons8-downtriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-b"
                        "utton\n"
"{\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: 30px;\n"
"}\n"
"\n"
"\n"
"QDateEdit::up-button:disabled ,\n"
"QDateEdit::down-button:disabled\n"
"    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"	background: rgb(241, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"\n"
"/*********************************************/\n"
"\n"
"QSpinBox, QDoubleSpinBox  \n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QSpinBox:enabled, QDoubleSpinBox:enabled{\n"
"color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"	color:(210, 210, 210);\n"
"}\n"
"\n"
"QSpinBox:focus , QDoubleSpinBox:focus\n"
"{\n"
"	background-color:red;\n"
"}\n"
"\n"
""
                        "QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/assets/icons/icons8-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/assets/icons/icons8-downtriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button   {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: 30px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus{\n"
"	background: rgb(241, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"\n"
"\n"
"/***********************************"
                        "********/\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	border:2px solid rgb(6, 76, 130);\n"
"	border-radius: 3px;\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image:url(:/assets/icons/icons8-check-50.png);\n"
"	background-color:rgb(6, 76, 130);\n"
"}\n"
"\n"
"/*******************************************/\n"
"QLineEdit\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
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
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(12, 80, 139, 255), stop:100 rgba(10, 66, 112, 255));\n"
"    width: 20px;\n"
"\n"
"\n"
""
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
"QTabBar::tab:!selected {\n"
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
"	selection-background-color: black"
                        ";\n"
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
"	background: #e4f0fa;\n"
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
        self.verticalLayout = QVBoxLayout(NodeSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainFrame = QFrame(NodeSetting)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"#mainFrame{\n"
"	background-color:#fff;\n"
"	border: 2px solid #a0a0a0;\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame = QFrame(self.mainFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.close_btn = QPushButton(self.horizontalFrame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"background-color:transparent;\n"
"min-width:30px;\n"
"max-width:30px;")
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-close-black-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.horizontalFrame_2 = QFrame(self.mainFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 30)
        self.label = QLabel(self.horizontalFrame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.node_name_input = QLineEdit(self.horizontalFrame_2)
        self.node_name_input.setObjectName(u"node_name_input")
        self.node_name_input.setMaximumSize(QSize(300, 16777215))
        self.node_name_input.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.node_name_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.node_type_combobox = QComboBox(self.horizontalFrame_2)
        self.node_type_combobox.addItem("")
        self.node_type_combobox.addItem("")
        self.node_type_combobox.setObjectName(u"node_type_combobox")

        self.horizontalLayout_2.addWidget(self.node_type_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.horizontalFrame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalFrame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.node_ns = QLineEdit(self.horizontalFrame_2)
        self.node_ns.setObjectName(u"node_ns")
        self.node_ns.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.node_ns)

        self.label_4 = QLabel(self.horizontalFrame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.node_i = QLineEdit(self.horizontalFrame_2)
        self.node_i.setObjectName(u"node_i")
        self.node_i.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.node_i)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.horizontalFrame_2)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(NodeSetting)

        QMetaObject.connectSlotsByName(NodeSetting)
    # setupUi

    def retranslateUi(self, NodeSetting):
        NodeSetting.setWindowTitle(QCoreApplication.translate("NodeSetting", u"Form", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("NodeSetting", u"Node Name: ", None))
        self.label.setProperty("styleClass", QCoreApplication.translate("NodeSetting", u"title", None))
        self.node_type_combobox.setItemText(0, QCoreApplication.translate("NodeSetting", u"writable", None))
        self.node_type_combobox.setItemText(1, QCoreApplication.translate("NodeSetting", u"readable", None))

        self.label_2.setText(QCoreApplication.translate("NodeSetting", u"Node Address:", None))
        self.label_2.setProperty("styleClass", QCoreApplication.translate("NodeSetting", u"title", None))
        self.label_3.setText(QCoreApplication.translate("NodeSetting", u"ns", None))
        self.node_ns.setText(QCoreApplication.translate("NodeSetting", u"555", None))
        self.label_4.setText(QCoreApplication.translate("NodeSetting", u"i:", None))
    # retranslateUi

