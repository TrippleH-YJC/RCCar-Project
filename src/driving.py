from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
import mysql.connector
from threading import Timer, Lock
from time import sleep
import signal
import sys
from time import sleep
import datetime
from threading import Thread, Event
from ultrasonic_servo_plot_module import *

def closeDB(signal, frame):
    print("BYE")
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    cur.close()
    db.close()
    timer.cancel()
    timer2.cancel()
    sys.exit(0)


def polling():
    global cur, db, ready

    lock.acquire()
    cur.execute("select * from command order by time desc limit 1")
    for (id, time, cmd_string, arg_string, is_finish) in cur:
        if is_finish == 1: break
        ready = (cmd_string, arg_string)
        cur.execute("update command set is_finish=1 where is_finish=0")

    db.commit()
    lock.release()

    global timer
    timer = Timer(0.1, polling)
    timer.start()


def sensing():
    global cur, db


    time = datetime.datetime.now()
    num1 = 0
    num2 = 0
    num3 = 0
    meta_string = '0|0|0'
    is_finish = 0

    # print(num1, num2, num3)
    query = "insert into sensing(time, num1, num2, num3, meta_string, is_finish) values (%s, %s, %s, %s, %s, %s)"
    value = (time, num1, num2, num3, meta_string, is_finish)

    lock.acquire()
    cur.execute(query, value)
    db.commit()
    lock.release()

    global timer2
    timer2 = Timer(1, sensing)
    timer2.start()


def go():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.FORWARD)


def back():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.BACKWARD)


def stop():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.RELEASE)


def left():
    pwm.setPWM(1, 0, 288)


def mid():
    pwm.setPWM(1, 0, 363)


def right():
    pwm.setPWM(1, 0, 413)

def auto():
    th2.start()

# init
db = mysql.connector.connect("HOSTIP", user='USERNAME', password='PASSWORD', database='DBNAME',
                             auth_plugin='mysql_native_password')
cur = db.cursor()
ready = None
timer = None

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)
pwm = PWM(0x6F)
pwm.setPWMFreq(50)
timer2 = None
lock = Lock()

signal.signal(signal.SIGINT, closeDB)
polling()
sensing()

def ultrasonic_work():
    while True:
        sleep(0.1)
        sweep()

def auto_work():
    myMotor.setSpeed(45)
    myMotor.run(Raspi_MotorHAT.FORWARD)
    pwm_value = 363
    while True:
        sleep(0.3)
        if event.is_set():
            myMotor.run(Raspi_MotorHAT.RELEASE)
            return

        val = int(get_dir())
        # val = int(val)
        print("val ", val)
        if val < 0:
            val = int(val / 2 + val)

        pwm_value = val / 1 + 363

        if pwm_value < 288:
            pwm_value = 289

        if pwm_value > 413:
            pwm_value = 412

        pwm.setPWM(1, 0, int(pwm_value))



th1 = Thread(target = ultrasonic_work)
event = Event()
th2 = Thread(target = auto_work)
th1.start()

# main thread
while True:
    sleep(0.1)
    if ready == None: continue

    cmd, arg = ready
    ready = None
    if cmd == "auto": auto()
    else: event.set()

    if cmd == "go": go()
    if cmd == "back": back()
    if cmd == "stop": stop()
    if cmd == "left": left()
    if cmd == "mid": mid()
    if cmd == "right": right()

