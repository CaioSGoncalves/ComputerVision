import cv2
import numpy as np
from matplotlib import pyplot as plt
from window import Window
from cg_util import plot_channels_hist

red_color = (0,0,255)
white_color = (255,255,255)
window_len = 5

def exercise_1():
    cv2.imshow("Exercise 1.1", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def exercise_2():
    colors = ('b','g','r')
    # colors = ('g')
    max_value = 256
    plt.title("Exercise 1.2") 
    plot_channels_hist(img, colors, max_value)
    plt.show()

def exercise_3():
    cv2.namedWindow('Exercise 1.3')
    cv2.setMouseCallback('Exercise 1.3',draw_window)  
    cv2.imshow("Exercise 1.3", img)  
    while(1):
        key = cv2.waitKey(20) & 0xFF  
        if key == 27:
            break
    cv2.destroyAllWindows()    

def draw_window(event,x,y,flags,param):    
    if event == cv2.EVENT_MOUSEMOVE:        
        clean_image()
        window = Window(img,x,y,window_len)
        if window.it_fits():
            window.draw_retangle(red_color)
            window.put_informations(white_color)
            window.draw_new_frame()
        cv2.imshow("Exercise 1.3", img)

def clean_image():
    global img
    img = default_img.copy()

def main():
    global default_img
    default_img = cv2.imread("images/guardians1.png")
    clean_image()
    exercise_1()
    exercise_2()
    exercise_3()

if __name__ == "__main__":
    main()
