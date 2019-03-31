import cv2
import numpy as np
from matplotlib import pyplot as plt
from video import Video

video = None

def exercise_A():
    video.read()
    video.print_info()
    video.show()
    cv2.destroyAllWindows()

def exercise_B():
    video.read()
    mean_t,std_t,var_t = video.calculate_data_measures()
    print("\nMeans Before Normalization")
    video.print_data_measures(mean_t, std_t, var_t, np.mean)
    print("\nVariance Before Normalization")
    video.print_data_measures(mean_t, std_t, var_t, np.var)
    mean_t_norm = cv2.normalize(mean_t, None)
    std_t_norm = cv2.normalize(std_t, None)
    var_t_norm = cv2.normalize(var_t, None)
    cv2.norm(mean_t_norm, mean_t, cv2.NORM_L1)
    cv2.norm(std_t_norm, std_t, cv2.NORM_L1)
    cv2.norm(var_t_norm, var_t, cv2.NORM_L1)
    print("\nMeans After Normalization")
    video.print_data_measures(mean_t_norm, std_t_norm, var_t_norm, np.mean)
    print("\nVariance After Normalization")
    video.print_data_measures(mean_t_norm, std_t_norm, var_t_norm, np.var)
    print("\nL1-Metric Mean/Std: ", cv2.norm(mean_t_norm, std_t, cv2.NORM_L1))
    print("\nL1-Metric Mean/Var: ", cv2.norm(mean_t_norm, var_t, cv2.NORM_L1))
    print("\nL1-Metric Var/Std: ", cv2.norm(var_t_norm, std_t, cv2.NORM_L1))

    plt.figure('Before Normalization')
    plt.plot(mean_t, label='Mean')
    plt.plot(var_t, label='Var')
    plt.plot(std_t, label='Std')
    plt.legend()

    plt.figure('After Normalization')
    plt.plot(mean_t_norm, label='Mean-Normalized')
    plt.plot(var_t_norm, label='Var-Normalized')
    plt.plot(std_t_norm, label='Std-Normalized')
    plt.legend()

    plt.show()

def main():
    global video
    video = Video("videos/teste.mp4")
    exercise_A()
    exercise_B()

if __name__ == "__main__":
    main()


