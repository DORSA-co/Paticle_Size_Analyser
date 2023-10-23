# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QDateEdit, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import Assets_rc
import Assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1369, 908)
        icon = QIcon()
        icon.addFile(u"../../../../../../.designer/backup/Icons/app_logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
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
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
""
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
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"    selection-background-color: rgb(6, 76, 130);\n"
"	selection-color: rgb(6, 76, 130);\n"
""
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
"QDateEdit::down-button\n"
"{\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(6, 76, 130);\n"
"    width: 30px;\n"
"}\n"
"\n"
""
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
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/assets/icons/icons8-uptriangle-48.png);\n"
"	wi"
                        "dth: 10px;\n"
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
"/*******************************************/\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"	border:2px solid rgb(6, "
                        "76, 130);\n"
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
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(12, 80, 139, 255), stop:100 rgba(10, 66, 112, 255));\n"
"    width: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/*******************************************/\n"
"\n"
"QTabBar::tab:selected"
                        " {\n"
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
"	selection-background-color: black;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleS"
                        "pinBox:hover{\n"
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
        self.dorsa_logo.setPixmap(QPixmap(u":/assets/general/dorsa_white.png"))
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

        self.toolbar_logined_username_lbl = QLabel(self.header)
        self.toolbar_logined_username_lbl.setObjectName(u"toolbar_logined_username_lbl")
        self.toolbar_logined_username_lbl.setStyleSheet(u"color:#ffffff;")

        self.horizontalLayout_4.addWidget(self.toolbar_logined_username_lbl)

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
"background-color: rgba(31, 32, 85, 100);\n"
" }")
        self.win_buttons.setFrameShape(QFrame.StyledPanel)
        self.win_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.win_buttons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.toolbar_login_logout_btn = QPushButton(self.win_buttons)
        self.toolbar_login_logout_btn.setObjectName(u"toolbar_login_logout_btn")
        self.toolbar_login_logout_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/icons8-user-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolbar_login_logout_btn.setIcon(icon1)
        self.toolbar_login_logout_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.toolbar_login_logout_btn)

        self.line_13 = QFrame(self.win_buttons)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"Line{\n"
