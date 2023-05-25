from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time

from gpiozero import DistanceSensor

import math

import matplotlib as plt
import numpy as np

# servo settings
mh = Raspi_MotorHAT(addr=0x6f)

servo = mh._pwm
servo.setPWMFreq(50)
NEUTRAL = 310
MOVE_RANGE = 205

# ultrasonic settings
us_in1 = 18
us_out1 = 17
us_in2 = 21
us_out2 = 20
us1 = DistanceSensor(us_in1, us_out1)
us2 = DistanceSensor(us_in2, us_out2)


# ultrasonic functions
def get_deg(step):
    return (step - NEUTRAL) / MOVE_RANGE * 90 + 90


def get_distance(repeat, deg):
    dist1 = 0.0
    dist2 = 0.0
    for it in range(repeat):
        dist1 += us1.distance
        dist2 += us2.distance
        time.sleep(0.06)
    dist1 /= repeat
    dist2 /= repeat
    deg = math.radians(deg)
    #return math.sin(deg) * dist1, - math.cos(deg) * dist1, - math.sin(deg) * dist2, math.cos(deg) * dist2, dist1, dist2
    return math.cos(deg) * dist1, math.sin(deg) * dist1, - math.cos(deg) * dist2, - math.sin(deg) * dist2, dist1, dist2


# coordinates
cords_x = np.zeros(MOVE_RANGE * 4)
cords_y = np.zeros(MOVE_RANGE * 4)
dist = np.zeros(MOVE_RANGE * 4)


# coordinating functions
def get_cord(step):
    repeats = 1
    servo.setPWM(0, 0, step)
    return get_distance(repeats, get_deg(step))


def sweep():
    steps = 5
    start = NEUTRAL - MOVE_RANGE
    bias = MOVE_RANGE * 2
    for it in range(start, start + bias, steps):
        x1, y1, x2, y2, d1, d2 = get_cord(it)
        cords_x[it - start] = x1
        cords_y[it - start] = y1
        cords_x[it - start + bias] = x2
        cords_y[it - start + bias] = y2
        dist[it - start] = d1
        dist[it - start + bias] = d2
    for it in range(start + bias - 1, start - 1, - steps):
        x1, y1, x2, y2, d1, d2 = get_cord(it)
        cords_x[it - start] = x1
        cords_y[it - start] = y1
        cords_x[it - start + bias] = x2
        cords_y[it - start + bias] = y2
        dist[it - start] = d1
        dist[it - start + bias] = d2
    for it in range(0, MOVE_RANGE * 4, 10):
        print(it, dist[it])

# routing
def get_dir_old():
    bias = MOVE_RANGE
    window_shift = 25
    left = int(bias - MOVE_RANGE / 2 + window_shift)
    right = int(bias + MOVE_RANGE / 2 + window_shift)
    part_sum = 0
    max_sum = 0
    interval = int(MOVE_RANGE / 4)
    max_dir = left
    for it in range(left, left + interval):
        part_sum += dist[it] * dist[it]
    max_sum = part_sum
    print("left+interval", left + interval, "right", right + 1)
    for it in range(left + interval, right + 1):
        part_sum += dist[it] * dist[it] - dist[it - interval] * dist[it - interval]
        print("sum:", max_sum, part_sum)
        if max_sum < part_sum:
            print("changed:", it - interval + 1)
            max_sum = part_sum
            max_dir = it - interval + 1
    shift = 0 # 보정값
    strength = 0.4
    return - (max_dir + int(interval / 2) - bias + shift) * strength

def get_dir():
    window_shift = 25
    bias = MOVE_RANGE + window_shift
    left = int(bias - MOVE_RANGE + window_shift)
    right = int(bias + MOVE_RANGE)
    add_dir = 0
    add_value = 0
    for it in range(left, right + 1):
        powed = pow(dist[it] * 2, 4)
        add_dir += it * powed
        add_value += powed
    shift = 0 # 보정값
    strength = 1.8
    return - (add_dir / add_value - bias + shift) * strength

# ploting
# test
# sweep()
