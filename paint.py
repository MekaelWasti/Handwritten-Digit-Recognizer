from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QIcon, QImage, QColor, QAction, QPainter, QPen
from PyQt6.QtCore import Qt, QPoint, QEvent, QSize
from PyQt6 import uic
from mlalgo import *

import sys

# Add Icon (Override Windows defaulting to python icon)
import ctypes
myappid = '1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Window(QMainWindow):
    
    def __init__(self):
        # Initial Set Up
        super(Window,self).__init__()
        uic.loadUi("MainWindow.ui",self)
        self.setWindowTitle("Handwritten Digit Recognizer")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(1280,720)
        self.setFixedSize(1280,720)

        # Remove Window Title Bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Create Drawing Portion
        # size = QSize(53,20)
        size = QSize(853,720)
        self.image = QImage(size, QImage.Format.Format_RGB32)
        self.image.fill(QColor(23,23,23)) #Black Fill
        # self.image.fill(QColor(255,255,255)) #White Fill

        self.drawing = False
        # self.brushSize = 2
        self.brushSize = 25
        self.brushColor = QColor(255,255,255)

        self.lastPoint = QPoint()

        # Connect Methods to Buttons
        self.recognizeButton.clicked.connect(self.recognize)
        self.closeButton.clicked.connect(self.exitApplication)
        self.clearButton.clicked.connect(self.clear)
        self.resultLabel = self.resultView
        
        # Change button on hover
        self.closeButton.setStyleSheet(
            "QPushButton {"
                "border: none;"
	            "image: url(Close.png)"
            "}"

            "QPushButton:hover:!pressed {"
                "border: none;"
	            "image: url(Close_hover.png)"
            "}"
            )
        
        self.maximizeButton.setStyleSheet(
            "QPushButton {"
                "border: none;"
	            "image: url(Maximize.png)"
            "}"

            "QPushButton:hover:!pressed {"
                "border: none;"
	            "image: url(Maximize_hover.png)"
            "}"
            )
        
        self.minimizeButton.setStyleSheet(
            "QPushButton {"
                "border: none;"
	            "image: url(Minimize.png)"
            "}"

            "QPushButton:hover:!pressed {"
                "border: none;"
	            "image: url(Minimize_hover.png)"
            "}"
            )

        
        # Menu
        # mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu("File")
        # brushMenu = mainMenu.addMenu("Brush Size")
        # brushColor = mainMenu.addMenu("Brush Color")

        # Actions
        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        # fileMenu.addAction(saveAction)
        
        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        # fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        
        # Brush Menu
        threepxAction = QAction(QIcon("icons/threepx.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        # brushMenu.addAction(threepxAction)
        
        fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        # brushMenu.addAction(fivepxAction)
        
        sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+D")
        # brushMenu.addAction(sevenpxAction)
        
        ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        # brushMenu.addAction(ninepxAction)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        # brushColor.addAction(blackAction)

        whiteAction = QAction(QIcon("icons/white.png"), "White", self)
        whiteAction.setShortcut("Ctrl+W")
        # brushColor.addAction(whiteAction)
        
        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        # brushColor.addAction(redAction)
        
        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        # brushColor.addAction(greenAction)
        
        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+y")
        # brushColor.addAction(yellowAction)


    def mousePressEvent(self,event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            print(self.lastPoint) 


    def mouseMoveEvent(self,event):
        if (event.buttons() and Qt.MouseButton.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine , Qt.PenCapStyle.RoundCap ,Qt.PenJoinStyle.RoundJoin))
            # painter.setPen(QPen(self.brushColor,self.brushSize,Qt.BrushStyle.SolidPattern SolidLine,Qt.RoundCap,Qt.RoundJoin))
            painter.drawLine(self.lastPoint,event.pos())
            self.lastPoint = event.pos()
            self.update()


    def mouseReleaseEvent(self,event):
        if event.button == Qt.MouseButton.LeftButton:
            self.drawing = False


    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        # canvasPainter.drawImage(self.rect(),self.image,self.image.rect())
        canvasPainter.drawImage(0,0,self.image)


    # Clear Event
    def clear(self,event):
        self.image.fill(QColor(23,23,23))
        self.update()

    # Clear Key Event
    def keyPressEvent(self,event):
        if event.key() == Qt.Key.Key_C:
            self.clear(event)


    def exitApplication(self):
        print("closed")
        QApplication.quit()

    # Recognize Event
    def recognize(self):
        # self.image.save("1.png")
        self.image.save("1.png")
        # image = test()
        result,wordedNumber = test()
        
        self.resultLabel.setText(str(result) + "   |   " + wordedNumber)
        self.resultLabel.setStyleSheet(
            "QLabel {"
                "font: 700 21pt 'Inter';"
                "color: rgb(50,50,50);"
                "text-align: center;"
                "letter-spacing: 3px"
            "}"
            )


        


    
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()


