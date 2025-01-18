# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1297, 582)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 20, 891, 501))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(990, 60, 111, 41))
        self.InsertButton = QPushButton(self.centralwidget)
        self.InsertButton.setObjectName(u"InsertButton")
        self.InsertButton.setGeometry(QRect(1110, 60, 121, 41))
        self.SearchButton = QPushButton(self.centralwidget)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setGeometry(QRect(990, 110, 111, 41))
        self.DeleteButton = QPushButton(self.centralwidget)
        self.DeleteButton.setObjectName(u"DeleteButton")
        self.DeleteButton.setGeometry(QRect(1110, 110, 121, 41))
        self.DeleteWholeTreeButton = QPushButton(self.centralwidget)
        self.DeleteWholeTreeButton.setObjectName(u"DeleteWholeTreeButton")
        self.DeleteWholeTreeButton.setGeometry(QRect(990, 170, 241, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(990, 20, 241, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(960, 220, 301, 71))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(920, 300, 451, 211))
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1297, 21))
        self.menuBST = QMenu(self.menubar)
        self.menuBST.setObjectName(u"menuBST")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuBST.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.InsertButton.setText(QCoreApplication.translate("MainWindow", u"insert", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.DeleteWholeTreeButton.setText(QCoreApplication.translate("MainWindow", u"delete whole tree ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Wprowadz warto\u015b\u0107</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Informacje o aktualnie wy\u015bwietlanym</span></p><p align=\"center\"><span style=\" font-size:12pt;\">drzewie:</span></p></body></html>", None))
        self.label_4.setText("")
        self.menuBST.setTitle(QCoreApplication.translate("MainWindow", u"BST", None))
    # retranslateUi

