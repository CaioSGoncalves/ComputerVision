import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from matplotlib import pyplot as plt


def smooth_image(gray, filter):
    if filter is 1:
        return cv2.blur(gray,(3,3))
    else:
        return cv2.medianBlur(gray,5)

def calculate_coocc(img):
    coocc = greycomatrix(img, [1], [0], np.max(img)+1, symmetric=True, normed=True)
    return coocc

def calculate_homogeneity(coocc):
    return greycoprops(coocc, 'homogeneity')[0,0]

def calculate_uniformity(coocc):
    return greycoprops(coocc, 'ASM')[0,0]

def calculate_s_r_properties(gray, filter):
    s = list()
    r = list()

    smooth = smooth_image(gray, filter)
    s.append(smooth)
    residual = gray - smooth
    r.append(residual)

    for _ in range(30):
        smooth = smooth_image(smooth, filter)
        s.append(smooth)
        residual = gray - smooth
        r.append(residual)

    gray_coocc = calculate_coocc(gray)
    T = gray_coocc.sum()

    s_coocc = list()
    r_coocc = list()
    for n in range(len(s)):
        s_coocc.append(calculate_coocc(s[n]))
        r_coocc.append(calculate_coocc(r[n]))

    s_homogeneity = list()
    r_homogeneity = list()
    s_uniformity = list()
    r_uniformity = list()

    for n in range(len(s_coocc)):
        s_homogeneity.append(calculate_homogeneity(s_coocc[n]) / T)
        r_homogeneity.append(calculate_homogeneity(r_coocc[n]) / T)

        s_uniformity.append(calculate_uniformity(s_coocc[n]) / T)
        r_uniformity.append(calculate_uniformity(r_coocc[n]) / T)
    return s_homogeneity, r_homogeneity, s_uniformity, r_uniformity


# image = cv2.imread("images/indoor.jpg")
# image = cv2.imread("images/outdoor.jpg")
image = cv2.imread("images/foto.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
s_homogeneity_box, r_homogeneity_box, s_uniformity_box, r_uniformity_box = calculate_s_r_properties(gray, 1)
s_homogeneity_median, r_homogeneity_median, s_uniformity_median, r_uniformity_median = calculate_s_r_properties(gray, 2)


plt.figure('Homogeneity')
plt.plot(s_homogeneity_box, label='S box')
plt.plot(r_homogeneity_box, label='R box')
plt.plot(s_homogeneity_median, label='S median')
plt.plot(r_homogeneity_median, label='R median')
plt.legend()

plt.figure('Uniformity')
plt.plot(s_uniformity_box, label='S box')
plt.plot(r_uniformity_box, label='R box')
plt.plot(s_homogeneity_median, label='S median')
plt.plot(r_homogeneity_median, label='R median')
plt.legend()

plt.show()





# cv2.imshow('Original Image', gray)
# cv2.imshow('Smooth Image', smooth)
# cv2.imshow('Residual Image', residual)

# while(1):
# 	key = cv2.waitKey(20) & 0xFF 
# 	if key == 27:
# 		break   
