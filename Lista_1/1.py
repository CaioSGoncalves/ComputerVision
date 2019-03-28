import cv2
import numpy as np
from matplotlib import pyplot as plt

red_color = (0,0,255)
white_color = (255,255,255)
window_len = 11

def exercise_1():
    cv2.imshow("Exercise 1.1", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def exercise_2():
    colors = ('b','g','r')
    max_value = 256
    ranges=[0,max_value]
    plt.title("Exercise 1.2")    
    for i,color in enumerate(colors):
        hist = cv2.calcHist(images=[img],channels=[i],mask=None,histSize=[max_value],ranges=ranges)
        plt.plot(hist,color = color)
        plt.xlim([0,max_value])
    plt.legend(colors)
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
        draw_window_retangle(img,x,y,window_len)
        put_cordinates(img,x,y,window_len)
        put_bgr_values(img,x,y,window_len)
        put_mean_std(img,x,y,window_len)
        cv2.imshow("Exercise 1.3", img)

def get_window_cordinates(x,y,length):
    x1 = x - length
    x2 = x + length
    y1 = y - length
    y2 = y + length
    return x1,x2,y1,y2

def draw_window_retangle(img, x,y,length):
    x1,x2,y1,y2 = get_window_cordinates(x,y,length)
    top_left = (x1,y1)
    bottom_right = (x2,y2)    
    cv2.rectangle(img,top_left,bottom_right,red_color,0)

def get_window_values(img, x,y,length):
    x1,x2,y1,y2 = get_window_cordinates(x,y,length)
    return img[y1:y2+1,x1:x2+1]

def put_cordinates(img, x,y,length):
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Cordinates ({0}, {1})".format(x, y)
    cordinate = (x-(120),y-(window_len+4))
    cv2.putText(img,text,cordinate,font,0.5,white_color,1,cv2.LINE_AA)

def put_bgr_values(img, x,y,length):
    font = cv2.FONT_HERSHEY_SIMPLEX
    pixel = img[y,x]
    text = "RGB: ({0}, {1}, {2})".format(pixel[2],pixel[1],pixel[0]) + "  Intensity {0:.2f}".format(sum(pixel)/len(pixel))
    cordinate = (x-(120),y+(window_len+16))
    cv2.putText(img,text,cordinate,font,0.5,white_color,1,cv2.LINE_AA)

def put_mean_std(img, x,y,length):
    font = cv2.FONT_HERSHEY_SIMPLEX
    window = get_window_values(img, x,y,length)
    w_std = np.std(window)
    w_mean = np.mean(window)
    text = "W-Mean: {0:.2f} W-Std: {1:.2f}".format(w_mean, w_std) + " W-Shape: {0}".format(window.shape)
    cordinate = (x-(120),y+(window_len+32))
    cv2.putText(img,text,cordinate,font,0.5,white_color,1,cv2.LINE_AA)

def clean_image():
    global img
    img = default_img.copy()

def main():
    global default_img
    default_img = cv2.imread("images/guardians1.png")
    clean_image()
    # exercise_1()
    # exercise_2()
    exercise_3()

if __name__ == "__main__":
    main()
