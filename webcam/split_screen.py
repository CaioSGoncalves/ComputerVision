import cv2
import numpy as np
from window import Window
import constants as const

class Split_Screen:

    width = None
    height = None
    center = None
    left = None
    right = None
    window_center = None
    window_left = None 
    window_right = None  

    def __init__(self, cap):    
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        self.width = int(size[0]/3)
        self.height = int(size[1])

        x_center = int(size[0]/2)
        y_center = int(size[1]/2)

        self.center = ( x_center, y_center )
        self.left = ( x_center - self.width, y_center )
        self.right = ( x_center + self.width, y_center )

    def load_windows(self, img):
        self.window_center = Window(img, self.center[0], self.center[1], self.width, self.height)
        self.window_left = Window(img, self.left[0], self.left[1], self.width, self.height)
        self.window_right = Window(img, self.right[0], self.right[1], self.width, self.height)

    def draw_retangles(self, line_width=3):
        self.window_center.draw_retangle(const.red_color, line_width)
        self.window_left.draw_retangle(const.blue_color, line_width)
        self.window_right.draw_retangle(const.green_color, line_width)

    def show_windows(self, size=(500, 500)):
        self.window_center.show_window("Center Window", size)
        self.window_left.show_window("Left Window", size)
        self.window_right.show_window("Right Window", size)

    def object_in_windows(self, x):
        if (x < self.window_left.x_range[1]):
            print('left')
        elif (x < self.window_center.x_range[1]):
            print('center')
        elif (x < self.window_right.x_range[1]):
            print('right')

            