import time, board, busio
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from scipy import ndimage
from PIL import Image
from datetime import datetime

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
mlx_shape = (24,32) # mlx90640 shape
sleeping_time = 7 # capturing interval in second

while True:
    try:
        mlx.getFrame(frame)
    except:
        print("Too high refresh rate")
    new_frame = np.rot90(np.fliplr(np.reshape(frame,(24,32)))) # the starting pixel of MLX90640 is located at the top right corner
    text_filename = datetime.now().strftime('PATH-TO-YOUR-TEXT-FOLDER/%Y-%m-%d_%H-%M-%S.txt')
    img_filename = datetime.now().strftime('PATH-TO-YOUR-IMAGE-FOLDER/%Y-%m-%d_%H-%M-%S.png')
    plt.imshow(new_frame)
    np.savetxt(text_filename, new_frame, delimiter=',')
    plt.savefig(img_filename)
    time.sleep(sleeping_time)