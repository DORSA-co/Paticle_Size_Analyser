# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_signal_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Assets_rc

class Ui_inputSignalSetting(object):
    def setupUi(self, inputSignalSetting):
        if not inputSignalSetting.objectName():
            inputSignalSetting.setObjectName(u"inputSignalSetting")
        inputSignalSetting.resize(650, 90)
        inputSignalSetting.setMinimumSize(QSize(0, 90))
        inputSignalSetting.setMaximumSize(QSize(650, 90))
        inputSignalSetting.setStyleSheet(u"#SignalSetting{\n"
"\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(inputSignalSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(inputSignalSetting)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 0))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"#main_frame{\n"
"	background-color: #F7F8FA;\n"
"	border-radius:15px;\n"
"	border: 1px solid rgb(232, 233, 235);\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.signal_name_combobox = QComboBox(self.main_frame)
        self.signal_name_combobox.setObjectName(u"signal_name_combobox")
        self.signal_name_combobox.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.signal_name_combobox)

        self.condition_combobox = QComboBox(self.main_frame)
        self.condition_combobox.addItem("")
        self.condition_combobox.addItem("")
        self.condition_combobox.addItem("")
        self.condition_combobox.addItem("")
        self.condition_combobox.addItem("")
        self.condition_combobox.setObjectName(u"condition_combobox")
        self.condition_combobox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.condition_combobox)

        self.signal_value = QDoubleSpinBox(self.main_frame)
        self.signal_value.setObjectName(u"signal_value")
        self.signal_value.setMinimumSize(QSize(120, 0))
        self.signal_value.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.signal_value)

        self.remove_btn = QPushButton(self.main_frame)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setStyleSheet(u"background-color:transparent;\n"
"min-width:30px;\n"
"max-width:30px;")
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-close-black-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.remove_btn)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(inputSignalSetting)

        QMetaObject.connectSlotsByName(inputSignalSetting)
    # setupUi

    def retranslateUi(self, inputSignalSetting):
        inputSignalSetting.setWindowTitle(QCoreApplication.translate("inputSignalSetting", u"Form", None))
        self.label.setText(QCoreApplication.translate("inputSignalSetting", u"Signal: ", None))
        self.condition_combobox.setItemText(0, QCoreApplication.translate("inputSignalSetting", u"be True", None))
        self.condition_combobox.setItemText(1, QCoreApplication.translate("inputSignalSetting", u"be False", None))
        self.condition_combobox.setItemText(2, QCoreApplication.translate("inputSignalSetting", u">", None))
        self.condition_combobox.setItemText(3, QCoreApplication.translate("inputSignalSetting", u"<", None))
        self.condition_combobox.setItemText(4, QCoreApplication.translate("inputSignalSetting", u"=", None))

        self.remove_btn.setText("")
    # retranslateUi

