import cv2
import numpy as np

T = 128

def binary_image(img):
    new_img = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (new_img[i,j] > T):
                new_img[i,j] = 1
            else:
                new_img[i,j] = 255
    return new_img        


img = cv2.imread("images/foto.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new_img = binary_image(img)

cv2.imshow('Source image', img)
cv2.imshow('Binary image', new_img)

while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   