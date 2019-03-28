import cv2
import numpy as np

class Window:

    x_center = None
    y_center = None
    length = None
    top_left = None
    bottom_right = None
    image = None
    values = None
    center_pixel = None   

    def __init__(self, img, x, y, length):    
        self.x_center = x
        self.y_center = y
        self.length = length
        self.image = img
        self.def_cordinates_and_values()

    def def_cordinates_and_values(self):
        x1 = self.x_center - self.length
        x2 = self.x_center + self.length
        y1 = self.y_center - self.length
        y2 = self.y_center + self.length
        self.top_left = (x1,y1)
        self.bottom_right = (x2,y2)
        self.def_values(x1, x2, y1, y2)

    def def_values(self, x1, x2, y1, y2):
        self.values = self.image[y1:y2+1,x1:x2+1]
        self.center_pixel = self.image[self.y_center,self.x_center]

    def draw_retangle(self, color):        
        cv2.rectangle(self.image,self.top_left,self.bottom_right,color,0)

    def put_informations(self, color):
        self.put_cordinates(color)
        self.put_rgb_values(color)
        self.put_mean_std(color)

    def put_cordinates(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Cordinates ({0}, {1})".format(self.x_center, self.y_center)
        cordinate = (self.x_center-(120),self.y_center-(self.length+4))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def put_rgb_values(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "RGB: ({0}, {1}, {2})".format(self.center_pixel[2],self.center_pixel[1],self.center_pixel[0])
        text += "  Intensity {0:.2f}".format(sum(self.center_pixel)/len(self.center_pixel))
        cordinate = (self.x_center-(120),self.y_center+(self.length+16))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def put_mean_std(self, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        w_std = np.std(self.values)
        w_mean = np.mean(self.values)
        text = "W-Mean: {0:.2f} W-Std: {1:.2f}".format(w_mean, w_std) + " W-Shape: {0}".format(self.values.shape)
        cordinate = (self.x_center-(120),self.y_center+(self.length+32))
        cv2.putText(self.image,text,cordinate,font,0.5,color,1,cv2.LINE_AA)

    def draw_new_frame(self):
        cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Window', 200,200)
        cv2.imshow("Window", self.values)

    def it_fits(self):
        window_shape = self.values.shape[:2]
        x_len_fits = window_shape[0] == 2*self.length + 1
        y_len_fits = window_shape[1] == 2*self.length + 1
        return x_len_fits and y_len_fits