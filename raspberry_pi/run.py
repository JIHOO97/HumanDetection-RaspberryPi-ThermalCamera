import time, board, busio
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import adafruit_bitbangio as bitbangio
from scipy import ndimage
from PIL import Image
from datetime import datetime

# Change the address if there are multiple thermal cameras connected
SCL = board.D24 # GPIO24
SDA = board.D23 # GPIO23
i2c = bitbangio.I2C(SCL, SDA) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_1_HZ # set refresh rate
mlx_shape = (24,32) # mlx90640 shape

model = tf.keras.models.load_model('PATH-TO-YOUR-MODEL') # load your model
frame = np.zeros(mlx_shape[0]*mlx_shape[1]) # 768 pts

def predict(frame, idx):
    mlx.getFrame(frame)
    new_frame = np.rot90(np.fliplr(np.reshape(frame,(24,32)))) # the shape and rotation should be consistent
    new_frame = np.reshape(new_frame,(1,32,24,1)) # reshape to fit the model
    print(new_frame.shape)
    predicted = list(model.predict(new_frame)) # get prediction
    if predicted[0][0] > predicted[0][1]:
        print(f'{idx}: negative')
    else:
        print(f'{idx}: positive')

