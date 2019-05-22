import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from matplotlib import pyplot as plt

def smooth_image(gray):
    return cv2.blur(gray,(3,3))
    # return cv2.medianBlur(img,5)

def calculate_coocc(img):
    # coocc = img.T.dot(img)
    coocc = greycomatrix(img, [1], [0], 256, symmetric=True, normed=True)
    return coocc[:, :, 0, 0]

def calculate_uniformity(coocc):
    return True

def calculate_homogeneity(coocc):
    return True

img = cv2.imread("images/foto.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

s = list()
r = list()

smooth = smooth_image(gray)


s.append(smooth)
residual = gray - smooth
r.append(residual)

for _ in range(30):
    smooth = smooth_image(smooth)
    s.append(smooth)
    residual = gray - smooth
    r.append(residual)

gray_coocc = calculate_coocc(gray)
T = gray_coocc.sum()

print(gray.shape)
print(gray_coocc.shape)
print(gray_coocc)

# s_coocc = list()
# r_coocc = list()
# for n in range(len(s)):
#     s_coocc.append(calculate_coocc(s[n]))
#     r_coocc.append(calculate_coocc(r[n]))

# s_homogeneity = list()
# r_homogeneity = list()
# s_uniformity = list()
# r_uniformity = list()

# for n in range(len(s_coocc)):
#     s_homogeneity.append(calculate_homogeneity(s_coocc[n]) / T)
#     r_homogeneity.append(calculate_homogeneity(r_coocc[n]) / T)

#     s_uniformity.append(calculate_uniformity(s_coocc[n]) / T)
#     r_uniformity.append(calculate_uniformity(r_coocc[n]) / T)

# plt.figure('Homogeneity')
# plt.plot(s_homogeneity, label='S')
# plt.plot(r_homogeneity, label='R')
# plt.legend()

# plt.figure('Uniformity')
# plt.plot(s_uniformity, label='S')
# plt.plot(r_uniformity, label='R')
# plt.legend()





# cv2.imshow('Original Image', gray)
# cv2.imshow('Smooth Image', smooth)
# cv2.imshow('Residual Image', residual)

# while(1):
# 	key = cv2.waitKey(20) & 0xFF 
# 	if key == 27:
# 		break   
