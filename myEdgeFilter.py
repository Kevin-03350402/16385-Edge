import numpy as np
from scipy import signal    # For signal.gaussian function
import scipy
import cv2
import os
import math
from myImageFilter import myImageFilter

sobelx = np.array([-1,0,1])
sobelx = sobelx.reshape((1,3))
sobely = sobelx.reshape((3,1))

xsobel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
ysobel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])





def matchangle(angle):
        
        if angle < 0 :
            # if negative, map to the correct domain
            angle += math.pi
        if 0 <= angle < 1/8*math.pi:
            return 0
        elif 1/8*math.pi<= angle <3/8*math.pi:
            return 45
        elif 3/8*math.pi<= angle <5/8*math.pi:
            return 90
        elif 5/8*math.pi<= angle <7/8*math.pi:
            return 135
        elif 7/8*math.pi<= angle <=math.pi:
            return 0
    

    

def myEdgeFilter(img0, sigma):
    rows = img0.shape[0]
    cols = img0.shape[1]
    # generate gaussian filter
    hsize = 2 * math.ceil(3 * sigma) + 1
    gm = scipy.signal.gaussian(hsize,sigma)



    gmx = gm.reshape(gm.shape[0],1)
    gmy = gm.reshape(1,gm.shape[0])
    
    gaussian = gmx*gmy
    gaussian = gaussian/(np.sum(gaussian))
    
    img1 = myImageFilter(img0,gaussian)
    # derivative wrt x

    xedge = myImageFilter(img1 ,sobelx)
    # derivative wrt y

    yedge = myImageFilter(img1,sobely)


    # find the magnitude
    magnitude = np.sqrt(np.add(np.square(xedge),np.square(yedge)))
    
    # create a new matrix to handle Non-maximum suppression
    newimg = np.copy(magnitude)
    for i in range (2, rows-1):
        for j in range (2, cols-1):
                angle = math.atan2(yedge[i,j],xedge[i,j])

                # map to 0 
                if matchangle (angle) == 0:
                    left = magnitude[i,j-1]
                    mid = magnitude[i,j]
                    right = magnitude[i,j+1]
                    if left > mid or right > mid:
                        newimg[i,j] = 0
                    else:
                        newimg[i,j] = mid
                # map to 45
                if matchangle (angle) == 45:
                    left = magnitude[i-1,j-1]
                    mid = magnitude[i,j]
                    right = magnitude[i+1,j+1]
                    if left > mid or right > mid:
                        newimg[i,j] = 0
                    else:
                        newimg[i,j] = mid
                # map to 90:
                if matchangle (angle) == 90:
                    left = magnitude[i-1,j]
                    mid = magnitude[i,j]
                    right = magnitude[i+1,j]
                    if left > mid or right > mid:
                        newimg[i,j] = 0
                    else:
                        newimg[i,j] = mid
                # map to 135
                if matchangle (angle) == 135:
                    left = magnitude[i-1,j+1]
                    mid = magnitude[i,j]
                    right = magnitude[i+1,j-1]
                    if left > mid or right > mid:
                        newimg[i,j] = 0
                    else:
                        newimg[i,j] = mid
    return newimg


    