"	max-width: 120px;\n"
"	background-color:rgba(255, 255, 255, 50);\n"
"	margin: 0 15px;\n"
"}")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_13)

        self.horizontalSpacer_55 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_55)

        self.minimize_btn = QPushButton(self.win_buttons)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(16777215, 40))
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/general/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon2)
        self.minimize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.win_buttons)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setEnabled(True)
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(16777215, 40))
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/general/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon3)
        self.maximize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.win_buttons)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(16777215, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/assets/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon4)
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
        self.sidebar.setMinimumSize(QSize(180, 0))
        self.sidebar.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar.setStyleSheet(u"QFrame#sidebar{\n"
"background-color:rgb(6, 76, 130);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	color: #ffffff;\n"
"	min-height: 40px;\n"
"	text-align: left;\n"
"	icon-size:25px;\n"
"	background-color:rgba(0,0,0,0);\n"
"\n"
"	border-bottom:2px solid rgba(255,255,255,100);\n"
"	border-radius : 0px;\n"
"	min-width:0px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    font-size:14px; \n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"Line{\n"
"	max-width: 120px;\n"
"	background-color:rgba(255, 255, 255, 50);\n"
"	margin: 0 15px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 11, 20, -1)
        self.sidebar_main_btn = QPushButton(self.sidebar)
        self.sidebar_main_btn.setObjectName(u"sidebar_main_btn")
        self.sidebar_main_btn.setEnabled(True)
        self.sidebar_main_btn.setMinimumSize(QSize(0, 42))
        icon5 = QIcon()
        icon5.addFile(u":/assets/icons/icons8-home-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_main_btn.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.sidebar_main_btn)

        self.sidebar_report_btn = QPushButton(self.sidebar)
        self.sidebar_report_btn.setObjectName(u"sidebar_report_btn")
        self.sidebar_report_btn.setMinimumSize(QSize(0, 42))
        icon6 = QIcon()
        icon6.addFile(u":/assets/icons/report-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_report_btn.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.sidebar_report_btn)

        self.sidebar_grading_ranges_btn = QPushButton(self.sidebar)
        self.sidebar_grading_ranges_btn.setObjectName(u"sidebar_grading_ranges_btn")
        icon7 = QIcon()
        icon7.addFile(u":/assets/icons/icons8-bar-chart-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_grading_ranges_btn.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.sidebar_grading_ranges_btn)

        self.sidebar_settings_btn = QPushButton(self.sidebar)
        self.sidebar_settings_btn.setObjectName(u"sidebar_settings_btn")
        self.sidebar_settings_btn.setMinimumSize(QSize(0, 42))
        icon8 = QIcon()
        icon8.addFile(u":/assets/icons/icons8-settings-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_settings_btn.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.sidebar_settings_btn)

        self.sidebar_calib_btn = QPushButton(self.sidebar)
        self.sidebar_calib_btn.setObjectName(u"sidebar_calib_btn")
        self.sidebar_calib_btn.setMinimumSize(QSize(0, 42))
        icon9 = QIcon()
        icon9.addFile(u":/assets/icons/icons8-ruler-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_calib_btn.setIcon(icon9)

        self.verticalLayout_2.addWidget(self.sidebar_calib_btn)

        self.sidebar_users_btn = QPushButton(self.sidebar)
        self.sidebar_users_btn.setObjectName(u"sidebar_users_btn")
        self.sidebar_users_btn.setMinimumSize(QSize(0, 42))
        icon10 = QIcon()
        icon10.addFile(u":/assets/icons/icons8-users-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_users_btn.setIcon(icon10)

        self.verticalLayout_2.addWidget(self.sidebar_users_btn)

        self.sidebar_help_btn = QPushButton(self.sidebar)
        self.sidebar_help_btn.setObjectName(u"sidebar_help_btn")
        self.sidebar_help_btn.setMinimumSize(QSize(0, 42))
        icon11 = QIcon()
        icon11.addFile(u":/assets/icons/icons8-question-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_help_btn.setIcon(icon11)

        self.verticalLayout_2.addWidget(self.sidebar_help_btn)

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
"#single_report_page,\n"
"#compare_page\n"
" {\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/assets/icons/icons8-video-call-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_liveview_checkbox.setIcon(icon12)
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
        icon13 = QIcon()
        icon13.addFile(u":/assets/icons/icons8-draw-pen-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_drawing_checkbox.setIcon(icon13)
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
        self.mainpage_live_image_lbl.setSizeIncrement(QSize(500, 500))
        self.mainpage_live_image_lbl.setStyleSheet(u"border: 2px solid rgb(50, 50, 50);\n"
"border-radius: 0px;\n"
"margin: 0px;\n"
"max-width:700px;\n"
"max-height:700px;\n"
"\n"
"background-color:rgb(50,50,50);\n"
"\n"
"\n"
"")
        self.mainpage_live_image_lbl.setTextFormat(Qt.AutoText)
        self.mainpage_live_image_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.mainpage_live_image_lbl.setScaledContents(False)
        self.mainpage_live_image_lbl.setAlignment(Qt.AlignCenter)
        self.mainpage_live_image_lbl.setWordWrap(False)
        self.mainpage_live_image_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.mainpage_live_image_lbl)


        self.mainpage_left_frame.addLayout(self.horizontalLayout_6)

        self.mainpage_error_lbl = QLabel(self.mainpage_left_frame_2)
        self.mainpage_error_lbl.setObjectName(u"mainpage_error_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainpage_error_lbl.sizePolicy().hasHeightForWidth())
        self.mainpage_error_lbl.setSizePolicy(sizePolicy)
        self.mainpage_error_lbl.setMaximumSize(QSize(16787, 60))
        self.mainpage_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"")
        self.mainpage_error_lbl.setWordWrap(True)

        self.mainpage_left_frame.addWidget(self.mainpage_error_lbl)

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
        icon14 = QIcon()
        icon14.addFile(u":/assets/icons/play-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_start_btn.setIcon(icon14)

        self.horizontalLayout_5.addWidget(self.mainpage_start_btn)

        self.mainpage_faststart_btn = QPushButton(self.horizontalFrame)
        self.mainpage_faststart_btn.setObjectName(u"mainpage_faststart_btn")
        self.mainpage_faststart_btn.setEnabled(False)
        self.mainpage_faststart_btn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/assets/icons/fast-forwards-arrow-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_faststart_btn.setIcon(icon15)

        self.horizontalLayout_5.addWidget(self.mainpage_faststart_btn)

        self.mainpage_stop_btn = QPushButton(self.horizontalFrame)
        self.mainpage_stop_btn.setObjectName(u"mainpage_stop_btn")
        self.mainpage_stop_btn.setEnabled(False)
        self.mainpage_stop_btn.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/assets/icons/stop50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_stop_btn.setIcon(icon16)

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
        self.mainpage_timer_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_timer_lbl.setObjectName(u"mainpage_timer_lbl")

        self.gridLayout_12.addWidget(self.mainpage_timer_lbl, 3, 4, 1, 1)

        self.label_34 = QLabel(self.mainpage_informaition_groupBox)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_34, 3, 3, 1, 1)

        self.mainpage_mean_oval_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_mean_oval_lbl.setObjectName(u"mainpage_mean_oval_lbl")

        self.gridLayout_12.addWidget(self.mainpage_mean_oval_lbl, 1, 7, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_41, 3, 2, 1, 1)

        self.mainpage_fps_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_fps_lbl.setObjectName(u"mainpage_fps_lbl")

        self.gridLayout_12.addWidget(self.mainpage_fps_lbl, 3, 1, 1, 1)

        self.mainpage_avrage_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_avrage_lbl.setObjectName(u"mainpage_avrage_lbl")
        self.mainpage_avrage_lbl.setTextFormat(Qt.AutoText)
        self.mainpage_avrage_lbl.setWordWrap(False)
        self.mainpage_avrage_lbl.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_12.addWidget(self.mainpage_avrage_lbl, 1, 1, 1, 1)

        self.label_5 = QLabel(self.mainpage_informaition_groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)

        self.mainpage_std_lbl = QLabel(self.mainpage_informaition_groupBox)
        self.mainpage_std_lbl.setObjectName(u"mainpage_std_lbl")

        self.gridLayout_12.addWidget(self.mainpage_std_lbl, 1, 4, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_42, 3, 5, 1, 1)

        self.label_33 = QLabel(self.mainpage_informaition_groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_33, 3, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_40, 1, 8, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_31, 1, 5, 1, 1)

        self.label_37 = QLabel(self.mainpage_informaition_groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_12.addWidget(self.label_37, 3, 7, 1, 1)

        self.label_3 = QLabel(self.mainpage_informaition_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;\n"
"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_3, 1, 6, 1, 1)

        self.label_36 = QLabel(self.mainpage_informaition_groupBox)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;\n"
"")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_36, 3, 6, 1, 1)

        self.label_12 = QLabel(self.mainpage_informaition_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(4, 55, 93);\n"
"font-weight: bold;")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_12, 1, 3, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_30, 1, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.mainpage_informaition_groupBox)

        self.mainpage_report_button = QPushButton(self.mainpage_livebox_frame)
        self.mainpage_report_button.setObjectName(u"mainpage_report_button")
        self.mainpage_report_button.setEnabled(True)
        self.mainpage_report_button.setStyleSheet(u"QPushButton{\n"
"	min-height:40px;\n"
"	border-radius:3px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(54, 193, 142);\n"
"	max-width: 200px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(147, 147, 147);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(40, 144, 106);\n"
"}\n"
"")
        self.mainpage_report_button.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.mainpage_report_button)


        self.mainpage_left_frame.addWidget(self.mainpage_livebox_frame)


        self.horizontalLayout_2.addWidget(self.mainpage_left_frame_2)

        self.line_9 = QFrame(self.main_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(5, 5))
        self.line_9.setSizeIncrement(QSize(5, 0))
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_9)

        self.mainpage_right_frame = QFrame(self.main_page)
        self.mainpage_right_frame.setObjectName(u"mainpage_right_frame")
        self.mainpage_right_frame.setMinimumSize(QSize(500, 0))
        self.left_main_page_ = QVBoxLayout(self.mainpage_right_frame)
        self.left_main_page_.setSpacing(0)
        self.left_main_page_.setObjectName(u"left_main_page_")
        self.left_main_page_.setContentsMargins(11, 5, -1, 5)
        self.frame = QFrame(self.mainpage_right_frame)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_35 = QHBoxLayout(self.frame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 1, -1, -1)
        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_61)

        self.mainpage_warnings_frame = QFrame(self.frame)
        self.mainpage_warnings_frame.setObjectName(u"mainpage_warnings_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainpage_warnings_frame.sizePolicy().hasHeightForWidth())
        self.mainpage_warnings_frame.setSizePolicy(sizePolicy1)
        self.mainpage_warnings_frame.setMinimumSize(QSize(0, 0))
        self.mainpage_warnings_frame.setMaximumSize(QSize(16777215, 16777215))
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
        self.groupBox_2.setMinimumSize(QSize(0, 100))
        self.groupBox_2.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.mainpage_illumination_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_illumination_warning_btn.setObjectName(u"mainpage_illumination_warning_btn")
        self.mainpage_illumination_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/assets/icons/icons8-headlight-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_illumination_warning_btn.setIcon(icon17)
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
        icon18 = QIcon()
        icon18.addFile(u":/assets/icons/icons8-thermometer-red-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_tempreture_warning_btn.setIcon(icon18)
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
        icon19 = QIcon()
        icon19.addFile(u":/assets/icons/icons8-connection-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_camera_connection_warning_btn.setIcon(icon19)
        self.mainpage_camera_connection_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_camera_connection_warning_btn, 0, 2, 1, 1)

        self.mainpage_camera_grabbing_warning_btn = QPushButton(self.groupBox_2)
        self.mainpage_camera_grabbing_warning_btn.setObjectName(u"mainpage_camera_grabbing_warning_btn")
        self.mainpage_camera_grabbing_warning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainpage_camera_grabbing_warning_btn.setStyleSheet(u"")
        icon20 = QIcon()
        icon20.addFile(u":/assets/icons/icons8-camera-green-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_camera_grabbing_warning_btn.setIcon(icon20)
        self.mainpage_camera_grabbing_warning_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.mainpage_camera_grabbing_warning_btn, 0, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.mainpage_error_msg_frame = QFrame(self.mainpage_warnings_frame)
        self.mainpage_error_msg_frame.setObjectName(u"mainpage_error_msg_frame")
        self.verticalLayout_23 = QVBoxLayout(self.mainpage_error_msg_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.mainpage_warning_massage_lbl = QLabel(self.mainpage_error_msg_frame)
        self.mainpage_warning_massage_lbl.setObjectName(u"mainpage_warning_massage_lbl")
        self.mainpage_warning_massage_lbl.setStyleSheet(u"color:rgb(255, 204, 2);\n"
"padding-left:15px;")

        self.verticalLayout_23.addWidget(self.mainpage_warning_massage_lbl)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_68)

        self.mainpage_close_error_btn = QPushButton(self.mainpage_error_msg_frame)
        self.mainpage_close_error_btn.setObjectName(u"mainpage_close_error_btn")
        self.mainpage_close_error_btn.setMinimumSize(QSize(124, 30))
        self.mainpage_close_error_btn.setMaximumSize(QSize(124, 40))
        self.mainpage_close_error_btn.setStyleSheet(u"QPushButton{\n"
"max-width:50px;\n"
"min-width:50px;\n"
"min-height:30px;\n"
"padding:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:none;\n"
"background-color: rgba(255,255,255,20);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/assets/icons/icons8-chevron-up-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainpage_close_error_btn.setIcon(icon21)

        self.horizontalLayout_41.addWidget(self.mainpage_close_error_btn)


        self.verticalLayout_23.addLayout(self.horizontalLayout_41)


        self.verticalLayout_7.addWidget(self.mainpage_error_msg_frame)


        self.horizontalLayout_35.addWidget(self.mainpage_warnings_frame)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_60)


        self.left_main_page_.addWidget(self.frame)

        self.verticalSpacer_18 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.left_main_page_.addItem(self.verticalSpacer_18)

        self.mainpage_grading_chart_frame = QVBoxLayout()
        self.mainpage_grading_chart_frame.setObjectName(u"mainpage_grading_chart_frame")
        self.mainpage_grading_chart_frame.setContentsMargins(0, 10, -1, -1)

        self.left_main_page_.addLayout(self.mainpage_grading_chart_frame)

        self.line_2 = QFrame(self.mainpage_right_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.left_main_page_.addWidget(self.line_2)

        self.verticalSpacer_37 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.left_main_page_.addItem(self.verticalSpacer_37)

        self.mainpage_second_chart_frame = QVBoxLayout()
        self.mainpage_second_chart_frame.setObjectName(u"mainpage_second_chart_frame")
        self.mainpage_second_chart_frame.setContentsMargins(0, 10, -1, -1)

        self.left_main_page_.addLayout(self.mainpage_second_chart_frame)


        self.horizontalLayout_2.addWidget(self.mainpage_right_frame)

        self.main_pages_stackw.addWidget(self.main_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.horizontalLayout_27 = QHBoxLayout(self.report_page)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.reportspage_filters_frame = QFrame(self.report_page)
        self.reportspage_filters_frame.setObjectName(u"reportspage_filters_frame")
        self.reportspage_filters_frame.setStyleSheet(u"#reportspage_filters_frame{\n"
"	border:  2px solid rgb(150,150,150);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	/*min-width:700px*/\n"
"	max-width: 400px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(50,50,50);\n"
"	font-size:16px;\n"
"	margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"	font-size: 18px;	\n"
"	border: 1px solid rgba(6, 76, 130, 120);\n"
"	border-radius: 5px;\n"
"	margin-bottom: 30px;\n"
"	padding: 10px;\n"
"	padding-top: 30px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"	image: url(:/assets/Assets/icons/icons8-check-50.png);\n"
"	background-color: rgb(6, 76, 130);\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"	width: 15px;\n"
"    height: 15px;\n"
"	border:1px solid rgb(6, 76, 130);\n"
"	border-radius: 3px;\n"
"}\n"
"")
        self.reportpage_filters_frame = QVBoxLayout(self.reportspage_filters_frame)
        self.reportpage_filters_frame.setObjectName(u"reportpage_filters_frame")
        self.label_70 = QLabel(self.reportspage_filters_frame)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);\n"
"")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.reportpage_filters_frame.addWidget(self.label_70)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.reportpage_filters_frame.addItem(self.verticalSpacer_23)

        self.scrollArea_2 = QScrollArea(self.reportspage_filters_frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"\n"
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
"        background-color:rgb(6, 76, 130);\n"
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
"    QSc"
                        "rollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
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
"\n"
"\n"
"")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.filters_scrollAreaWidgetContents = QWidget()
        self.filters_scrollAreaWidgetContents.setObjectName(u"filters_scrollAreaWidgetContents")
        self.filters_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 322, 1758))
        self.filters_scrollAreaWidgetContents.setStyleSheet(u"#filters_scrollAreaWidgetContents{\n"
"	background-color: #ffffff;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.filters_scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.reportpage_filtername_groupbox = QGroupBox(self.filters_scrollAreaWidgetContents)
        self.reportpage_filtername_groupbox.setObjectName(u"reportpage_filtername_groupbox")
        self.reportpage_filtername_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.reportpage_filtername_groupbox.setCheckable(True)
        self.reportpage_filtername_groupbox.setChecked(False)
        self.verticalLayout_18 = QVBoxLayout(self.reportpage_filtername_groupbox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_22 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer_22)

        self.reportpage_filtername_frame = QFrame(self.reportpage_filtername_groupbox)
        self.reportpage_filtername_frame.setObjectName(u"reportpage_filtername_frame")
        self.reportpage_filtername_frame.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_16 = QGridLayout(self.reportpage_filtername_frame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(-1, 1, -1, -1)
        self.label_71 = QLabel(self.reportpage_filtername_frame)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_16.addWidget(self.label_71, 0, 0, 1, 1)

        self.reportpage_filtername_input = QLineEdit(self.reportpage_filtername_frame)
        self.reportpage_filtername_input.setObjectName(u"reportpage_filtername_input")

        self.gridLayout_16.addWidget(self.reportpage_filtername_input, 0, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.reportpage_filtername_frame)


        self.verticalLayout_15.addWidget(self.reportpage_filtername_groupbox)

        self.reportpage_filterusername_groupbox = QGroupBox(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterusername_groupbox.setObjectName(u"reportpage_filterusername_groupbox")
        self.reportpage_filterusername_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.reportpage_filterusername_groupbox.setCheckable(True)
        self.reportpage_filterusername_groupbox.setChecked(False)
        self.verticalLayout_36 = QVBoxLayout(self.reportpage_filterusername_groupbox)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_38 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_36.addItem(self.verticalSpacer_38)

        self.reportpage_filterusername_frame = QFrame(self.reportpage_filterusername_groupbox)
        self.reportpage_filterusername_frame.setObjectName(u"reportpage_filterusername_frame")
        self.reportpage_filterusername_frame.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_20 = QGridLayout(self.reportpage_filterusername_frame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(-1, 1, -1, -1)
        self.label_74 = QLabel(self.reportpage_filterusername_frame)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_20.addWidget(self.label_74, 0, 0, 1, 1)

        self.reportpage_filterusername_input = QLineEdit(self.reportpage_filterusername_frame)
        self.reportpage_filterusername_input.setObjectName(u"reportpage_filterusername_input")

        self.gridLayout_20.addWidget(self.reportpage_filterusername_input, 0, 1, 1, 1)


        self.verticalLayout_36.addWidget(self.reportpage_filterusername_frame)


        self.verticalLayout_15.addWidget(self.reportpage_filterusername_groupbox)

        self.reportpage_filterdate_groupbox = QGroupBox(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterdate_groupbox.setObjectName(u"reportpage_filterdate_groupbox")
        self.reportpage_filterdate_groupbox.setCheckable(True)
        self.reportpage_filterdate_groupbox.setChecked(False)
        self.verticalLayout_19 = QVBoxLayout(self.reportpage_filterdate_groupbox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_25 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_19.addItem(self.verticalSpacer_25)

        self.reportpage_filterdate_frame = QFrame(self.reportpage_filterdate_groupbox)
        self.reportpage_filterdate_frame.setObjectName(u"reportpage_filterdate_frame")
        self.gridLayout_15 = QGridLayout(self.reportpage_filterdate_frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 1, 1, -1)
        self.reportpage_end_date_dateedit = QDateEdit(self.reportpage_filterdate_frame)
        self.reportpage_end_date_dateedit.setObjectName(u"reportpage_end_date_dateedit")

        self.gridLayout_15.addWidget(self.reportpage_end_date_dateedit, 1, 1, 1, 1)

        self.label_73 = QLabel(self.reportpage_filterdate_frame)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_15.addWidget(self.label_73, 1, 0, 1, 1)

        self.label_72 = QLabel(self.reportpage_filterdate_frame)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_15.addWidget(self.label_72, 0, 0, 1, 1)

        self.reportpage_start_date_dateedit = QDateEdit(self.reportpage_filterdate_frame)
        self.reportpage_start_date_dateedit.setObjectName(u"reportpage_start_date_dateedit")

        self.gridLayout_15.addWidget(self.reportpage_start_date_dateedit, 0, 1, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_56, 0, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.reportpage_filterdate_frame)


        self.verticalLayout_15.addWidget(self.reportpage_filterdate_groupbox)

        self.reportpage_filterstandards_warning_lbl = QLabel(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterstandards_warning_lbl.setObjectName(u"reportpage_filterstandards_warning_lbl")
        self.reportpage_filterstandards_warning_lbl.setStyleSheet(u"color: rgb(255, 95, 84);")
        self.reportpage_filterstandards_warning_lbl.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.reportpage_filterstandards_warning_lbl)

        self.reportpage_filterstandards_groupbox = QGroupBox(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterstandards_groupbox.setObjectName(u"reportpage_filterstandards_groupbox")
        self.reportpage_filterstandards_groupbox.setCheckable(True)
        self.reportpage_filterstandards_groupbox.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.reportpage_filterstandards_groupbox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_26 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_26)

        self.reportpage_filterstandards_frame = QFrame(self.reportpage_filterstandards_groupbox)
        self.reportpage_filterstandards_frame.setObjectName(u"reportpage_filterstandards_frame")
        self.reportpage_filterstandards_frame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.reportpage_filterstandards_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 1, -1, -1)
        self.reportpage_standards_filter_table = QTableWidget(self.reportpage_filterstandards_frame)
        if (self.reportpage_standards_filter_table.columnCount() < 2):
            self.reportpage_standards_filter_table.setColumnCount(2)
        if (self.reportpage_standards_filter_table.rowCount() < 5):
            self.reportpage_standards_filter_table.setRowCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.reportpage_standards_filter_table.setItem(0, 1, __qtablewidgetitem)
        self.reportpage_standards_filter_table.setObjectName(u"reportpage_standards_filter_table")
        self.reportpage_standards_filter_table.setMinimumSize(QSize(0, 0))
        self.reportpage_standards_filter_table.setMaximumSize(QSize(16777215, 16777215))
        self.reportpage_standards_filter_table.setStyleSheet(u"")
        self.reportpage_standards_filter_table.setFrameShape(QFrame.NoFrame)
        self.reportpage_standards_filter_table.setFrameShadow(QFrame.Sunken)
        self.reportpage_standards_filter_table.setLineWidth(0)
        self.reportpage_standards_filter_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.reportpage_standards_filter_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.reportpage_standards_filter_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reportpage_standards_filter_table.setTabKeyNavigation(True)
        self.reportpage_standards_filter_table.setDefaultDropAction(Qt.IgnoreAction)
        self.reportpage_standards_filter_table.setAlternatingRowColors(False)
        self.reportpage_standards_filter_table.setTextElideMode(Qt.ElideLeft)
        self.reportpage_standards_filter_table.setShowGrid(False)
        self.reportpage_standards_filter_table.setRowCount(5)
        self.reportpage_standards_filter_table.setColumnCount(2)
        self.reportpage_standards_filter_table.horizontalHeader().setVisible(False)
        self.reportpage_standards_filter_table.horizontalHeader().setHighlightSections(False)
        self.reportpage_standards_filter_table.verticalHeader().setVisible(False)
        self.reportpage_standards_filter_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_20.addWidget(self.reportpage_standards_filter_table)


        self.verticalLayout_14.addWidget(self.reportpage_filterstandards_frame)


        self.verticalLayout_15.addWidget(self.reportpage_filterstandards_groupbox)

        self.reportpage_filterranges_warning_lbl = QLabel(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterranges_warning_lbl.setObjectName(u"reportpage_filterranges_warning_lbl")
        self.reportpage_filterranges_warning_lbl.setStyleSheet(u"color: rgb(255, 95, 84);")
        self.reportpage_filterranges_warning_lbl.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.reportpage_filterranges_warning_lbl)

        self.reportpage_filterranges_groupbox = QGroupBox(self.filters_scrollAreaWidgetContents)
        self.reportpage_filterranges_groupbox.setObjectName(u"reportpage_filterranges_groupbox")
        self.reportpage_filterranges_groupbox.setCheckable(True)
        self.reportpage_filterranges_groupbox.setChecked(False)
        self.verticalLayout_45 = QVBoxLayout(self.reportpage_filterranges_groupbox)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalSpacer_45 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_45)

        self.reportpage_filterranges_frame = QFrame(self.reportpage_filterranges_groupbox)
        self.reportpage_filterranges_frame.setObjectName(u"reportpage_filterranges_frame")
        self.reportpage_filterranges_frame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_47 = QVBoxLayout(self.reportpage_filterranges_frame)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(-1, 1, -1, -1)
        self.reportpage_filter_standards_combobox = QComboBox(self.reportpage_filterranges_frame)
        self.reportpage_filter_standards_combobox.setObjectName(u"reportpage_filter_standards_combobox")

        self.verticalLayout_47.addWidget(self.reportpage_filter_standards_combobox)

        self.reportpage_standards_filter_ranges_table = QTableWidget(self.reportpage_filterranges_frame)
        if (self.reportpage_standards_filter_ranges_table.rowCount() < 15):
            self.reportpage_standards_filter_ranges_table.setRowCount(15)
        self.reportpage_standards_filter_ranges_table.setObjectName(u"reportpage_standards_filter_ranges_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reportpage_standards_filter_ranges_table.sizePolicy().hasHeightForWidth())
        self.reportpage_standards_filter_ranges_table.setSizePolicy(sizePolicy2)
        self.reportpage_standards_filter_ranges_table.setMinimumSize(QSize(0, 0))
        self.reportpage_standards_filter_ranges_table.setMaximumSize(QSize(16777215, 16777215))
        self.reportpage_standards_filter_ranges_table.setStyleSheet(u"")
        self.reportpage_standards_filter_ranges_table.setFrameShape(QFrame.NoFrame)
        self.reportpage_standards_filter_ranges_table.setFrameShadow(QFrame.Sunken)
        self.reportpage_standards_filter_ranges_table.setLineWidth(0)
        self.reportpage_standards_filter_ranges_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.reportpage_standards_filter_ranges_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.reportpage_standards_filter_ranges_table.setAutoScroll(True)
        self.reportpage_standards_filter_ranges_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reportpage_standards_filter_ranges_table.setTabKeyNavigation(True)
        self.reportpage_standards_filter_ranges_table.setDefaultDropAction(Qt.IgnoreAction)
        self.reportpage_standards_filter_ranges_table.setAlternatingRowColors(False)
        self.reportpage_standards_filter_ranges_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.reportpage_standards_filter_ranges_table.setTextElideMode(Qt.ElideLeft)
        self.reportpage_standards_filter_ranges_table.setShowGrid(False)
        self.reportpage_standards_filter_ranges_table.setRowCount(15)
        self.reportpage_standards_filter_ranges_table.setColumnCount(0)
        self.reportpage_standards_filter_ranges_table.horizontalHeader().setVisible(False)
        self.reportpage_standards_filter_ranges_table.horizontalHeader().setMinimumSectionSize(50)
        self.reportpage_standards_filter_ranges_table.horizontalHeader().setHighlightSections(False)
        self.reportpage_standards_filter_ranges_table.verticalHeader().setVisible(False)
        self.reportpage_standards_filter_ranges_table.verticalHeader().setMinimumSectionSize(35)
        self.reportpage_standards_filter_ranges_table.verticalHeader().setDefaultSectionSize(35)
        self.reportpage_standards_filter_ranges_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_47.addWidget(self.reportpage_standards_filter_ranges_table)


        self.verticalLayout_45.addWidget(self.reportpage_filterranges_frame)


        self.verticalLayout_15.addWidget(self.reportpage_filterranges_groupbox)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_24)

        self.scrollArea_2.setWidget(self.filters_scrollAreaWidgetContents)

        self.reportpage_filters_frame.addWidget(self.scrollArea_2)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_58)

        self.reportpage_apply_filters_btn = QPushButton(self.reportspage_filters_frame)
        self.reportpage_apply_filters_btn.setObjectName(u"reportpage_apply_filters_btn")

        self.horizontalLayout_31.addWidget(self.reportpage_apply_filters_btn)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_59)


        self.reportpage_filters_frame.addLayout(self.horizontalLayout_31)


        self.horizontalLayout_27.addWidget(self.reportspage_filters_frame)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(5, 0, -1, -1)
        self.reportspage_all_checkbox = QCheckBox(self.report_page)
        self.reportspage_all_checkbox.setObjectName(u"reportspage_all_checkbox")

        self.horizontalLayout_57.addWidget(self.reportspage_all_checkbox)

        self.line_25 = QFrame(self.report_page)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setMinimumSize(QSize(20, 0))
        self.line_25.setStyleSheet(u"color:rgba(12, 80, 139, 150);")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setLineWidth(1)
        self.line_25.setFrameShape(QFrame.VLine)

        self.horizontalLayout_57.addWidget(self.line_25)

        self.reportspage_delete_selections_btn = QPushButton(self.report_page)
        self.reportspage_delete_selections_btn.setObjectName(u"reportspage_delete_selections_btn")
        self.reportspage_delete_selections_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(197, 63, 59);\n"
"border: 2px solid rgb(197, 63, 59);\n"
"min-width: 80px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(152, 46, 44);\n"
"border: 2px solid rgb(152, 46, 44);\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/assets/Assets/icons/icons8-remove-table-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportspage_delete_selections_btn.setIcon(icon22)
        self.reportspage_delete_selections_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_57.addWidget(self.reportspage_delete_selections_btn)

        self.reportpage_rebuild_btn = QPushButton(self.report_page)
        self.reportpage_rebuild_btn.setObjectName(u"reportpage_rebuild_btn")
        self.reportpage_rebuild_btn.setEnabled(True)
        self.reportpage_rebuild_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(41, 147, 108);\n"
"border: 2px solid rgb(41, 147, 108);\n"
"min-width: 80px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(27, 98, 71);\n"
"border: 2px solid rgb(27, 98, 71);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
" color: #a0a0a0;\n"
"border: 2px solid #a0a0a0;\n"
"\n"
"}")

        self.horizontalLayout_57.addWidget(self.reportpage_rebuild_btn)

        self.line_26 = QFrame(self.report_page)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setMinimumSize(QSize(20, 0))
        self.line_26.setStyleSheet(u"color:rgba(12, 80, 139, 150);")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setLineWidth(1)
        self.line_26.setFrameShape(QFrame.VLine)

        self.horizontalLayout_57.addWidget(self.line_26)

        self.label_48 = QLabel(self.report_page)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_57.addWidget(self.label_48)

        self.reportpage_compare_standards_combobox = QComboBox(self.report_page)
        self.reportpage_compare_standards_combobox.setObjectName(u"reportpage_compare_standards_combobox")

        self.horizontalLayout_57.addWidget(self.reportpage_compare_standards_combobox)

        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_88)

        self.reportpage_compare_btn = QPushButton(self.report_page)
        self.reportpage_compare_btn.setObjectName(u"reportpage_compare_btn")
        self.reportpage_compare_btn.setStyleSheet(u"QPushButton{\n"
"/*	max-width: 100px;*/\n"
"	min-width: 120px;\n"
"	min-height: 40px;\n"
"	background-color: rgb(200, 96, 26);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(173, 83, 22);\n"
"\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/assets/Assets/icons/icons8-compare-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportpage_compare_btn.setIcon(icon23)
        self.reportpage_compare_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_57.addWidget(self.reportpage_compare_btn)

        self.horizontalSpacer_101 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_101)

        self.line_27 = QFrame(self.report_page)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setMinimumSize(QSize(20, 0))
        self.line_27.setStyleSheet(u"color:rgba(12, 80, 139, 150);")
        self.line_27.setFrameShadow(QFrame.Plain)
        self.line_27.setLineWidth(1)
        self.line_27.setFrameShape(QFrame.VLine)

        self.horizontalLayout_57.addWidget(self.line_27)


        self.verticalLayout_38.addLayout(self.horizontalLayout_57)

        self.line_21 = QFrame(self.report_page)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_38.addWidget(self.line_21)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 0, -1, -1)
        self.reportpage_samples_table = QTableWidget(self.report_page)
        if (self.reportpage_samples_table.columnCount() < 5):
            self.reportpage_samples_table.setColumnCount(5)
        if (self.reportpage_samples_table.rowCount() < 11):
            self.reportpage_samples_table.setRowCount(11)
        self.reportpage_samples_table.setObjectName(u"reportpage_samples_table")
        self.reportpage_samples_table.setEnabled(True)
        self.reportpage_samples_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.reportpage_samples_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.reportpage_samples_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reportpage_samples_table.setRowCount(11)
        self.reportpage_samples_table.setColumnCount(5)
        self.reportpage_samples_table.verticalHeader().setDefaultSectionSize(45)

        self.horizontalLayout_61.addWidget(self.reportpage_samples_table)


        self.verticalLayout_38.addLayout(self.horizontalLayout_61)


        self.horizontalLayout_27.addLayout(self.verticalLayout_38)

        self.main_pages_stackw.addWidget(self.report_page)
        self.grading_ranges_page = QWidget()
        self.grading_ranges_page.setObjectName(u"grading_ranges_page")
        self.verticalLayout_30 = QVBoxLayout(self.grading_ranges_page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.gradingranges_tabs = QTabWidget(self.grading_ranges_page)
        self.gradingranges_tabs.setObjectName(u"gradingranges_tabs")
        self.gradingranges_tabs.setStyleSheet(u"QTabBar::tab{\n"
"	height:40px;\n"
"	width: 300px;\n"
"\n"
"}\n"
"\n"
"\n"
"#new_standard_tab,\n"
"#all_standards_tab\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.gradingranges_tabs.setUsesScrollButtons(True)
        self.gradingranges_tabs.setDocumentMode(False)
        self.gradingranges_tabs.setTabsClosable(False)
        self.gradingranges_tabs.setMovable(False)
        self.gradingranges_tabs.setTabBarAutoHide(False)
        self.all_standards_tab = QWidget()
        self.all_standards_tab.setObjectName(u"all_standards_tab")
        self.verticalLayout_32 = QVBoxLayout(self.all_standards_tab)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.settingpage_grading_standards_groupbox = QGroupBox(self.all_standards_tab)
        self.settingpage_grading_standards_groupbox.setObjectName(u"settingpage_grading_standards_groupbox")
        sizePolicy1.setHeightForWidth(self.settingpage_grading_standards_groupbox.sizePolicy().hasHeightForWidth())
        self.settingpage_grading_standards_groupbox.setSizePolicy(sizePolicy1)
        self.verticalLayout_17 = QVBoxLayout(self.settingpage_grading_standards_groupbox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, 10, -1, -1)
        self.settingpage_grading_standards_table = QTableWidget(self.settingpage_grading_standards_groupbox)
        if (self.settingpage_grading_standards_table.columnCount() < 4):
            self.settingpage_grading_standards_table.setColumnCount(4)
        if (self.settingpage_grading_standards_table.rowCount() < 2):
            self.settingpage_grading_standards_table.setRowCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.settingpage_grading_standards_table.setItem(0, 0, __qtablewidgetitem1)
        self.settingpage_grading_standards_table.setObjectName(u"settingpage_grading_standards_table")
        self.settingpage_grading_standards_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 16pt;\n"
"	font-weight:bold;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
"")
        self.settingpage_grading_standards_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.settingpage_grading_standards_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.settingpage_grading_standards_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.settingpage_grading_standards_table.setWordWrap(True)
        self.settingpage_grading_standards_table.setRowCount(2)
        self.settingpage_grading_standards_table.setColumnCount(4)
        self.settingpage_grading_standards_table.horizontalHeader().setMinimumSectionSize(60)
        self.settingpage_grading_standards_table.horizontalHeader().setDefaultSectionSize(100)
        self.settingpage_grading_standards_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.settingpage_grading_standards_table.horizontalHeader().setStretchLastSection(True)
        self.settingpage_grading_standards_table.verticalHeader().setVisible(False)
        self.settingpage_grading_standards_table.verticalHeader().setCascadingSectionResizes(False)
        self.settingpage_grading_standards_table.verticalHeader().setMinimumSectionSize(23)
        self.settingpage_grading_standards_table.verticalHeader().setDefaultSectionSize(45)
        self.settingpage_grading_standards_table.verticalHeader().setHighlightSections(True)
        self.settingpage_grading_standards_table.verticalHeader().setProperty("showSortIndicator", False)
        self.settingpage_grading_standards_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_51.addWidget(self.settingpage_grading_standards_table)


        self.verticalLayout_17.addLayout(self.horizontalLayout_51)


        self.verticalLayout_32.addWidget(self.settingpage_grading_standards_groupbox)

        self.gradingranges_tabs.addTab(self.all_standards_tab, "")
        self.new_standard_tab = QWidget()
        self.new_standard_tab.setObjectName(u"new_standard_tab")
        self.new_standard_tab.setStyleSheet(u"")
        self.horizontalLayout_22 = QHBoxLayout(self.new_standard_tab)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_65 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_65)

        self.settingpage_grading_new_standards_groupbox = QGroupBox(self.new_standard_tab)
        self.settingpage_grading_new_standards_groupbox.setObjectName(u"settingpage_grading_new_standards_groupbox")
        self.settingpage_grading_new_standards_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.settingpage_grading_new_standards_groupbox)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.settingpage_grading_editmode_lbl = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_grading_editmode_lbl.setObjectName(u"settingpage_grading_editmode_lbl")
        self.settingpage_grading_editmode_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color:rgb(6, 76, 130);\n"
"padding:5px;\n"
"margin-bottom:20px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"")
        self.settingpage_grading_editmode_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.settingpage_grading_editmode_lbl)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, 1, -1, -1)
        self.label_27 = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(40, 0))
        self.label_27.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_55.addWidget(self.label_27)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_22)

        self.settingpage_grading_name_inpt = QLineEdit(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_grading_name_inpt.setObjectName(u"settingpage_grading_name_inpt")
        self.settingpage_grading_name_inpt.setStyleSheet(u"")

        self.horizontalLayout_55.addWidget(self.settingpage_grading_name_inpt)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_18)


        self.verticalLayout_31.addLayout(self.horizontalLayout_55)

        self.line_31 = QFrame(self.settingpage_grading_new_standards_groupbox)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setMinimumSize(QSize(0, 5))
        self.line_31.setLineWidth(1)
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_31)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_28 = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"max-width:300px;")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.settingpage_grading_low_limit_spinbox = QDoubleSpinBox(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_grading_low_limit_spinbox.setObjectName(u"settingpage_grading_low_limit_spinbox")
        self.settingpage_grading_low_limit_spinbox.setStyleSheet(u"max-width:100px;\n"
"min-width: 50px;")
        self.settingpage_grading_low_limit_spinbox.setMaximum(25.000000000000000)

        self.horizontalLayout_24.addWidget(self.settingpage_grading_low_limit_spinbox)

        self.horizontalSpacer_20 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_20)

        self.label_29 = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"max-width:300px;")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.settingpage_grading_up_limit_spinbox = QDoubleSpinBox(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_grading_up_limit_spinbox.setObjectName(u"settingpage_grading_up_limit_spinbox")
        self.settingpage_grading_up_limit_spinbox.setStyleSheet(u"max-width:100px;\n"
"min-width: 50px;")
        self.settingpage_grading_up_limit_spinbox.setMaximum(25.000000000000000)

        self.horizontalLayout_24.addWidget(self.settingpage_grading_up_limit_spinbox)

        self.horizontalSpacer_19 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_19)

        self.settingpage_pelletizing_add_range_btn = QPushButton(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_pelletizing_add_range_btn.setObjectName(u"settingpage_pelletizing_add_range_btn")
        self.settingpage_pelletizing_add_range_btn.setStyleSheet(u"max-width: 50px;\n"
"min-width: 50px;")

        self.horizontalLayout_24.addWidget(self.settingpage_pelletizing_add_range_btn)


        self.verticalLayout_31.addLayout(self.horizontalLayout_24)

        self.line_32 = QFrame(self.settingpage_grading_new_standards_groupbox)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setMinimumSize(QSize(0, 5))
        self.line_32.setLineWidth(1)
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_32)

        self.settingpage_grading_warning_lbl = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.settingpage_grading_warning_lbl.setObjectName(u"settingpage_grading_warning_lbl")
        self.settingpage_grading_warning_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"")

        self.verticalLayout_31.addWidget(self.settingpage_grading_warning_lbl)

        self.label_26 = QLabel(self.settingpage_grading_new_standards_groupbox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"max-width: 200;\n"
"font-size:20px;\n"
"color:rgb(6, 76, 130);\n"
"font-weight:bold;")

        self.verticalLayout_31.addWidget(self.label_26)

        self.settingpage_grading_ranges_table = QTableWidget(self.settingpage_grading_new_standards_groupbox)
        if (self.settingpage_grading_ranges_table.columnCount() < 5):
            self.settingpage_grading_ranges_table.setColumnCount(5)
        if (self.settingpage_grading_ranges_table.rowCount() < 1):
            self.settingpage_grading_ranges_table.setRowCount(1)
        self.settingpage_grading_ranges_table.setObjectName(u"settingpage_grading_ranges_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settingpage_grading_ranges_table.sizePolicy().hasHeightForWidth())
        self.settingpage_grading_ranges_table.setSizePolicy(sizePolicy3)
        self.settingpage_grading_ranges_table.setMaximumSize(QSize(16777215, 500))
        self.settingpage_grading_ranges_table.setSizeIncrement(QSize(0, 0))
        self.settingpage_grading_ranges_table.setBaseSize(QSize(0, 0))
        self.settingpage_grading_ranges_table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.settingpage_grading_ranges_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
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
        self.settingpage_grading_ranges_table.horizontalHeader().setDefaultSectionSize(120)
        self.settingpage_grading_ranges_table.verticalHeader().setVisible(False)
        self.settingpage_grading_ranges_table.verticalHeader().setDefaultSectionSize(45)

        self.verticalLayout_31.addWidget(self.settingpage_grading_ranges_table, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_31.addItem(self.verticalSpacer_10)

        self.horizontalFrame_5 = QFrame(self.settingpage_grading_new_standards_groupbox)
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


        self.verticalLayout_31.addWidget(self.horizontalFrame_5)

        self.gradingranges_new_standard_success_frame = QFrame(self.settingpage_grading_new_standards_groupbox)
        self.gradingranges_new_standard_success_frame.setObjectName(u"gradingranges_new_standard_success_frame")
        self.gradingranges_new_standard_success_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(58, 209, 154);\n"
"}\n"
"")
        self.gradingranges_new_standard_success_frame.setFrameShape(QFrame.StyledPanel)
        self.gradingranges_new_standard_success_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.gradingranges_new_standard_success_frame)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_90 = QLabel(self.gradingranges_new_standard_success_frame)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMaximumSize(QSize(50, 50))
        self.label_90.setPixmap(QPixmap(u":/assets/Assets/icons/icons8-check-150.png"))
        self.label_90.setScaledContents(True)

        self.horizontalLayout_43.addWidget(self.label_90)

        self.gradingranges_new_standard_success_lbl = QLabel(self.gradingranges_new_standard_success_frame)
        self.gradingranges_new_standard_success_lbl.setObjectName(u"gradingranges_new_standard_success_lbl")
        self.gradingranges_new_standard_success_lbl.setMinimumSize(QSize(0, 50))
        self.gradingranges_new_standard_success_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")
        self.gradingranges_new_standard_success_lbl.setScaledContents(False)

        self.horizontalLayout_43.addWidget(self.gradingranges_new_standard_success_lbl)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_72)


        self.verticalLayout_31.addWidget(self.gradingranges_new_standard_success_frame)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_9)


        self.horizontalLayout_45.addLayout(self.verticalLayout_31)

        self.line_3 = QFrame(self.settingpage_grading_new_standards_groupbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(16, 0))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_45.addWidget(self.line_3)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, -1, -1)

        self.verticalLayout_33.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_45.addLayout(self.verticalLayout_33)


        self.verticalLayout_22.addLayout(self.horizontalLayout_45)


        self.horizontalLayout_22.addWidget(self.settingpage_grading_new_standards_groupbox)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_75)

        self.gradingranges_tabs.addTab(self.new_standard_tab, "")

        self.verticalLayout_30.addWidget(self.gradingranges_tabs)

        self.main_pages_stackw.addWidget(self.grading_ranges_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 0, 10, -1)
        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_63)

        self.settingpage_tabs = QTabWidget(self.settings_page)
        self.settingpage_tabs.setObjectName(u"settingpage_tabs")
        self.settingpage_tabs.setEnabled(True)
        self.settingpage_tabs.setAutoFillBackground(False)
        self.settingpage_tabs.setStyleSheet(u"#settingpage_tabs{\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font-size: 14px;\n"
"	/*max-width:80px;*/\n"
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
"#settingpage_storage_tab,\n"
"#settingpage_pelletizing_tab,\n"
"#settingpage_algorithm_tab,\n"
"#settingpage_sample_tab,\n"
"#settingpage_export_tab\n"
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
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

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

        self.settingpage_tabs.addTab(self.settingpage_general_tab, "")
        self.settingpage_sample_tab = QWidget()
        self.settingpage_sample_tab.setObjectName(u"settingpage_sample_tab")
        self.settingpage_sample_tab.setStyleSheet(u"")
        self.verticalLayout_41 = QVBoxLayout(self.settingpage_sample_tab)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.settingpage_sample_auto_name_groupbox = QGroupBox(self.settingpage_sample_tab)
        self.settingpage_sample_auto_name_groupbox.setObjectName(u"settingpage_sample_auto_name_groupbox")
        self.settingpage_sample_auto_name_groupbox.setStyleSheet(u"QGroupBox::indicator:checked {\n"
"	image: url(:/assets/Assets/icons/icons8-check-50.png);\n"
"	background-color: rgb(6, 76, 130);\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"	width: 15px;\n"
"    height: 15px;\n"
"	border:1px solid rgb(6, 76, 130);\n"
"	border-radius: 3px;\n"
"}\n"
"")
        self.settingpage_sample_auto_name_groupbox.setCheckable(True)
        self.verticalLayout_42 = QVBoxLayout(self.settingpage_sample_auto_name_groupbox)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.settingpage_sample_autoname_frame = QFrame(self.settingpage_sample_auto_name_groupbox)
        self.settingpage_sample_autoname_frame.setObjectName(u"settingpage_sample_autoname_frame")
        self.verticalLayout_44 = QVBoxLayout(self.settingpage_sample_autoname_frame)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 1, -1, 1)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.settingpage_sample_text1_input = QLineEdit(self.settingpage_sample_autoname_frame)
        self.settingpage_sample_text1_input.setObjectName(u"settingpage_sample_text1_input")

        self.gridLayout_9.addWidget(self.settingpage_sample_text1_input, 0, 1, 1, 1)

        self.label_68 = QLabel(self.settingpage_sample_autoname_frame)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_9.addWidget(self.label_68, 0, 0, 1, 1)

        self.horizontalSpacer_95 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_95, 0, 2, 1, 1)


        self.verticalLayout_44.addLayout(self.gridLayout_9)

        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_44.addItem(self.verticalSpacer_42)

        self.verticalFrame = QFrame(self.settingpage_sample_autoname_frame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"QPushButton{\n"
"min-width:100px;\n"
"background-color: rgb(150,150,150);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50,50,50);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"	font-size: 14px;\n"
"	max-width:200px;\n"
"	min-width:100px;\n"
"	margin-left:10px;\n"
"	\n"
"}\n"
"")
        self.verticalLayout_46 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, 12, -1, 22)
        self.gridFrame_3 = QFrame(self.verticalFrame)
        self.gridFrame_3.setObjectName(u"gridFrame_3")
        self.gridFrame_3.setStyleSheet(u"")
        self.gridLayout_23 = QGridLayout(self.gridFrame_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 1, -1, -1)
        self.label_106 = QLabel(self.gridFrame_3)
        self.label_106.setObjectName(u"label_106")
        sizePolicy1.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy1)
        self.label_106.setTextFormat(Qt.AutoText)
        self.label_106.setScaledContents(False)
        self.label_106.setAlignment(Qt.AlignCenter)
        self.label_106.setWordWrap(False)

        self.gridLayout_23.addWidget(self.label_106, 0, 2, 1, 1)

        self.horizontalSpacer_104 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_104, 1, 1, 1, 1)

        self.horizontalSpacer_102 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_102, 1, 3, 1, 1)

        self.label_99 = QLabel(self.gridFrame_3)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_99, 0, 4, 1, 1)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_94, 1, 5, 1, 1)

        self.label_103 = QLabel(self.gridFrame_3)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(110, 0))
        self.label_103.setMaximumSize(QSize(210, 16777215))
        self.label_103.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_103, 0, 0, 1, 1)

        self.settingpage_sample_text1_code_btn = QPushButton(self.gridFrame_3)
        self.settingpage_sample_text1_code_btn.setObjectName(u"settingpage_sample_text1_code_btn")

        self.gridLayout_23.addWidget(self.settingpage_sample_text1_code_btn, 1, 4, 1, 1)

        self.settingpage_sample_spacer_code_btn = QPushButton(self.gridFrame_3)
        self.settingpage_sample_spacer_code_btn.setObjectName(u"settingpage_sample_spacer_code_btn")

        self.gridLayout_23.addWidget(self.settingpage_sample_spacer_code_btn, 1, 0, 1, 1)

        self.settingpage_sample_username_code_btn = QPushButton(self.gridFrame_3)
        self.settingpage_sample_username_code_btn.setObjectName(u"settingpage_sample_username_code_btn")

        self.gridLayout_23.addWidget(self.settingpage_sample_username_code_btn, 1, 2, 1, 1)


        self.verticalLayout_46.addWidget(self.gridFrame_3)

        self.gridFrame = QFrame(self.verticalFrame)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.gridFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_96 = QLabel(self.gridFrame)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"font-size:20px;")

        self.gridLayout_3.addWidget(self.label_96, 0, 0, 1, 1)

        self.label_76 = QLabel(self.gridFrame)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(110, 0))
        self.label_76.setMaximumSize(QSize(210, 16777215))
        self.label_76.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_76, 1, 1, 1, 1)

        self.settingpage_sample_day_code_btn = QPushButton(self.gridFrame)
        self.settingpage_sample_day_code_btn.setObjectName(u"settingpage_sample_day_code_btn")

        self.gridLayout_3.addWidget(self.settingpage_sample_day_code_btn, 2, 2, 1, 1)

        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_93, 2, 3, 1, 1)

        self.settingpage_sample_minute_code_btn = QPushButton(self.gridFrame)
        self.settingpage_sample_minute_code_btn.setObjectName(u"settingpage_sample_minute_code_btn")

        self.gridLayout_3.addWidget(self.settingpage_sample_minute_code_btn, 2, 5, 1, 1)

        self.label_75 = QLabel(self.gridFrame)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(110, 0))
        self.label_75.setMaximumSize(QSize(210, 16777215))
        self.label_75.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_75, 1, 0, 1, 1)

        self.label_92 = QLabel(self.gridFrame)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(110, 0))
        self.label_92.setMaximumSize(QSize(210, 16777215))
        self.label_92.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_92, 1, 5, 1, 1)

        self.settingpage_sample_month_code_btn = QPushButton(self.gridFrame)
        self.settingpage_sample_month_code_btn.setObjectName(u"settingpage_sample_month_code_btn")

        self.gridLayout_3.addWidget(self.settingpage_sample_month_code_btn, 2, 1, 1, 1)

        self.label_91 = QLabel(self.gridFrame)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(110, 0))
        self.label_91.setMaximumSize(QSize(210, 16777215))
        self.label_91.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_91, 1, 4, 1, 1)

        self.horizontalSpacer_96 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_96, 2, 6, 1, 1)

        self.settingpage_sample_year_code_btn = QPushButton(self.gridFrame)
        self.settingpage_sample_year_code_btn.setObjectName(u"settingpage_sample_year_code_btn")

        self.gridLayout_3.addWidget(self.settingpage_sample_year_code_btn, 2, 0, 1, 1)

        self.label_77 = QLabel(self.gridFrame)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(110, 0))
        self.label_77.setMaximumSize(QSize(210, 16777215))
        self.label_77.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_77, 1, 2, 1, 1)

        self.settingpage_sample_houre_code_btn = QPushButton(self.gridFrame)
        self.settingpage_sample_houre_code_btn.setObjectName(u"settingpage_sample_houre_code_btn")

        self.gridLayout_3.addWidget(self.settingpage_sample_houre_code_btn, 2, 4, 1, 1)


        self.verticalLayout_46.addWidget(self.gridFrame)


        self.verticalLayout_44.addWidget(self.verticalFrame)

        self.verticalSpacer_44 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_44.addItem(self.verticalSpacer_44)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, -1, -1)
        self.label_97 = QLabel(self.settingpage_sample_autoname_frame)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_60.addWidget(self.label_97)

        self.settingpage_sample_auto_name_input = QLineEdit(self.settingpage_sample_autoname_frame)
        self.settingpage_sample_auto_name_input.setObjectName(u"settingpage_sample_auto_name_input")
        self.settingpage_sample_auto_name_input.setStyleSheet(u"max-width:800px;")
        self.settingpage_sample_auto_name_input.setReadOnly(True)

        self.horizontalLayout_60.addWidget(self.settingpage_sample_auto_name_input)

        self.settingpage_sample_auto_name_clear_btn = QPushButton(self.settingpage_sample_autoname_frame)
        self.settingpage_sample_auto_name_clear_btn.setObjectName(u"settingpage_sample_auto_name_clear_btn")

        self.horizontalLayout_60.addWidget(self.settingpage_sample_auto_name_clear_btn)


        self.verticalLayout_44.addLayout(self.horizontalLayout_60)


        self.verticalLayout_42.addWidget(self.settingpage_sample_autoname_frame)


        self.verticalLayout_41.addWidget(self.settingpage_sample_auto_name_groupbox)

        self.verticalSpacer_43 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_41.addItem(self.verticalSpacer_43)

        self.groupBox_6 = QGroupBox(self.settingpage_sample_tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_43 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_66 = QLabel(self.groupBox_6)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_14.addWidget(self.label_66, 0, 0, 1, 1)

        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_98, 0, 2, 1, 1)

        self.settingpage_sample_default_standard_comboxos = QComboBox(self.groupBox_6)
        self.settingpage_sample_default_standard_comboxos.setObjectName(u"settingpage_sample_default_standard_comboxos")

        self.gridLayout_14.addWidget(self.settingpage_sample_default_standard_comboxos, 0, 1, 1, 1)

        self.label_93 = QLabel(self.groupBox_6)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_14.addWidget(self.label_93, 1, 0, 1, 1)

        self.settingpage_sample_save_image_checkbox = QCheckBox(self.groupBox_6)
        self.settingpage_sample_save_image_checkbox.setObjectName(u"settingpage_sample_save_image_checkbox")

        self.gridLayout_14.addWidget(self.settingpage_sample_save_image_checkbox, 1, 1, 1, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_14)


        self.verticalLayout_41.addWidget(self.groupBox_6)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_99 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_99)

        self.settingpage_sample_save_btn = QPushButton(self.settingpage_sample_tab)
        self.settingpage_sample_save_btn.setObjectName(u"settingpage_sample_save_btn")

        self.horizontalLayout_59.addWidget(self.settingpage_sample_save_btn)

        self.settingpage_sample_cancel_btn = QPushButton(self.settingpage_sample_tab)
        self.settingpage_sample_cancel_btn.setObjectName(u"settingpage_sample_cancel_btn")

        self.horizontalLayout_59.addWidget(self.settingpage_sample_cancel_btn)

        self.horizontalSpacer_100 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_100)


        self.verticalLayout_41.addLayout(self.horizontalLayout_59)

        self.settingpage_tabs.addTab(self.settingpage_sample_tab, "")
        self.settingpage_export_tab = QWidget()
        self.settingpage_export_tab.setObjectName(u"settingpage_export_tab")
        self.verticalLayout_59 = QVBoxLayout(self.settingpage_export_tab)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_113 = QLabel(self.settingpage_export_tab)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(110, 0))
        self.label_113.setStyleSheet(u"min-width:100px;")

        self.horizontalLayout_67.addWidget(self.label_113)

        self.settingpage_export_report_excel_path_input = QLineEdit(self.settingpage_export_tab)
        self.settingpage_export_report_excel_path_input.setObjectName(u"settingpage_export_report_excel_path_input")
        self.settingpage_export_report_excel_path_input.setEnabled(False)
        self.settingpage_export_report_excel_path_input.setMinimumSize(QSize(730, 41))
        self.settingpage_export_report_excel_path_input.setMaximumSize(QSize(310, 16777215))
        self.settingpage_export_report_excel_path_input.setStyleSheet(u"QLineEdit{\n"
"min-width: 700px;\n"
"\n"
"}")

        self.horizontalLayout_67.addWidget(self.settingpage_export_report_excel_path_input)

        self.settingpage_export_load_report_excel_btn = QPushButton(self.settingpage_export_tab)
        self.settingpage_export_load_report_excel_btn.setObjectName(u"settingpage_export_load_report_excel_btn")
        self.settingpage_export_load_report_excel_btn.setStyleSheet(u"QPushButton{\n"
"min-width:40px;\n"
"min-height: 40px;\n"
"\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/assets/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingpage_export_load_report_excel_btn.setIcon(icon24)

        self.horizontalLayout_67.addWidget(self.settingpage_export_load_report_excel_btn)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_66)


        self.verticalLayout_59.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_114 = QLabel(self.settingpage_export_tab)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(110, 0))
        self.label_114.setStyleSheet(u"min-width:100px;")

        self.horizontalLayout_68.addWidget(self.label_114)

        self.settingpage_export_compare_excel_path_input = QLineEdit(self.settingpage_export_tab)
        self.settingpage_export_compare_excel_path_input.setObjectName(u"settingpage_export_compare_excel_path_input")
        self.settingpage_export_compare_excel_path_input.setEnabled(False)
        self.settingpage_export_compare_excel_path_input.setMinimumSize(QSize(730, 41))
        self.settingpage_export_compare_excel_path_input.setMaximumSize(QSize(310, 16777215))
        self.settingpage_export_compare_excel_path_input.setStyleSheet(u"QLineEdit{\n"
"min-width: 700px;\n"
"\n"
"}")

        self.horizontalLayout_68.addWidget(self.settingpage_export_compare_excel_path_input)

        self.settingpage_export_load_compare_excel_btn = QPushButton(self.settingpage_export_tab)
        self.settingpage_export_load_compare_excel_btn.setObjectName(u"settingpage_export_load_compare_excel_btn")
        self.settingpage_export_load_compare_excel_btn.setStyleSheet(u"QPushButton{\n"
"min-width:40px;\n"
"min-height: 40px;\n"
"\n"
"}")
        self.settingpage_export_load_compare_excel_btn.setIcon(icon24)

        self.horizontalLayout_68.addWidget(self.settingpage_export_load_compare_excel_btn)

        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_112)


        self.verticalLayout_59.addLayout(self.horizontalLayout_68)

        self.verticalSpacer_8 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_59.addItem(self.verticalSpacer_8)

        self.tabWidget_2 = QTabWidget(self.settingpage_export_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"#tab,\n"
"#tab1{\n"
"	background-color:rgb(90, 117, 127);\n"
"\n"
"\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background:rgb(90, 117, 127);\n"
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
"	width: 250px;\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(255,255,255);\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border: none\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_61 = QVBoxLayout(self.tab)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalSpacer_28 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_61.addItem(self.verticalSpacer_28)

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        brush = QBrush(QColor(40, 40, 40, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(12, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(13, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(14, 0, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"	border: 1px solid rgb(12, 80, 139);\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid rgb(12, 80, 139);\n"
"\n"
"}")
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_61.addWidget(self.tableWidget)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_59.addWidget(self.tabWidget_2)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_113)

        self.settingpage_export_save_btn = QPushButton(self.settingpage_export_tab)
        self.settingpage_export_save_btn.setObjectName(u"settingpage_export_save_btn")

        self.horizontalLayout_70.addWidget(self.settingpage_export_save_btn)

        self.settingpage_export_cancel_btn = QPushButton(self.settingpage_export_tab)
        self.settingpage_export_cancel_btn.setObjectName(u"settingpage_export_cancel_btn")

        self.horizontalLayout_70.addWidget(self.settingpage_export_cancel_btn)

        self.settingpage_export_restore_btn = QPushButton(self.settingpage_export_tab)
        self.settingpage_export_restore_btn.setObjectName(u"settingpage_export_restore_btn")

        self.horizontalLayout_70.addWidget(self.settingpage_export_restore_btn)

        self.horizontalSpacer_114 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_114)


        self.verticalLayout_59.addLayout(self.horizontalLayout_70)

        self.settingpage_tabs.addTab(self.settingpage_export_tab, "")
        self.settingpage_storage_tab = QWidget()
        self.settingpage_storage_tab.setObjectName(u"settingpage_storage_tab")
        self.verticalLayout_24 = QVBoxLayout(self.settingpage_storage_tab)
        self.verticalLayout_24.setSpacing(30)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_4 = QGroupBox(self.settingpage_storage_tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(False)
        self.gridLayout_24 = QGridLayout(self.groupBox_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_98 = QLabel(self.groupBox_4)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_98, 1, 0, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_35, 0, 0, 1, 1)

        self.settingpage_db_password = QLineEdit(self.groupBox_4)
        self.settingpage_db_password.setObjectName(u"settingpage_db_password")

        self.gridLayout_24.addWidget(self.settingpage_db_password, 1, 1, 1, 1)

        self.settingpage_db_username = QLineEdit(self.groupBox_4)
        self.settingpage_db_username.setObjectName(u"settingpage_db_username")

        self.gridLayout_24.addWidget(self.settingpage_db_username, 0, 1, 1, 1)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_111, 0, 2, 1, 1)

        self.label_102 = QLabel(self.groupBox_4)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_102, 2, 0, 1, 1)

        self.settingpage_db_host = QLineEdit(self.groupBox_4)
        self.settingpage_db_host.setObjectName(u"settingpage_db_host")

        self.gridLayout_24.addWidget(self.settingpage_db_host, 2, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.settingpage_storage_tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"max-width: 300px;")

        self.gridLayout_11.addWidget(self.label_32, 1, 4, 1, 1)

        self.settingpage_storage_life_time_spinbox = QSpinBox(self.groupBox_5)
        self.settingpage_storage_life_time_spinbox.setObjectName(u"settingpage_storage_life_time_spinbox")
        self.settingpage_storage_life_time_spinbox.setMaximum(365)

        self.gridLayout_11.addWidget(self.settingpage_storage_life_time_spinbox, 1, 5, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_23, 1, 6, 1, 1)

        self.settingpage_storage_auto_clean_checkbox = QCheckBox(self.groupBox_5)
        self.settingpage_storage_auto_clean_checkbox.setObjectName(u"settingpage_storage_auto_clean_checkbox")
        self.settingpage_storage_auto_clean_checkbox.setEnabled(True)
        self.settingpage_storage_auto_clean_checkbox.setStyleSheet(u"")
        self.settingpage_storage_auto_clean_checkbox.setCheckable(True)
        self.settingpage_storage_auto_clean_checkbox.setChecked(False)
        self.settingpage_storage_auto_clean_checkbox.setTristate(False)

        self.gridLayout_11.addWidget(self.settingpage_storage_auto_clean_checkbox, 1, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_21, 1, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_11.addWidget(self.label_31, 1, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.settingpage_storage_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_17 = QGridLayout(self.groupBox_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.settingpage_storage_select_dir_btn = QPushButton(self.groupBox_3)
        self.settingpage_storage_select_dir_btn.setObjectName(u"settingpage_storage_select_dir_btn")
        self.settingpage_storage_select_dir_btn.setStyleSheet(u"QPushButton{\n"
"min-width:40px;\n"
"min-height: 40px;\n"
"\n"
"}")
        self.settingpage_storage_select_dir_btn.setIcon(icon24)

        self.gridLayout_17.addWidget(self.settingpage_storage_select_dir_btn, 0, 2, 1, 1)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_57, 0, 3, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setStyleSheet(u"min-width:100px;")

        self.gridLayout_17.addWidget(self.label, 0, 0, 1, 1)

        self.settingpage_storage_path_input = QLineEdit(self.groupBox_3)
        self.settingpage_storage_path_input.setObjectName(u"settingpage_storage_path_input")
        self.settingpage_storage_path_input.setEnabled(False)
        self.settingpage_storage_path_input.setMinimumSize(QSize(730, 41))
        self.settingpage_storage_path_input.setMaximumSize(QSize(310, 16777215))
        self.settingpage_storage_path_input.setStyleSheet(u"QLineEdit{\n"
"min-width: 700px;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.settingpage_storage_path_input, 0, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_3)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_74)

        self.settingpage_storage_save_btn = QPushButton(self.settingpage_storage_tab)
        self.settingpage_storage_save_btn.setObjectName(u"settingpage_storage_save_btn")

        self.horizontalLayout_42.addWidget(self.settingpage_storage_save_btn)

        self.settingpage_storage_cancel_btn = QPushButton(self.settingpage_storage_tab)
        self.settingpage_storage_cancel_btn.setObjectName(u"settingpage_storage_cancel_btn")

        self.horizontalLayout_42.addWidget(self.settingpage_storage_cancel_btn)

        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_67)


        self.verticalLayout_24.addLayout(self.horizontalLayout_42)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_27)

        self.settingpage_tabs.addTab(self.settingpage_storage_tab, "")
        self.settingpage_camera_tab = QWidget()
        self.settingpage_camera_tab.setObjectName(u"settingpage_camera_tab")
        self.settingpage_camera_tab.setEnabled(True)
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
        self.settingpage_camera_start_btn.setIcon(icon14)
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
        self.settingpage_camera_exposure_spinbox.setEnabled(True)
        self.settingpage_camera_exposure_spinbox.setMaximum(20000)
        self.settingpage_camera_exposure_spinbox.setValue(10000)

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

        self.label_69 = QLabel(self.settingpage_camera_left_side)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"max-width: 16666px;\n"
"color: rgb(6, 76, 130);")

        self.camera_setting_lef_side.addWidget(self.label_69)

        self.settingpage_camera_AOI_group = QGroupBox(self.settingpage_camera_left_side)
        self.settingpage_camera_AOI_group.setObjectName(u"settingpage_camera_AOI_group")
        self.gridLayout_6 = QGridLayout(self.settingpage_camera_AOI_group)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.settingpage_camera_width_lbl = QLabel(self.settingpage_camera_AOI_group)
        self.settingpage_camera_width_lbl.setObjectName(u"settingpage_camera_width_lbl")
        self.settingpage_camera_width_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.settingpage_camera_width_lbl, 1, 0, 1, 1)

        self.settingpage_camera_height_spinbox = QSpinBox(self.settingpage_camera_AOI_group)
        self.settingpage_camera_height_spinbox.setObjectName(u"settingpage_camera_height_spinbox")
        self.settingpage_camera_height_spinbox.setMaximum(5000)
        self.settingpage_camera_height_spinbox.setValue(2000)

        self.gridLayout_6.addWidget(self.settingpage_camera_height_spinbox, 2, 2, 1, 1)

        self.settingpage_camera_width_spinbox = QSpinBox(self.settingpage_camera_AOI_group)
        self.settingpage_camera_width_spinbox.setObjectName(u"settingpage_camera_width_spinbox")
        self.settingpage_camera_width_spinbox.setMaximum(5000)
        self.settingpage_camera_width_spinbox.setSingleStep(10)
        self.settingpage_camera_width_spinbox.setValue(2400)

        self.gridLayout_6.addWidget(self.settingpage_camera_width_spinbox, 1, 2, 1, 1)

        self.settingpage_camera_height_lbl = QLabel(self.settingpage_camera_AOI_group)
        self.settingpage_camera_height_lbl.setObjectName(u"settingpage_camera_height_lbl")
        self.settingpage_camera_height_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.settingpage_camera_height_lbl, 2, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_14, 1, 3, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_35, 1, 1, 1, 1)


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
        self.settingpage_camera_save_btn.setEnabled(True)

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

        self.line_17 = QFrame(self.settingpage_camera_tab)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_17)

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
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color:rgb(240,240,240)\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 5, -1, 5)
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

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

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

        self.line_23 = QFrame(self.settingpage_camera_tab)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setMinimumSize(QSize(10, 10))
        self.line_23.setSizeIncrement(QSize(0, 0))
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.settingpage_camera_right_side.addWidget(self.line_23)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.settingpage_camera_right_side.addItem(self.verticalSpacer_39)


        self.horizontalLayout_15.addLayout(self.settingpage_camera_right_side)

        self.settingpage_tabs.addTab(self.settingpage_camera_tab, "")
        self.settingpage_algorithm_tab = QWidget()
        self.settingpage_algorithm_tab.setObjectName(u"settingpage_algorithm_tab")
        self.verticalLayout_25 = QVBoxLayout(self.settingpage_algorithm_tab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, -1, 0, 0)
        self.settingpage_algorithm_border_spinbox = QSpinBox(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_border_spinbox.setObjectName(u"settingpage_algorithm_border_spinbox")
        self.settingpage_algorithm_border_spinbox.setMaximum(1000)

        self.gridLayout_19.addWidget(self.settingpage_algorithm_border_spinbox, 1, 1, 1, 1)

        self.label_24 = QLabel(self.settingpage_algorithm_tab)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_19.addWidget(self.label_24, 1, 0, 1, 1)

        self.settingpage_algorithm_threshould_spinbox = QSpinBox(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_threshould_spinbox.setObjectName(u"settingpage_algorithm_threshould_spinbox")
        self.settingpage_algorithm_threshould_spinbox.setMaximum(255)

        self.gridLayout_19.addWidget(self.settingpage_algorithm_threshould_spinbox, 0, 1, 1, 1)

        self.label_22 = QLabel(self.settingpage_algorithm_tab)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_19.addWidget(self.label_22, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout_19)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 21, -1, -1)
        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_78)

        self.settingpage_algorithm_save_btn = QPushButton(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_save_btn.setObjectName(u"settingpage_algorithm_save_btn")

        self.horizontalLayout_44.addWidget(self.settingpage_algorithm_save_btn)

        self.settingpage_algorithm_cancel_btn = QPushButton(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_cancel_btn.setObjectName(u"settingpage_algorithm_cancel_btn")

        self.horizontalLayout_44.addWidget(self.settingpage_algorithm_cancel_btn)

        self.settingpage_algorithm_restor_default_btn = QPushButton(self.settingpage_algorithm_tab)
        self.settingpage_algorithm_restor_default_btn.setObjectName(u"settingpage_algorithm_restor_default_btn")

        self.horizontalLayout_44.addWidget(self.settingpage_algorithm_restor_default_btn)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_77)


        self.verticalLayout_25.addLayout(self.horizontalLayout_44)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_6)

        self.settingpage_tabs.addTab(self.settingpage_algorithm_tab, "")

        self.horizontalLayout_33.addWidget(self.settingpage_tabs)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_64)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)

        self.frame1 = QFrame(self.settings_page)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 35))
        self.frame1.setSizeIncrement(QSize(0, 0))
