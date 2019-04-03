import cv2
import numpy as np
from matplotlib import pyplot as plt
from window import Window
from cg_util import plot_channels_hist,esc_pressed

red_color = (0,0,255)
white_color = (255,255,255)
window_len = 11
default_img, img = None,None

def exercise_1():
    cv2.imshow("Exercise 1.1", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def exercise_2():
    colors = ('b','g','r')
    max_value = 256
    plt.title("Exercise 1.2") 
    plot_channels_hist(img, colors, max_value)
    plt.show()

def exercise_3():
    cv2.namedWindow('Exercise 1.3')
    cv2.setMouseCallback('Exercise 1.3',draw_window)  
    cv2.imshow("Exercise 1.3", img)  
    while(1):
        key = cv2.waitKey(20) 
        if esc_pressed(key):
            break
    cv2.destroyAllWindows()    

def draw_window(event,x,y,flags,param):    
    if event == cv2.EVENT_MOUSEMOVE:        
        clean_image()
        window = Window(img,x,y,window_len,window_len)
        if window.it_fits():
            window.draw_retangle(red_color)
            window.put_informations(white_color)
            window.show_window()
        cv2.imshow("Exercise 1.3", img)

def clean_image():
    global img
    img = default_img.copy()

def init(image_path):
    global default_img
    default_img = cv2.imread(image_path)
    clean_image()

def main():
    init("images/guardians1.png")
    exercise_1()
    exercise_2()
    exercise_3()

if __name__ == "__main__":
    main()

    
