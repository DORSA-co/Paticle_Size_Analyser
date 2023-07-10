# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import Assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1337, 878)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/Icons/app_logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
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
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color:rgb(22, 38, 76)\n"
"\n"
"}\n"
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
"QComboBox:disabled\n"
"{\n"
"	border:2px solid rgb(210, 210, 210);\n"
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
"	 background-color: rgb(6, 76, 130);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled \n"
"{\n"
"	 background-color: rgb(21"
                        "0, 210, 210);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"    selection-background-color: rgb(6, 76, 130);\n"
"	selection-color: #ffffff;\n"
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
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"QSpinBox:focus , QDoubleSpinBox:focus\n"
"{\n"
"	background-color:red;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
""
                        "}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/assets/Assets/icons/icons8-downtriangle-48.png);\n"
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
"/*******************************************/\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	border:2px solid rgb(6, 76, 130);\n"
"	border-radius: 3px;\n"
""
                        "	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image:url(:/assets/Assets/icons/icons8-check-50.png);\n"
"	background-color:rgb(6, 76, 130);\n"
"}\n"
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
"QTabBar::tab:!selected {\n"
"	"
                        "border-left: 1px solid rgb(199, 199, 199);\n"
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
"	background: #e4f0fa;\n"
"}\n"
"\n"
"QTimeEdit:foc"
                        "us {\n"
"	color: white;\n"
"	background: #0078D7;\n"
"	selection-background-color: black;\n"
"}\n"
"\n"
"QListView::item{\n"
"	height: 30px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setCursor(QCursor(Qt.OpenHandCursor))
        self.header.setStyleSheet(u"QFrame{\n"
"	background: #0C508B;\n"
"}\n"
"")
        self.header.setFrameShape(QFrame.WinPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dorsa_logo = QLabel(self.frame_5)
        self.dorsa_logo.setObjectName(u"dorsa_logo")
        self.dorsa_logo.setMaximumSize(QSize(110, 16777215))
        self.dorsa_logo.setPixmap(QPixmap(u":/assets/Assets/general/dorsa_white.png"))
        self.dorsa_logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.dorsa_logo)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background:white")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.title = QLabel(self.frame_5)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-size: 14pt;\n"
