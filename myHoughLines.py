import numpy as np
import cv2  # For cv2.dilate function
from numpy import unravel_index

def islocalmax(H,i,j):
    mid = H[i,j]
    upleft = H[i-1,j-1]
    up = H[i-1,j]
    upright = H[i-1,j+1]
    left = H[i,j-1]
    right = H[i,j+1]
    downleft = H[i+1,j-1]
    down = H[i+1,j]
    downright = H[i+1,j+1]
    if mid > upleft and mid>up and mid>upright and mid>left and mid>right and mid>downleft and mid>down and mid>downright:
        return mid
    else:
        return 0

def myHoughLines(H, nLines):
    # cited the method of using dilate from:
    # https://appdividend.com/2022/03/15/python-cv2-dilate/
    
    rows = H.shape[0]
    cols = H.shape[1]
    newh = np.zeros((rows,cols))
    for i in range (2, rows-1):
        for j in range (2,cols-1):
            # compare with its neighbours
            # non-maximum suppression
            newh[i,j] = islocalmax(H,i,j)
    rhos = []
    thetas = []
    for j in range (0,nLines):
        # find the row, col that is the max

        currmr, currmc = np.unravel_index(np.argmax(newh,axis = None), newh.shape)
        
        rhos.append(currmr)
        thetas.append(currmc)
        newh[currmr,currmc] = 0
    return [rhos, thetas]

    
