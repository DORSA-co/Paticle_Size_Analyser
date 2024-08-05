# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_signal_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Assets_rc

class Ui_outputSignalSetting(object):
    def setupUi(self, outputSignalSetting):
        if not outputSignalSetting.objectName():
            outputSignalSetting.setObjectName(u"outputSignalSetting")
        outputSignalSetting.resize(650, 90)
        outputSignalSetting.setMinimumSize(QSize(0, 90))
        outputSignalSetting.setMaximumSize(QSize(650, 90))
        outputSignalSetting.setStyleSheet(u"#SignalSetting{\n"
"\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(outputSignalSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(outputSignalSetting)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 0))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"#main_frame{\n"
"	background-color: #F7F8FA;\n"
"	border-radius:15px;\n"
"	border: 1px solid rgb(232, 233, 235);\n"
"}")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.signal_name_combobox = QComboBox(self.main_frame)
        self.signal_name_combobox.setObjectName(u"signal_name_combobox")
        self.signal_name_combobox.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout.addWidget(self.signal_name_combobox)

        self.value_numeric = QDoubleSpinBox(self.main_frame)
        self.value_numeric.setObjectName(u"value_numeric")
        self.value_numeric.setMinimumSize(QSize(120, 0))
        self.value_numeric.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.value_numeric)

        self.value_bool = QComboBox(self.main_frame)
        self.value_bool.addItem("")
        self.value_bool.addItem("")
        self.value_bool.setObjectName(u"value_bool")
        self.value_bool.setMinimumSize(QSize(100, 0))
        self.value_bool.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.value_bool)

        self.remove_btn = QPushButton(self.main_frame)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setStyleSheet(u"background-color:transparent;\n"
"min-width:30px;\n"
"max-width:30px;")
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-close-black-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.remove_btn)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(outputSignalSetting)

        QMetaObject.connectSlotsByName(outputSignalSetting)
    # setupUi

    def retranslateUi(self, outputSignalSetting):
        outputSignalSetting.setWindowTitle(QCoreApplication.translate("outputSignalSetting", u"Form", None))
        self.label.setText(QCoreApplication.translate("outputSignalSetting", u"Signal: ", None))
        self.value_bool.setItemText(0, QCoreApplication.translate("outputSignalSetting", u"True", None))
        self.value_bool.setItemText(1, QCoreApplication.translate("outputSignalSetting", u"False", None))

        self.remove_btn.setText("")
    # retranslateUi

