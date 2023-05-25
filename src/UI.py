# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(570, 340, 50, 50))
        self.startButton.setMinimumSize(QSize(50, 50))
        self.startButton.setMaximumSize(QSize(50, 50))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(500, 340, 50, 50))
        self.stopButton.setMinimumSize(QSize(50, 50))
        self.stopButton.setMaximumSize(QSize(50, 50))
        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setGeometry(QRect(280, 300, 70, 40))
        self.goButton.setMinimumSize(QSize(70, 40))
        self.goButton.setMaximumSize(QSize(70, 40))
        self.midButton = QPushButton(self.centralwidget)
        self.midButton.setObjectName(u"midButton")
        self.midButton.setGeometry(QRect(280, 350, 70, 40))
        self.midButton.setMinimumSize(QSize(70, 40))
        self.midButton.setMaximumSize(QSize(70, 40))
        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setGeometry(QRect(200, 350, 70, 40))
        self.leftButton.setMinimumSize(QSize(70, 40))
        self.leftButton.setMaximumSize(QSize(70, 40))
        self.RightButton = QPushButton(self.centralwidget)
        self.RightButton.setObjectName(u"RightButton")
        self.RightButton.setGeometry(QRect(360, 350, 70, 40))
        self.RightButton.setMinimumSize(QSize(70, 40))
        self.RightButton.setMaximumSize(QSize(70, 40))
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(280, 400, 70, 40))
        self.backButton.setMinimumSize(QSize(70, 40))
        self.backButton.setMaximumSize(QSize(70, 40))
        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(20, 40, 241, 231))
        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(630, 40, 251, 231))
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(290, 30, 320, 240))
        self.image_label.setMinimumSize(QSize(320, 240))
        self.image_label.setMaximumSize(QSize(320, 240))
        self.image_label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.autoButton = QPushButton(self.centralwidget)
        self.autoButton.setObjectName(u"autoButton")
        self.autoButton.setGeometry(QRect(640, 340, 50, 50))
        self.autoButton.setMinimumSize(QSize(50, 50))
        self.autoButton.setMaximumSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.stopButton.clicked.connect(MainWindow.stop)
        self.RightButton.clicked.connect(MainWindow.right)
        self.leftButton.clicked.connect(MainWindow.left)
        self.goButton.clicked.connect(MainWindow.go)
        self.midButton.clicked.connect(MainWindow.mid)
        self.backButton.clicked.connect(MainWindow.back)
        self.autoButton.clicked.connect(MainWindow.auto)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.RightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.image_label.setText("")
        self.autoButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
    # retranslateUi

