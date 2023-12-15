# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'point2d.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        if not mainForm.objectName():
            mainForm.setObjectName(u"mainForm")
        mainForm.resize(202, 91)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainForm.sizePolicy().hasHeightForWidth())
        mainForm.setSizePolicy(sizePolicy)
        mainForm.setStyleSheet(u"QLabel{\n"
"	color:#404040;\n"
"}\n"
"\n"
"#mainForm{\n"
"background-color:;\n"
"	color: rgb(248, 248, 248);\n"
"	border:1px solid #404040;\n"
"}")
        self.gridLayout = QGridLayout(mainForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.x_title = QLabel(mainForm)
        self.x_title.setObjectName(u"x_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.x_title.sizePolicy().hasHeightForWidth())
        self.x_title.setSizePolicy(sizePolicy1)
        self.x_title.setMinimumSize(QSize(50, 0))
        self.x_title.setMaximumSize(QSize(100, 16777215))
        self.x_title.setSizeIncrement(QSize(0, 0))
        self.x_title.setStyleSheet(u"font-weight:bold;\n"
"font-size: 14px;")

        self.gridLayout.addWidget(self.x_title, 0, 0, 1, 1)

        self.y_title = QLabel(mainForm)
        self.y_title.setObjectName(u"y_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.y_title.sizePolicy().hasHeightForWidth())
        self.y_title.setSizePolicy(sizePolicy2)
        self.y_title.setMinimumSize(QSize(50, 0))
        self.y_title.setMaximumSize(QSize(100, 16777215))
        self.y_title.setStyleSheet(u"font-weight:bold;\n"
"font-size: 14px;")

        self.gridLayout.addWidget(self.y_title, 1, 0, 1, 1)

        self.x_value = QLabel(mainForm)
        self.x_value.setObjectName(u"x_value")

        self.gridLayout.addWidget(self.x_value, 0, 1, 1, 1)

        self.y_value = QLabel(mainForm)
        self.y_value.setObjectName(u"y_value")

        self.gridLayout.addWidget(self.y_value, 1, 1, 1, 1)


        self.retranslateUi(mainForm)

        QMetaObject.connectSlotsByName(mainForm)
    # setupUi

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QCoreApplication.translate("mainForm", u"Form", None))
        self.x_title.setText(QCoreApplication.translate("mainForm", u"X-name:", None))
        self.y_title.setText(QCoreApplication.translate("mainForm", u"y-name:", None))
        self.x_value.setText(QCoreApplication.translate("mainForm", u"x-value", None))
        self.y_value.setText(QCoreApplication.translate("mainForm", u"y-value", None))
    # retranslateUi

