import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def get_first_order_derivative(gray):
    scale = 1
    delta = 0
    ddepth = cv.CV_64F
    # ddepth = cv.CV_64F
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad

def get_second_order_derivative(gray):
    laplacian = cv.Laplacian(gray,cv.CV_64F)
    return cv.convertScaleAbs(laplacian)

def get_my_edge_detector(gray):
    first = get_first_order_derivative(gray)
    second = get_second_order_derivative(gray)
    edge_image_sum = cv.addWeighted(first, 0.5, second, 0.5, 0)
    edge_image_mult = cv.multiply(first, second)
    return edge_image_sum, edge_image_mult

def main(path):
    src = cv.imread(path, cv.IMREAD_COLOR)
    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    first = get_first_order_derivative(gray)
    second = get_second_order_derivative(gray)
    edge_image_sum, edge_image_mult = get_my_edge_detector(gray)

    cv.imshow("Gray Image", gray)
    cv.imshow("First Derivative Image", first)
    cv.imshow("Second Derivative Image", second)
    cv.imshow("Sum Edge Detector Image", edge_image_sum)
    cv.imshow("Multiply Edge Detector Image", edge_image_mult)

    while(1):
        key = cv.waitKey(20) & 0xFF 
        if key == 27:
            break          
    cv.destroyAllWindows()
    
    return 0
    
if __name__ == "__main__":
    # main("images/noisy2.jpg")
    main("images/foto.png")