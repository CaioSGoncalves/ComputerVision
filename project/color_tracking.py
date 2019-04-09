import numpy as np
import cv2
from cg_util import esc_pressed


def nothing(x):
    pass

cv2.namedWindow('MASK')
cap = cv2.VideoCapture(0)

red_lower = (12, 255, 0)
red_upper = (62, 255, 255)

kernel = np.ones((5,5),np.uint8)

while(True):
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, red_lower, red_upper)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        maxArea = cv2.contourArea(contours[0])
        contourId = 0
        i = 0
        for cnt in contours:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourId = i
            i += 1
        cnt = contours[contourId]
        x,y,w,h = cv2.boundingRect(cnt)
        if(maxArea > 100.0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)     

    cv2.imshow('RGB', frame)
    cv2.imshow('HSV', hsv_frame)
    cv2.imshow('MASK', mask)

    if esc_pressed(cv2.waitKey(1)):
        break

cap.release()
cv2.destroyAllWindows()