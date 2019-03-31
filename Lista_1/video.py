import cv2
import numpy as np
from cg_util import calculate_image_measures,esc_pressed

class Video:

    file_path = None
    value = None

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        video = cv2.VideoCapture(self.file_path)
        if not video.isOpened():
            raise IOError("Could not open video")
        self.value = video

    def show(self):
        while True:
            ret, frame = self.value.read()
            if ret:
                cv2.imshow("Exercise A", frame)
            key = cv2.waitKey(20)
            if esc_pressed(key):
                break
        self.value.release()

    def print_info(self):
        fps = self.value.get(cv2.CAP_PROP_FPS)
        count = self.value.get(cv2.CAP_PROP_FRAME_COUNT)
        size = (int(self.value.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.value.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print("FPS: {0:.2f}".format(fps))
        print("Number of frames: ", count)
        print("WIDTH: ", size[0])
        print("HEIGHT: ", size[1])

    def calculate_data_measures(self):
        mean_t = list()
        std_t = list()
        variance_t = list()
        while True:
            ret, frame = self.value.read()
            if ret:
                mean,std,variance = calculate_image_measures(frame)
                mean_t.append(mean)
                std_t.append(std)
                variance_t.append(variance)
            else:
                break
        self.value.release()
        return np.asarray(mean_t),np.asarray(std_t),np.asarray(variance_t)

    def print_data_measures(self, mean_t, std_t, var_t, function):
        print("Mean: ", function(mean_t))
        print("Std: ", function(std_t))     

    