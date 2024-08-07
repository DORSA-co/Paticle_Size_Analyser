# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'write_signal_hmi.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from uiUtils.GUIComponents import SwitchControl
import Assets_rc

class Ui_writeSignalHMI(object):
    def setupUi(self, writeSignalHMI):
        if not writeSignalHMI.objectName():
            writeSignalHMI.setObjectName(u"writeSignalHMI")
        writeSignalHMI.resize(400, 90)
        writeSignalHMI.setMinimumSize(QSize(250, 90))
        writeSignalHMI.setMaximumSize(QSize(400, 90))
        writeSignalHMI.setStyleSheet(u"#SignalSetting{\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: transparent;\n"
"border:none;\n"
"}")
        self.verticalLayout = QVBoxLayout(writeSignalHMI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(writeSignalHMI)
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
        self.name_label.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.name_label)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox = QDoubleSpinBox(self.main_frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)

        self.write_bool_value_frame = QFrame(self.main_frame)
        self.write_bool_value_frame.setObjectName(u"write_bool_value_frame")
        self.write_bool_value_frame.setMinimumSize(QSize(20, 0))
        self.write_bool_value_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.write_bool_value_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.write_bool_value_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.write_bool_value_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout.addWidget(self.label_2)

        self.checkBox = SwitchControl(self.write_bool_value_frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.checkBox)

        self.label_3 = QLabel(self.write_bool_value_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font-weight:bold;")

        self.horizontalLayout.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.write_bool_value_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(writeSignalHMI)

        QMetaObject.connectSlotsByName(writeSignalHMI)
    # setupUi

    def retranslateUi(self, writeSignalHMI):
        writeSignalHMI.setWindowTitle(QCoreApplication.translate("writeSignalHMI", u"Form", None))
        self.main_frame.setProperty("state", QCoreApplication.translate("writeSignalHMI", u"off", None))
        self.name_label.setText(QCoreApplication.translate("writeSignalHMI", u"name", None))
        self.label_2.setText(QCoreApplication.translate("writeSignalHMI", u"off", None))
        self.checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("writeSignalHMI", u"on", None))
    # retranslateUi