"	font-weight: bold;\n"
"}")

        self.horizontalLayout_3.addWidget(self.title)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.win_buttons = QFrame(self.header)
        self.win_buttons.setObjectName(u"win_buttons")
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
"background-color: rgb(31, 32, 85, 100);\n"
" }")
        self.win_buttons.setFrameShape(QFrame.StyledPanel)
        self.win_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.win_buttons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.win_buttons)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(16777215, 40))
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/Assets/general/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.win_buttons)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setEnabled(True)
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(16777215, 40))
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/Assets/general/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.win_buttons)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(16777215, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/Assets/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.close_btn)


        self.horizontalLayout_4.addWidget(self.win_buttons)


        self.verticalLayout.addWidget(self.header)

        self.middle = QFrame(self.centralwidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setFrameShape(QFrame.NoFrame)
        self.middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.middle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.middle)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(150, 16777215))
        self.sidebar.setStyleSheet(u"QFrame#sidebar{\n"
"background-color:rgb(6, 76, 130);\n"
"min-width:150px;\n"
"max-width:150px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	color: #ffffff;\n"
"	min-height: 40px;\n"
"	text-align: left;\n"
"    margin-left:15px;\n"
"	icon-size:25px;\n"
"	background-color:rgb(0,0,0,0);\n"
"	min-width:150px;\n"
"max-width:150px;\n"
"    }\n"
"\n"
"    QPushButton:hover{\n"
"    font-size:14px; \n"
"font-weight:bold;\n"
"}\n"
"\n"
"Line{\n"
"	max-width: 120px;\n"
"	background-color:rgba(255, 255, 255, 50);\n"
"	margin: 0 15px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sidebar_main_btn = QPushButton(self.sidebar)
        self.sidebar_main_btn.setObjectName(u"sidebar_main_btn")
        icon4 = QIcon()
        icon4.addFile(u":/assets/Assets/icons/icons8-home-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_main_btn.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.sidebar_main_btn)

        self.line_3 = QFrame(self.sidebar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.pushButton = QPushButton(self.sidebar)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/assets/Assets/icons/icons8-login-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.line_13 = QFrame(self.sidebar)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_13)

        self.sidebar_report_btn = QPushButton(self.sidebar)
        self.sidebar_report_btn.setObjectName(u"sidebar_report_btn")
        icon6 = QIcon()
        icon6.addFile(u":/assets/Assets/icons/report-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_report_btn.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.sidebar_report_btn)

        self.line_4 = QFrame(self.sidebar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.sidebar_settings_btn = QPushButton(self.sidebar)
        self.sidebar_settings_btn.setObjectName(u"sidebar_settings_btn")
        icon7 = QIcon()
        icon7.addFile(u":/assets/Assets/icons/icons8-settings-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_settings_btn.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.sidebar_settings_btn)

        self.line_5 = QFrame(self.sidebar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.sidebar_calib_btn = QPushButton(self.sidebar)
        self.sidebar_calib_btn.setObjectName(u"sidebar_calib_btn")
        icon8 = QIcon()
        icon8.addFile(u":/assets/Assets/icons/icons8-ruler-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_calib_btn.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.sidebar_calib_btn)

        self.line_6 = QFrame(self.sidebar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.sidebar_users_btn = QPushButton(self.sidebar)
        self.sidebar_users_btn.setObjectName(u"sidebar_users_btn")
        icon9 = QIcon()
        icon9.addFile(u":/assets/Assets/icons/icons8-users-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_users_btn.setIcon(icon9)

        self.verticalLayout_2.addWidget(self.sidebar_users_btn)

        self.line_7 = QFrame(self.sidebar)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.sidebar_help_btn = QPushButton(self.sidebar)
        self.sidebar_help_btn.setObjectName(u"sidebar_help_btn")
        icon10 = QIcon()
        icon10.addFile(u":/assets/Assets/icons/icons8-question-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_help_btn.setIcon(icon10)

        self.verticalLayout_2.addWidget(self.sidebar_help_btn)

        self.line_8 = QFrame(self.sidebar)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.main_pages_stackw = QStackedWidget(self.middle)
        self.main_pages_stackw.setObjectName(u"main_pages_stackw")
        self.main_pages_stackw.setMouseTracking(False)
        self.main_pages_stackw.setStyleSheet(u"#main_page,\n"
"#report_page,\n"
"#settings_page,\n"
"#calibration_page,\n"
"#users_page,\n"
"#help_page,\n"
"#single_report_page\n"
" {\n"
"	background-color: #ffffff;\n"
"}\n"
"")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_2 = QHBoxLayout(self.main_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainpage_left_frame_2 = QFrame(self.main_page)
        self.mainpage_left_frame_2.setObjectName(u"mainpage_left_frame_2")
        self.mainpage_left_frame_2.setMaximumSize(QSize(700, 16777215))
        self.mainpage_left_frame = QVBoxLayout(self.mainpage_left_frame_2)
        self.mainpage_left_frame.setObjectName(u"mainpage_left_frame")
        self.mainpage_left_frame.setContentsMargins(0, 0, 0, 0)
        self.mainpage_toolbox_frame = QFrame(self.mainpage_left_frame_2)
        self.mainpage_toolbox_frame.setObjectName(u"mainpage_toolbox_frame")
        self.mainpage_toolbox_frame.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"		\n"
"}\n"
"\n"
"#mainpage_toolbox_frame\n"
"{\n"
"	max-height:50px;\n"
"}\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.mainpage_toolbox_frame)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_36 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_36)

        self.mainpage_liveview_checkbox = QCheckBox(self.mainpage_toolbox_frame)
        self.mainpage_liveview_checkbox.setObjectName(u"mainpage_liveview_checkbox")
        self.mainpage_liveview_checkbox.setLayoutDirection(Qt.RightToLeft)
        icon11 = QIcon()
        icon11.addFile(u":/assets/Assets/icons/icons8-video-call-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_liveview_checkbox.setIcon(icon11)
        self.mainpage_liveview_checkbox.setIconSize(QSize(40, 40))
        self.mainpage_liveview_checkbox.setChecked(True)

        self.horizontalLayout_23.addWidget(self.mainpage_liveview_checkbox)

        self.horizontalSpacer_28 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_28)

        self.line_16 = QFrame(self.mainpage_toolbox_frame)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_23.addWidget(self.line_16)

        self.horizontalSpacer_37 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_37)

        self.mainpage_drawing_checkbox = QCheckBox(self.mainpage_toolbox_frame)
        self.mainpage_drawing_checkbox.setObjectName(u"mainpage_drawing_checkbox")
        self.mainpage_drawing_checkbox.setLayoutDirection(Qt.RightToLeft)
        icon12 = QIcon()
        icon12.addFile(u":/assets/Assets/icons/icons8-draw-pen-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_drawing_checkbox.setIcon(icon12)
        self.mainpage_drawing_checkbox.setIconSize(QSize(35, 35))
        self.mainpage_drawing_checkbox.setChecked(True)

        self.horizontalLayout_23.addWidget(self.mainpage_drawing_checkbox)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)


        self.mainpage_left_frame.addWidget(self.mainpage_toolbox_frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.mainpage_live_image_lbl = QLabel(self.mainpage_left_frame_2)
        self.mainpage_live_image_lbl.setObjectName(u"mainpage_live_image_lbl")
        self.mainpage_live_image_lbl.setMaximumSize(QSize(704, 704))
        self.mainpage_live_image_lbl.setStyleSheet(u"border: 2px solid rgb(45, 86, 136);\n"
"border-radius: 8px;\n"
"margin: 0px;\n"
"max-width:700px;\n"
"max-height:700px;\n"
"\n"
"background-color:rgb(50, 50, 50);")
        self.mainpage_live_image_lbl.setTextFormat(Qt.AutoText)
        self.mainpage_live_image_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.mainpage_live_image_lbl.setScaledContents(False)
        self.mainpage_live_image_lbl.setAlignment(Qt.AlignCenter)
        self.mainpage_live_image_lbl.setWordWrap(False)
        self.mainpage_live_image_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.mainpage_live_image_lbl)


        self.mainpage_left_frame.addLayout(self.horizontalLayout_6)

        self.mainpage_livebox_frame = QFrame(self.mainpage_left_frame_2)
        self.mainpage_livebox_frame.setObjectName(u"mainpage_livebox_frame")
        self.mainpage_livebox_frame.setStyleSheet(u"")
        self.mainpage_livebox_frame.setFrameShape(QFrame.StyledPanel)
        self.mainpage_livebox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainpage_livebox_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 5, 5)
        self.horizontalFrame = QFrame(self.mainpage_livebox_frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u".QPushButton{\n"
"	border-radius:3px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(22, 38, 76)\n"
"	\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"	background-color: rgb(4, 3, 29)\n"
"	\n"
"}\n"
".QPushButton:disabled {\n"
"background-color:rgb(147, 147, 147);\n"
"}\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mainpage_start_btn = QPushButton(self.horizontalFrame)
        self.mainpage_start_btn.setObjectName(u"mainpage_start_btn")
        self.mainpage_start_btn.setEnabled(True)
        self.mainpage_start_btn.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/assets/Assets/icons/play-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_start_btn.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.mainpage_start_btn)

        self.mainpage_faststart_btn = QPushButton(self.horizontalFrame)
        self.mainpage_faststart_btn.setObjectName(u"mainpage_faststart_btn")
        self.mainpage_faststart_btn.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/assets/Assets/icons/fast-forwards-arrow-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_faststart_btn.setIcon(icon14)

        self.horizontalLayout_5.addWidget(self.mainpage_faststart_btn)

        self.mainpage_stop_btn = QPushButton(self.horizontalFrame)
        self.mainpage_stop_btn.setObjectName(u"mainpage_stop_btn")
        self.mainpage_stop_btn.setEnabled(False)
        self.mainpage_stop_btn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/assets/Assets/icons/stop50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_stop_btn.setIcon(icon15)

        self.horizontalLayout_5.addWidget(self.mainpage_stop_btn)


        self.verticalLayout_5.addWidget(self.horizontalFrame)

        self.mainpage_informaition_groupBox = QGroupBox(self.mainpage_livebox_frame)
        self.mainpage_informaition_groupBox.setObjectName(u"mainpage_informaition_groupBox")
        self.mainpage_informaition_groupBox.setStyleSheet(u"#mainpage_informaition_groupBox{\n"
"font-size: 18px;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 14px;\n"
"	margin: 5px 0px;\n"
"	color: rgb(53, 53, 53);\n"
"}")
        self.gridLayout_12 = QGridLayout(self.mainpage_informaition_groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(5)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(-1, 10, -1, 6)
        self.label_5 = QLabel(self.mainpage_informaition_groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_30, 1, 2, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_42, 3, 5, 1, 1)

        self.label_35 = QLabel(self.mainpage_informaition_groupBox)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_12.addWidget(self.label_35, 3, 4, 1, 1)

        self.label_37 = QLabel(self.mainpage_informaition_groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_12.addWidget(self.label_37, 3, 7, 1, 1)

        self.mainpage_fps_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_fps_lbl.setObjectName(u"mainpage_fps_lbl")

        self.gridLayout_12.addWidget(self.mainpage_fps_lbl, 3, 1, 1, 1)

        self.label_12 = QLabel(self.mainpage_informaition_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_12, 1, 3, 1, 1)

        self.label_34 = QLabel(self.mainpage_informaition_groupBox)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_34, 3, 3, 1, 1)

        self.mainpage_std_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_std_lbl.setObjectName(u"mainpage_std_lbl")

        self.gridLayout_12.addWidget(self.mainpage_std_lbl, 1, 4, 1, 1)

        self.label_33 = QLabel(self.mainpage_informaition_groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_33, 3, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_40, 1, 8, 1, 1)

        self.label_36 = QLabel(self.mainpage_informaition_groupBox)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;\n"
"")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_36, 3, 6, 1, 1)

        self.mainpage_avrage_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_avrage_lbl.setObjectName(u"mainpage_avrage_lbl")

        self.gridLayout_12.addWidget(self.mainpage_avrage_lbl, 1, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_31, 1, 5, 1, 1)

        self.mainpage_mean_oval_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_mean_oval_lbl.setObjectName(u"mainpage_mean_oval_lbl")

        self.gridLayout_12.addWidget(self.mainpage_mean_oval_lbl, 1, 7, 1, 1)

        self.label_3 = QLabel(self.mainpage_informaition_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;\n"
"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_3, 1, 6, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_41, 3, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.mainpage_informaition_groupBox)

        self.mainpage_report_button = QPushButton(self.mainpage_livebox_frame)
        self.mainpage_report_button.setObjectName(u"mainpage_report_button")
        self.mainpage_report_button.setStyleSheet(u".QPushButton{\n"
"	min-height:40px;\n"
"	border-radius:3px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(147, 147, 147);\n"
"	max-width: 200px;\n"
"}\n"
"\n"
"")
        self.mainpage_report_button.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.mainpage_report_button)


        self.mainpage_left_frame.addWidget(self.mainpage_livebox_frame)


        self.horizontalLayout_2.addWidget(self.mainpage_left_frame_2)

        self.line_9 = QFrame(self.main_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_9)

        self.mainpage_right_frame = QFrame(self.main_page)
        self.mainpage_right_frame.setObjectName(u"mainpage_right_frame")
        self.mainpage_right_frame.setMinimumSize(QSize(500, 0))
        self.left_main_page_ = QVBoxLayout(self.mainpage_right_frame)
        self.left_main_page_.setSpacing(0)
        self.left_main_page_.setObjectName(u"left_main_page_")
        self.left_main_page_.setContentsMargins(11, 0, -1, 5)
        self.mainpage_warnings_frame = QFrame(self.mainpage_right_frame)
        self.mainpage_warnings_frame.setObjectName(u"mainpage_warnings_frame")
        self.mainpage_warnings_frame.setMinimumSize(QSize(0, 80))
        self.mainpage_warnings_frame.setMaximumSize(QSize(16777215, 130))
        self.mainpage_warnings_frame.setStyleSheet(u"#mainpage_warnings_frame{\n"
"	background-color:rgb(49, 49, 49);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QGroupBox {\n"
"\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"	\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border: 1px solid rgb(150, 150, 150);\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	max-height: 40px;\n"
"	min-height: 40px;\n"
"\n"
"	max-width: 40px;\n"
"	min-width: 40px;\n"
"\n"
"	margin: 0px auto;\n"
"	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mainpage_warnings_frame.setFrameShape(QFrame.StyledPanel)
        self.mainpage_warnings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainpage_warnings_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.mainpage_warnings_frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.mainpage_illumination_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_illumination_warning_btn.setObjectName(u"mainpage_illumination_warning_btn")
        self.mainpage_illumination_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/assets/Assets/icons/icons8-headlight-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_illumination_warning_btn.setIcon(icon16)
        self.mainpage_illumination_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_illumination_warning_btn, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)

        self.mainpage_tempreture_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_tempreture_warning_btn.setObjectName(u"mainpage_tempreture_warning_btn")
        self.mainpage_tempreture_warning_btn.setMinimumSize(QSize(114, 40))
        self.mainpage_tempreture_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainpage_tempreture_warning_btn.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/assets/Assets/icons/icons8-thermometer-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_tempreture_warning_btn.setIcon(icon17)
        self.mainpage_tempreture_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_tempreture_warning_btn, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 2, 3, 1, 1)

        self.mainpage_camera_connection_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_camera_connection_warning_btn.setObjectName(u"mainpage_camera_connection_warning_btn")
        self.mainpage_camera_connection_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/assets/Assets/icons/icons8-connection-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_camera_connection_warning_btn.setIcon(icon18)
        self.mainpage_camera_connection_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_camera_connection_warning_btn, 0, 2, 1, 1)

        self.mainpage_camera_grabbing_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_camera_grabbing_warning_btn.setObjectName(u"mainpage_camera_grabbing_warning_btn")
        self.mainpage_camera_grabbing_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainpage_camera_grabbing_warning_btn.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/assets/Assets/icons/icons8-camera-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_camera_grabbing_warning_btn.setIcon(icon19)
        self.mainpage_camera_grabbing_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_camera_grabbing_warning_btn, 0, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.mainpage_warning_massage_lbl = QLabel(self.mainpage_warnings_frame)
        self.mainpage_warning_massage_lbl.setObjectName(u"mainpage_warning_massage_lbl")
        self.mainpage_warning_massage_lbl.setStyleSheet(u"color:rgb(255, 204, 2);\n"
"padding-left:15px;")

        self.verticalLayout_7.addWidget(self.mainpage_warning_massage_lbl)


        self.left_main_page_.addWidget(self.mainpage_warnings_frame)

        self.verticalSpacer_18 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.left_main_page_.addItem(self.verticalSpacer_18)

        self.label = QLabel(self.mainpage_right_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;\n"
"color:rgb(52, 52, 52)")
        self.label.setAlignment(Qt.AlignCenter)

        self.left_main_page_.addWidget(self.label)

        self.mainpage_grading_chart_frame = QHBoxLayout()
        self.mainpage_grading_chart_frame.setObjectName(u"mainpage_grading_chart_frame")
        self.mainpage_grading_chart_frame.setContentsMargins(9, 0, -1, -1)

        self.left_main_page_.addLayout(self.mainpage_grading_chart_frame)

        self.widget = QWidget(self.mainpage_right_frame)
        self.widget.setObjectName(u"widget")

        self.left_main_page_.addWidget(self.widget)

        self.line_2 = QFrame(self.mainpage_right_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.left_main_page_.addWidget(self.line_2)

        self.label_2 = QLabel(self.mainpage_right_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;\n"
"color:rgb(52, 52, 52)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.left_main_page_.addWidget(self.label_2)

        self.mainpage_second_chart_frame = QHBoxLayout()
        self.mainpage_second_chart_frame.setObjectName(u"mainpage_second_chart_frame")

        self.left_main_page_.addLayout(self.mainpage_second_chart_frame)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_main_page_.addItem(self.verticalSpacer_17)


        self.horizontalLayout_2.addWidget(self.mainpage_right_frame)

        self.main_pages_stackw.addWidget(self.main_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.main_pages_stackw.addWidget(self.report_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"*{color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"	font-size: 18px;	\n"
"	border: 1px solid rgba(6, 76, 130, 120);\n"
"	border-radius: 5px;\n"
"	margin-bottom: 30px;\n"
"	padding-top: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.settingpage_tabs = QTabWidget(self.settings_page)
        self.settingpage_tabs.setObjectName(u"settingpage_tabs")
        self.settingpage_tabs.setAutoFillBackground(False)
        self.settingpage_tabs.setStyleSheet(u"\n"
"\n"
"QLabel\n"
"{\n"
"	font-size: 14px;\n"
"	max-width:80px;\n"
"	min-width:80px;\n"
"	margin-left:10px;\n"
"}\n"
"\n"
"QComboBox, QSpinBox, QDoubleSpinBox, QLineEdit\n"
"{\n"
"	max-width:280px;\n"
"	min-width:200px;\n"
"}\n"
"\n"
"#settingpage_camera_tab,\n"
"#settingpage_general_tab, \n"
"#settingpage_pelletizing_tab,\n"
"#settingpage_algorithm_tab\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.settingpage_tabs.setTabPosition(QTabWidget.North)
        self.settingpage_tabs.setTabShape(QTabWidget.Rounded)
        self.settingpage_tabs.setDocumentMode(False)
        self.settingpage_tabs.setTabsClosable(False)
        self.settingpage_tabs.setMovable(False)
        self.settingpage_tabs.setTabBarAutoHide(False)
        self.settingpage_general_tab = QWidget()
        self.settingpage_general_tab.setObjectName(u"settingpage_general_tab")
        self.gridLayout_4 = QGridLayout(self.settingpage_general_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.settingpage_general_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_17, 0, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_25, 1, 0, 1, 1)

        self.settingpage_general_language_combobox = QComboBox(self.groupBox)
        self.settingpage_general_language_combobox.addItem("")
        self.settingpage_general_language_combobox.addItem("")
        self.settingpage_general_language_combobox.setObjectName(u"settingpage_general_language_combobox")

        self.gridLayout_10.addWidget(self.settingpage_general_language_combobox, 2, 2, 1, 1)

        self.settingpage_general_color_combobox = QComboBox(self.groupBox)
        self.settingpage_general_color_combobox.setObjectName(u"settingpage_general_color_combobox")

        self.gridLayout_10.addWidget(self.settingpage_general_color_combobox, 1, 2, 1, 1)

        self.settingpage_general_font_combobox = QComboBox(self.groupBox)
        self.settingpage_general_font_combobox.setObjectName(u"settingpage_general_font_combobox")

        self.gridLayout_10.addWidget(self.settingpage_general_font_combobox, 0, 2, 1, 1)

        self.label_30 = QLabel(self.groupBox)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_23, 0, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_32, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.settingpage_general_tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"max-width: 300px;")

        self.gridLayout_11.addWidget(self.label_32, 1, 4, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_5)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(365)

        self.gridLayout_11.addWidget(self.spinBox_2, 1, 5, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_23, 1, 6, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.gridLayout_11.addWidget(self.checkBox, 1, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_21, 1, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_11.addWidget(self.label_31, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.horizontalFrame_3 = QFrame(self.settingpage_general_tab)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setStyleSheet(u"color: #ffffff;")
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 28, -1, -1)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.pushButton_12 = QPushButton(self.horizontalFrame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_21.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.horizontalFrame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_21.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.horizontalFrame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_21.addWidget(self.pushButton_10)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)


        self.gridLayout_4.addWidget(self.horizontalFrame_3, 2, 0, 1, 1)

        self.settingpage_tabs.addTab(self.settingpage_general_tab, "")
        self.settingpage_grading_tab = QWidget()
        self.settingpage_grading_tab.setObjectName(u"settingpage_grading_tab")
        self.horizontalLayout_22 = QHBoxLayout(self.settingpage_grading_tab)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.groupBox_4 = QGroupBox(self.settingpage_grading_tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_24.addWidget(self.label_27)

        self.settingpage_grading_name_inpt = QLineEdit(self.groupBox_4)
        self.settingpage_grading_name_inpt.setObjectName(u"settingpage_grading_name_inpt")
        self.settingpage_grading_name_inpt.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.settingpage_grading_name_inpt)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_8 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_22.addItem(self.verticalSpacer_8)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.settingpage_grading_up_limit_spinbox = QDoubleSpinBox(self.groupBox_4)
        self.settingpage_grading_up_limit_spinbox.setObjectName(u"settingpage_grading_up_limit_spinbox")
        self.settingpage_grading_up_limit_spinbox.setStyleSheet(u"max-width:100px;\n"
"min-width: 50px;")
        self.settingpage_grading_up_limit_spinbox.setMaximum(25.000000000000000)

        self.gridLayout_13.addWidget(self.settingpage_grading_up_limit_spinbox, 0, 4, 1, 1)

        self.settingpage_grading_low_limit_spinbox = QDoubleSpinBox(self.groupBox_4)
        self.settingpage_grading_low_limit_spinbox.setObjectName(u"settingpage_grading_low_limit_spinbox")
        self.settingpage_grading_low_limit_spinbox.setStyleSheet(u"max-width:100px;\n"
"min-width: 50px;")
        self.settingpage_grading_low_limit_spinbox.setMaximum(25.000000000000000)

        self.gridLayout_13.addWidget(self.settingpage_grading_low_limit_spinbox, 0, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)

        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"max-width:300px;")

        self.gridLayout_13.addWidget(self.label_28, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_19, 0, 5, 1, 1)

        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"max-width:300px;")

        self.gridLayout_13.addWidget(self.label_29, 0, 3, 1, 1)

        self.settingpage_pelletizing_add_range_btn = QPushButton(self.groupBox_4)
        self.settingpage_pelletizing_add_range_btn.setObjectName(u"settingpage_pelletizing_add_range_btn")
        self.settingpage_pelletizing_add_range_btn.setMinimumSize(QSize(0, 35))
        self.settingpage_pelletizing_add_range_btn.setStyleSheet(u"#settingpage_pelletizing_add_range_btn{\n"
"background-color:rgba(255, 255, 255,0);\n"
"color: white;\n"
"max-width: 50px;\n"
"min-width: 0px;\n"
"\n"
"}\n"
"\n"
"#settingpage_pelletizing_add_range_btn:hover{\n"
"background-color:rgba(255, 255, 255,0);\n"
"border: 2px solid rgba(110, 188, 54,20);\n"
"border-radius: 200px;\n"
"\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/assets/Assets/icons/icons8-plus-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingpage_pelletizing_add_range_btn.setIcon(icon20)
        self.settingpage_pelletizing_add_range_btn.setIconSize(QSize(45, 45))

        self.gridLayout_13.addWidget(self.settingpage_pelletizing_add_range_btn, 0, 6, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_13)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_22.addItem(self.verticalSpacer_10)

        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"max-width: 200;\n"
"font-size:20px;\n"
"color:rgb(6, 76, 130);\n"
"font-weight:bold;")

        self.verticalLayout_22.addWidget(self.label_26)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(9, 18, -1, -1)
        self.settingpage_grading_ranges_table = QTableWidget(self.groupBox_4)
        if (self.settingpage_grading_ranges_table.columnCount() < 5):
            self.settingpage_grading_ranges_table.setColumnCount(5)
        if (self.settingpage_grading_ranges_table.rowCount() < 1):
            self.settingpage_grading_ranges_table.setRowCount(1)
        self.settingpage_grading_ranges_table.setObjectName(u"settingpage_grading_ranges_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingpage_grading_ranges_table.sizePolicy().hasHeightForWidth())
        self.settingpage_grading_ranges_table.setSizePolicy(sizePolicy)
        self.settingpage_grading_ranges_table.setSizeIncrement(QSize(0, 0))
        self.settingpage_grading_ranges_table.setBaseSize(QSize(0, 0))
        self.settingpage_grading_ranges_table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.settingpage_grading_ranges_table.setStyleSheet(u"\n"
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
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}\n"
"\n"
"")
        self.settingpage_grading_ranges_table.setFrameShape(QFrame.NoFrame)
        self.settingpage_grading_ranges_table.setFrameShadow(QFrame.Sunken)
        self.settingpage_grading_ranges_table.setLineWidth(1)
        self.settingpage_grading_ranges_table.setMidLineWidth(0)
        self.settingpage_grading_ranges_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.settingpage_grading_ranges_table.setAutoScroll(True)
        self.settingpage_grading_ranges_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.settingpage_grading_ranges_table.setTabKeyNavigation(True)
        self.settingpage_grading_ranges_table.setProperty("showDropIndicator", True)
        self.settingpage_grading_ranges_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.settingpage_grading_ranges_table.setTextElideMode(Qt.ElideMiddle)
        self.settingpage_grading_ranges_table.setShowGrid(True)
        self.settingpage_grading_ranges_table.setSortingEnabled(False)
        self.settingpage_grading_ranges_table.setRowCount(1)
        self.settingpage_grading_ranges_table.setColumnCount(5)
        self.settingpage_grading_ranges_table.verticalHeader().setVisible(False)

        self.horizontalLayout_28.addWidget(self.settingpage_grading_ranges_table)


        self.verticalLayout_22.addLayout(self.horizontalLayout_28)

        self.horizontalFrame_5 = QFrame(self.groupBox_4)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setStyleSheet(u"color: #ffffff;")
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 17, -1, -1)
        self.horizontalSpacer_24 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_24)

        self.settingpage_grading_save_btn = QPushButton(self.horizontalFrame_5)
        self.settingpage_grading_save_btn.setObjectName(u"settingpage_grading_save_btn")

        self.horizontalLayout_20.addWidget(self.settingpage_grading_save_btn)

        self.settingpage_grading_cancel_btn = QPushButton(self.horizontalFrame_5)
        self.settingpage_grading_cancel_btn.setObjectName(u"settingpage_grading_cancel_btn")

        self.horizontalLayout_20.addWidget(self.settingpage_grading_cancel_btn)

        self.horizontalSpacer_25 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)


        self.verticalLayout_22.addWidget(self.horizontalFrame_5)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)


        self.horizontalLayout_22.addWidget(self.groupBox_4)

        self.horizontalSpacer_18 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.groupBox_3 = QGroupBox(self.settingpage_grading_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.settingpage_grading_standards_table = QTableWidget(self.groupBox_3)
        self.settingpage_grading_standards_table.setObjectName(u"settingpage_grading_standards_table")
        self.settingpage_grading_standards_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_17.addWidget(self.settingpage_grading_standards_table)


        self.horizontalLayout_22.addWidget(self.groupBox_3)

        self.settingpage_tabs.addTab(self.settingpage_grading_tab, "")
        self.settingpage_camera_tab = QWidget()
        self.settingpage_camera_tab.setObjectName(u"settingpage_camera_tab")
        self.horizontalLayout_15 = QHBoxLayout(self.settingpage_camera_tab)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.settingpage_camera_left_side = QFrame(self.settingpage_camera_tab)
        self.settingpage_camera_left_side.setObjectName(u"settingpage_camera_left_side")
        self.settingpage_camera_left_side.setStyleSheet(u"")
        self.camera_setting_lef_side = QVBoxLayout(self.settingpage_camera_left_side)
        self.camera_setting_lef_side.setObjectName(u"camera_setting_lef_side")
        self.settingpage_connection_buttons_frame = QFrame(self.settingpage_camera_left_side)
        self.settingpage_connection_buttons_frame.setObjectName(u"settingpage_connection_buttons_frame")
        self.settingpage_connection_buttons_frame.setStyleSheet(u"QPushButton{\n"
"	width: 50px;\n"
"	min-width: 50px;\n"
"	max-width: 50px;\n"
"	background-color:rgb(48, 48, 48);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"\n"
"#settingpage_connection_buttons_frame\n"
"{\n"
"	margin-bottom: 20px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:rgb(175, 175, 175);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.settingpage_connection_buttons_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, -1)
        self.settingpage_camera_start_btn = QPushButton(self.settingpage_connection_buttons_frame)
        self.settingpage_camera_start_btn.setObjectName(u"settingpage_camera_start_btn")
        self.settingpage_camera_start_btn.setStyleSheet(u"")
        self.settingpage_camera_start_btn.setIcon(icon13)
        self.settingpage_camera_start_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_18.addWidget(self.settingpage_camera_start_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)


        self.camera_setting_lef_side.addWidget(self.settingpage_connection_buttons_frame)

        self.settingpage_camera_device_group = QGroupBox(self.settingpage_camera_left_side)
        self.settingpage_camera_device_group.setObjectName(u"settingpage_camera_device_group")
        self.settingpage_camera_device_group.setLayoutDirection(Qt.LeftToRight)
        self.settingpage_camera_device_group.setAutoFillBackground(False)
        self.gridLayout_7 = QGridLayout(self.settingpage_camera_device_group)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.settingpage_camera_device_lbl = QLabel(self.settingpage_camera_device_group)
        self.settingpage_camera_device_lbl.setObjectName(u"settingpage_camera_device_lbl")
        self.settingpage_camera_device_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.settingpage_camera_device_lbl, 0, 0, 1, 1)

        self.settingpage_camera_fps_lbl = QLabel(self.settingpage_camera_device_group)
        self.settingpage_camera_fps_lbl.setObjectName(u"settingpage_camera_fps_lbl")
        self.settingpage_camera_fps_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.settingpage_camera_fps_lbl, 1, 0, 1, 1)

        self.settingpage_camera_device_combobox = QComboBox(self.settingpage_camera_device_group)
        self.settingpage_camera_device_combobox.setObjectName(u"settingpage_camera_device_combobox")
        self.settingpage_camera_device_combobox.setEnabled(False)

        self.gridLayout_7.addWidget(self.settingpage_camera_device_combobox, 0, 2, 1, 1)

        self.settingpage_camera_fps_spinbox = QSpinBox(self.settingpage_camera_device_group)
        self.settingpage_camera_fps_spinbox.setObjectName(u"settingpage_camera_fps_spinbox")
        self.settingpage_camera_fps_spinbox.setEnabled(True)

        self.gridLayout_7.addWidget(self.settingpage_camera_fps_spinbox, 1, 2, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_33, 0, 1, 1, 1)


        self.camera_setting_lef_side.addWidget(self.settingpage_camera_device_group)

        self.settingpage_camera_control_group = QGroupBox(self.settingpage_camera_left_side)
        self.settingpage_camera_control_group.setObjectName(u"settingpage_camera_control_group")
        self.gridLayout_8 = QGridLayout(self.settingpage_camera_control_group)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.settingpage_camera_exposure_lbl = QLabel(self.settingpage_camera_control_group)
        self.settingpage_camera_exposure_lbl.setObjectName(u"settingpage_camera_exposure_lbl")
        self.settingpage_camera_exposure_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.settingpage_camera_exposure_lbl, 0, 0, 1, 1)

        self.settingpage_camera_exposure_spinbox = QSpinBox(self.settingpage_camera_control_group)
        self.settingpage_camera_exposure_spinbox.setObjectName(u"settingpage_camera_exposure_spinbox")

        self.gridLayout_8.addWidget(self.settingpage_camera_exposure_spinbox, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.settingpage_camera_gain_lbl = QLabel(self.settingpage_camera_control_group)
        self.settingpage_camera_gain_lbl.setObjectName(u"settingpage_camera_gain_lbl")
        self.settingpage_camera_gain_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.settingpage_camera_gain_lbl, 1, 0, 1, 1)

        self.settingpage_camera_gain_spinbox = QSpinBox(self.settingpage_camera_control_group)
        self.settingpage_camera_gain_spinbox.setObjectName(u"settingpage_camera_gain_spinbox")

        self.gridLayout_8.addWidget(self.settingpage_camera_gain_spinbox, 1, 2, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_34, 0, 1, 1, 1)


        self.camera_setting_lef_side.addWidget(self.settingpage_camera_control_group)

        self.settingpage_camera_AOI_group = QGroupBox(self.settingpage_camera_left_side)
        self.settingpage_camera_AOI_group.setObjectName(u"settingpage_camera_AOI_group")
        self.gridLayout_6 = QGridLayout(self.settingpage_camera_AOI_group)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.settingpage_camera_width_lbl = QLabel(self.settingpage_camera_AOI_group)
        self.settingpage_camera_width_lbl.setObjectName(u"settingpage_camera_width_lbl")
        self.settingpage_camera_width_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.settingpage_camera_width_lbl, 0, 0, 1, 1)

        self.settingpage_camera_height_lbl = QLabel(self.settingpage_camera_AOI_group)
        self.settingpage_camera_height_lbl.setObjectName(u"settingpage_camera_height_lbl")
        self.settingpage_camera_height_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.settingpage_camera_height_lbl, 1, 0, 1, 1)

        self.settingpage_camera_height_spinbox = QSpinBox(self.settingpage_camera_AOI_group)
        self.settingpage_camera_height_spinbox.setObjectName(u"settingpage_camera_height_spinbox")

        self.gridLayout_6.addWidget(self.settingpage_camera_height_spinbox, 1, 2, 1, 1)

        self.settingpage_camera_width_spinbox = QSpinBox(self.settingpage_camera_AOI_group)
        self.settingpage_camera_width_spinbox.setObjectName(u"settingpage_camera_width_spinbox")

        self.gridLayout_6.addWidget(self.settingpage_camera_width_spinbox, 0, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_14, 0, 3, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_35, 0, 1, 1, 1)


        self.camera_setting_lef_side.addWidget(self.settingpage_camera_AOI_group)

        self.horizontalFrame_2 = QFrame(self.settingpage_camera_left_side)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: #ffffff;\n"
"\n"
"}")
        self.settingpage_camera_connect_groupe = QHBoxLayout(self.horizontalFrame_2)
        self.settingpage_camera_connect_groupe.setObjectName(u"settingpage_camera_connect_groupe")
        self.settingpage_camera_connect_groupe.setContentsMargins(-1, 1, -1, -1)
        self.settingpage_camera_save_btn = QPushButton(self.horizontalFrame_2)
        self.settingpage_camera_save_btn.setObjectName(u"settingpage_camera_save_btn")

        self.settingpage_camera_connect_groupe.addWidget(self.settingpage_camera_save_btn)

        self.settingpage_camera_cancel_btn = QPushButton(self.horizontalFrame_2)
        self.settingpage_camera_cancel_btn.setObjectName(u"settingpage_camera_cancel_btn")

        self.settingpage_camera_connect_groupe.addWidget(self.settingpage_camera_cancel_btn)

        self.settingpage_camera_restore_btn = QPushButton(self.horizontalFrame_2)
        self.settingpage_camera_restore_btn.setObjectName(u"settingpage_camera_restore_btn")

        self.settingpage_camera_connect_groupe.addWidget(self.settingpage_camera_restore_btn)


        self.camera_setting_lef_side.addWidget(self.horizontalFrame_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.camera_setting_lef_side.addItem(self.verticalSpacer_5)


        self.horizontalLayout_15.addWidget(self.settingpage_camera_left_side)

        self.settingpage_camera_right_side = QVBoxLayout()
        self.settingpage_camera_right_side.setObjectName(u"settingpage_camera_right_side")
        self.settingpage_camera_live_lbl = QLabel(self.settingpage_camera_tab)
        self.settingpage_camera_live_lbl.setObjectName(u"settingpage_camera_live_lbl")
        self.settingpage_camera_live_lbl.setMinimumSize(QSize(10, 0))
        self.settingpage_camera_live_lbl.setMaximumSize(QSize(810, 800))
        self.settingpage_camera_live_lbl.setToolTipDuration(-2)
        self.settingpage_camera_live_lbl.setStyleSheet(u"min-width : 0;\n"
"max-width : 800px;\n"
"max-height : 800px;\n"
"")
        self.settingpage_camera_live_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.settingpage_camera_live_lbl.setScaledContents(False)
        self.settingpage_camera_live_lbl.setAlignment(Qt.AlignCenter)

        self.settingpage_camera_right_side.addWidget(self.settingpage_camera_live_lbl)

        self.horizontalFrame_4 = QFrame(self.settingpage_camera_tab)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setStyleSheet(u"QLabel\n"
"{\n"
"	width:auto;\n"
"	max-width: auto;\n"
"	min-width: 0px;\n"
"\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 19, -1, -1)
        self.label_13 = QLabel(self.horizontalFrame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(47, 0))
        self.label_13.setMaximumSize(QSize(47, 16777215))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.label_15 = QLabel(self.horizontalFrame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(47, 0))
        self.label_15.setMaximumSize(QSize(47, 16777215))

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)

        self.label_20 = QLabel(self.horizontalFrame_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.label_21 = QLabel(self.horizontalFrame_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_11)


        self.settingpage_camera_right_side.addWidget(self.horizontalFrame_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.settingpage_camera_right_side.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_15.addLayout(self.settingpage_camera_right_side)

        self.settingpage_tabs.addTab(self.settingpage_camera_tab, "")
        self.settingpage_algorithm_tab = QWidget()
        self.settingpage_algorithm_tab.setObjectName(u"settingpage_algorithm_tab")
        self.gridLayout_9 = QGridLayout(self.settingpage_algorithm_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.settingpage_algorithm_circularity_spinbox = QDoubleSpinBox(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_circularity_spinbox.setObjectName(u"settingpage_algorithm_circularity_spinbox")

        self.gridLayout_9.addWidget(self.settingpage_algorithm_circularity_spinbox, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.label_22 = QLabel(self.settingpage_algorithm_tab)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1)

        self.settingpage_algorithm_threshould_spinbox = QSpinBox(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_threshould_spinbox.setObjectName(u"settingpage_algorithm_threshould_spinbox")
        self.settingpage_algorithm_threshould_spinbox.setMaximum(255)

        self.gridLayout_9.addWidget(self.settingpage_algorithm_threshould_spinbox, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(1353, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.label_24 = QLabel(self.settingpage_algorithm_tab)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_9.addWidget(self.label_24, 1, 0, 1, 1)

        self.settingpage_tabs.addTab(self.settingpage_algorithm_tab, "")

        self.verticalLayout_6.addWidget(self.settingpage_tabs)

        self.main_pages_stackw.addWidget(self.settings_page)
        self.calibration_page = QWidget()
        self.calibration_page.setObjectName(u"calibration_page")
        self.horizontalLayout_8 = QHBoxLayout(self.calibration_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.calibrationpage_left_side = QFrame(self.calibration_page)
        self.calibrationpage_left_side.setObjectName(u"calibrationpage_left_side")
        self.calibrationpage_left_side.setStyleSheet(u"#calibrationpage_left_side{\n"
"	padding: 10px;\n"
"	padding-top: 30px;\n"
"	border: 2px solid rgb(6, 76, 130);\n"
"}\n"
"\n"
".QLabel{\n"
"	font-size:25px;\n"
"	font-weight: bold;\n"
"	color:rgb(11, 64, 120);\n"
"	margin-right:30px;\n"
"}\n"
"\n"
".QPushButton\n"
"{\n"
"	color: #ffffff;\n"
"	background-color:rgb(6, 76, 130);\n"
"	min-height: 40px;\n"
"	border-radius: 5px;\n"
"	min-width:200px;\n"
"	font-size:14px;\n"
"}\n"
"/*********************************************/\n"
".QPushButton:hover\n"
"{\n"
"	background-color:rgb(50,50,50);\n"
"}\n"
"\n"
"/*********************************************/\n"
"\n"
"QprogressBar\n"
"{\n"
"	min-height:200px;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"min-width:150px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"min-width:157px;\n"
"}\n"
"\n"
"\n"
".Line{\n"
"	min-height:20px;\n"
"}")
        self.calibrationpage_left_side.setFrameShape(QFrame.StyledPanel)
        self.calibrationpage_left_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.calibrationpage_left_side)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.calibrationpage_step1_lbl = QLabel(self.calibrationpage_left_side)
        self.calibrationpage_step1_lbl.setObjectName(u"calibrationpage_step1_lbl")

        self.horizontalLayout_9.addWidget(self.calibrationpage_step1_lbl)

        self.calibrationpage_check_btn = QPushButton(self.calibrationpage_left_side)
        self.calibrationpage_check_btn.setObjectName(u"calibrationpage_check_btn")
        icon21 = QIcon()
        icon21.addFile(u":/assets/Assets/icons/icons8-eye-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calibrationpage_check_btn.setIcon(icon21)

        self.horizontalLayout_9.addWidget(self.calibrationpage_check_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_10 = QFrame(self.calibrationpage_left_side)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.calibrationpage_step2_lbl = QLabel(self.calibrationpage_left_side)
        self.calibrationpage_step2_lbl.setObjectName(u"calibrationpage_step2_lbl")

        self.horizontalLayout_10.addWidget(self.calibrationpage_step2_lbl)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.calibrationpage_left_side)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size:16px;\n"
"font-weight:normal;\n"
"color:rgb(31, 31, 31);\n"
"margin-right:5px;")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.calibrationpage_calib_type_combobox = QComboBox(self.calibrationpage_left_side)
        self.calibrationpage_calib_type_combobox.addItem("")
        self.calibrationpage_calib_type_combobox.addItem("")
        self.calibrationpage_calib_type_combobox.setObjectName(u"calibrationpage_calib_type_combobox")
        self.calibrationpage_calib_type_combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.calibrationpage_calib_type_combobox.setDuplicatesEnabled(False)
        self.calibrationpage_calib_type_combobox.setFrame(True)

        self.horizontalLayout_12.addWidget(self.calibrationpage_calib_type_combobox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.calibrationpage_left_side)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size:16px;\n"
"font-weight:normal;\n"
"color:rgb(31, 31, 31);\n"
"margin-right:5px;")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.calibrationpage_calib_itrs_spinbox = QSpinBox(self.calibrationpage_left_side)
        self.calibrationpage_calib_itrs_spinbox.setObjectName(u"calibrationpage_calib_itrs_spinbox")
        self.calibrationpage_calib_itrs_spinbox.setMinimumSize(QSize(187, 41))

        self.horizontalLayout_14.addWidget(self.calibrationpage_calib_itrs_spinbox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line_11 = QFrame(self.calibrationpage_left_side)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_11)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.calibrationpage_step3_lbl = QLabel(self.calibrationpage_left_side)
        self.calibrationpage_step3_lbl.setObjectName(u"calibrationpage_step3_lbl")

        self.horizontalLayout_11.addWidget(self.calibrationpage_step3_lbl)

        self.calibrationpage_calib_btn = QPushButton(self.calibrationpage_left_side)
        self.calibrationpage_calib_btn.setObjectName(u"calibrationpage_calib_btn")
        self.calibrationpage_calib_btn.setIcon(icon13)

        self.horizontalLayout_11.addWidget(self.calibrationpage_calib_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.line_12 = QFrame(self.calibrationpage_left_side)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_12)

        self.calibrationpage_process_progressbar = QProgressBar(self.calibrationpage_left_side)
        self.calibrationpage_process_progressbar.setObjectName(u"calibrationpage_process_progressbar")
        self.calibrationpage_process_progressbar.setStyleSheet(u"")
        self.calibrationpage_process_progressbar.setValue(24)

        self.verticalLayout_3.addWidget(self.calibrationpage_process_progressbar)

        self.verticalSpacer_19 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_19)

        self.calibrationpage_result_groupbox = QGroupBox(self.calibrationpage_left_side)
        self.calibrationpage_result_groupbox.setObjectName(u"calibrationpage_result_groupbox")
        self.calibrationpage_result_groupbox.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	font-weight: normal;\n"
"\n"
"}")
        self.calibrationpage_result_groupbox.setCheckable(False)
        self.calibrationpage_result_groupbox.setChecked(False)
        self.gridLayout = QGridLayout(self.calibrationpage_result_groupbox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.calibrationpage_prev_acc_lbl = QLabel(self.calibrationpage_result_groupbox)
        self.calibrationpage_prev_acc_lbl.setObjectName(u"calibrationpage_prev_acc_lbl")

        self.gridLayout.addWidget(self.calibrationpage_prev_acc_lbl, 0, 1, 1, 1)

        self.label_38 = QLabel(self.calibrationpage_result_groupbox)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.calibrationpage_result_groupbox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 1, 0, 1, 1)

        self.calibrationpage_new_acc_lbl = QLabel(self.calibrationpage_result_groupbox)
        self.calibrationpage_new_acc_lbl.setObjectName(u"calibrationpage_new_acc_lbl")

        self.gridLayout.addWidget(self.calibrationpage_new_acc_lbl, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.calibrationpage_result_groupbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.calibrationpage_last_calib_tabel = QTableWidget(self.calibrationpage_left_side)
        if (self.calibrationpage_last_calib_tabel.columnCount() < 4):
            self.calibrationpage_last_calib_tabel.setColumnCount(4)
        if (self.calibrationpage_last_calib_tabel.rowCount() < 1):
            self.calibrationpage_last_calib_tabel.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 3, __qtablewidgetitem3)
        self.calibrationpage_last_calib_tabel.setObjectName(u"calibrationpage_last_calib_tabel")
        self.calibrationpage_last_calib_tabel.setEnabled(True)
        self.calibrationpage_last_calib_tabel.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(False)
        font1.setItalic(False)
        self.calibrationpage_last_calib_tabel.setFont(font1)
        self.calibrationpage_last_calib_tabel.setMouseTracking(False)
        self.calibrationpage_last_calib_tabel.setStyleSheet(u"QHeaderView::section {\n"
"    background-color:rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 11pt;\n"
"    border-style: none;\n"
"    border-right: 2px solid rgba(255, 255, 255,50);\n"
"	\n"
"}\n"
"\n"
"")
        self.calibrationpage_last_calib_tabel.setFrameShape(QFrame.NoFrame)
        self.calibrationpage_last_calib_tabel.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.calibrationpage_last_calib_tabel.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.calibrationpage_last_calib_tabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.calibrationpage_last_calib_tabel.setAlternatingRowColors(False)
        self.calibrationpage_last_calib_tabel.setTextElideMode(Qt.ElideNone)
        self.calibrationpage_last_calib_tabel.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.calibrationpage_last_calib_tabel.setShowGrid(True)
        self.calibrationpage_last_calib_tabel.setGridStyle(Qt.SolidLine)
        self.calibrationpage_last_calib_tabel.setSortingEnabled(False)
        self.calibrationpage_last_calib_tabel.setRowCount(1)
        self.calibrationpage_last_calib_tabel.setColumnCount(4)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setVisible(False)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setCascadingSectionResizes(True)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setDefaultSectionSize(125)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setHighlightSections(False)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setProperty("showSortIndicator", False)
        self.calibrationpage_last_calib_tabel.horizontalHeader().setStretchLastSection(True)
        self.calibrationpage_last_calib_tabel.verticalHeader().setVisible(False)
        self.calibrationpage_last_calib_tabel.verticalHeader().setCascadingSectionResizes(False)
        self.calibrationpage_last_calib_tabel.verticalHeader().setHighlightSections(True)
        self.calibrationpage_last_calib_tabel.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_3.addWidget(self.calibrationpage_last_calib_tabel)


        self.horizontalLayout_8.addWidget(self.calibrationpage_left_side)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.calibrationpage_right_side = QVBoxLayout()
        self.calibrationpage_right_side.setObjectName(u"calibrationpage_right_side")
        self.calibrationpage_right_side.setContentsMargins(0, -1, -1, -1)
        self.calibrationpage_liveimage_lbl = QLabel(self.calibration_page)
        self.calibrationpage_liveimage_lbl.setObjectName(u"calibrationpage_liveimage_lbl")
        self.calibrationpage_liveimage_lbl.setStyleSheet(u"max-width : 800px;\n"
"max-height : 800px;")
        self.calibrationpage_liveimage_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.calibrationpage_liveimage_lbl.setScaledContents(False)
        self.calibrationpage_liveimage_lbl.setAlignment(Qt.AlignCenter)
        self.calibrationpage_liveimage_lbl.setWordWrap(False)

        self.calibrationpage_right_side.addWidget(self.calibrationpage_liveimage_lbl)


        self.horizontalLayout_8.addLayout(self.calibrationpage_right_side)

        self.main_pages_stackw.addWidget(self.calibration_page)
        self.users_page = QWidget()
        self.users_page.setObjectName(u"users_page")
        self.verticalLayout_9 = QVBoxLayout(self.users_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.user_tabs = QTabWidget(self.users_page)
        self.user_tabs.setObjectName(u"user_tabs")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridFrame_2 = QFrame(self.tab_2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	color: rgb(52, 52, 52);\n"
"	padding-right: 20px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	max-width: 300px;\n"
"\n"
"}")
        self.gridLayout_5 = QGridLayout(self.gridFrame_2)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.userpage_user_role_combobox = QComboBox(self.gridFrame_2)
        self.userpage_user_role_combobox.addItem("")
        self.userpage_user_role_combobox.setObjectName(u"userpage_user_role_combobox")

        self.gridLayout_5.addWidget(self.userpage_user_role_combobox, 6, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 5, 0, 1, 1)

        self.userpage_password_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_password_inpt.setObjectName(u"userpage_password_inpt")

        self.gridLayout_5.addWidget(self.userpage_password_inpt, 2, 1, 1, 1)

        self.userpage_username_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_username_inpt.setObjectName(u"userpage_username_inpt")

        self.gridLayout_5.addWidget(self.userpage_username_inpt, 0, 1, 1, 1)

        self.label_19 = QLabel(self.gridFrame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_19, 6, 0, 1, 1)

        self.label_16 = QLabel(self.gridFrame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)

        self.userpage_confirm_password_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_confirm_password_inpt.setObjectName(u"userpage_confirm_password_inpt")
        self.userpage_confirm_password_inpt.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.userpage_confirm_password_inpt, 4, 1, 1, 1)

        self.label_17 = QLabel(self.gridFrame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 3, 0, 1, 1)

        self.label_18 = QLabel(self.gridFrame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_18, 4, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 7, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 1, 0, 1, 1)

        self.userspage_add_user_btn = QPushButton(self.gridFrame_2)
        self.userspage_add_user_btn.setObjectName(u"userspage_add_user_btn")
        self.userspage_add_user_btn.setStyleSheet(u"max-width: 120px;")
        icon22 = QIcon()
        icon22.addFile(u":/assets/Assets/icons/icons8-plus-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userspage_add_user_btn.setIcon(icon22)

        self.gridLayout_5.addWidget(self.userspage_add_user_btn, 8, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.gridFrame_2)

        self.verticalSpacer_20 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)

        self.userspage_register_error_lbl = QLabel(self.tab_2)
        self.userspage_register_error_lbl.setObjectName(u"userspage_register_error_lbl")
        self.userspage_register_error_lbl.setStyleSheet(u"color:rgb(255, 101, 96);\n"
"font-weight:bold;")

        self.verticalLayout_10.addWidget(self.userspage_register_error_lbl)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.user_tabs.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.user_tabs.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.userspage_user_heading_lbl = QLabel(self.tab_4)
        self.userspage_user_heading_lbl.setObjectName(u"userspage_user_heading_lbl")
        self.userspage_user_heading_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);\n"
"min-height: 80px;\n"
"max-height: 80px;")

        self.verticalLayout_11.addWidget(self.userspage_user_heading_lbl)

        self.userpage_all_users_table = QTableWidget(self.tab_4)
        if (self.userpage_all_users_table.columnCount() < 5):
            self.userpage_all_users_table.setColumnCount(5)
        if (self.userpage_all_users_table.rowCount() < 3):
            self.userpage_all_users_table.setRowCount(3)
        self.userpage_all_users_table.setObjectName(u"userpage_all_users_table")
        self.userpage_all_users_table.setAutoFillBackground(False)
        self.userpage_all_users_table.setStyleSheet(u"\n"
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
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"")
        self.userpage_all_users_table.setFrameShape(QFrame.StyledPanel)
        self.userpage_all_users_table.setFrameShadow(QFrame.Raised)
        self.userpage_all_users_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.userpage_all_users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userpage_all_users_table.setDefaultDropAction(Qt.IgnoreAction)
        self.userpage_all_users_table.setAlternatingRowColors(False)
        self.userpage_all_users_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.userpage_all_users_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userpage_all_users_table.setTextElideMode(Qt.ElideMiddle)
        self.userpage_all_users_table.setSortingEnabled(False)
        self.userpage_all_users_table.setCornerButtonEnabled(True)
        self.userpage_all_users_table.setRowCount(3)
        self.userpage_all_users_table.setColumnCount(5)
        self.userpage_all_users_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_11.addWidget(self.userpage_all_users_table)

        self.user_tabs.addTab(self.tab_4, "")

        self.verticalLayout_9.addWidget(self.user_tabs)

        self.main_pages_stackw.addWidget(self.users_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.verticalLayout_16 = QVBoxLayout(self.help_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.helppage_tabs = QTabWidget(self.help_page)
        self.helppage_tabs.setObjectName(u"helppage_tabs")
        self.helppages_about_tab = QWidget()
        self.helppages_about_tab.setObjectName(u"helppages_about_tab")
        self.helppage_tabs.addTab(self.helppages_about_tab, "")
        self.helppages_document_tab = QWidget()
        self.helppages_document_tab.setObjectName(u"helppages_document_tab")
        self.helppage_tabs.addTab(self.helppages_document_tab, "")

        self.verticalLayout_16.addWidget(self.helppage_tabs)

        self.main_pages_stackw.addWidget(self.help_page)
        self.single_report_page = QWidget()
        self.single_report_page.setObjectName(u"single_report_page")
        self.single_report_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.single_report_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 5, -1, -1)
        self.horizontalFrame1 = QFrame(self.single_report_page)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(25, 68, 105);\n"
"font-size: 14px;\n"
"min-width:80px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(25, 68, 105);\n"
"}\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 1, -1, -1)
        self.pushButton_2 = QPushButton(self.horizontalFrame1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"")
        icon23 = QIcon()
        icon23.addFile(u":/assets/Assets/icons/icons8-back-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon23)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.pushButton_2)

        self.line_14 = QFrame(self.horizontalFrame1)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_14)

        self.pushButton_3 = QPushButton(self.horizontalFrame1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon24 = QIcon()
        icon24.addFile(u":/assets/Assets/icons/icons8-export-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon24)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_3)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_46)


        self.verticalLayout_8.addWidget(self.horizontalFrame1)

        self.scrollArea = QScrollArea(self.single_report_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: rgb(50, 50, 50);\n"
"        width: 20px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color:rgb(21, 142, 241);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    Q"
                        "ScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -54, 1143, 1519))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents\n"
"{\n"
"background-color:#ffffff;\n"
"\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox\n"
"{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"	border: 3px solid rgb(12, 80, 139);\n"
"	border-radius: 10px;\n"
"	padding: 20px 5px;\n"
"	background-color:rgba(12, 80, 139,5);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    color: rgb(6, 76, 130);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size:15px;\n"
"\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(11, 25, -1, 25)
        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_3.addWidget(self.label_42, 0, 4, 1, 1)

        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_3.addWidget(self.label_44, 0, 13, 1, 1)

        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_41.setProperty("title", True)

        self.gridLayout_3.addWidget(self.label_41, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6.setProperty("title", True)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_62 = QLabel(self.groupBox_6)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_3.addWidget(self.label_62, 1, 4, 1, 1)

        self.label_61 = QLabel(self.groupBox_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_61, 1, 3, 1, 1)

        self.label_40 = QLabel(self.groupBox_6)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 0, 1, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_45, 0, 14, 1, 1)

        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_43.setProperty("title", True)

        self.gridLayout_3.addWidget(self.label_43, 0, 12, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_51, 0, 8, 1, 1)

        self.label_66 = QLabel(self.groupBox_6)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_3.addWidget(self.label_66, 0, 7, 1, 1)

        self.label_67 = QLabel(self.groupBox_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")

        self.gridLayout_3.addWidget(self.label_67, 0, 9, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_43, 0, 2, 1, 1)

        self.label_60 = QLabel(self.groupBox_6)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_3.addWidget(self.label_60, 1, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_6)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_3.addWidget(self.label_68, 0, 10, 1, 1)

        self.label_65 = QLabel(self.groupBox_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")

        self.gridLayout_3.addWidget(self.label_65, 0, 6, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_44, 0, 5, 1, 1)

        self.label_59 = QLabel(self.groupBox_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_59, 1, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_52, 0, 11, 1, 1)

        self.label_63 = QLabel(self.groupBox_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_63, 1, 6, 1, 1)

        self.label_64 = QLabel(self.groupBox_6)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_3.addWidget(self.label_64, 1, 7, 1, 1)


        self.verticalLayout_12.addWidget(self.groupBox_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.label_46 = QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"margin-top: 50px;\n"
"\n"
"font-size: 24px;\n"
"color:rgb(25, 68, 105);\n"
"font-weight: bold;\n"
"\n"
"border-left-width: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(6, 76, 130);\n"
"\n"
"\n"
"padding: 10px 0px")

        self.verticalLayout_12.addWidget(self.label_46)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_53)

        self.mainpage_statistics_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.mainpage_statistics_table.columnCount() < 5):
            self.mainpage_statistics_table.setColumnCount(5)
        if (self.mainpage_statistics_table.rowCount() < 4):
            self.mainpage_statistics_table.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.mainpage_statistics_table.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.mainpage_statistics_table.setItem(1, 1, __qtablewidgetitem5)
        self.mainpage_statistics_table.setObjectName(u"mainpage_statistics_table")
        self.mainpage_statistics_table.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainpage_statistics_table.sizePolicy().hasHeightForWidth())
        self.mainpage_statistics_table.setSizePolicy(sizePolicy1)
        self.mainpage_statistics_table.setMaximumSize(QSize(16777215, 16777215))
        self.mainpage_statistics_table.setSizeIncrement(QSize(0, 0))
        self.mainpage_statistics_table.setBaseSize(QSize(0, 0))
        self.mainpage_statistics_table.setFont(font1)
        self.mainpage_statistics_table.setFocusPolicy(Qt.NoFocus)
        self.mainpage_statistics_table.setStyleSheet(u"QTableWidget{\n"
"	min-height: 200px;\n"
"	font-size: 16px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
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
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}\n"
"\n"
"")
        self.mainpage_statistics_table.setFrameShadow(QFrame.Raised)
        self.mainpage_statistics_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainpage_statistics_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mainpage_statistics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.mainpage_statistics_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mainpage_statistics_table.setAlternatingRowColors(False)
        self.mainpage_statistics_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.mainpage_statistics_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mainpage_statistics_table.setTextElideMode(Qt.ElideMiddle)
        self.mainpage_statistics_table.setGridStyle(Qt.SolidLine)
        self.mainpage_statistics_table.setWordWrap(True)
        self.mainpage_statistics_table.setRowCount(4)
        self.mainpage_statistics_table.setColumnCount(5)
        self.mainpage_statistics_table.horizontalHeader().setMinimumSectionSize(50)
        self.mainpage_statistics_table.horizontalHeader().setDefaultSectionSize(180)
        self.mainpage_statistics_table.horizontalHeader().setHighlightSections(True)
        self.mainpage_statistics_table.horizontalHeader().setStretchLastSection(False)
        self.mainpage_statistics_table.verticalHeader().setVisible(False)
        self.mainpage_statistics_table.verticalHeader().setDefaultSectionSize(40)
        self.mainpage_statistics_table.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_7.addWidget(self.mainpage_statistics_table)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_54)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.label_45 = QLabel(self.scrollAreaWidgetContents)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"margin-top: 50px;\n"
"\n"
"font-size: 24px;\n"
"color:rgb(25, 68, 105);\n"
"font-weight: bold;\n"
"\n"
"border-left-width: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(6, 76, 130);\n"
"\n"
"\n"
"padding: 10px 0px")

        self.verticalLayout_12.addWidget(self.label_45)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 250, -1, -1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"margin-top: 50px;\n"
"\n"
"font-size: 24px;\n"
"color:rgb(25, 68, 105);\n"
"font-weight: bold;\n"
"\n"
"border-left-width: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(6, 76, 130);\n"
"\n"
"\n"
"padding: 10px 0px")

        self.verticalLayout_12.addWidget(self.label_47)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, -1)
        self.report_single_pellet_frame = QFrame(self.scrollAreaWidgetContents)
        self.report_single_pellet_frame.setObjectName(u"report_single_pellet_frame")
        self.report_single_pellet_frame.setStyleSheet(u"#report_single_pellet_frame{\n"
"border: 1px solid rgb(12, 80, 139);\n"
"border-radius: 10px;\n"
"background-color: rgb(6, 76, 130);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color:#ffffff;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.report_single_pellet_frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 12, -1, -1)
        self.label_48 = QLabel(self.report_single_pellet_frame)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"max-width: 400px;\n"
"max-height: 400px;")
        self.label_48.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_48)

        self.horizontalFrame_31 = QFrame(self.report_single_pellet_frame)
        self.horizontalFrame_31.setObjectName(u"horizontalFrame_31")
        self.horizontalFrame_31.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0 );\n"
"	min-width: 0px;\n"
"	min-height: 50px;\n"
"}")
        self.horizontalLayout_30 = QHBoxLayout(self.horizontalFrame_31)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(1, 13, -1, -1)
        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_49)

        self.pushButton_4 = QPushButton(self.horizontalFrame_31)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u":/assets/Assets/icons/icons8-previous-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon25)
        self.pushButton_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_30.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalFrame_31)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u":/assets/Assets/icons/icons8-next-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon26)
        self.pushButton_5.setIconSize(QSize(50, 50))

        self.horizontalLayout_30.addWidget(self.pushButton_5)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_48)


        self.verticalLayout_13.addWidget(self.horizontalFrame_31)


        self.horizontalLayout_29.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_47)

        self.signle_pellet_info_groupbox = QGroupBox(self.report_single_pellet_frame)
        self.signle_pellet_info_groupbox.setObjectName(u"signle_pellet_info_groupbox")
        self.signle_pellet_info_groupbox.setStyleSheet(u"#signle_pellet_info_groupbox{\n"
"	border: 1px solid #ffffff;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.signle_pellet_info_groupbox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_51 = QLabel(self.signle_pellet_info_groupbox)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_51, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.label_55 = QLabel(self.signle_pellet_info_groupbox)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_55, 1, 3, 1, 1)

        self.label_53 = QLabel(self.signle_pellet_info_groupbox)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_53, 2, 3, 1, 1)

        self.label_58 = QLabel(self.signle_pellet_info_groupbox)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_14.addWidget(self.label_58, 3, 1, 1, 1)

        self.label_54 = QLabel(self.signle_pellet_info_groupbox)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_14.addWidget(self.label_54, 2, 4, 1, 1)

        self.label_56 = QLabel(self.signle_pellet_info_groupbox)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_14.addWidget(self.label_56, 1, 4, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_39, 2, 5, 1, 1)

        self.label_57 = QLabel(self.signle_pellet_info_groupbox)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_57, 3, 0, 1, 1)

        self.label_52 = QLabel(self.signle_pellet_info_groupbox)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_14.addWidget(self.label_52, 2, 1, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_38, 2, 2, 1, 1)

        self.label_50 = QLabel(self.signle_pellet_info_groupbox)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_14.addWidget(self.label_50, 1, 1, 1, 1)

        self.label_49 = QLabel(self.signle_pellet_info_groupbox)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_49, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_16, 0, 0, 1, 1)


        self.horizontalLayout_29.addWidget(self.signle_pellet_info_groupbox)


        self.horizontalLayout_26.addWidget(self.report_single_pellet_frame)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_50)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.main_pages_stackw.addWidget(self.single_report_page)

        self.horizontalLayout.addWidget(self.main_pages_stackw)


        self.verticalLayout.addWidget(self.middle)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 25))
        self.footer.setMaximumSize(QSize(16777215, 48))
        self.footer.setStyleSheet(u"QFrame{\n"
"	background: #2C313A;\n"
"	\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"	font-size: 9pt;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	font-size: 9pt;\n"
"}\n"
"")
        self.footer.setFrameShape(QFrame.WinPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.footer)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 10, 0)
        self.label_7 = QLabel(self.footer)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_7.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.line_15 = QFrame(self.footer)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setMaximumSize(QSize(1, 15))
        self.line_15.setStyleSheet(u"background: white;")
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QFrame.VLine)

        self.horizontalLayout_17.addWidget(self.line_15)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 12))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.main_pages_stackw.setCurrentIndex(6)
        self.settingpage_tabs.setCurrentIndex(2)
        self.user_tabs.setCurrentIndex(1)
        self.helppage_tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dorsa Width Gauge", None))
        self.dorsa_logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Particle Size Analyzer", None))
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.sidebar_main_btn.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.sidebar_report_btn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.sidebar_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sidebar_calib_btn.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.sidebar_users_btn.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.sidebar_help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.mainpage_liveview_checkbox.setText("")
        self.mainpage_drawing_checkbox.setText("")
