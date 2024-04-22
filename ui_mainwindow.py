# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(393, 510)
        font = QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(72, 200, 191);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grd_tasks = QGridLayout()
        self.grd_tasks.setObjectName(u"grd_tasks")

        self.verticalLayout.addLayout(self.grd_tasks)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Wide Latin"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font: 13pt \"Wide Latin\";\n"
"background-color: rgb(85, 85, 255);\n"
"")

        self.verticalLayout.addWidget(self.label_4)

        self.txt_newTask = QLineEdit(self.centralwidget)
        self.txt_newTask.setObjectName(u"txt_newTask")
        self.txt_newTask.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.txt_newTask.setFont(font2)
        self.txt_newTask.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.txt_newTask)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font: 13pt \"Wide Latin\";")

        self.verticalLayout.addWidget(self.label_2)

        self.txt_desc = QTextEdit(self.centralwidget)
        self.txt_desc.setObjectName(u"txt_desc")
        self.txt_desc.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.txt_desc.setFont(font3)
        self.txt_desc.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.txt_desc)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 13pt \"Wide Latin\";\n"
"background-color: rgb(255, 170, 255);")

        self.verticalLayout.addWidget(self.label)

        self.txt_priority = QLineEdit(self.centralwidget)
        self.txt_priority.setObjectName(u"txt_priority")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_priority.sizePolicy().hasHeightForWidth())
        self.txt_priority.setSizePolicy(sizePolicy)
        self.txt_priority.setMaximumSize(QSize(50, 16777215))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.txt_priority.setFont(font4)
        self.txt_priority.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.txt_priority)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"font: 13pt \"Wide Latin\";")

        self.verticalLayout.addWidget(self.label_3)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        self.dateTimeEdit.setFont(font5)
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.btn_newTask = QPushButton(self.centralwidget)
        self.btn_newTask.setObjectName(u"btn_newTask")
        self.btn_newTask.setFont(font2)
        self.btn_newTask.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.verticalLayout.addWidget(self.btn_newTask)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 393, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"                             Title:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                    Description:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"   Priority:(low<5   High>5)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"                Date  and Time:", None))
        self.btn_newTask.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

