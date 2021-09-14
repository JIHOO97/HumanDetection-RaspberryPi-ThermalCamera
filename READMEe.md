# Human Detection using Raspberry Pi and MLX90640(thermal camera)

Sanitizing COVID19 has been a difficult and tiring job. It takes a few hours to completely sanitize an average-sized house. The final goal of this project is to develop
an automated UV-cleaner to sanitize COVID19 automatically. Ultraviolet-C radiation not only sanitize COVID19, but it also combats virus-contaminated areas. 
However, long term exposure to UV-C radiations is expected to be harmful to people and animals. In order to minimize this unfavorable effect, peole must be detected by 
the sanitizing machine. Hence, we are going to deploy deep learning model to Raspberry Pi to control the robot system accordingly. Thermal camera(MLX90640) is used to
detect people even when there is no lights.

## Hardware
- Raspberry Pi 4
- two MLX90640 (thermal camera)
- mini HDMI cable

## Raspberry Pi Setup
**Reference:** [Detect people with a RaspberryPi, a thermal camera, Platypush and Tensorflow](https://blog.platypush.tech/article/Detect-people-with-a-RaspberryPi-a-thermal-camera-Platypush-and-a-pinch-of-machine-learning)

