import numpy as np
import argparse
import cv2

T = 250

original = cv2.imread("images/formas.jpg")
image = cv2.imread("images/formas.jpg", 0);
J = image.copy()

height, width = image.shape

for x in range(0, width):
    for y in range(0, height):
    	if J[y,x] < T:
    		J[y,x] = 0
    	else:
    		J[y,x] = 255

ret, thresh = cv2.threshold(J, 0, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

components = len(contours) - 1

print("Total area: {}".format(height*width))
print("Number of black components: {}\n".format(components))

for i in range(components): 
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if area > 1000:
        perimeter = cv2.arcLength(cnt,True)
        print("Componente {}: ".format(i+1))
        print("Area: {}".format(area))
        print("Perimetro: {}\n".format(perimeter))

cv2.imshow("Image", original)
cv2.imshow("Binary Image", J)

while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   