#if QT_CONFIG(accessibility)
        self.mainpage_live_image_lbl.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.mainpage_live_image_lbl.setText("")
        self.mainpage_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mainpage_faststart_btn.setText(QCoreApplication.translate("MainWindow", u"Fast Start", None))
        self.mainpage_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.mainpage_informaition_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Avrage:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"05:31", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.mainpage_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"STD:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.mainpage_std_lbl.setText(QCoreApplication.translate("MainWindow", u"1.6mm", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Cam Tempreture(\u00b0C):", None))
        self.mainpage_avrage_lbl.setText(QCoreApplication.translate("MainWindow", u"12.8 mm", None))
        self.mainpage_mean_oval_lbl.setText(QCoreApplication.translate("MainWindow", u"78%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mean Oval:", None))
        self.mainpage_report_button.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"System Status", None))
        self.mainpage_illumination_warning_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tempreture", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Camera Connection", None))
        self.mainpage_tempreture_warning_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ilumination", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Camera Grabbing", None))
        self.mainpage_camera_connection_warning_btn.setText("")
        self.mainpage_camera_grabbing_warning_btn.setText("")
        self.mainpage_warning_massage_lbl.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Grading Chart", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ovality Chart", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Interface Setting", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"App Color", None))
        self.settingpage_general_language_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.settingpage_general_language_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Persian", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Report Life Time (days) :", None))
        self.checkBox.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Auto Clean:", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Restor Defualt", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_general_tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Define Ranges", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Lower Limit(mm):", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Upper Limit(mm):", None))
        self.settingpage_pelletizing_add_range_btn.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Defined Ranges", None))
        self.settingpage_grading_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_grading_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Standards", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_grading_tab), QCoreApplication.translate("MainWindow", u"Grading", None))
        self.settingpage_camera_start_btn.setText("")
        self.settingpage_camera_device_group.setTitle(QCoreApplication.translate("MainWindow", u"Device Setting", None))
        self.settingpage_camera_device_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.settingpage_camera_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.settingpage_camera_control_group.setTitle(QCoreApplication.translate("MainWindow", u"Control And Analog Setting", None))
        self.settingpage_camera_exposure_lbl.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.settingpage_camera_gain_lbl.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.settingpage_camera_AOI_group.setTitle(QCoreApplication.translate("MainWindow", u"AOI Setting", None))
        self.settingpage_camera_width_lbl.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.settingpage_camera_height_lbl.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.settingpage_camera_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_camera_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.settingpage_camera_restore_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Default", None))
        self.settingpage_camera_live_lbl.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"RGB:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Temp: ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Threshould", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Circularity", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_algorithm_tab), QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.calibrationpage_step1_lbl.setText(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.calibrationpage_check_btn.setText(QCoreApplication.translate("MainWindow", u" Check", None))
        self.calibrationpage_step2_lbl.setText(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Calibration Type :", None))
        self.calibrationpage_calib_type_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.calibrationpage_calib_type_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mean", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"iteration", None))
        self.calibrationpage_step3_lbl.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.calibrationpage_calib_btn.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        self.calibrationpage_result_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Done", None))
        self.calibrationpage_prev_acc_lbl.setText(QCoreApplication.translate("MainWindow", u"0.1 mm", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Accuracy Befor Calibration:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Accuracy After Calibration:", None))
        self.calibrationpage_new_acc_lbl.setText(QCoreApplication.translate("MainWindow", u"0.08 mm", None))

        __sortingEnabled = self.calibrationpage_last_calib_tabel.isSortingEnabled()
        self.calibrationpage_last_calib_tabel.setSortingEnabled(False)
        ___qtablewidgetitem = self.calibrationpage_last_calib_tabel.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"2022-06-23", None));
        ___qtablewidgetitem1 = self.calibrationpage_last_calib_tabel.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Alimalek", None));
        ___qtablewidgetitem2 = self.calibrationpage_last_calib_tabel.item(0, 2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"0.098", None));
        self.calibrationpage_last_calib_tabel.setSortingEnabled(__sortingEnabled)

        self.calibrationpage_last_calib_tabel.setProperty("Date", "")
        self.calibrationpage_liveimage_lbl.setText("")
        self.userpage_user_role_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"User Role:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"username:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"pasword Confirm:", None))
        self.userspage_add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.userspage_register_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"register user", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.userspage_user_heading_lbl.setText(QCoreApplication.translate("MainWindow", u"Only Admin Can Access", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"All Users", None))
        self.helppage_tabs.setTabText(self.helppage_tabs.indexOf(self.helppages_about_tab), QCoreApplication.translate("MainWindow", u"About", None))
        self.helppage_tabs.setTabText(self.helppage_tabs.indexOf(self.helppages_document_tab), QCoreApplication.translate("MainWindow", u"Document", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"General Information", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"2023-05-12", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"AX256", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sample Name:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"2mm", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"STD:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"no-name", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Standard:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"12:17", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"user:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"16mm", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"its.bigs", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Avrage:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"11mm", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Statictics", None))

        __sortingEnabled1 = self.mainpage_statistics_table.isSortingEnabled()
        self.mainpage_statistics_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.mainpage_statistics_table.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem4 = self.mainpage_statistics_table.item(1, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        self.mainpage_statistics_table.setSortingEnabled(__sortingEnabled1)

        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Particles", None))
        self.label_48.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Max Radius:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Valum:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Avg Radius:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"70%", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"28mm", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"64 (mm3)", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Circulartity:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"17mm", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Designed and Developed by Dideh Rayan Sanati Esfahan (Dorsa)", None))
    # retranslateUi

