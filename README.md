# RCCar Project
## 협로 주행 구현.
[현대모비스 - 협로주행](https://www.hyundai.co.kr/story/CONT0000000000016475)
<br>

## 기간
### ***2023.05.18 ~ 2023.05.25***

<br>

## Pic & Intro (자동차 사진, Intro)
![Intro](./pics/Intro.gif) <br>
![Pic1](./pics/1.jpg) <br>
![Pic2](./pics/2.jpg) <br>

## Demonstration Video(Youtube)
### Demo
[![시연 영상](http://img.youtube.com/vi/k7AG5jW5c-g/0.jpg)](https://www.youtube.com/watch?v=k7AG5jW5c-g) <br>
### Path
[![경로 촬영 영상](http://img.youtube.com/vi/eMNNFYP314Y/0.jpg)](https://www.youtube.com/watch?v=eMNNFYP314Y) <br>

## Firmware, Pakcages(Installation) Info
- rpi firmware: 6.1.25-v8+
- python: 3.9.2
- opencv : 4.7.0
- aws ec2 : ubuntu 22.04
- pyside : rpi(2), pc(6)

## Hardware Info
- rpi mode : 4B
- motor driver module : stepper Motor HAT v0.2 (UGEEK)
- servomotor(steering system part) : MG 966R
- servomotor(ultrasound part) : SG90
- ultrasound module : HC-SR04
- 30W DC-DC컨버터 : [link](https://www.amazon.com/Voltage-Supply-12V24V-Module-Charging/dp/B07WZMKD28)

## What's Missing, Limitation

## Files
remote_control.py ( import )
UI.py : Qt designer UI 

driving.py ( import )
Raspi_I2C.py  
Raspi_MotorHAT.py
Raspi_PWM_Servo_Driver.py : 3 Motor HAT Driver Library above
ultrasonic_servo_plot_module.py : ultrasound module ( user defined )

## How to Start
### UI Part
```shell
python3 remote_control.py
```
### Car Part
```shell
python3 driving.py
```

# Fin.
