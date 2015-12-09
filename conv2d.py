import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import imageio
import MyModule as mm

def conv2d(x,h):
    (Nrx,Ncx) = x.shape
    (Nrh,Nch) = h.shape
    y = np.zeros((Nrx + Nrh - 1,Ncx + Nch -1), dtype=x.dtype)
    (Nry,Ncy) = y.shape
    for m in range(Nry):
        for n in range(Ncy):
            for l in range(Nrh):
                for k in range(Nch):
                    mx=m+Nrh//2-l
                    nx=n+Nch//2-k
                    if (mx>=0 and mx<Nrx and nx>=0 and nx<Ncx):
                        y[m,n] += x[mx,nx]*h[l,k]
    return(y)
    
def conv2dsep(x,h,v):
    (Nrx,Ncx)=x.shape
    y=np.zeros((Nrx+len(h)-1, Ncx+len(v)-1))
    for m in range(Nrx):
        y[m,:]=mm.conv(x[m,:],h)
    for n in range(Ncx+len(v)-1):
        y[:,n]=mm.conv(y[:Nrx,n],v)
    return(y)

x=np.array([1,2,3,4,5,6,7,8,9,0,0,9,8,7,6,5,4,3,2,1,2,4,6,8,0]).reshape(5,5)
h=[1,3,1]
v=[1,3,1]
hv=np.outer(h,v)
y1=conv2d(x,hv)
y2=conv2dsep(x,h,v)


# img = imageio.imread('lena.png')
# 
# h=np.array([0,0,0,0,1,0,0,0,-1]).reshape(3,3)
# 
# y=conv2d(img,h)
# 
# imageio.imwrite('lenaconved.png',y)
# 
# h1=np.array([-1,0 ,0,0,1,0,0,0,0]).reshape(3,3)
# 
# y=conv2d(img,h1)
# 
# imageio.imwrite('lenaconved1.png',y)