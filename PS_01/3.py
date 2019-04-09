import cv2
import numpy as np
from matplotlib import pyplot as plt
from frequency_image import Frequency_Image

def exercise_A():
    img_1 = cv2.imread('images/shot.png',0)
    img_2 = cv2.imread('images/starlord.png',0)
    img_2 = cv2.resize(img_2, (1200,600))
    print("Img_1.shape: ", img_1.shape)
    print("Img_2.shape: ", img_2.shape)

    freq_img_1 = Frequency_Image(img_1)
    freq_img_2 = Frequency_Image(img_2)

    magnitude_1, phase_1 = freq_img_1.get_magnitude_phase()
    magnitude_2, phase_2 = freq_img_2.get_magnitude_phase()

    freq_img_1.update_magnitude_phase(magnitude_1, phase_1)
    freq_img_2.update_magnitude_phase(magnitude_2, phase_2)

    img_back_1 = freq_img_1.img_back
    img_back_2 = freq_img_2.img_back

    plt.figure('Image 1')
    plt.title('Image 1')
    plt.imshow(img_1, cmap = 'gray')

    # plt.figure('Magnitude Spectrum 1')
    # plt.title('Magnitude Spectrum 1')
    # plt.imshow(freq_img_1.img_spectrum, cmap = 'gray')

    plt.figure('First Rebuild Image')
    plt.title('First Rebuild Image')
    plt.imshow(img_back_1, cmap = 'gray')

    plt.figure('Image 2')
    plt.title('Image 2')
    plt.imshow(img_2, cmap = 'gray')

    # plt.figure('Magnitude Spectrum 2')
    # plt.title('Magnitude Spectrum 2')
    # plt.imshow(freq_img_2.img_spectrum, cmap = 'gray')

    plt.figure('Second Rebuild Image')
    plt.title('Second Rebuild Image')
    plt.imshow(img_back_2, cmap = 'gray')

    plt.show()

def exercise_B():
    img = cv2.imread('images/guardians1.png',0)
    cv2.imshow("Exercise 3.B", img)
    transform_images_magnitude_phase_mean(img)


def transform_images_magnitude_phase_mean(img):
    freq_img = Frequency_Image(img)
    magnitude, phase = freq_img.get_magnitude_phase()

    const = 100
    const2 = 1000

    magnitude[:] = np.mean(magnitude)
    freq_img.update_magnitude_phase(magnitude=magnitude)
    img_back = freq_img.img_back
    freq_img.img_back_show('Exercise - Magnitude = Mean')

    freq_img.init_magnitude_phase()

    phase[:] = np.mean(phase)
    freq_img.update_magnitude_phase(phase=phase)
    img_back = freq_img.img_back
    freq_img.img_back_show('Exercise - Phase = Mean')

    plt.show()

    cv2.waitKey()

def exercise_C():
    img = cv2.imread('images/foto.png',0)
    cv2.imshow("Exercise 3.C", img)
    transform_images_magnitude_phase_mean(img)


def main():
    exercise_A()
    exercise_B()
    exercise_C()

if __name__ == "__main__":
    main()

    