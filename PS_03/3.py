import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

original = cv2.imread('images/formas.jpg')
img = cv2.imread('images/formas.jpg', 0)
img = cv2.GaussianBlur(img, (3, 3), 0)

def binarize_image():
    for x in range (img.shape[0]):
        for y in range (img.shape[1]):
            if(img[x][y] < 250):
                img[x][y] = 255
            else:
                img[x][y] = 0

binarize_image()
binary = img.copy()

components, output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
sizes = stats[1:, -1]
components = components - 1
min_size = 1000
img_output = np.zeros((output.shape))
for i in range(components):
    if sizes[i] >= min_size:
        img_output[output == i + 1] = 255

img_output = np.uint8(img_output)
contours, _ = cv2.findContours(img_output,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_output = cv2.cvtColor(img_output,cv2.COLOR_GRAY2RGB)

for i in range(len(contours)):
    if len(contours[i]) > 4:
        ellipse = cv2.fitEllipse(contours[i])
        cv2.ellipse(img_output,ellipse,(255,0,0),2)
        (x,y),(ma,MA),angle = ellipse
        theta = (angle+90) * np.pi/180
        xa =  int(round(x + MA/2 * np.cos(theta)))
        ya =  int(round(y + MA/2 * np.sin(theta)))
        xb =  int(round(x - MA/2 * np.cos(theta)))
        yb =  int(round(y - MA/2 * np.sin(theta)))
        cv2.line(img_output, (xa,ya), (xb,yb), (0,0,255), thickness=2, lineType=8)
        cv2.circle(img_output,(int(x), int(y)), 2, (0,255,0), 3)

cv2.imshow('Original', original)
cv2.imshow('Binary', binary)
cv2.imshow('Output', img_output)

while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   