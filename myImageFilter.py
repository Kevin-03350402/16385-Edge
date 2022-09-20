import numpy as np
import cv2
import os




def myImageFilter(img0, h):
    # YOUR CODE HERE
    # get the size of the input matrix
    height = h.shape[0]
    width = h.shape[1]
    # totalrange of i is -rows//2 to rows//2
    # totalrange of j is -cols//2 to cols//2
    # we should pad the image by c//2 by cols, r//2 by rows
    pad_img =np.pad(img0, [(height//2, ), (width//2, )], mode='edge')


    img_rows = img0.shape[0]
    img_cols = img0.shape[1]
    newimage = np.zeros((img_rows,img_cols))
    for i in range (img_rows):
        for j in range (img_cols):
            temp = pad_img[i:i+height,j:j+width]

            pixel = np.multiply(temp,h)
            # we then replace the matrix with the sum of he matrix
            p_value = np.sum(pixel)
            newimage[i][j] = p_value
    return newimage




    

    
