import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from window import Window
from frequency_image import Frequency_Image

red_color = (0,0,255)
white_color = (255,255,255)
window_len = 33
default_img, img, edge_map = None,None, None

def main():
    cv.namedWindow('Image')
    cv.setMouseCallback('Image',draw_window)  
    cv.imshow("Image", img)  
    while(1):
        key = cv.waitKey(20) & 0xFF 
        if key == 27:
            break          
    cv.destroyAllWindows()    


def draw_window(event,x,y,flags,param):    
    if event == cv.EVENT_MOUSEMOVE:        
        clean_image()
        window = Window(img,x,y,window_len,window_len)
        if window.it_fits():
            window.draw_retangle(white_color)
            window.show_window()
            window.show_magnitude_window()
            window.show_phase_window()
            window.show_edge_map_window()
        cv.imshow("Image", img)

def clean_image():
    global img
    img = default_img.copy()

def init(image_path):
    global default_img
    global edge_map
    default_img = cv.imread(image_path)
    default_img = cv.GaussianBlur(default_img, (3, 3), 0)
    default_img = cv.cvtColor(default_img, cv.COLOR_BGR2GRAY)    
    edge_map = cv.Canny(default_img,80,120)
    cv.imshow("Edge Map", edge_map)
    clean_image()    

if __name__ == "__main__":
    # init("images/foto.png")
    init("images/noisy2.jpg")
    main()
    
