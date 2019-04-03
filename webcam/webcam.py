import numpy as np
import cv2
from cg_util import esc_pressed
from split_screen import Split_Screen
import constants as const


cap = cv2.VideoCapture(0)
split_screen = Split_Screen(cap)
face_detect = cv2.CascadeClassifier("Classifiers/haarcascade_frontalface_default.xml")

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    split_screen.load_windows(frame)
    split_screen.draw_retangles()
    split_screen.show_windows()

    faces_video = face_detect.detectMultiScale(gray, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, width, heigth) in faces_video:
        cv2.rectangle(frame, (x, y), (x + width, y + heigth), const.green_color, 2)
        split_screen.object_in_windows(x+(width//2))
    
    cv2.imshow('frame', frame)
    if esc_pressed(cv2.waitKey(1)):
        break
        
cap.release()
cv2.destroyAllWindows()


