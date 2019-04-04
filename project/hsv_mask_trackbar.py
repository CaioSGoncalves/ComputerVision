import numpy as np
import cv2
from cg_util import esc_pressed

def nothing(x):
    pass

cv2.namedWindow('MASK')
cap = cv2.VideoCapture(0)

red_lower = (20, 53, 57)
red_upper = (32, 255, 198)

cv2.createTrackbar('H-MIN','MASK',0,255,nothing)
cv2.createTrackbar('H-MAX','MASK',0,255,nothing)

cv2.createTrackbar('S-MIN','MASK',0,255,nothing)
cv2.createTrackbar('S-MAX','MASK',0,255,nothing)

cv2.createTrackbar('V-MIN','MASK',0,255,nothing)
cv2.createTrackbar('V-MAX','MASK',0,255,nothing)

while(True):
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    red_lower = (cv2.getTrackbarPos('H-MIN','MASK'), cv2.getTrackbarPos('S-MIN','MASK'), cv2.getTrackbarPos('V-MIN','MASK'))
    red_upper = (cv2.getTrackbarPos('H-MAX','MASK'), cv2.getTrackbarPos('S-MAX','MASK'), cv2.getTrackbarPos('V-MAX','MASK'))


    mask = cv2.inRange(hsv_frame, red_lower, red_upper)
    
    cv2.imshow('MASK', mask)

    if esc_pressed(cv2.waitKey(1)):
        break

cap.release()
cv2.destroyAllWindows()