import cv2
from matplotlib import pyplot as plt
import numpy as np

def esc_pressed(key):
    key = key & 0xFF
    return key == 27

def plot_channels_hist(img, colors, max_value):
    ranges=[0,max_value]    
    for i,color in enumerate(colors):     
        hist = cv2.calcHist(images=[img],channels=[i],mask=None,histSize=[max_value],ranges=ranges)
        plt.plot(hist,color = color)
        plt.xlim([0,max_value])
    plt.legend(colors)
    plt.show()

def calculate_image_measures(image):
    mean = np.mean(image)
    std = np.std(image)
    variance = np.var(image)
    return mean,std,variance
    
    