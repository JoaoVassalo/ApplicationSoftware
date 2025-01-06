# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MergeDatasetFormqaLyIh.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, page, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.main_page = page

        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                                   "	border-radius: 15px;\n"
                                                   "	border: 2px solid #F98600;\n"
                                                   "	color: white;\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_5.addWidget(self.textEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Final File Name", None))
    # retranslateUi

