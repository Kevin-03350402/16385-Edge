import numpy as np
import math

def myHoughTransform(Im, rhoRes, thetaRes):
    # set m to be the diagonal length of the input image
    m = math.ceil(math.sqrt((Im.shape[0])**2 + (Im.shape[1])**2))
    img_hough = np.zeros((math.floor(m/rhoRes)+1,math.floor(2*np.pi/thetaRes)+1))
    # 0 to m, 0 to 2pi/thetares
    # img_hough have m/rhoRes rows and 2*np.pi/thetaRes columns
    rhoScale = np.arange(0, m, rhoRes)
    thetaScale = np.arange(0, 2*math.pi, thetaRes)

    for x in range(Im.shape[0]):
        for y in range(Im.shape[1]):
            if Im[x,y] ==1:
                
                # iterate all angles from 0 to 2pi
                thetalength = len(thetaScale)
                for i in range (thetalength):
                    theta = thetaScale[i]
                    rho = y*math.cos(theta) + x*math.sin(theta)
                    # remove the cases where rho is negative
                    if rho >= 0:
                        # map rho to the closest index
                        index = int(rho/rhoRes)

                        img_hough[index,i] += 1

    return ([img_hough,rhoScale,thetaScale])

