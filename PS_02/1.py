import cv2
import numpy as np
from matplotlib import pyplot as plt

def plot_histogram(hist):
	plt.plot(hist)
	plt.xlim([0,255])
	plt.show()

def calculate_relative_hist(img, r=1):
	m, n = img.shape
	hist = cv2.calcHist(images=[img], channels=[0], mask=None,histSize=[256],ranges=[0,255])
	relative_hist = hist / (m * n)
	return relative_hist ** r

def calculate_g_equal(relative_hist, Q):
	g_equal = np.zeros(256)
	G_MAX = 255
	for i in range(256):
		soma = 0
		for j in range(i+1):
			soma += relative_hist[j]
		g_equal[i] = (G_MAX/Q) * soma
	return g_equal

def equalize(img, g_equal):
	n, m = img.shape
	new_img = np.zeros(img.shape)
	for i in range(n):
		for j in range(m):
			value = img[i,j]
			new_img[i,j] = g_equal[value]
	return new_img

def equalize_image(img, r=1):
	relative_hist = calculate_relative_hist(img, r)
	Q = relative_hist.sum()
	g_equal = calculate_g_equal(relative_hist, Q)
	new_img = equalize(img, g_equal)
	return new_img

def plot_results(img, n):
	original_mean = np.mean(img)
	mean = list()
	for r in range(n):
		new_img = equalize_image(img, r)
		mean.append(np.mean(new_img))	
	plt.plot(mean)
	plt.xlabel('r')
	plt.ylabel('Mean of Values')
	plt.hlines(original_mean, xmin=0, xmax=n)
	# plt.xlim([0,255])
	plt.show()

img_path = "images/noisy2.jpg"
img = cv2.imread("images/noisy.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plot_results(img,5)

# new_img = equalize_image(img, r=100)
# cv2.imshow('Source image', img)
# cv2.imshow('Equalized image', new_img)

cv2.waitKey()
cv2.destroyAllWindows()