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

def get_equation():
    m = uniform(-2,2)
    c = uniform(-2,2)
    return m, c

def get_equation_value(m, x, c):
    y = m*x + c
    return int(y)

def draw_line(img, line_length, density, noisy_img):
    m, c = get_equation()
    n = randint(0, img.shape[1]-line_length)

    for i in range(n, n + line_length):
        y = get_equation_value(m, i, c)
        if y < img.shape[0] and y > 0:
            img[y,i] = 1
            for _ in range(density):
                near_y = y + randint(-5,5)
                if abs(near_y) < img.shape[0]:
                    noisy_img[near_y, i] = 1
        else:
            return False
    return True

def generate_image(n_lines, line_length, density, noisy):
    img = np.zeros((600,800,3), np.uint8)
    noisy_img = img.copy()
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            rand = randint(0,noisy)
            if rand is 0:
                noisy_img[j,i] = 1    
            else:
                noisy_img[j,i] = 255
            img[j,i] = 255
    for i in range(n_lines):
        copy_img = img.copy()
        copy_noisy_img = noisy_img.copy()
        line_ok = draw_line(img, line_length, density, noisy_img)
        while(line_ok is False):
            img = copy_img.copy()
            noisy_img = copy_noisy_img.copy()
            line_ok = draw_line(img, line_length, density, noisy_img)
            
    return img, noisy_img


d = 150
# line_length = 200

img, noisy_img = generate_image(n_lines=10, line_length=300, density=5, noisy=20)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines_img = detect_lines1(img, edges, d)
# lines_img = detect_lines2(img, edges, d, line_length)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines_noisy_img = detect_lines1(noisy_img, edges, d)
# lines_noisy_img = detect_lines2(noisy_img, edges, d, line_length)

cv2.namedWindow('True Line Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('True Line Image',800,800)
cv2.imshow('True Line Image', img)

cv2.namedWindow('Detection True Line Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detection True Line Image',800,800)
cv2.imshow('Detection True Line Image', lines_img)

cv2.namedWindow('Noisy Line Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Noisy Line Image', 800,800)
cv2.imshow('Noisy Line Image', noisy_img)

cv2.namedWindow('Detection Noisy Line Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detection Noisy Line Image', 800,800)
cv2.imshow('Detection Noisy Line Image', lines_noisy_img)







while(1):
	key = cv2.waitKey(20) & 0xFF 
	if key == 27:
		break   