#if QT_CONFIG(accessibility)
        self.frame1.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.frame1.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(48, 48, 48);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(226, 226, 226);\n"
"}\n"
"\n"
"")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame1)
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(10, 3, 10, 3)
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_62)

        self.settingpage_save_massage_lbl = QLabel(self.frame1)
        self.settingpage_save_massage_lbl.setObjectName(u"settingpage_save_massage_lbl")
        self.settingpage_save_massage_lbl.setStyleSheet(u"font-size: 15px;")

        self.horizontalLayout_32.addWidget(self.settingpage_save_massage_lbl)

        self.settingpage_save_gif_lbl = QLabel(self.frame1)
        self.settingpage_save_gif_lbl.setObjectName(u"settingpage_save_gif_lbl")
        self.settingpage_save_gif_lbl.setMinimumSize(QSize(0, 0))
        self.settingpage_save_gif_lbl.setMaximumSize(QSize(20, 20))
        self.settingpage_save_gif_lbl.setStyleSheet(u"font-size: 15px;")
        self.settingpage_save_gif_lbl.setScaledContents(True)
        self.settingpage_save_gif_lbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_32.addWidget(self.settingpage_save_gif_lbl)


        self.verticalLayout_6.addWidget(self.frame1)

        self.main_pages_stackw.addWidget(self.settings_page)
        self.calibration_page = QWidget()
        self.calibration_page.setObjectName(u"calibration_page")
        self.horizontalLayout_8 = QHBoxLayout(self.calibration_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget = QTabWidget(self.calibration_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabBar::tab:selected {\n"
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
"	width: 260px;\n"
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
"background-color: rgb(48, 48, 48);\n"
"}")
        self.cilbration = QWidget()
        self.cilbration.setObjectName(u"cilbration")
        self.horizontalLayout_52 = QHBoxLayout(self.cilbration)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.calibrationpage_left_side = QFrame(self.cilbration)
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
        icon25 = QIcon()
        icon25.addFile(u":/assets/icons/icons8-eye-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calibrationpage_check_btn.setIcon(icon25)

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
        self.calibrationpage_calib_btn.setIcon(icon14)

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
        __qtablewidgetitem18 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.calibrationpage_last_calib_tabel.setItem(0, 3, __qtablewidgetitem21)
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


        self.horizontalLayout_52.addWidget(self.calibrationpage_left_side)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_2)

        self.calibrationpage_liveimage_lbl = QLabel(self.cilbration)
        self.calibrationpage_liveimage_lbl.setObjectName(u"calibrationpage_liveimage_lbl")
        self.calibrationpage_liveimage_lbl.setStyleSheet(u"max-width : 800px;\n"
"max-height : 800px;")
        self.calibrationpage_liveimage_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.calibrationpage_liveimage_lbl.setScaledContents(False)
        self.calibrationpage_liveimage_lbl.setAlignment(Qt.AlignCenter)
        self.calibrationpage_liveimage_lbl.setWordWrap(False)

        self.horizontalLayout_52.addWidget(self.calibrationpage_liveimage_lbl)

        self.tabWidget.addTab(self.cilbration, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_48 = QVBoxLayout(self.tab_7)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(-1, 0, -1, -1)
        self.label_95 = QLabel(self.tab_7)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_62.addWidget(self.label_95)

        self.validationpage_hypotest_test_count_spinbox = QSpinBox(self.tab_7)
        self.validationpage_hypotest_test_count_spinbox.setObjectName(u"validationpage_hypotest_test_count_spinbox")
        self.validationpage_hypotest_test_count_spinbox.setMaximum(10)

        self.horizontalLayout_62.addWidget(self.validationpage_hypotest_test_count_spinbox)

        self.horizontalSpacer_106 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_106)

        self.line_29 = QFrame(self.tab_7)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.VLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_62.addWidget(self.line_29)

        self.label_94 = QLabel(self.tab_7)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_62.addWidget(self.label_94)

        self.validationpage_hypotest_standards_combobox = QComboBox(self.tab_7)
        self.validationpage_hypotest_standards_combobox.setObjectName(u"validationpage_hypotest_standards_combobox")

        self.horizontalLayout_62.addWidget(self.validationpage_hypotest_standards_combobox)

        self.horizontalSpacer_107 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_107)

        self.label_110 = QLabel(self.tab_7)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_62.addWidget(self.label_110)

        self.horizontalSpacer_103 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_103)

        self.line_28 = QFrame(self.tab_7)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.VLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_62.addWidget(self.line_28)

        self.validationpage_verify_type = QComboBox(self.tab_7)
        self.validationpage_verify_type.setObjectName(u"validationpage_verify_type")

        self.horizontalLayout_62.addWidget(self.validationpage_verify_type)

        self.horizontalSpacer_105 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_105)

        self.validationpage_hypotest_calculate_btn = QPushButton(self.tab_7)
        self.validationpage_hypotest_calculate_btn.setObjectName(u"validationpage_hypotest_calculate_btn")

        self.horizontalLayout_62.addWidget(self.validationpage_hypotest_calculate_btn)


        self.verticalLayout_48.addLayout(self.horizontalLayout_62)

        self.line_24 = QFrame(self.tab_7)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_24)

        self.scrollArea_5 = QScrollArea(self.tab_7)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.sticalhyp_scroll_area = QWidget()
        self.sticalhyp_scroll_area.setObjectName(u"sticalhyp_scroll_area")
        self.sticalhyp_scroll_area.setGeometry(QRect(0, 0, 1143, 673))
        self.verticalLayout_49 = QVBoxLayout(self.sticalhyp_scroll_area)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.validationpage_hypotest_sections_layout = QVBoxLayout()
        self.validationpage_hypotest_sections_layout.setSpacing(25)
        self.validationpage_hypotest_sections_layout.setObjectName(u"validationpage_hypotest_sections_layout")
        self.validationpage_hypotest_sections_layout.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout_49.addLayout(self.validationpage_hypotest_sections_layout)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_16)

        self.scrollArea_5.setWidget(self.sticalhyp_scroll_area)

        self.verticalLayout_48.addWidget(self.scrollArea_5)

        self.tabWidget.addTab(self.tab_7, "")

        self.horizontalLayout_8.addWidget(self.tabWidget)

        self.main_pages_stackw.addWidget(self.calibration_page)
        self.users_page = QWidget()
        self.users_page.setObjectName(u"users_page")
        self.users_page.setStyleSheet(u"#user_tabs\n"
"{\n"
"\n"
"	background-color:#ffffff;\n"
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.users_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.user_tabs = QTabWidget(self.users_page)
        self.user_tabs.setObjectName(u"user_tabs")
        self.user_tabs.setStyleSheet(u"#all_users_tab,\n"
"#user_profile_tab,\n"
"#user_register_tab\n"
"{\n"
"	\n"
"	background-color: #ffffff;\n"
"\n"
"}")
        self.user_register_tab = QWidget()
        self.user_register_tab.setObjectName(u"user_register_tab")
        self.verticalLayout_10 = QVBoxLayout(self.user_register_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridFrame_2 = QFrame(self.user_register_tab)
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
        icon26 = QIcon()
        icon26.addFile(u":/assets/Assets/icons/icons8-plus-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userspage_add_user_btn.setIcon(icon26)

        self.gridLayout_5.addWidget(self.userspage_add_user_btn, 8, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.gridFrame_2)

        self.verticalSpacer_20 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)

        self.userspage_register_error_lbl = QLabel(self.user_register_tab)
        self.userspage_register_error_lbl.setObjectName(u"userspage_register_error_lbl")
        self.userspage_register_error_lbl.setMinimumSize(QSize(310, 35))
        self.userspage_register_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"")

        self.verticalLayout_10.addWidget(self.userspage_register_error_lbl)

        self.userspage_register_success_frame = QFrame(self.user_register_tab)
        self.userspage_register_success_frame.setObjectName(u"userspage_register_success_frame")
        self.userspage_register_success_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(58, 209, 154);\n"
"}")
        self.userspage_register_success_frame.setFrameShape(QFrame.StyledPanel)
        self.userspage_register_success_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.userspage_register_success_frame)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_88 = QLabel(self.userspage_register_success_frame)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(50, 50))
        self.label_88.setPixmap(QPixmap(u":/assets/icons/icons8-check-150.png"))
        self.label_88.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.label_88)

        self.userspage_register_success_lbl = QLabel(self.userspage_register_success_frame)
        self.userspage_register_success_lbl.setObjectName(u"userspage_register_success_lbl")
        self.userspage_register_success_lbl.setMinimumSize(QSize(0, 50))
        self.userspage_register_success_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")
        self.userspage_register_success_lbl.setScaledContents(False)

        self.horizontalLayout_39.addWidget(self.userspage_register_success_lbl)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_70)


        self.verticalLayout_10.addWidget(self.userspage_register_success_frame)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.user_tabs.addTab(self.user_register_tab, "")
        self.user_profile_tab = QWidget()
        self.user_profile_tab.setObjectName(u"user_profile_tab")
        self.verticalLayout_21 = QVBoxLayout(self.user_profile_tab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.userpage_editprofile_edit_profile_groupbox = QGroupBox(self.user_profile_tab)
        self.userpage_editprofile_edit_profile_groupbox.setObjectName(u"userpage_editprofile_edit_profile_groupbox")
        self.userpage_editprofile_edit_profile_groupbox.setStyleSheet(u"QLabel{\n"
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
        self.horizontalLayout_34 = QHBoxLayout(self.userpage_editprofile_edit_profile_groupbox)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(25)
        self.label_79 = QLabel(self.userpage_editprofile_edit_profile_groupbox)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_79, 0, 0, 1, 1)

        self.label_78 = QLabel(self.userpage_editprofile_edit_profile_groupbox)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_78, 1, 0, 1, 1)

        self.userpage_editprofile_user_role_combobox = QComboBox(self.userpage_editprofile_edit_profile_groupbox)
        self.userpage_editprofile_user_role_combobox.addItem("")
        self.userpage_editprofile_user_role_combobox.setObjectName(u"userpage_editprofile_user_role_combobox")

        self.gridLayout_18.addWidget(self.userpage_editprofile_user_role_combobox, 1, 1, 1, 1)

        self.userpage_editprofile_username_inpt = QLineEdit(self.userpage_editprofile_edit_profile_groupbox)
        self.userpage_editprofile_username_inpt.setObjectName(u"userpage_editprofile_username_inpt")

        self.gridLayout_18.addWidget(self.userpage_editprofile_username_inpt, 0, 1, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_39, 0, 2, 1, 1)


        self.verticalLayout_26.addLayout(self.gridLayout_18)

        self.userpage_editprofile_edit_error_lbl = QLabel(self.userpage_editprofile_edit_profile_groupbox)
        self.userpage_editprofile_edit_error_lbl.setObjectName(u"userpage_editprofile_edit_error_lbl")
        self.userpage_editprofile_edit_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 100px;\n"
