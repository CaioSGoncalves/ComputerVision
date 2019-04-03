import cv2
import numpy as np
from cg_util import calculate_image_measures

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

    def draw_retangle(self, color, line_width=0):        
        cv2.rectangle(self.image,self.top_left,self.bottom_right,color,line_width)

    def put_informations(self, color):
        self.put_cordinates(color)
        self.put_rgb_values(color)
        self.put_mean_std(color)

    def put_cordinates(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Cordinates ({0}, {1})".format(self.x_center, self.y_center)
        cordinate = (self.x_center-(120),self.y_center-(self.height+4))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def put_rgb_values(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "RGB: ({0}, {1}, {2})".format(self.center_pixel[2],self.center_pixel[1],self.center_pixel[0])
        text += "  Intensity {0:.2f}".format(sum(self.center_pixel)/len(self.center_pixel))
        cordinate = (self.x_center-(120),self.y_center+(self.height+16))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def put_mean_std(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        w_mean,w_std,_ = calculate_image_measures(self.values)
        text = "W-Mean: {0:.2f} W-Std: {1:.2f}".format(w_mean, w_std) + " W-Shape: {0}".format(self.values.shape)
        cordinate = (self.x_center-(120),self.y_center+(self.height+32))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def show_window(self, window_name="Window", size=(200,200)):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, size[0], size[1])
        cv2.imshow(window_name, self.values)

    def it_fits(self):
        window_shape = self.values.shape[:2]
        x_len_fits = window_shape[0] == self.width
        y_len_fits = window_shape[1] == self.height
        return x_len_fits and y_len_fits

        