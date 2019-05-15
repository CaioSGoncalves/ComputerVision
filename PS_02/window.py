import cv2
import numpy as np
from frequency_image import Frequency_Image

class Window:

    x_center = None
    y_center = None
    height = None
    width = None
    top_left = None
    bottom_right = None
    image = None
    values = None
    center_pixel = None
    x_range = None
    y_range = None   

    def __init__(self, img, x, y, width, height):    
        self.x_center = x
        self.y_center = y
        self.width = width
        self.height = height
        self.image = img
        self.def_cordinates_and_values()

    def def_cordinates_and_values(self):
        x1 = self.x_center - self.width//2
        x2 = self.x_center + self.width//2
        y1 = self.y_center - self.height//2
        y2 = self.y_center + self.height//2
        self.top_left = (x1,y1)
        self.bottom_right = (x2,y2)
        self.x_range = (x1, x2)
        self.y_range = (y1, y2)
        self.def_values(x1, x2, y1, y2)

    def def_values(self, x1, x2, y1, y2):
        self.values = self.image[y1:y2+1,x1:x2+1]
        self.center_pixel = self.image[self.y_center,self.x_center]

    def draw_retangle(self, color, line_width=1):        
        cv2.rectangle(self.image,self.top_left,self.bottom_right,color,line_width)

    def show_window(self, window_name="Window", size=(200,200)):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, size[0], size[1])
        cv2.imshow(window_name, self.values)
        cv2.resizeWindow(window_name,400,400)

    def it_fits(self):
        window_shape = self.values.shape[:2]
        x_len_fits = window_shape[0] == self.width
        y_len_fits = window_shape[1] == self.height
        return x_len_fits and y_len_fits

    def show_magnitude_window(self, window_name="Magnitude Window", size=(200,200)):
        freq_img_1 = Frequency_Image(self.values)
        magnitude_1, _ = freq_img_1.get_magnitude_phase()
        magnitude_1 = cv2.convertScaleAbs(magnitude_1)
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, size[0], size[1])
        cv2.imshow(window_name, magnitude_1)
        cv2.resizeWindow(window_name,400,400)
    
    def show_phase_window(self, window_name="Phase Window", size=(200,200)):
        freq_img_1 = Frequency_Image(self.values)
        _, phase_1 = freq_img_1.get_magnitude_phase()
        phase_1 = cv2.convertScaleAbs(phase_1)
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, size[0], size[1])
        cv2.imshow(window_name, phase_1)
        cv2.resizeWindow(window_name,400,400)

    def get_edge_map(self, gray):
        scale = 1
        delta = 0
        ddepth = cv2.CV_64F
        grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)    
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        return grad

    def show_edge_map_window(self, window_name="Edge Map Window", size=(200,200)):
        new_values = cv2.Canny(self.values,80,120)
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, size[0], size[1])
        cv2.imshow(window_name, new_values)
        cv2.resizeWindow(window_name,400,400)
        