# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'read_signal_hmi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Assets_rc

class Ui_readSignalHMI(object):
    def setupUi(self, readSignalHMI):
        if not readSignalHMI.objectName():
            readSignalHMI.setObjectName(u"readSignalHMI")
        readSignalHMI.resize(300, 52)
        readSignalHMI.setMinimumSize(QSize(300, 50))
        readSignalHMI.setMaximumSize(QSize(300, 52))
        readSignalHMI.setStyleSheet(u"#SignalSetting{\n"
"\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(readSignalHMI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(readSignalHMI)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 0))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"#main_frame{\n"
"	background-color: #F7F8FA;\n"
"	border-radius:15px;\n"
"	border: 1px solid rgb(232, 233, 235);\n"
"}\n"
"\n"
"#main_frame[state=\"active\"]{\n"
"	border: 2px solid rgb(63, 206, 73);\n"
"}\n"
"\n"
"#main_frame[state=\"off\"]{\n"
"	border: 1px solid rgb(232, 233, 235);\n"
"}\n"
"\n"
"#main_frame[state=\"not_active\"]{\n"
"	border: 2px solid rgb(213, 63, 65);\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_label = QLabel(self.main_frame)
        self.name_label.setObjectName(u"name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QSize(100, 0))
        self.name_label.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.name_label)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.numeric_value_indicator = QLabel(self.main_frame)
        self.numeric_value_indicator.setObjectName(u"numeric_value_indicator")
        sizePolicy.setHeightForWidth(self.numeric_value_indicator.sizePolicy().hasHeightForWidth())
        self.numeric_value_indicator.setSizePolicy(sizePolicy)
        self.numeric_value_indicator.setStyleSheet(u"color:#808080;\n"
"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.numeric_value_indicator, 0, Qt.AlignmentFlag.AlignRight)

        self.bool_value_indicator = QLabel(self.main_frame)
        self.bool_value_indicator.setObjectName(u"bool_value_indicator")
        self.bool_value_indicator.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bool_value_indicator.sizePolicy().hasHeightForWidth())
        self.bool_value_indicator.setSizePolicy(sizePolicy)
        self.bool_value_indicator.setMinimumSize(QSize(30, 30))
        self.bool_value_indicator.setMaximumSize(QSize(30, 30))
        self.bool_value_indicator.setStyleSheet(u"QLabel{\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel[state=\"true\"]{\n"
"	\n"
"	background-color: rgb(85, 170, 127);\n"
"}\n"
"\n"
"QLabel[state=\"false\"]{\n"
"	\n"
"	background-color: rgb(170, 51, 51);\n"
"}\n"
"\n"
"\n"
"QLabel:disabled{\n"
"	background-color: rgb(200,200,200);\n"
"}")
        self.bool_value_indicator.setProperty("state", False)

        self.horizontalLayout_2.addWidget(self.bool_value_indicator)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(readSignalHMI)

        QMetaObject.connectSlotsByName(readSignalHMI)
    # setupUi

    def retranslateUi(self, readSignalHMI):
        readSignalHMI.setWindowTitle(QCoreApplication.translate("readSignalHMI", u"Form", None))
        self.main_frame.setProperty("state", QCoreApplication.translate("readSignalHMI", u"off", None))
        self.name_label.setText(QCoreApplication.translate("readSignalHMI", u"name", None))
        self.numeric_value_indicator.setText(QCoreApplication.translate("readSignalHMI", u"0.0", None))
        self.bool_value_indicator.setText(QCoreApplication.translate("readSignalHMI", u"-", None))
    # retranslateUi

