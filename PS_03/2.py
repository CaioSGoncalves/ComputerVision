import cv2
import numpy as np

img = cv2.imread("images/foto.png")
blur = cv2.blur(img,(3,3))


cv2.imshow('Original Image', img)
cv2.imshow('Blur Image', blur)


while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   