"max-width: 16777px;\n"
"max-height: 30px;\n"
"")

        self.verticalLayout_26.addWidget(self.userpage_editprofile_edit_error_lbl)

        self.horizontalFrame1 = QFrame(self.userpage_editprofile_edit_profile_groupbox)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setStyleSheet(u"QPushButton {\n"
"max-width: 120px;\n"
"}")
        self.horizontalLayout_36 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 30, -1, -1)
        self.userpage_editprofile_update_btn = QPushButton(self.horizontalFrame1)
        self.userpage_editprofile_update_btn.setObjectName(u"userpage_editprofile_update_btn")
        self.userpage_editprofile_update_btn.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.userpage_editprofile_update_btn)

        self.userpage_editprofile_cancel_btn = QPushButton(self.horizontalFrame1)
        self.userpage_editprofile_cancel_btn.setObjectName(u"userpage_editprofile_cancel_btn")

        self.horizontalLayout_36.addWidget(self.userpage_editprofile_cancel_btn)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_69)


        self.verticalLayout_26.addWidget(self.horizontalFrame1)


        self.horizontalLayout_34.addLayout(self.verticalLayout_26)


        self.verticalLayout_21.addWidget(self.userpage_editprofile_edit_profile_groupbox)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_21.addItem(self.verticalSpacer_35)

        self.userpage_editprofile_change_pass_groupbox = QGroupBox(self.user_profile_tab)
        self.userpage_editprofile_change_pass_groupbox.setObjectName(u"userpage_editprofile_change_pass_groupbox")
        self.userpage_editprofile_change_pass_groupbox.setStyleSheet(u"QLabel{\n"
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
        self.horizontalLayout_37 = QHBoxLayout(self.userpage_editprofile_change_pass_groupbox)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(30)
        self.label_80 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_80, 0, 0, 1, 1)

        self.label_81 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_81, 1, 0, 1, 1)

        self.userpage_editprofile_confirm_new_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_confirm_new_password_inpt.setObjectName(u"userpage_editprofile_confirm_new_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_confirm_new_password_inpt, 2, 1, 1, 1)

        self.userpage_editprofile_old_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_old_password_inpt.setObjectName(u"userpage_editprofile_old_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_old_password_inpt, 0, 1, 1, 1)

        self.label_86 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_86, 2, 0, 1, 1)

        self.userpage_editprofile_new_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_new_password_inpt.setObjectName(u"userpage_editprofile_new_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_new_password_inpt, 1, 1, 1, 1)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_73, 0, 2, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_22)

        self.userpage_editprofile_changepass_error_lbl = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_changepass_error_lbl.setObjectName(u"userpage_editprofile_changepass_error_lbl")
        self.userpage_editprofile_changepass_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"max-height: 30px;\n"
"")

        self.verticalLayout_27.addWidget(self.userpage_editprofile_changepass_error_lbl)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 30, -1, -1)
        self.userpage_editprofile_change_password_btn = QPushButton(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_change_password_btn.setObjectName(u"userpage_editprofile_change_password_btn")
        self.userpage_editprofile_change_password_btn.setStyleSheet(u"max-width: 120px;")

        self.horizontalLayout_38.addWidget(self.userpage_editprofile_change_password_btn)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_97)


        self.verticalLayout_27.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_37.addLayout(self.verticalLayout_27)


        self.verticalLayout_21.addWidget(self.userpage_editprofile_change_pass_groupbox)

        self.userspage_editprofile_success_frame = QFrame(self.user_profile_tab)
        self.userspage_editprofile_success_frame.setObjectName(u"userspage_editprofile_success_frame")
        self.userspage_editprofile_success_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(58, 209, 154);\n"
