# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectSelectionPageGKOxFU.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 320)
        Form.setMinimumSize(QSize(240, 320))
        Form.setMaximumSize(QSize(240, 320))
        Form.setStyleSheet(u"background-color: rgb(225, 225, 218);")
        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(50, 70, 140, 140))
        self.listView.setMinimumSize(QSize(140, 140))
        self.listView.setMaximumSize(QSize(140, 140))
        self.listView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 140, 15))
        self.label.setMinimumSize(QSize(140, 15))
        self.label.setMaximumSize(QSize(140, 15))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 240, 75, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(9, 35, 55);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	color: rgb(9, 35, 55);\n"
"	background-color: rgb(150, 169, 173);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"OPEN PROJECT", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"OPEN", None))
    # retranslateUi

