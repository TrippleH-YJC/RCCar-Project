from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from UI import Ui_MainWindow
import mysql.connector
import sys
import cv2
import time

class myapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)

        self.db = mysql.connector.connect("HOSTIP", user='USERNAME', password='PASSWORD', database='DBNAME',
                             auth_plugin='mysql_native_password')
        self.cur = self.db.cursor()
        self.cur.execute('delete from command where is_finish=1')

        time = QDateTime().currentDateTime().toPython()

        # timer setting
        self.timer = QTimer()
        self.timer.setInterval(500)  # 500ms
        self.timer.timeout.connect(self.pollingQuery)

        self.th.start()

    def setImage(self, img):
        self.ui.image_label.setPixmap(img)
    
    # DB
    def insertCommand(self, cmd_string, arg_string):
        time = QDateTime().currentDateTime().toPython()
        is_finish = 0

        query = "insert into command(time, cmd_string, arg_string, is_finish) values (%s, %s, %s, %s)"
        value = (time, cmd_string, arg_string, is_finish)

        self.cur.execute(query, value)
        self.db.commit()

    def start(self):
        self.timer.start()

    def go(self):
        self.insertCommand("go", "0")

    def stop(self):
        self.insertCommand("stop", "0")

    def back(self):
        self.insertCommand("back", "0")

    def left(self):
        self.insertCommand("left", "0")

    def mid(self):
        self.insertCommand("mid", "0")

    def right(self):
        self.insertCommand("right", "0")

    def auto(self):
        self.insertCommand("auto", "0")

    def pollingQuery(self):
        self.cur.execute('delete from command where is_finish=1')

        self.cur.execute("select * from command order by time desc limit 15")
        self.ui.logText.clear()
        for (id, time, cmd_string, arg_string, is_finish) in self.cur:
            str = "%d | %s | %6s | %6s | %4d" % (
            id, time.strftime("%Y%m%d %H:%M:%S"), cmd_string, arg_string, is_finish)
            self.ui.logText.appendPlainText(str)

        self.cur.execute("select * from sensing order by time desc limit 15")
        self.ui.sensingText.clear()
        for (id, time, num1, num2, num3, meta_string, is_finish) in self.cur:
            str = "%d | %s | %6s | %6s | %6s | %10s | %4d" % (
            id, time.strftime("%Y%m%d %H:%M:%S"), num1, num2, num3, meta_string, is_finish)
            self.ui.sensingText.appendPlainText(str)
        self.db.commit()

    def closeEvent(self, event):
        self.cur.close()
        self.db.close()
        self.th.terminate()
        self.th.wait(3000)
        self.close()

class MyThread(QThread):
    mySignal = Signal(QPixmap)

    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 320)
        self.cam.set(4, 240)
        self.prev_time = 0
        self.FPS = 3

    def run(self):
        while True:
            ret, self.img = self.cam.read()
            current_time = time.time() - self.prev_time
            if ret and current_time > 1./self.FPS:
                self.prev_time = time.time()
                self.printImage(self.img)
            # sleep(0.1)
        
    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        pix_img = QPixmap(img)
        self.mySignal.emit(pix_img)

app = QApplication()
win = myapp()
win.show()
app.exec_()