"}")
        self.userspage_editprofile_success_frame.setFrameShape(QFrame.StyledPanel)
        self.userspage_editprofile_success_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.userspage_editprofile_success_frame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_89 = QLabel(self.userspage_editprofile_success_frame)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(50, 50))
        self.label_89.setPixmap(QPixmap(u":/assets/icons/icons8-check-150.png"))
        self.label_89.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.label_89)

        self.userspage_editprofile_success_lbl = QLabel(self.userspage_editprofile_success_frame)
        self.userspage_editprofile_success_lbl.setObjectName(u"userspage_editprofile_success_lbl")
        self.userspage_editprofile_success_lbl.setMinimumSize(QSize(0, 50))
        self.userspage_editprofile_success_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")
        self.userspage_editprofile_success_lbl.setScaledContents(False)

        self.horizontalLayout_40.addWidget(self.userspage_editprofile_success_lbl)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_71)


        self.verticalLayout_21.addWidget(self.userspage_editprofile_success_frame)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_36)

        self.user_tabs.addTab(self.user_profile_tab, "")
        self.all_users_tab = QWidget()
        self.all_users_tab.setObjectName(u"all_users_tab")
        self.verticalLayout_11 = QVBoxLayout(self.all_users_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.userspage_user_heading_lbl = QLabel(self.all_users_tab)
        self.userspage_user_heading_lbl.setObjectName(u"userspage_user_heading_lbl")
        self.userspage_user_heading_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);\n"
"min-height: 80px;\n"
"max-height: 80px;")

        self.verticalLayout_11.addWidget(self.userspage_user_heading_lbl)

        self.userpage_all_users_table = QTableWidget(self.all_users_tab)
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

        self.user_tabs.addTab(self.all_users_tab, "")

        self.verticalLayout_9.addWidget(self.user_tabs)

        self.main_pages_stackw.addWidget(self.users_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.verticalLayout_16 = QVBoxLayout(self.help_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.helppage_tabs = QTabWidget(self.help_page)
        self.helppage_tabs.setObjectName(u"helppage_tabs")
        self.helppage_tabs.setStyleSheet(u"helppage_about_tab{\n"
"background-color:#ffffff;\n"
"\n"
"}")
        self.helppage_about_tab = QWidget()
        self.helppage_about_tab.setObjectName(u"helppage_about_tab")
        self.verticalLayout_28 = QVBoxLayout(self.helppage_about_tab)
        self.verticalLayout_28.setSpacing(20)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.scrollArea_3 = QScrollArea(self.helppage_about_tab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(16777215, 900))
        self.scrollArea_3.setStyleSheet(u"#aboutScrollArea{\n"
"background-color:#ffffff;\n"
"\n"
"}\n"
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
" "
                        "       subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
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
        self.scrollArea_3.setWidgetResizable(True)
        self.aboutScrollArea = QWidget()
        self.aboutScrollArea.setObjectName(u"aboutScrollArea")
        self.aboutScrollArea.setGeometry(QRect(0, 0, 1143, 673))
        self.verticalLayout_29 = QVBoxLayout(self.aboutScrollArea)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_82 = QLabel(self.aboutScrollArea)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);")

        self.verticalLayout_29.addWidget(self.label_82)

        self.label_83 = QLabel(self.aboutScrollArea)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_83)

        self.label_85 = QLabel(self.aboutScrollArea)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);")

        self.verticalLayout_29.addWidget(self.label_85)

        self.label_87 = QLabel(self.aboutScrollArea)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_87)

        self.scrollArea_3.setWidget(self.aboutScrollArea)

        self.verticalLayout_28.addWidget(self.scrollArea_3)

        self.commandLinkButton = QCommandLinkButton(self.helppage_about_tab)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout_28.addWidget(self.commandLinkButton)

        self.helppage_tabs.addTab(self.helppage_about_tab, "")
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
        self.horizontalFrame2 = QFrame(self.single_report_page)
        self.horizontalFrame2.setObjectName(u"horizontalFrame2")
        self.horizontalFrame2.setStyleSheet(u"QPushButton{\n"
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
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 1, -1, -1)
        self.sreportpage_back_btn = QPushButton(self.horizontalFrame2)
        self.sreportpage_back_btn.setObjectName(u"sreportpage_back_btn")
        self.sreportpage_back_btn.setStyleSheet(u"")
        icon27 = QIcon()
        icon27.addFile(u":/assets/icons/icons8-back-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sreportpage_back_btn.setIcon(icon27)
        self.sreportpage_back_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.sreportpage_back_btn)

        self.line_14 = QFrame(self.horizontalFrame2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_14)

        self.sreportpage_export_btn = QPushButton(self.horizontalFrame2)
        self.sreportpage_export_btn.setObjectName(u"sreportpage_export_btn")
        icon28 = QIcon()
        icon28.addFile(u":/assets/icons/icons8-export-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sreportpage_export_btn.setIcon(icon28)
        self.sreportpage_export_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.sreportpage_export_btn)

        self.line_20 = QFrame(self.horizontalFrame2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_20)

        self.sreportpage_rebuild_btn = QPushButton(self.horizontalFrame2)
        self.sreportpage_rebuild_btn.setObjectName(u"sreportpage_rebuild_btn")
        icon29 = QIcon()
        icon29.addFile(u":/assets/icons/icons8-retweet-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sreportpage_rebuild_btn.setIcon(icon29)
        self.sreportpage_rebuild_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.sreportpage_rebuild_btn)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_46)


        self.verticalLayout_8.addWidget(self.horizontalFrame2)

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
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1145, 3092))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents\n"
"{\n"
"background-color:#ffffff;\n"
"\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox\n"
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
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(11, 25, -1, 25)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, -1, -1)
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);\n"
"margin: 5px 0px;")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6.setProperty("title", True)

        self.horizontalLayout_46.addWidget(self.label_6)

        self.sreportpage_name_lbl = QLabel(self.groupBox_7)
        self.sreportpage_name_lbl.setObjectName(u"sreportpage_name_lbl")
        self.sreportpage_name_lbl.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")

        self.horizontalLayout_46.addWidget(self.sreportpage_name_lbl)

        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_76)


        self.verticalLayout_34.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_30 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_34.addItem(self.verticalSpacer_30)

        self.line_5 = QFrame(self.groupBox_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 3))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_5)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_81 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_81)

        self.label_44 = QLabel(self.groupBox_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"max-width:30px;\n"
"max-height:30px;")
        self.label_44.setPixmap(QPixmap(u":/assets/icons/icons8-user-gray-50.png"))
        self.label_44.setScaledContents(True)

        self.horizontalLayout_48.addWidget(self.label_44)

        self.label_67 = QLabel(self.groupBox_7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")

        self.horizontalLayout_48.addWidget(self.label_67)

        self.sreportpage_user_lbl = QLabel(self.groupBox_7)
        self.sreportpage_user_lbl.setObjectName(u"sreportpage_user_lbl")

        self.horizontalLayout_48.addWidget(self.sreportpage_user_lbl)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_82)


        self.verticalLayout_34.addLayout(self.horizontalLayout_48)

        self.line_4 = QFrame(self.groupBox_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_4)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_80 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_80)

        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"max-width:30px;\n"
"max-height:30px;")
        self.label_2.setPixmap(QPixmap(u":/assets/icons/icons8-date-50.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_47.addWidget(self.label_2)

        self.label_41 = QLabel(self.groupBox_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_41)

        self.sreportpage_date_lbl = QLabel(self.groupBox_7)
        self.sreportpage_date_lbl.setObjectName(u"sreportpage_date_lbl")

        self.horizontalLayout_47.addWidget(self.sreportpage_date_lbl)

        self.horizontalSpacer_43 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_43)

        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"max-width:30px;\n"
"max-height:30px;")
        self.label_40.setPixmap(QPixmap(u":/assets/icons/icons8-clock-50.png"))
        self.label_40.setScaledContents(True)

        self.horizontalLayout_47.addWidget(self.label_40)

        self.label_65 = QLabel(self.groupBox_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")

        self.horizontalLayout_47.addWidget(self.label_65)

        self.sreportpage_time_lbl = QLabel(self.groupBox_7)
        self.sreportpage_time_lbl.setObjectName(u"sreportpage_time_lbl")

        self.horizontalLayout_47.addWidget(self.sreportpage_time_lbl)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_79)


        self.verticalLayout_34.addLayout(self.horizontalLayout_47)

        self.line_6 = QFrame(self.groupBox_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 3))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_6)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_83 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_83)

        self.label_42 = QLabel(self.groupBox_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"max-width:30px;\n"
"max-height:30px;")
        self.label_42.setPixmap(QPixmap(u":/assets/icons/icons8-bar-chart-gray-50.png"))
        self.label_42.setScaledContents(True)

        self.horizontalLayout_49.addWidget(self.label_42)

        self.label_43 = QLabel(self.groupBox_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(40, 40, 40);\n"
"margin: 5px 0px;")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_43.setProperty("title", True)

        self.horizontalLayout_49.addWidget(self.label_43)

        self.sreportpage_standard_lbl = QLabel(self.groupBox_7)
        self.sreportpage_standard_lbl.setObjectName(u"sreportpage_standard_lbl")

        self.horizontalLayout_49.addWidget(self.sreportpage_standard_lbl)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_85)


        self.verticalLayout_34.addLayout(self.horizontalLayout_49)

        self.line_7 = QFrame(self.groupBox_7)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(0, 3))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_7)

        self.verticalSpacer_34 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_34.addItem(self.verticalSpacer_34)

        self.sreportpage_description_lbl = QLabel(self.groupBox_7)
        self.sreportpage_description_lbl.setObjectName(u"sreportpage_description_lbl")
        self.sreportpage_description_lbl.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.sreportpage_description_lbl)


        self.verticalLayout_12.addWidget(self.groupBox_7)

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

        self.verticalSpacer_17 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_17)

        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setLineWidth(1)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setTabStopDistance(82.000000000000000)

        self.verticalLayout_12.addWidget(self.textEdit)

        self.verticalSpacer_46 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_46)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_86)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, -1, 14)
        self.label_104 = QLabel(self.scrollAreaWidgetContents)
        self.label_104.setObjectName(u"label_104")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(False)
        font2.setItalic(True)
        self.label_104.setFont(font2)
        self.label_104.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_104.setTextFormat(Qt.PlainText)

        self.verticalLayout_50.addWidget(self.label_104, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(6, 76, 130);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(50, -1, 50, 11)
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_44)

        self.label_60 = QLabel(self.frame_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")

        self.horizontalLayout_50.addWidget(self.label_60)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_45)


        self.verticalLayout_35.addLayout(self.horizontalLayout_50)

        self.line_8 = QFrame(self.frame_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"Line{\n"
"	background-color:rgba(255, 255, 255, 50);\n"
"}")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_35.addWidget(self.line_8)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, -1, -1)
        self.label_59 = QLabel(self.frame_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_59)

        self.sreportpage_avrage_lbl = QLabel(self.frame_2)
        self.sreportpage_avrage_lbl.setObjectName(u"sreportpage_avrage_lbl")
        self.sreportpage_avrage_lbl.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout_53.addWidget(self.sreportpage_avrage_lbl)

        self.label_54 = QLabel(self.frame_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color:#ffffff;")

        self.horizontalLayout_53.addWidget(self.label_54)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_51)

        self.label_61 = QLabel(self.frame_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"margin: 5px 0px;\n"
"color: #ffffff;")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_61)

        self.sreportpage_std_lbl = QLabel(self.frame_2)
        self.sreportpage_std_lbl.setObjectName(u"sreportpage_std_lbl")
        self.sreportpage_std_lbl.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout_53.addWidget(self.sreportpage_std_lbl)

        self.label_53 = QLabel(self.frame_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color:#ffffff;")

        self.horizontalLayout_53.addWidget(self.label_53)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_52)

        self.label_63 = QLabel(self.frame_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_63)

        self.sreportpage_mode_lbl = QLabel(self.frame_2)
        self.sreportpage_mode_lbl.setObjectName(u"sreportpage_mode_lbl")
        self.sreportpage_mode_lbl.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout_53.addWidget(self.sreportpage_mode_lbl)

        self.label_51 = QLabel(self.frame_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color:#ffffff;")

        self.horizontalLayout_53.addWidget(self.label_51)


        self.verticalLayout_35.addLayout(self.horizontalLayout_53)


        self.verticalLayout_50.addWidget(self.frame_2)


        self.horizontalLayout_54.addLayout(self.verticalLayout_50)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_84)


        self.verticalLayout_12.addLayout(self.horizontalLayout_54)

        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 120))
        self.textEdit_2.setStyleSheet(u"")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit_2.setLineWrapColumnOrWidth(0)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setOverwriteMode(False)

        self.verticalLayout_12.addWidget(self.textEdit_2)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_31)

        self.sreportpage_statictics_desc2 = QLabel(self.scrollAreaWidgetContents)
        self.sreportpage_statictics_desc2.setObjectName(u"sreportpage_statictics_desc2")
        self.sreportpage_statictics_desc2.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.sreportpage_statictics_desc2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_53)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 15, -1, 15)
        self.label_105 = QLabel(self.scrollAreaWidgetContents)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font2)
        self.label_105.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_105.setTextFormat(Qt.PlainText)

        self.verticalLayout_53.addWidget(self.label_105, 0, Qt.AlignHCenter)

        self.sreportpage_statictics_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.sreportpage_statictics_table.columnCount() < 5):
            self.sreportpage_statictics_table.setColumnCount(5)
        if (self.sreportpage_statictics_table.rowCount() < 4):
            self.sreportpage_statictics_table.setRowCount(4)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sreportpage_statictics_table.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.sreportpage_statictics_table.setItem(1, 1, __qtablewidgetitem23)
        self.sreportpage_statictics_table.setObjectName(u"sreportpage_statictics_table")
        self.sreportpage_statictics_table.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sreportpage_statictics_table.sizePolicy().hasHeightForWidth())
        self.sreportpage_statictics_table.setSizePolicy(sizePolicy4)
        self.sreportpage_statictics_table.setMaximumSize(QSize(16777215, 16777215))
        self.sreportpage_statictics_table.setSizeIncrement(QSize(0, 0))
        self.sreportpage_statictics_table.setBaseSize(QSize(0, 0))
        self.sreportpage_statictics_table.setFont(font1)
        self.sreportpage_statictics_table.setFocusPolicy(Qt.NoFocus)
        self.sreportpage_statictics_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
