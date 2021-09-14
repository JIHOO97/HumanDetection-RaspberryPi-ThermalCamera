# Human Detection using Raspberry Pi and MLX90640(thermal camera)

Manually sanitizing COVID19 has been a difficult and tiring job. It takes a few hours to completely sanitize an average-sized house. The final goal of this project is to develop
an automated UV-cleaner to sanitize COVID19 automatically. Ultraviolet-C radiation not only sanitize COVID19, but it also combats virus-contaminated areas. 
However, long term exposure to UV-C radiations is expected to be harmful to people and animals. In order to minimize this unfavorable effect, peole must be detected by 
the sanitizing machine. Hence, we are going to deploy deep learning model to Raspberry Pi to control the robot system accordingly. Thermal camera(MLX90640) is used to
detect people even when there is no lights.

## Hardware
- Raspberry Pi 4 (4GB RAM is used)
- two MLX90640 (thermal camera)
- mini HDMI cable

## Raspberry Pi Setup
**Reference:** [Detect people with a RaspberryPi, a thermal camera, Platypush and Tensorflow](https://blog.platypush.tech/article/Detect-people-with-a-RaspberryPi-a-thermal-camera-Platypush-and-a-pinch-of-machine-learning)

1. Download NOOBS and set up Raspbian operating system. Follow this [link](https://www.youtube.com/watch?v=BpJCAafw2qE&t=1055s)
2. Install the required modules and setup the I2C interface to connect MLX90640
'''
# Install the dependencies
[sudo] apt-get install libi2c-dev

# Enable the I2C interface
echo dtparam=i2c_arm=on | sudo tee -a /boot/config.txt

# It's advised to configure the SPI bus baud rate to
# 400kHz to support the higher throughput of the sensor
echo dtparam=i2c1_baudrate=400000 | sudo tee -a /boot/config.txt

# A reboot is required here if you didn't have the
# options above enabled in your /boot/config.txt
[sudo] reboot

# Clone the driver's codebase
git clone https://github.com/pimoroni/mlx90640-library
cd mlx90640-library

# Compile the rawrgb example
make clean
make bcm2835
make I2C_MODE=LINUX examples/rawrgb
'''

