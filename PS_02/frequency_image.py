import cv2
import numpy as np
from matplotlib import pyplot as plt

class Frequency_Image:

    fourier = None
    fourier_shift = None
    fourier_inverse = None
    img_spectrum = None
    img_back = None
    magnitude = None
    phase = None

    def __init__(self, img):
        self.fourier_transform(img)
        self.init_magnitude_phase()
        self.calculate_spectrum()
        self.inverse_fourier_transform()

    def init_magnitude_phase(self):
        plane = cv2.split(self.fourier_shift)
        self.magnitude, self.phase = cv2.cartToPolar(plane[0], plane[1])

    def update_magnitude_phase(self, magnitude=None, phase=None):
        if magnitude is not None:
            self.magnitude = magnitude
        if phase is not None:
            self.phase = phase
        self.calculate_spectrum()
        self.inverse_fourier_transform()

    def calculate_spectrum(self):
        self.img_spectrum = 20*np.log(self.magnitude)

    def get_magnitude_phase(self):
        return self.magnitude, self.phase

    def fourier_transform(self, img):
        self.fourier = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
        self.fourier_shift = np.fft.fftshift(self.fourier)

    def inverse_fourier_transform(self):
        plane = cv2.polarToCart(self.magnitude, self.phase)
        fourier = cv2.merge(plane)
        fourier_inv_shift = np.fft.ifftshift(fourier)
        img_back = cv2.idft(fourier_inv_shift)    
        new_plane = cv2.split(img_back)
        self.img_back = cv2.magnitude(new_plane[0],new_plane[1])

    def img_back_show(self, title='Image Back'):
        plt.figure(title)
        plt.title(title)
        plt.imshow(self.img_back, cmap = 'gray')

    