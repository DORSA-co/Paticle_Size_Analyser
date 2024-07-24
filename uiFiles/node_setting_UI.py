# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Assets_rc

class Ui_NodeSetting(object):
    def setupUi(self, NodeSetting):
        if not NodeSetting.objectName():
            NodeSetting.setObjectName(u"NodeSetting")
        NodeSetting.resize(823, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NodeSetting.sizePolicy().hasHeightForWidth())
        NodeSetting.setSizePolicy(sizePolicy)
        NodeSetting.setMinimumSize(QSize(0, 80))
        NodeSetting.setMaximumSize(QSize(16777215, 80))
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
"")
        self.verticalLayout = QVBoxLayout(NodeSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainFrame = QFrame(NodeSetting)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"\n"
"#mainFrame{\n"
"	background-color: #F7F8FA;\n"
"	border-radius:15px;\n"
"	border: 1px solid rgb(232, 233, 235);\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame_2 = QFrame(self.mainFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.label = QLabel(self.horizontalFrame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.node_name_input = QLineEdit(self.horizontalFrame_2)
        self.node_name_input.setObjectName(u"node_name_input")
        self.node_name_input.setMaximumSize(QSize(300, 16777215))
        self.node_name_input.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.node_name_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.node_type_combobox = QComboBox(self.horizontalFrame_2)
        self.node_type_combobox.addItem("")
        self.node_type_combobox.addItem("")
        self.node_type_combobox.setObjectName(u"node_type_combobox")

        self.horizontalLayout_2.addWidget(self.node_type_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.remove_btn = QPushButton(self.horizontalFrame_2)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setStyleSheet(u"background-color:transparent;\n"
"min-width:30px;\n"
"max-width:30px;")
        icon = QIcon()
        icon.addFile(u":/assets/icons/icons8-close-black-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.remove_btn)


        self.verticalLayout_2.addWidget(self.horizontalFrame_2)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(NodeSetting)

        QMetaObject.connectSlotsByName(NodeSetting)
    # setupUi

    def retranslateUi(self, NodeSetting):
        NodeSetting.setWindowTitle(QCoreApplication.translate("NodeSetting", u"Form", None))
        self.label.setText(QCoreApplication.translate("NodeSetting", u"Node Name: ", None))
        self.label.setProperty("styleClass", QCoreApplication.translate("NodeSetting", u"title", None))
        self.node_type_combobox.setItemText(0, QCoreApplication.translate("NodeSetting", u"writable", None))
        self.node_type_combobox.setItemText(1, QCoreApplication.translate("NodeSetting", u"readable", None))

        self.label_2.setText(QCoreApplication.translate("NodeSetting", u"Node Address:", None))
        self.label_2.setProperty("styleClass", QCoreApplication.translate("NodeSetting", u"title", None))
        self.label_3.setText(QCoreApplication.translate("NodeSetting", u"ns", None))
        self.node_ns.setText(QCoreApplication.translate("NodeSetting", u"555", None))
        self.label_4.setText(QCoreApplication.translate("NodeSetting", u"i:", None))
        self.remove_btn.setText("")
    # retranslateUi