"")
        self.sreportpage_statictics_table.setFrameShape(QFrame.Box)
        self.sreportpage_statictics_table.setFrameShadow(QFrame.Raised)
        self.sreportpage_statictics_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sreportpage_statictics_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sreportpage_statictics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sreportpage_statictics_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sreportpage_statictics_table.setAlternatingRowColors(False)
        self.sreportpage_statictics_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.sreportpage_statictics_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sreportpage_statictics_table.setTextElideMode(Qt.ElideMiddle)
        self.sreportpage_statictics_table.setGridStyle(Qt.SolidLine)
        self.sreportpage_statictics_table.setWordWrap(True)
        self.sreportpage_statictics_table.setRowCount(4)
        self.sreportpage_statictics_table.setColumnCount(5)
        self.sreportpage_statictics_table.horizontalHeader().setMinimumSectionSize(50)
        self.sreportpage_statictics_table.horizontalHeader().setDefaultSectionSize(180)
        self.sreportpage_statictics_table.horizontalHeader().setHighlightSections(True)
        self.sreportpage_statictics_table.horizontalHeader().setStretchLastSection(False)
        self.sreportpage_statictics_table.verticalHeader().setVisible(False)
        self.sreportpage_statictics_table.verticalHeader().setDefaultSectionSize(40)
        self.sreportpage_statictics_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_53.addWidget(self.sreportpage_statictics_table)


        self.horizontalLayout_7.addLayout(self.verticalLayout_53)

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

        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setLineWidth(1)
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_12.addWidget(self.textEdit_3)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(61, 0, -1, -1)
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.textEdit_4 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 30))
        self.textEdit_4.setMaximumSize(QSize(16777215, 30))
        self.textEdit_4.setStyleSheet(u"")
        self.textEdit_4.setFrameShape(QFrame.NoFrame)
        self.textEdit_4.setLineWidth(1)
        self.textEdit_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_54.addWidget(self.textEdit_4)

        self.report_grading_chart_frame = QHBoxLayout()
        self.report_grading_chart_frame.setObjectName(u"report_grading_chart_frame")
        self.report_grading_chart_frame.setSizeConstraint(QLayout.SetFixedSize)
        self.report_grading_chart_frame.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_54.addLayout(self.report_grading_chart_frame)

        self.label_107 = QLabel(self.scrollAreaWidgetContents)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font2)
        self.label_107.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_107.setTextFormat(Qt.PlainText)

        self.verticalLayout_54.addWidget(self.label_107, 0, Qt.AlignHCenter)


        self.horizontalLayout_25.addLayout(self.verticalLayout_54)

        self.line_18 = QFrame(self.scrollAreaWidgetContents)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setMinimumSize(QSize(3, 0))
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_18)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.textEdit_5 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(0, 30))
        self.textEdit_5.setMaximumSize(QSize(16777215, 30))
        self.textEdit_5.setStyleSheet(u"")
        self.textEdit_5.setFrameShape(QFrame.NoFrame)
        self.textEdit_5.setLineWidth(1)
        self.textEdit_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_55.addWidget(self.textEdit_5)

        self.report_cum_chart_frame = QHBoxLayout()
        self.report_cum_chart_frame.setObjectName(u"report_cum_chart_frame")
        self.report_cum_chart_frame.setSizeConstraint(QLayout.SetFixedSize)
        self.report_cum_chart_frame.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_55.addLayout(self.report_cum_chart_frame)

        self.label_108 = QLabel(self.scrollAreaWidgetContents)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setFont(font2)
        self.label_108.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_108.setTextFormat(Qt.PlainText)

        self.verticalLayout_55.addWidget(self.label_108, 0, Qt.AlignHCenter)


        self.horizontalLayout_25.addLayout(self.verticalLayout_55)

        self.verticalSpacer_32 = QSpacerItem(10, 300, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.verticalSpacer_32)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMinimumSize(QSize(0, 30))
        self.textEdit_6.setMaximumSize(QSize(16777215, 30))
        self.textEdit_6.setStyleSheet(u"")
        self.textEdit_6.setFrameShape(QFrame.NoFrame)
        self.textEdit_6.setLineWidth(1)
        self.textEdit_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_56.addWidget(self.textEdit_6)

        self.report_gaussian_chart_frame = QHBoxLayout()
        self.report_gaussian_chart_frame.setObjectName(u"report_gaussian_chart_frame")
        self.report_gaussian_chart_frame.setSizeConstraint(QLayout.SetFixedSize)
        self.report_gaussian_chart_frame.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_56.addLayout(self.report_gaussian_chart_frame)

        self.label_109 = QLabel(self.scrollAreaWidgetContents)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font2)
        self.label_109.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_109.setTextFormat(Qt.PlainText)

        self.verticalLayout_56.addWidget(self.label_109, 0, Qt.AlignHCenter)


        self.horizontalLayout_63.addLayout(self.verticalLayout_56)

        self.line_30 = QFrame(self.scrollAreaWidgetContents)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setMinimumSize(QSize(3, 0))
        self.line_30.setFrameShape(QFrame.VLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_63.addWidget(self.line_30)

        self.verticalSpacer_33 = QSpacerItem(10, 300, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.verticalSpacer_33)


        self.verticalLayout_12.addLayout(self.horizontalLayout_63)

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

        self.textEdit_7 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMinimumSize(QSize(0, 110))
        self.textEdit_7.setStyleSheet(u"")
        self.textEdit_7.setFrameShape(QFrame.NoFrame)
        self.textEdit_7.setLineWidth(1)
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_12.addWidget(self.textEdit_7)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_90 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_90)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, -1, -1, -1)
        self.report_single_pellet_frame = QFrame(self.scrollAreaWidgetContents)
        self.report_single_pellet_frame.setObjectName(u"report_single_pellet_frame")
        self.report_single_pellet_frame.setMinimumSize(QSize(300, 0))
        self.report_single_pellet_frame.setMaximumSize(QSize(400, 16777215))
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
        self.verticalLayout_13 = QVBoxLayout(self.report_single_pellet_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(-1, 16, -1, -1)
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_48)

        self.sreportpage_particle_image_lbl = QLabel(self.report_single_pellet_frame)
        self.sreportpage_particle_image_lbl.setObjectName(u"sreportpage_particle_image_lbl")
        self.sreportpage_particle_image_lbl.setMinimumSize(QSize(300, 300))
        self.sreportpage_particle_image_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.sreportpage_particle_image_lbl.setStyleSheet(u"background-color:#ffffff;")
        self.sreportpage_particle_image_lbl.setPixmap(QPixmap(u":/assets/Assets/images/camera-error-500.png"))
        self.sreportpage_particle_image_lbl.setScaledContents(False)
        self.sreportpage_particle_image_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.sreportpage_particle_image_lbl)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_49)


        self.verticalLayout_13.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(-1, 31, -1, -1)
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_50)

        self.signle_pellet_info_groupbox = QGroupBox(self.report_single_pellet_frame)
        self.signle_pellet_info_groupbox.setObjectName(u"signle_pellet_info_groupbox")
        self.signle_pellet_info_groupbox.setMinimumSize(QSize(300, 0))
        self.signle_pellet_info_groupbox.setMaximumSize(QSize(300, 16777215))
        self.signle_pellet_info_groupbox.setStyleSheet(u"#signle_pellet_info_groupbox{\n"
"	border: 1px solid #ffffff;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"Line{\n"
"	background-color: rgba(255,255,255,50);\n"
"}")
        self.verticalLayout_37 = QVBoxLayout(self.signle_pellet_info_groupbox)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(3, 8, -1, -1)
        self.sreportpage_particle_area_lbl = QLabel(self.signle_pellet_info_groupbox)
        self.sreportpage_particle_area_lbl.setObjectName(u"sreportpage_particle_area_lbl")

        self.gridLayout_21.addWidget(self.sreportpage_particle_area_lbl, 0, 1, 1, 1)

        self.sreportpage_particle_avg_r_lbl_title = QLabel(self.signle_pellet_info_groupbox)
        self.sreportpage_particle_avg_r_lbl_title.setObjectName(u"sreportpage_particle_avg_r_lbl_title")
        self.sreportpage_particle_avg_r_lbl_title.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.sreportpage_particle_avg_r_lbl_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.sreportpage_particle_avg_r_lbl_title, 2, 0, 1, 1)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_87, 0, 3, 1, 1)

        self.sreportpage_particle_volume_lbl = QLabel(self.signle_pellet_info_groupbox)
        self.sreportpage_particle_volume_lbl.setObjectName(u"sreportpage_particle_volume_lbl")

        self.gridLayout_21.addWidget(self.sreportpage_particle_volume_lbl, 1, 1, 1, 1)

        self.label_58 = QLabel(self.signle_pellet_info_groupbox)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_21.addWidget(self.label_58, 2, 2, 1, 1)

        self.label_50 = QLabel(self.signle_pellet_info_groupbox)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_21.addWidget(self.label_50, 0, 2, 1, 1)

        self.label_55 = QLabel(self.signle_pellet_info_groupbox)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_55, 1, 0, 1, 1)

        self.label_52 = QLabel(self.signle_pellet_info_groupbox)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_21.addWidget(self.label_52, 1, 2, 1, 1)

        self.sreportpage_particle_avg_r_lbl = QLabel(self.signle_pellet_info_groupbox)
        self.sreportpage_particle_avg_r_lbl.setObjectName(u"sreportpage_particle_avg_r_lbl")

        self.gridLayout_21.addWidget(self.sreportpage_particle_avg_r_lbl, 2, 1, 1, 1)

        self.label_49 = QLabel(self.signle_pellet_info_groupbox)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_62 = QLabel(self.signle_pellet_info_groupbox)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font-size: 15px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"margin: 5px 0px;")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_62, 3, 0, 1, 1)

        self.sreportpage_particle_max_r_lbl = QLabel(self.signle_pellet_info_groupbox)
        self.sreportpage_particle_max_r_lbl.setObjectName(u"sreportpage_particle_max_r_lbl")

        self.gridLayout_21.addWidget(self.sreportpage_particle_max_r_lbl, 3, 1, 1, 1)

        self.label_64 = QLabel(self.signle_pellet_info_groupbox)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_21.addWidget(self.label_64, 3, 2, 1, 1)


        self.verticalLayout_37.addLayout(self.gridLayout_21)


        self.horizontalLayout_66.addWidget(self.signle_pellet_info_groupbox)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_89)


        self.verticalLayout_13.addLayout(self.horizontalLayout_66)


        self.verticalLayout_52.addWidget(self.report_single_pellet_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_4)


        self.horizontalLayout_26.addLayout(self.verticalLayout_52)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_38)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(31, -1, -1, -1)
        self.sreportpage_particels_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.sreportpage_particels_table.columnCount() < 4):
            self.sreportpage_particels_table.setColumnCount(4)
        if (self.sreportpage_particels_table.rowCount() < 1):
            self.sreportpage_particels_table.setRowCount(1)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.sreportpage_particels_table.setItem(0, 1, __qtablewidgetitem24)
        self.sreportpage_particels_table.setObjectName(u"sreportpage_particels_table")
        self.sreportpage_particels_table.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.sreportpage_particels_table.sizePolicy().hasHeightForWidth())
        self.sreportpage_particels_table.setSizePolicy(sizePolicy4)
        self.sreportpage_particels_table.setMaximumSize(QSize(16777215, 16777215))
        self.sreportpage_particels_table.setSizeIncrement(QSize(0, 0))
        self.sreportpage_particels_table.setBaseSize(QSize(0, 0))
        self.sreportpage_particels_table.setFont(font1)
        self.sreportpage_particels_table.setFocusPolicy(Qt.NoFocus)
        self.sreportpage_particels_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
"")
        self.sreportpage_particels_table.setFrameShape(QFrame.Box)
        self.sreportpage_particels_table.setFrameShadow(QFrame.Raised)
        self.sreportpage_particels_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sreportpage_particels_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sreportpage_particels_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sreportpage_particels_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sreportpage_particels_table.setAlternatingRowColors(False)
        self.sreportpage_particels_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.sreportpage_particels_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sreportpage_particels_table.setTextElideMode(Qt.ElideMiddle)
        self.sreportpage_particels_table.setGridStyle(Qt.SolidLine)
        self.sreportpage_particels_table.setWordWrap(True)
        self.sreportpage_particels_table.setRowCount(1)
        self.sreportpage_particels_table.setColumnCount(4)
        self.sreportpage_particels_table.horizontalHeader().setVisible(False)
        self.sreportpage_particels_table.horizontalHeader().setDefaultSectionSize(120)
        self.sreportpage_particels_table.horizontalHeader().setHighlightSections(True)
        self.sreportpage_particels_table.horizontalHeader().setStretchLastSection(False)
        self.sreportpage_particels_table.verticalHeader().setVisible(False)
        self.sreportpage_particels_table.verticalHeader().setMinimumSectionSize(120)
        self.sreportpage_particels_table.verticalHeader().setDefaultSectionSize(120)
        self.sreportpage_particels_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_51.addWidget(self.sreportpage_particels_table)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_100 = QLabel(self.scrollAreaWidgetContents)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_29.addWidget(self.label_100)

        self.sreportpage_current_page = QLabel(self.scrollAreaWidgetContents)
        self.sreportpage_current_page.setObjectName(u"sreportpage_current_page")

        self.horizontalLayout_29.addWidget(self.sreportpage_current_page)

        self.label_101 = QLabel(self.scrollAreaWidgetContents)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_29.addWidget(self.label_101)

        self.sreportpage_end_page = QLabel(self.scrollAreaWidgetContents)
        self.sreportpage_end_page.setObjectName(u"sreportpage_end_page")

        self.horizontalLayout_29.addWidget(self.sreportpage_end_page)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_29)

        self.horizontalSpacer_109 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_109)

        self.sreportpage_prev_particle_btn = QPushButton(self.scrollAreaWidgetContents)
        self.sreportpage_prev_particle_btn.setObjectName(u"sreportpage_prev_particle_btn")
        self.sreportpage_prev_particle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon30 = QIcon()
        icon30.addFile(u":/assets/icons/icons8-previous-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sreportpage_prev_particle_btn.setIcon(icon30)
        self.sreportpage_prev_particle_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_64.addWidget(self.sreportpage_prev_particle_btn)

        self.sreportpage_next_particle_btn = QPushButton(self.scrollAreaWidgetContents)
        self.sreportpage_next_particle_btn.setObjectName(u"sreportpage_next_particle_btn")
        self.sreportpage_next_particle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon31 = QIcon()
        icon31.addFile(u":/assets/icons/icons8-next-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sreportpage_next_particle_btn.setIcon(icon31)
        self.sreportpage_next_particle_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_64.addWidget(self.sreportpage_next_particle_btn)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_108)


        self.verticalLayout_51.addLayout(self.horizontalLayout_64)


        self.horizontalLayout_26.addLayout(self.verticalLayout_51)

        self.horizontalSpacer_47 = QSpacerItem(25, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_47)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.alaki_btn = QPushButton(self.scrollAreaWidgetContents)
        self.alaki_btn.setObjectName(u"alaki_btn")
        self.alaki_btn.setStyleSheet(u"background-color: #ffffff;\n"
"")

        self.verticalLayout_12.addWidget(self.alaki_btn)

        self.line_19 = QFrame(self.scrollAreaWidgetContents)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_19)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.main_pages_stackw.addWidget(self.single_report_page)
        self.compare_page = QWidget()
        self.compare_page.setObjectName(u"compare_page")
        self.verticalLayout_39 = QVBoxLayout(self.compare_page)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalFrame_6 = QFrame(self.compare_page)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalFrame_6.setStyleSheet(u"QPushButton{\n"
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
"\n"
"QFrame{\n"
"	max-height: 50px;\n"
"}")
        self.horizontalLayout_56 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(-1, 1, -1, -1)
        self.comparepage_back_btn = QPushButton(self.horizontalFrame_6)
        self.comparepage_back_btn.setObjectName(u"comparepage_back_btn")
        self.comparepage_back_btn.setStyleSheet(u"")
        self.comparepage_back_btn.setIcon(icon27)
        self.comparepage_back_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_56.addWidget(self.comparepage_back_btn)

        self.line_22 = QFrame(self.horizontalFrame_6)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_56.addWidget(self.line_22)

        self.comparepage_export_btn = QPushButton(self.horizontalFrame_6)
        self.comparepage_export_btn.setObjectName(u"comparepage_export_btn")
        self.comparepage_export_btn.setIcon(icon28)
        self.comparepage_export_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_56.addWidget(self.comparepage_export_btn)

        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_91)


        self.verticalLayout_39.addWidget(self.horizontalFrame_6)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 15, -1, 15)
        self.label_115 = QLabel(self.compare_page)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_69.addWidget(self.label_115)

        self.compare_attribute_combobox = QComboBox(self.compare_page)
        self.compare_attribute_combobox.setObjectName(u"compare_attribute_combobox")

        self.horizontalLayout_69.addWidget(self.compare_attribute_combobox)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_115)


        self.verticalLayout_39.addLayout(self.horizontalLayout_69)

        self.comparepage_progressbar = QProgressBar(self.compare_page)
        self.comparepage_progressbar.setObjectName(u"comparepage_progressbar")
        self.comparepage_progressbar.setValue(100)
        self.comparepage_progressbar.setTextVisible(False)

        self.verticalLayout_39.addWidget(self.comparepage_progressbar)

        self.scrollArea_4 = QScrollArea(self.compare_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setWidgetResizable(True)
        self.compareScrollAreaWidget = QWidget()
        self.compareScrollAreaWidget.setObjectName(u"compareScrollAreaWidget")
        self.compareScrollAreaWidget.setGeometry(QRect(0, 0, 1144, 1182))
        self.compareScrollAreaWidget.setStyleSheet(u"#compareScrollAreaWidget\n"
"{\n"
"background-color:#ffffff;\n"
"\n"
"}")
        self.verticalLayout_40 = QVBoxLayout(self.compareScrollAreaWidget)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_57 = QLabel(self.compareScrollAreaWidget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(6, 76, 130);\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"max-height: 22px;")

        self.verticalLayout_40.addWidget(self.label_57)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_6)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, -1, -1)
        self.label_111 = QLabel(self.compareScrollAreaWidget)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font2)
        self.label_111.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_111.setTextFormat(Qt.PlainText)

        self.verticalLayout_57.addWidget(self.label_111, 0, Qt.AlignHCenter)

        self.comparepage_compare_table = QTableWidget(self.compareScrollAreaWidget)
        if (self.comparepage_compare_table.columnCount() < 5):
            self.comparepage_compare_table.setColumnCount(5)
        if (self.comparepage_compare_table.rowCount() < 4):
            self.comparepage_compare_table.setRowCount(4)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.comparepage_compare_table.setItem(0, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.comparepage_compare_table.setItem(1, 1, __qtablewidgetitem26)
        self.comparepage_compare_table.setObjectName(u"comparepage_compare_table")
        self.comparepage_compare_table.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.comparepage_compare_table.sizePolicy().hasHeightForWidth())
        self.comparepage_compare_table.setSizePolicy(sizePolicy4)
        self.comparepage_compare_table.setMaximumSize(QSize(16777215, 16777215))
        self.comparepage_compare_table.setSizeIncrement(QSize(0, 0))
        self.comparepage_compare_table.setBaseSize(QSize(0, 0))
        self.comparepage_compare_table.setFont(font1)
        self.comparepage_compare_table.setFocusPolicy(Qt.NoFocus)
        self.comparepage_compare_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(6, 76, 130);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
