import cv2
import numpy as np
from random import uniform, randint


def detect_lines1(img, edges, min_n_points):
    lines = cv2.HoughLines(edges,1,np.pi/180,min_n_points)
    if lines is None:
        return img
    new_img = img.copy()
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(new_img,(x1,y1),(x2,y2),(0,0,255),2)
    return new_img

def detect_lines2(img, edges, min_n_points, minLineLength):
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,min_n_points,minLineLength,maxLineGap)
    if lines is None:
        return img
    new_img = img.copy()
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(new_img,(x1,y1),(x2,y2),(0,255,0),2)
    return new_img

def detect_lines_images(img, edges, min_n_points, minLineLength):
    return detect_lines1(img, edges, min_n_points), detect_lines2(img, edges, min_n_points, minLineLength)

def get_equation():
    m = uniform(0,2)
    c = uniform(-2,2)
    return m, c

def get_equation_value(m, x, c):
    y = m*x + c
    return int(y)

def draw_lines(img, line_length, density):
    m, c = get_equation()
    n = randint(0, img.shape[0]-line_length)

    for i in range(n, n + line_length):
        y = get_equation_value(m, i, c)
        if y < img.shape[1]:
            # img[i,y] = 1
            for _ in range(density):
                near_y = y + randint(-5,5)
                if near_y < img.shape[1]:
                    img[i,near_y] = 1

def generate_image(n_lines, line_length, density):
    img = np.zeros((600,600,3), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rand = randint(0,20)
            if rand is 5:
                img[i,j] = 1    
            else:
                img[i,j] = 255
    for i in range(n_lines):
        draw_lines(img, line_length, density)
    return img


# img = cv2.imread('images/kitchen.jpg')

img = generate_image(1, 300, 100)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

# lines1, lines2 = detect_lines_images(img, edges, min_n_points=165, minLineLength=100)
# lines1, lines2 = detect_lines_images(img, edges, min_n_points=300, minLineLength=300)

lines2 = detect_lines2(img, edges, 300, 100)
# lines2 = detect_lines1(img, edges, 300)

cv2.namedWindow('Orignal Image',cv2.WINDOW_NORMAL)
# cv2.namedWindow('Lines 1 Image',cv2.WINDOW_NORMAL)
cv2.namedWindow('Lines 2 Image',cv2.WINDOW_NORMAL)

cv2.resizeWindow('Orignal Image', 800,800)
# cv2.resizeWindow('Lines 1 Image', 600,600)
cv2.resizeWindow('Lines 2 Image', 800,800)

cv2.imshow('Orignal Image', gray)
# cv2.imshow('Lines 1 Image', lines1)
cv2.imshow('Lines 2 Image', lines2)


while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   