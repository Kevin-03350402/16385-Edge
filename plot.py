import numpy as np
import math
import matplotlib.pyplot as plt
rhoRes    = 2
thetaRes  = np.pi / 90
a = [10,10]
b = [20,20]
c = [30,30]
m = math.sqrt(30**2+30**2)


input = [a,b,c]
l = 2*math.floor(m/rhoRes)+1
c = math.floor(2*np.pi/thetaRes)+1

hough = np.zeros((l,c))

#rhoScale = np.arange(-m, m, rhoRes)
thetaScale = np.arange(0, 2*math.pi, thetaRes)

def vote(x,y):
    thetalength = len(thetaScale)
    for i in range (thetalength):
        theta = thetaScale[i]
        rho = y*math.cos(theta) + x*math.sin(theta)

        index = int(rho/rhoRes+m/rhoRes)

        
        hough[index,i] += 1


vote(10,10)
plt.imshow(hough)

plt.show()

vote(20,20)
plt.imshow(hough)
plt.show()

vote(30,30)
plt.imshow(hough)
plt.show()

x = [10,20,30]
y = [10,20,30]



plt.plot(x,y,marker='o')

plt.show()