"")
        self.comparepage_compare_table.setFrameShape(QFrame.NoFrame)
        self.comparepage_compare_table.setFrameShadow(QFrame.Raised)
        self.comparepage_compare_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.comparepage_compare_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.comparepage_compare_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.comparepage_compare_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.comparepage_compare_table.setAlternatingRowColors(True)
        self.comparepage_compare_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.comparepage_compare_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.comparepage_compare_table.setTextElideMode(Qt.ElideMiddle)
        self.comparepage_compare_table.setGridStyle(Qt.SolidLine)
        self.comparepage_compare_table.setWordWrap(True)
        self.comparepage_compare_table.setRowCount(4)
        self.comparepage_compare_table.setColumnCount(5)
        self.comparepage_compare_table.horizontalHeader().setMinimumSectionSize(50)
        self.comparepage_compare_table.horizontalHeader().setDefaultSectionSize(180)
        self.comparepage_compare_table.horizontalHeader().setHighlightSections(True)
        self.comparepage_compare_table.horizontalHeader().setStretchLastSection(False)
        self.comparepage_compare_table.verticalHeader().setVisible(False)
        self.comparepage_compare_table.verticalHeader().setDefaultSectionSize(40)
        self.comparepage_compare_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_57.addWidget(self.comparepage_compare_table)


        self.horizontalLayout_30.addLayout(self.verticalLayout_57)

        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_110)


        self.verticalLayout_40.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_40 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_40)

        self.label_84 = QLabel(self.compareScrollAreaWidget)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"color: rgb(6, 76, 130);\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"max-height: 22px;")

        self.verticalLayout_40.addWidget(self.label_84)

        self.frame_3 = QFrame(self.compareScrollAreaWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_3)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.charts_layout = QVBoxLayout()
        self.charts_layout.setObjectName(u"charts_layout")
        self.charts_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.charts_layout.setContentsMargins(-1, 10, -1, -1)

        self.verticalLayout_60.addLayout(self.charts_layout)


        self.verticalLayout_40.addWidget(self.frame_3)

        self.verticalSpacer_48 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_48)

        self.label_56 = QLabel(self.compareScrollAreaWidget)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: rgb(6, 76, 130);\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"max-height: 22px;")

        self.verticalLayout_40.addWidget(self.label_56)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_9)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, -1, -1)
        self.label_112 = QLabel(self.compareScrollAreaWidget)
        self.label_112.setObjectName(u"label_112")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy5)
        self.label_112.setFont(font2)
        self.label_112.setStyleSheet(u"QLabel{\n"
"	color: #707070;\n"
"	font-style: italic;\n"
"\n"
"}")
        self.label_112.setTextFormat(Qt.PlainText)

        self.verticalLayout_58.addWidget(self.label_112, 0, Qt.AlignHCenter)

        self.comparepage_compare_mean_table = QTableWidget(self.compareScrollAreaWidget)
        if (self.comparepage_compare_mean_table.columnCount() < 5):
            self.comparepage_compare_mean_table.setColumnCount(5)
        if (self.comparepage_compare_mean_table.rowCount() < 1):
            self.comparepage_compare_mean_table.setRowCount(1)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.comparepage_compare_mean_table.setItem(0, 1, __qtablewidgetitem27)
        self.comparepage_compare_mean_table.setObjectName(u"comparepage_compare_mean_table")
        self.comparepage_compare_mean_table.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.comparepage_compare_mean_table.sizePolicy().hasHeightForWidth())
        self.comparepage_compare_mean_table.setSizePolicy(sizePolicy4)
        self.comparepage_compare_mean_table.setMaximumSize(QSize(16777215, 100))
        self.comparepage_compare_mean_table.setSizeIncrement(QSize(0, 0))
        self.comparepage_compare_mean_table.setBaseSize(QSize(0, 0))
        self.comparepage_compare_mean_table.setFont(font1)
        self.comparepage_compare_mean_table.setFocusPolicy(Qt.NoFocus)
        self.comparepage_compare_mean_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
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
"    border-left: 1px solid #fffff8;	\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	font-size: 16px;\n"
"	color:rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"   padding: 10px;\n"
"}\n"
"")
        self.comparepage_compare_mean_table.setFrameShape(QFrame.NoFrame)
        self.comparepage_compare_mean_table.setFrameShadow(QFrame.Raised)
        self.comparepage_compare_mean_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.comparepage_compare_mean_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.comparepage_compare_mean_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.comparepage_compare_mean_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.comparepage_compare_mean_table.setAlternatingRowColors(False)
        self.comparepage_compare_mean_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.comparepage_compare_mean_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.comparepage_compare_mean_table.setTextElideMode(Qt.ElideMiddle)
        self.comparepage_compare_mean_table.setGridStyle(Qt.SolidLine)
        self.comparepage_compare_mean_table.setWordWrap(True)
        self.comparepage_compare_mean_table.setRowCount(1)
        self.comparepage_compare_mean_table.setColumnCount(5)
        self.comparepage_compare_mean_table.horizontalHeader().setMinimumSectionSize(50)
        self.comparepage_compare_mean_table.horizontalHeader().setDefaultSectionSize(180)
        self.comparepage_compare_mean_table.horizontalHeader().setHighlightSections(True)
        self.comparepage_compare_mean_table.horizontalHeader().setStretchLastSection(False)
        self.comparepage_compare_mean_table.verticalHeader().setVisible(False)
        self.comparepage_compare_mean_table.verticalHeader().setDefaultSectionSize(40)
        self.comparepage_compare_mean_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_58.addWidget(self.comparepage_compare_mean_table)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_47)


        self.horizontalLayout_58.addLayout(self.verticalLayout_58)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_92)


        self.verticalLayout_40.addLayout(self.horizontalLayout_58)

        self.verticalSpacer_41 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_41)

        self.scrollArea_4.setWidget(self.compareScrollAreaWidget)

        self.verticalLayout_39.addWidget(self.scrollArea_4)

        self.main_pages_stackw.addWidget(self.compare_page)

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
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_7.setFont(font3)

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
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.settingpage_general_font_combobox, self.settingpage_general_color_combobox)
        QWidget.setTabOrder(self.settingpage_general_color_combobox, self.settingpage_general_language_combobox)
        QWidget.setTabOrder(self.settingpage_general_language_combobox, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.settingpage_sample_auto_name_groupbox)
        QWidget.setTabOrder(self.settingpage_sample_auto_name_groupbox, self.settingpage_sample_text1_input)
        QWidget.setTabOrder(self.settingpage_sample_text1_input, self.settingpage_sample_spacer_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_spacer_code_btn, self.settingpage_sample_username_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_username_code_btn, self.settingpage_sample_text1_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_text1_code_btn, self.settingpage_sample_year_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_year_code_btn, self.settingpage_sample_month_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_month_code_btn, self.settingpage_sample_day_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_day_code_btn, self.settingpage_sample_houre_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_houre_code_btn, self.settingpage_sample_minute_code_btn)
        QWidget.setTabOrder(self.settingpage_sample_minute_code_btn, self.settingpage_sample_auto_name_input)
        QWidget.setTabOrder(self.settingpage_sample_auto_name_input, self.settingpage_sample_default_standard_comboxos)
        QWidget.setTabOrder(self.settingpage_sample_default_standard_comboxos, self.settingpage_sample_save_image_checkbox)
        QWidget.setTabOrder(self.settingpage_sample_save_image_checkbox, self.settingpage_sample_save_btn)
        QWidget.setTabOrder(self.settingpage_sample_save_btn, self.settingpage_sample_cancel_btn)
        QWidget.setTabOrder(self.settingpage_sample_cancel_btn, self.settingpage_db_username)
        QWidget.setTabOrder(self.settingpage_db_username, self.settingpage_db_password)
        QWidget.setTabOrder(self.settingpage_db_password, self.settingpage_db_host)
        QWidget.setTabOrder(self.settingpage_db_host, self.settingpage_storage_auto_clean_checkbox)
        QWidget.setTabOrder(self.settingpage_storage_auto_clean_checkbox, self.settingpage_storage_life_time_spinbox)
        QWidget.setTabOrder(self.settingpage_storage_life_time_spinbox, self.settingpage_storage_path_input)
        QWidget.setTabOrder(self.settingpage_storage_path_input, self.settingpage_storage_save_btn)
        QWidget.setTabOrder(self.settingpage_storage_save_btn, self.settingpage_storage_cancel_btn)
        QWidget.setTabOrder(self.settingpage_storage_cancel_btn, self.settingpage_camera_device_combobox)
        QWidget.setTabOrder(self.settingpage_camera_device_combobox, self.settingpage_camera_fps_spinbox)
        QWidget.setTabOrder(self.settingpage_camera_fps_spinbox, self.settingpage_camera_exposure_spinbox)
        QWidget.setTabOrder(self.settingpage_camera_exposure_spinbox, self.settingpage_camera_gain_spinbox)
        QWidget.setTabOrder(self.settingpage_camera_gain_spinbox, self.settingpage_camera_width_spinbox)
        QWidget.setTabOrder(self.settingpage_camera_width_spinbox, self.settingpage_camera_height_spinbox)
        QWidget.setTabOrder(self.settingpage_camera_height_spinbox, self.settingpage_camera_start_btn)
        QWidget.setTabOrder(self.settingpage_camera_start_btn, self.settingpage_camera_save_btn)
        QWidget.setTabOrder(self.settingpage_camera_save_btn, self.settingpage_camera_cancel_btn)
        QWidget.setTabOrder(self.settingpage_camera_cancel_btn, self.settingpage_camera_restore_btn)
        QWidget.setTabOrder(self.settingpage_camera_restore_btn, self.settingpage_algorithm_threshould_spinbox)
        QWidget.setTabOrder(self.settingpage_algorithm_threshould_spinbox, self.settingpage_algorithm_border_spinbox)
        QWidget.setTabOrder(self.settingpage_algorithm_border_spinbox, self.settingpage_algorithm_save_btn)
        QWidget.setTabOrder(self.settingpage_algorithm_save_btn, self.settingpage_algorithm_cancel_btn)
        QWidget.setTabOrder(self.settingpage_algorithm_cancel_btn, self.settingpage_algorithm_restor_default_btn)
        QWidget.setTabOrder(self.settingpage_algorithm_restor_default_btn, self.settingpage_grading_name_inpt)
        QWidget.setTabOrder(self.settingpage_grading_name_inpt, self.settingpage_grading_low_limit_spinbox)
        QWidget.setTabOrder(self.settingpage_grading_low_limit_spinbox, self.settingpage_grading_up_limit_spinbox)
        QWidget.setTabOrder(self.settingpage_grading_up_limit_spinbox, self.settingpage_pelletizing_add_range_btn)
        QWidget.setTabOrder(self.settingpage_pelletizing_add_range_btn, self.settingpage_grading_ranges_table)
        QWidget.setTabOrder(self.settingpage_grading_ranges_table, self.settingpage_grading_save_btn)
        QWidget.setTabOrder(self.settingpage_grading_save_btn, self.settingpage_grading_cancel_btn)
        QWidget.setTabOrder(self.settingpage_grading_cancel_btn, self.settingpage_tabs)
        QWidget.setTabOrder(self.settingpage_tabs, self.mainpage_report_button)
        QWidget.setTabOrder(self.mainpage_report_button, self.minimize_btn)
        QWidget.setTabOrder(self.minimize_btn, self.maximize_btn)
        QWidget.setTabOrder(self.maximize_btn, self.sidebar_grading_ranges_btn)
        QWidget.setTabOrder(self.sidebar_grading_ranges_btn, self.sidebar_report_btn)
        QWidget.setTabOrder(self.sidebar_report_btn, self.reportpage_standards_filter_table)
        QWidget.setTabOrder(self.reportpage_standards_filter_table, self.close_btn)
        QWidget.setTabOrder(self.close_btn, self.toolbar_login_logout_btn)
        QWidget.setTabOrder(self.toolbar_login_logout_btn, self.reportpage_filterusername_input)
        QWidget.setTabOrder(self.reportpage_filterusername_input, self.reportpage_filtername_input)
        QWidget.setTabOrder(self.reportpage_filtername_input, self.reportpage_filterusername_groupbox)
        QWidget.setTabOrder(self.reportpage_filterusername_groupbox, self.reportpage_end_date_dateedit)
        QWidget.setTabOrder(self.reportpage_end_date_dateedit, self.mainpage_stop_btn)
        QWidget.setTabOrder(self.mainpage_stop_btn, self.reportpage_start_date_dateedit)
        QWidget.setTabOrder(self.reportpage_start_date_dateedit, self.reportpage_filterdate_groupbox)
        QWidget.setTabOrder(self.reportpage_filterdate_groupbox, self.mainpage_faststart_btn)
        QWidget.setTabOrder(self.mainpage_faststart_btn, self.mainpage_illumination_warning_btn)
        QWidget.setTabOrder(self.mainpage_illumination_warning_btn, self.settingpage_sample_auto_name_clear_btn)
        QWidget.setTabOrder(self.settingpage_sample_auto_name_clear_btn, self.mainpage_tempreture_warning_btn)
        QWidget.setTabOrder(self.mainpage_tempreture_warning_btn, self.mainpage_close_error_btn)
        QWidget.setTabOrder(self.mainpage_close_error_btn, self.mainpage_camera_connection_warning_btn)
        QWidget.setTabOrder(self.mainpage_camera_connection_warning_btn, self.mainpage_camera_grabbing_warning_btn)
        QWidget.setTabOrder(self.mainpage_camera_grabbing_warning_btn, self.sidebar_users_btn)
        QWidget.setTabOrder(self.sidebar_users_btn, self.settingpage_storage_select_dir_btn)
        QWidget.setTabOrder(self.settingpage_storage_select_dir_btn, self.sidebar_main_btn)
        QWidget.setTabOrder(self.sidebar_main_btn, self.sidebar_help_btn)
        QWidget.setTabOrder(self.sidebar_help_btn, self.sidebar_calib_btn)
        QWidget.setTabOrder(self.sidebar_calib_btn, self.mainpage_liveview_checkbox)
        QWidget.setTabOrder(self.mainpage_liveview_checkbox, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.mainpage_drawing_checkbox)
        QWidget.setTabOrder(self.mainpage_drawing_checkbox, self.reportpage_apply_filters_btn)
        QWidget.setTabOrder(self.reportpage_apply_filters_btn, self.mainpage_start_btn)
        QWidget.setTabOrder(self.mainpage_start_btn, self.reportpage_filterstandards_groupbox)
        QWidget.setTabOrder(self.reportpage_filterstandards_groupbox, self.reportpage_filterranges_groupbox)
        QWidget.setTabOrder(self.reportpage_filterranges_groupbox, self.sidebar_settings_btn)
        QWidget.setTabOrder(self.sidebar_settings_btn, self.reportpage_standards_filter_ranges_table)
        QWidget.setTabOrder(self.reportpage_standards_filter_ranges_table, self.reportpage_filter_standards_combobox)
        QWidget.setTabOrder(self.reportpage_filter_standards_combobox, self.reportpage_filtername_groupbox)
        QWidget.setTabOrder(self.reportpage_filtername_groupbox, self.reportspage_all_checkbox)
        QWidget.setTabOrder(self.reportspage_all_checkbox, self.reportspage_delete_selections_btn)
        QWidget.setTabOrder(self.reportspage_delete_selections_btn, self.reportpage_rebuild_btn)
        QWidget.setTabOrder(self.reportpage_rebuild_btn, self.reportpage_compare_btn)
        QWidget.setTabOrder(self.reportpage_compare_btn, self.reportpage_compare_standards_combobox)
        QWidget.setTabOrder(self.reportpage_compare_standards_combobox, self.reportpage_samples_table)
        QWidget.setTabOrder(self.reportpage_samples_table, self.gradingranges_tabs)
        QWidget.setTabOrder(self.gradingranges_tabs, self.settingpage_grading_standards_table)
        QWidget.setTabOrder(self.settingpage_grading_standards_table, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.calibrationpage_check_btn)
        QWidget.setTabOrder(self.calibrationpage_check_btn, self.calibrationpage_calib_type_combobox)
        QWidget.setTabOrder(self.calibrationpage_calib_type_combobox, self.calibrationpage_calib_itrs_spinbox)
        QWidget.setTabOrder(self.calibrationpage_calib_itrs_spinbox, self.calibrationpage_calib_btn)
        QWidget.setTabOrder(self.calibrationpage_calib_btn, self.calibrationpage_last_calib_tabel)
        QWidget.setTabOrder(self.calibrationpage_last_calib_tabel, self.validationpage_hypotest_test_count_spinbox)
        QWidget.setTabOrder(self.validationpage_hypotest_test_count_spinbox, self.validationpage_hypotest_standards_combobox)
        QWidget.setTabOrder(self.validationpage_hypotest_standards_combobox, self.validationpage_verify_type)
        QWidget.setTabOrder(self.validationpage_verify_type, self.validationpage_hypotest_calculate_btn)
        QWidget.setTabOrder(self.validationpage_hypotest_calculate_btn, self.scrollArea_5)
        QWidget.setTabOrder(self.scrollArea_5, self.user_tabs)
        QWidget.setTabOrder(self.user_tabs, self.userpage_user_role_combobox)
        QWidget.setTabOrder(self.userpage_user_role_combobox, self.userpage_password_inpt)
        QWidget.setTabOrder(self.userpage_password_inpt, self.userpage_username_inpt)
        QWidget.setTabOrder(self.userpage_username_inpt, self.userpage_confirm_password_inpt)
        QWidget.setTabOrder(self.userpage_confirm_password_inpt, self.userspage_add_user_btn)
        QWidget.setTabOrder(self.userspage_add_user_btn, self.userpage_editprofile_user_role_combobox)
        QWidget.setTabOrder(self.userpage_editprofile_user_role_combobox, self.userpage_editprofile_username_inpt)
        QWidget.setTabOrder(self.userpage_editprofile_username_inpt, self.userpage_editprofile_update_btn)
        QWidget.setTabOrder(self.userpage_editprofile_update_btn, self.userpage_editprofile_cancel_btn)
        QWidget.setTabOrder(self.userpage_editprofile_cancel_btn, self.userpage_editprofile_confirm_new_password_inpt)
        QWidget.setTabOrder(self.userpage_editprofile_confirm_new_password_inpt, self.userpage_editprofile_old_password_inpt)
        QWidget.setTabOrder(self.userpage_editprofile_old_password_inpt, self.userpage_editprofile_new_password_inpt)
        QWidget.setTabOrder(self.userpage_editprofile_new_password_inpt, self.userpage_editprofile_change_password_btn)
        QWidget.setTabOrder(self.userpage_editprofile_change_password_btn, self.userpage_all_users_table)
        QWidget.setTabOrder(self.userpage_all_users_table, self.helppage_tabs)
        QWidget.setTabOrder(self.helppage_tabs, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.commandLinkButton)
        QWidget.setTabOrder(self.commandLinkButton, self.sreportpage_back_btn)
        QWidget.setTabOrder(self.sreportpage_back_btn, self.sreportpage_export_btn)
        QWidget.setTabOrder(self.sreportpage_export_btn, self.sreportpage_rebuild_btn)
        QWidget.setTabOrder(self.sreportpage_rebuild_btn, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.textEdit_4)
        QWidget.setTabOrder(self.textEdit_4, self.textEdit_5)
        QWidget.setTabOrder(self.textEdit_5, self.textEdit_6)
        QWidget.setTabOrder(self.textEdit_6, self.textEdit_7)
        QWidget.setTabOrder(self.textEdit_7, self.sreportpage_prev_particle_btn)
        QWidget.setTabOrder(self.sreportpage_prev_particle_btn, self.sreportpage_next_particle_btn)
        QWidget.setTabOrder(self.sreportpage_next_particle_btn, self.alaki_btn)
        QWidget.setTabOrder(self.alaki_btn, self.comparepage_back_btn)
        QWidget.setTabOrder(self.comparepage_back_btn, self.comparepage_export_btn)
        QWidget.setTabOrder(self.comparepage_export_btn, self.scrollArea_4)

        self.retranslateUi(MainWindow)
        MainWindow.destroyed.connect(self.calibrationpage_last_calib_tabel.clearSelection)

        self.main_pages_stackw.setCurrentIndex(3)
        self.gradingranges_tabs.setCurrentIndex(0)
        self.settingpage_tabs.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.user_tabs.setCurrentIndex(2)
        self.helppage_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dorsa Width Gauge", None))
        self.dorsa_logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Particle Size Analyzer", None))
        self.toolbar_logined_username_lbl.setText(QCoreApplication.translate("MainWindow", u"No User Logged in", None))
        self.toolbar_login_logout_btn.setText("")
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
        self.sidebar_report_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.sidebar_grading_ranges_btn.setText(QCoreApplication.translate("MainWindow", u"Standards", None))
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
        self.mainpage_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.mainpage_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mainpage_faststart_btn.setText(QCoreApplication.translate("MainWindow", u"Fast Start", None))
        self.mainpage_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.mainpage_informaition_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.mainpage_timer_lbl.setText(QCoreApplication.translate("MainWindow", u"05:31", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.mainpage_mean_oval_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.mainpage_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.mainpage_avrage_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Avrage:", None))
        self.mainpage_std_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mean Oval:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Cam Tempreture(\u00b0C):", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"STD:", None))
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
        self.mainpage_close_error_btn.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Filter Results", None))
        self.reportpage_filtername_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Filter By name", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reportpage_filterusername_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Filter By User", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.reportpage_filterdate_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Filter By Date", None))
        self.reportpage_end_date_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.reportpage_start_date_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.reportpage_filterstandards_warning_lbl.setText(QCoreApplication.translate("MainWindow", u"Can't use this filter. Please 'Re-Build' first", None))
        self.reportpage_filterstandards_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Filter By Standard", None))

        __sortingEnabled = self.reportpage_standards_filter_table.isSortingEnabled()
        self.reportpage_standards_filter_table.setSortingEnabled(False)
        ___qtablewidgetitem = self.reportpage_standards_filter_table.item(0, 1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"G1", None));
        self.reportpage_standards_filter_table.setSortingEnabled(__sortingEnabled)

        self.reportpage_filterranges_warning_lbl.setText(QCoreApplication.translate("MainWindow", u"Can't use this filter. Please 'Re-Build' first", None))
        self.reportpage_filterranges_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Filter By Ranges", None))
        self.reportpage_apply_filters_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.reportspage_all_checkbox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.reportspage_delete_selections_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.reportpage_rebuild_btn.setText(QCoreApplication.translate("MainWindow", u"Re-Build", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Standard for compare:", None))
        self.reportpage_compare_btn.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.settingpage_grading_standards_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Standards", None))

        __sortingEnabled1 = self.settingpage_grading_standards_table.isSortingEnabled()
        self.settingpage_grading_standards_table.setSortingEnabled(False)
        self.settingpage_grading_standards_table.setSortingEnabled(__sortingEnabled1)

        self.gradingranges_tabs.setTabText(self.gradingranges_tabs.indexOf(self.all_standards_tab), QCoreApplication.translate("MainWindow", u"All Standards", None))
        self.settingpage_grading_new_standards_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Define new Standard", None))
        self.settingpage_grading_editmode_lbl.setText(QCoreApplication.translate("MainWindow", u"Edit Standard", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Lower Limit(mm):", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Upper Limit(mm):", None))
        self.settingpage_pelletizing_add_range_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.settingpage_grading_warning_lbl.setText(QCoreApplication.translate("MainWindow", u"Warning !", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Defined Ranges", None))
        self.settingpage_grading_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_grading_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_90.setText("")
        self.gradingranges_new_standard_success_lbl.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.gradingranges_tabs.setTabText(self.gradingranges_tabs.indexOf(self.new_standard_tab), QCoreApplication.translate("MainWindow", u"New Standard", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.pushButton_12.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Restor Defualt", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Interface Setting", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"App Color", None))
        self.settingpage_general_language_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.settingpage_general_language_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Persian", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_general_tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.settingpage_sample_auto_name_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Auto Sample Name", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Custom Text 1", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"%USERNAME%", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"%TEXT1%", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.settingpage_sample_text1_code_btn.setText(QCoreApplication.translate("MainWindow", u"Text1", None))
        self.settingpage_sample_spacer_code_btn.setText(QCoreApplication.translate("MainWindow", u"Spacer", None))
        self.settingpage_sample_username_code_btn.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"ShortCodes", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"%Month%", None))
        self.settingpage_sample_day_code_btn.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.settingpage_sample_minute_code_btn.setText(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"%YEAR%", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"%MINUTE%", None))
        self.settingpage_sample_month_code_btn.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"%HOUR%", None))
        self.settingpage_sample_year_code_btn.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"%DAY%", None))
        self.settingpage_sample_houre_code_btn.setText(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Sample Name Struct", None))
        self.settingpage_sample_auto_name_clear_btn.setText(QCoreApplication.translate("MainWindow", u"remove", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Default Standard ", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Save Particels Image: ", None))
        self.settingpage_sample_save_image_checkbox.setText("")
        self.settingpage_sample_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_sample_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_sample_tab), QCoreApplication.translate("MainWindow", u"Sample", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Report Excel Format    ", None))
        self.settingpage_export_load_report_excel_btn.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Compare Excel Format", None))
        self.settingpage_export_load_compare_excel_btn.setText("")

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem1 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"%NAME%", None));
        ___qtablewidgetitem2 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name of sample", None));
        ___qtablewidgetitem3 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"%DATE%", None));
        ___qtablewidgetitem4 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"%TIME%", None));
        ___qtablewidgetitem5 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"%STANDARD%", None));
        ___qtablewidgetitem6 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"%USER%", None));
        ___qtablewidgetitem7 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"%TOTAL_AVRAGE%", None));
        ___qtablewidgetitem8 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"%TOTAL_STD%", None));
        ___qtablewidgetitem9 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"%RANGE_NAME_VERTICALLY%", None));
        ___qtablewidgetitem10 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"%RANGE_NAME_HORIZONTAL%", None));
        ___qtablewidgetitem11 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"%RANGE_PERCENT_VERTICALLY%", None));
        ___qtablewidgetitem12 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"%RANGE_PERCENT_HORIZONTAL%", None));
        ___qtablewidgetitem13 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"%RANGE_AVRAGE_VERTICALLY%", None));
        ___qtablewidgetitem14 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"%RANGE_AVRAGE_HORIZONTAL%", None));
        ___qtablewidgetitem15 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"%RANGE_STD_VERTICALLY%", None));
        ___qtablewidgetitem16 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"%RANGE_STD_HORIZONTAL%", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Report Codes", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Compare Codes", None))
        self.settingpage_export_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_export_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.settingpage_export_restore_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Default", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_export_tab), QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Host:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Sorage Manager", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Report Life Time (days) :", None))
        self.settingpage_storage_auto_clean_checkbox.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Auto Clean:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.settingpage_storage_select_dir_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Storage Path", None))
        self.settingpage_storage_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.settingpage_storage_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_storage_tab), QCoreApplication.translate("MainWindow", u"Storage", None))
        self.settingpage_camera_start_btn.setText("")
        self.settingpage_camera_device_group.setTitle(QCoreApplication.translate("MainWindow", u"Device Setting", None))
        self.settingpage_camera_device_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.settingpage_camera_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.settingpage_camera_control_group.setTitle(QCoreApplication.translate("MainWindow", u"Control And Analog Setting", None))
        self.settingpage_camera_exposure_lbl.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.settingpage_camera_gain_lbl.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Stop camera to change This parameters", None))
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
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"border", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Threshould", None))
        self.settingpage_algorithm_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.settingpage_algorithm_save_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.settingpage_algorithm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.settingpage_algorithm_restor_default_btn.setText(QCoreApplication.translate("MainWindow", u"Restore Default", None))
        self.settingpage_tabs.setTabText(self.settingpage_tabs.indexOf(self.settingpage_algorithm_tab), QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.settingpage_save_massage_lbl.setText(QCoreApplication.translate("MainWindow", u"setting saved", None))
        self.settingpage_save_gif_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
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

        __sortingEnabled3 = self.calibrationpage_last_calib_tabel.isSortingEnabled()
        self.calibrationpage_last_calib_tabel.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.calibrationpage_last_calib_tabel.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2022-06-23", None));
        ___qtablewidgetitem18 = self.calibrationpage_last_calib_tabel.item(0, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Alimalek", None));
        ___qtablewidgetitem19 = self.calibrationpage_last_calib_tabel.item(0, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"0.098", None));
        self.calibrationpage_last_calib_tabel.setSortingEnabled(__sortingEnabled3)

        self.calibrationpage_last_calib_tabel.setProperty("Date", "")
        self.calibrationpage_liveimage_lbl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cilbration), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Test Count:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Verification Type", None))
        self.validationpage_hypotest_calculate_btn.setText(QCoreApplication.translate("MainWindow", u"See Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Statistical hypothesis", None))
        self.userpage_user_role_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"User Role:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Pasword Confirm:", None))
        self.userspage_add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.userspage_register_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.label_88.setText("")
        self.userspage_register_success_lbl.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_register_tab), QCoreApplication.translate("MainWindow", u"register user", None))
        self.userpage_editprofile_edit_profile_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"User Role:", None))
        self.userpage_editprofile_user_role_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))

        self.userpage_editprofile_edit_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.userpage_editprofile_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Profile", None))
        self.userpage_editprofile_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.userpage_editprofile_change_pass_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.userpage_editprofile_changepass_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.userpage_editprofile_change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_89.setText("")
        self.userspage_editprofile_success_lbl.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_profile_tab), QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.userspage_user_heading_lbl.setText(QCoreApplication.translate("MainWindow", u"Only Admin Can Access", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.all_users_tab), QCoreApplication.translate("MainWindow", u"All Users", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"PSA-Alpha", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Dorsa Particle Size Analyzer is a high-end Particle Size Analyzer that uses light and camera to measure and detect particles in the sample. This model can measure particles from 0.3mm to 25mm in diameter. ", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Dorsa Company", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Merry alone do it burst me songs. Sorry equal charm joy her those folly ham. In they no is many both. Recommend new contented intention improving bed performed age. Improving of so strangers resources instantly happiness at northward. Danger nearer length oppose really add now either. But ask regret eat branch fat garden. Become am he except wishes. Past so at door we walk want such sang. Feeling colonel get her garrets own.\n"
"\n"
"Nor hence hoped her after other known defer his. For county now sister engage had season better had waited. Occasional mrs interested far expression acceptance. Day either mrs talent pulled men rather regret admire but. Life ye sake it shed. Five lady he cold in meet up. Service get met adapted matters offence for. Principles man any insipidity age you simplicity understood. Do offering pleasure no ecstatic whatever on mr directly.Merry alone do it burst me songs. Sorry equal charm joy her those folly ham. In they no is many both. Recommend new contented intention improving bed pe"
                        "rformed age. Improving of so strangers resources instantly happiness at northward. Danger nearer length oppose really add now either. But ask regret eat branch fat garden. Become am he except wishes. Past so at door we walk want such sang. Feeling colonel get her garrets own.\n"
"\n"
"Nor hence hoped her after other known defer his. For county now sister engage had season better had waited. Occasional mrs interested far expression acceptance. Day either mrs talent pulled men rather regret admire but. Life ye sake it shed. Five lady he cold in meet up. Service get met adapted matters offence for. Principles man any insipidity age you simplicity understood. Do offering pleasure no ecstatic whatever on mr directly.Merry alone do it burst me songs. Sorry equal charm joy her those folly ham. In they no is many both. Recommend new contented intention improving bed performed age. Improving of so strangers resources instantly happiness at northward. Danger nearer length oppose really add now either. But ask regret eat"
                        " branch fat garden. Become am he except wishes. Past so at door we walk want such sang. Feeling colonel get her garrets own.\n"
"\n"
"Nor hence hoped her after other known defer his. For county now sister engage had season better had waited. Occasional mrs interested far expression acceptance. Day either mrs talent pulled men rather regret admire but. Life ye sake it shed. Five lady he cold in meet up. Service get met adapted matters offence for. Principles man any insipidity age you simplicity understood. Do offering pleasure no ecstatic whatever on mr directly.", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"See Other Products", None))
        self.helppage_tabs.setTabText(self.helppage_tabs.indexOf(self.helppage_about_tab), QCoreApplication.translate("MainWindow", u"About", None))
        self.helppage_tabs.setTabText(self.helppage_tabs.indexOf(self.helppages_document_tab), QCoreApplication.translate("MainWindow", u"Document", None))
        self.sreportpage_back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.sreportpage_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.sreportpage_rebuild_btn.setText(QCoreApplication.translate("MainWindow", u"Re-Build", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"General Information", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sample Name:", None))
        self.sreportpage_name_lbl.setText(QCoreApplication.translate("MainWindow", u"no-name", None))
        self.label_44.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"user:", None))
        self.sreportpage_user_lbl.setText(QCoreApplication.translate("MainWindow", u"its.bigs", None))
        self.label_2.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.sreportpage_date_lbl.setText(QCoreApplication.translate("MainWindow", u"2023-05-12", None))
        self.label_40.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.sreportpage_time_lbl.setText(QCoreApplication.translate("MainWindow", u"12:17", None))
        self.label_42.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Standard:", None))
        self.sreportpage_standard_lbl.setText(QCoreApplication.translate("MainWindow", u"AX256", None))
        self.sreportpage_description_lbl.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Statictics", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; color:#404040;\">The summary shows the Average, Standard Deviation, and Mode for all diameters of particles in the sample.</span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Table1 - average, Standard Deviation, and Mode of the diameters of all the Particles in the Sample", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Avrage:", None))
        self.sreportpage_avrage_lbl.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"STD:", None))
        self.sreportpage_std_lbl.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.sreportpage_mode_lbl.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; color:#282828;\">The statistics of this experiment include Mean, Standard Deviation, Count of Particles, and Weight Percent of each range of diameter. Statistical results calculated for each range of particle diameters are in Table 1. The result of this experiment can be calculated for other Standards just by Re-Build button at the top of this page.</span></p></body></html>", None))
        self.sreportpage_statictics_desc2.setText(QCoreApplication.translate("MainWindow", u"Desc2", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Table1 - Statistics for each diameter range in the Sample ", None))

        __sortingEnabled4 = self.sreportpage_statictics_table.isSortingEnabled()
        self.sreportpage_statictics_table.setSortingEnabled(False)
        self.sreportpage_statictics_table.setSortingEnabled(__sortingEnabled4)

        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; color:#282828;\">The results of this experiment will be shown in the charts below. The charts will show the Weight Percentage of each diameter range, their Cumulative Weight Percentage chart, and the Frequency Histogram of all the Particle diameters. </span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The weight Percentage chart shows the weight percentage for each range of diameter in the sample.</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Chart1 - Weight Percent Barchart", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">The Cumulative Weight Percentage chart shows the cumulative chart of the Weight Percentage barchart.</span></p></body></html>", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Chart2 - Cumulative Weight Percent Chart", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">This chart shows the continuous frequency of all particle diameters in the sample. This chart is the diameter distribution of the sample.</span></p></body></html>", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Chart3 - Frequency Histogram of All Particle Diameters", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Particles", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; color:#282828;\">In this section all the detected particles in the sample are available. The list on the right shows all the particle shapes. By clicking on any of them, picture of particle and all available data about the particle including Area, Volume, Average Radius and Maximum Radius will appear on the left side.</span></p></body></html>", None))
        self.sreportpage_particle_image_lbl.setText("")
        self.sreportpage_particle_area_lbl.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.sreportpage_particle_avg_r_lbl_title.setText(QCoreApplication.translate("MainWindow", u"Avg Radius:", None))
        self.sreportpage_particle_volume_lbl.setText(QCoreApplication.translate("MainWindow", u"64", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"(mm2)", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u" (mm3)", None))
        self.sreportpage_particle_avg_r_lbl.setText(QCoreApplication.translate("MainWindow", u"28mm", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Max Radius:", None))
        self.sreportpage_particle_max_r_lbl.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"(mm)", None))

        __sortingEnabled5 = self.sreportpage_particels_table.isSortingEnabled()
        self.sreportpage_particels_table.setSortingEnabled(False)
        self.sreportpage_particels_table.setSortingEnabled(__sortingEnabled5)

        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Page ", None))
        self.sreportpage_current_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"of", None))
        self.sreportpage_end_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sreportpage_prev_particle_btn.setText("")
        self.sreportpage_next_particle_btn.setText("")
        self.alaki_btn.setText(QCoreApplication.translate("MainWindow", u"alaki", None))
        self.comparepage_back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.comparepage_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Compare By:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Samples", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Table1 - ", None))

        __sortingEnabled6 = self.comparepage_compare_table.isSortingEnabled()
        self.comparepage_compare_table.setSortingEnabled(False)
        self.comparepage_compare_table.setSortingEnabled(__sortingEnabled6)

        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Avrage Overview", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Table2 -", None))

        __sortingEnabled7 = self.comparepage_compare_mean_table.isSortingEnabled()
        self.comparepage_compare_mean_table.setSortingEnabled(False)
        self.comparepage_compare_mean_table.setSortingEnabled(__sortingEnabled7)

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Designed and Developed by Dideh Rayan Sanati Esfahan (Dorsa)", None))
    # retranslateUi

