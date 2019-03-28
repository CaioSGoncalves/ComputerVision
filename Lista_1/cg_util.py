import cv2
import numpy as np
from matplotlib import pyplot as plt

def esc_pressed():
    key = cv2.waitKey(20) & 0xFF
    return key == 27

def plot_channels_hist(img, colors, max_value):
    ranges=[0,max_value]    
    for i,color in enumerate(colors):     
        hist = cv2.calcHist(images=[img],channels=[i],mask=None,histSize=[max_value],ranges=ranges)
        plt.plot(hist,color = color)
        plt.xlim([0,max_value])
    plt.legend(colors)
    plt.show()
