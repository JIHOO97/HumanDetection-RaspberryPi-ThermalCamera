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
```
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
```
3. Install platypush python dependencies for tensorflow and MLX90640
```
[sudo] pip install 'platypush[tensorflow,mlx90640]'
```
4. Install additional dependencies and libraries
```
[sudo] apt-get install python3-numpy \
  libatlas-base-dev \
  libblas-dev \
  liblapack-dev \
  python3-dev \
  gfortran \
  python3-setuptools \
  python3-scipy \
  python3-h5py
```

```
# For image manipulation
[sudo] pip install opencv

# Install Jupyter notebook to run the training code
[sudo] pip install jupyterlab
# Then follow the instructions at https://jupyter.org/install

# Tensorflow framework for machine learning and utilities
[sudo] pip install tensorflow numpy matplotlib

# Clone my repository with the image and training utilities
# and the Jupyter notebooks that we'll use for training.
git clone https://github.com/BlackLight/imgdetect-utils ~/projects/imgdetect-utils
```

## Data collection
**File name:** capture.py

This file is to capture an image using MLX90640 in 3 seconds interval. 
**1,020** positive images and **921** negative images were collected, where positive means presence of a person and negative means an absence.

## Labelling
**File name:** label.py

This file is to label the collected images to either positive or negative.
Positive and negative images were splitted and stored in separate folders.

## Training and Save the model
**File name:** train.py

Layers | Activation function | Loss function | Optimizer | Epochs
------------ | ------------- | ------------- | ------------- | -------------
Three fully connected layers | RELU | categorical-crossentropy | Adam | 15

**Test Accuracy:** 96.8%

## Deploy the model
**File name:** run.py

Using the model created in the previous step, we were able to detect people in real-time(5 fps).
We used multiple thermal cameras to increase the view of the robot(MLX90640 has a 110degree view)

## References
1. [Detect people with a RaspberryPi, a thermal camera, Platypush and Tensorflow](https://blog.platypush.tech/article/Detect-people-with-a-RaspberryPi-a-thermal-camera-Platypush-and-a-pinch-of-machine-learning)
2. [How to setup Raspberry Pi](https://www.youtube.com/watch?v=BpJCAafw2qE&t=1055s)
3. [High Resolution Thermal Camera with Raspberry Pi and MLX90640](https://makersportal.com/blog/2020/6/8/high-resolution-thermal-camera-with-raspberry-pi-and-mlx90640)
