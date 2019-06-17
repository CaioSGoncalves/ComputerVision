import numpy as np
from matplotlib import pyplot as plt
import cv2
from pathlib import Path
from scipy.ndimage.filters import convolve as filter2

def getimgfiles(stem):
    stem = Path(stem).expanduser()
    path = stem.parent
    name = stem.name
    exts = ['.ppm','.bmp','.png','.jpg']
    for ext in exts:
        pat = name+'.*'+ext
        print('searching {}/{}'.format(path,pat))
        flist = sorted(path.glob(pat))
        if flist:
            break

    if not flist:
        raise FileNotFoundError('no files found under {} with {}'.format(stem,exts))

    print('analyzing {} files {}.*{}'.format(len(flist),stem,ext))

    return flist,ext   

def HS(im1, im2, alpha, Niter):

	#set up initial velocities
    uInitial = np.zeros([im1.shape[0],im1.shape[1]])
    vInitial = np.zeros([im1.shape[0],im1.shape[1]])

	# Set initial value for the flow vectors
    U = uInitial
    V = vInitial

	# Estimate derivatives
    [fx, fy, ft] = computeDerivatives(im1, im2)

    # fg,ax = plt.subplots(1,3,figsize=(18,5))
    # for f,a,t in zip((fx,fy,ft),ax,('$f_x$','$f_y$','$f_t$')):
    #     h=a.imshow(f,cmap='bwr')
    #     a.set_title(t)
    #     fg.colorbar(h,ax=a)
    # plt.show()

	# Averaging kernel
    kernel=np.array([[1/12, 1/6, 1/12],
                      [1/6,    0, 1/6],
                      [1/12, 1/6, 1/12]],float)

	# Iteration to reduce error
    for i in range(Niter):
#%% Compute local averages of the flow vectors
        uAvg = filter2(U,kernel)
        vAvg = filter2(V,kernel)
#%% common part of update step
        der = (fx*uAvg + fy*vAvg + ft) / (alpha**2 + fx**2 + fy**2)
#%% iterative step
        U = uAvg - fx * der
        V = vAvg - fy * der

    return U,V

def computeDerivatives(im1, im2):
#%% build kernels for calculating derivatives
    kernelX = np.array([[-1, 1],
                         [-1, 1]]) * .25 #kernel for computing d/dx
    kernelY = np.array([[-1,-1],
                         [ 1, 1]]) * .25 #kernel for computing d/dy
    kernelT = np.ones((2,2))*.25

    fx = filter2(im1,kernelX) + filter2(im2,kernelX)
    fy = filter2(im1,kernelY) + filter2(im2,kernelY)

    #ft = im2 - im1
    ft = filter2(im1,kernelT) + filter2(im2,-kernelT)

    return fx,fy,ft

def u_v_plot(u,v,img_new):

    cv2.imshow("U Image", u)
    cv2.imshow("V Image", v)
    cv2.imshow("Image", img_new)
    while(1):
        key = cv2.waitKey(20) & 0xFF 
        if key == 27:
            break

def demo(stem):
    flist,ext = getimgfiles(stem)

    for i in range(len(flist)-1):
        fn1 = str(stem) +'.'+ str(i) + ext
        img_old = cv2.imread(fn1, 0)
        img_old = cv2.GaussianBlur(img_old,(7,7),0)

        fn2 = str(stem) + '.' + str(i+1) + ext
        img_new = cv2.imread(fn2, 0)
        img_new = cv2.GaussianBlur(img_new,(7,7),0)

        # cv2.imshow("Old Image", img_old)
        # cv2.imshow("New Image", img_new)
        # while(1):
        #     key = cv2.waitKey(20) & 0xFF 
        #     if key == 27:
        #         break   

        [U,V] = HS(img_old, img_new, 1, 2)
        u_v_plot(U,V,img_new)

    return U,V


if __name__ == '__main__':
    path = "images/box/box"
    # path = "images/rubic/rubic"
    U,V = demo(path)

    # plt.show()
