import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from pathlib import Path

FILTER = 7
count = 0

def HS(im1, im2, alpha, ite,):

    #set up initial velocities
    uInitial = np.zeros([im1.shape[0],im1.shape[1]])
    vInitial = np.zeros([im1.shape[0],im1.shape[1]])

    # Set initial value for the flow vectors
    u = uInitial
    v = vInitial

    # Estimate derivatives
    [fx, fy, ft] = computeDerivatives(im1, im2)

    # Plot derivatives
    # fg,ax = plt.subplots(1,3,figsize=(18,5))
    # for f,a,t in zip((fx,fy,ft),ax,('$f_x$','$f_y$','$f_t$')):
    #     h=a.imshow(f,cmap='bwr')
    #     a.set_title(t)
    #     fg.colorbar(h,ax=a)
    #     plt.show()

    # Averaging kernel
    kernel=np.matrix([[1/12, 1/6, 1/12],[1/6, 0, 1/6],[1/12, 1/6, 1/12]])

    print(fx[100,100],fy[100,100],ft[100,100])

    # Iteration to reduce error
    for i in range(ite):
        # Compute local averages of the flow vectors
        uAvg = cv2.filter2D(u,-1,kernel)
        vAvg = cv2.filter2D(v,-1,kernel)

        uNumer = (fx.dot(uAvg) + fy.dot(vAvg) + ft).dot(ft)
        uDenom = alpha + fx**2 + fy**2
        u = uAvg - np.divide(uNumer,uDenom)

        # print np.linalg.norm(u)

        vNumer = (fx.dot(uAvg) + fy.dot(vAvg) + ft).dot(ft)
        vDenom = alpha + fx**2 + fy**2
        v = vAvg - np.divide(vNumer,vDenom)
    return (u,v)

def computeDerivatives(im1, im2):
	# build kernels for calculating derivatives
	kernelX = np.matrix([[-1,1],[-1,1]])*.25 #kernel for computing dx
	kernelY = np.matrix([[-1,-1],[1,1]])*.25 #kernel for computing dy
	kernelT = np.ones([2,2])*.25

	#apply the filter to every pixel using OpenCV's convolution function
	fx = cv2.filter2D(im1,-1,kernelX) + cv2.filter2D(im2,-1,kernelX)
	fy = cv2.filter2D(im1,-1,kernelY) + cv2.filter2D(im2,-1,kernelY)
	# ft = im2 - im1
	ft = cv2.filter2D(im2,-1,kernelT) + cv2.filter2D(im1,-1,-kernelT)
	return (fx,fy,ft)

def smoothImage(img,kernel):
	G = gaussFilter(kernel)
	smoothedImage=cv2.filter2D(img,-1,G)
	smoothedImage=cv2.filter2D(smoothedImage,-1,G.T)
	return smoothedImage

def gaussFilter(segma):
	kSize = 2*(segma*3)
	x = range(-kSize/2,kSize/2,1+1/kSize)
	x = np.array(x)
	G = (1/(2*np.pi)**.5*segma) * np.exp(-x**2/(2*segma**2))
	return G

def compareGraphs(u,v,img_new):
    print(np.mean(u))
    print(np.mean(v))
    scale = .00000001
    # plt.ion() #makes it so plots don't block code execution
    plt.imshow(img_new,cmap = 'gray')
	# plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(len(u)):
        if i%5 ==0:
            for j in range(len(u)):
                if j%5 == 0:                    
                    plt.arrow(j,i,v[i,j]*scale,u[i,j]*scale, color = 'red')
                pass
	# plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)
    plt.show()

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

        [U,V] = HS(img_old, img_new, 1, 10)
        compareGraphs(U,V,img_new)
    # print(np.max(U))

    return U,V


if __name__ == '__main__':
    path = "images/box/box"
    U,V = demo(path)

    # plt.show()