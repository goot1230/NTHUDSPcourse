import math 
import cmath
import matplotlib.pyplot as plt
import numpy as np
import time

def dftplot(x,X):
    N=len(X)
    Xreal=[0.0]*N
    Ximag=[0.0]*N
    Xamp=[0.0]*N
    Xphase=[0.0]*N
    
    for i in range(len(x)):
        Xreal[i]=X[i].real
        Ximag[i]=X[i].imag
        Xamp[i],Xphase[i]=cmath.polar(X[i])
        
    f,axarr=plt.subplots(3,2)
    axarr[0,0].plot(x)
    axarr[1,0].plot(Xreal)
    axarr[2,0].plot(Ximag)
    axarr[1,1].plot(Xamp)
    axarr[2,1].plot(Xphase)
    plt.show


def fft(x):
    N=len(x)
    if (N==1):
        X=x
    else:
        halfN=N//2
        xeven=np.zeros((halfN),dtype=complex)
        xodd=np.zeros((halfN),dtype=complex)
        for i in range(halfN):
            xeven[i]=x[2*i]
            xodd[i]=x[2*i+1]
        Xeven=fft(xeven)
        Xodd=fft(xodd)
        X=np.zeros((N),dtype=complex)
        for m in range(N):
            X[m]=Xeven[m % halfN]+Xodd[m %halfN]*cmath.exp(-1j*2*math.pi*m/N)
    return(X)
        



        
# N=128
# x=np.zeros((N),dtype=complex)
# for n in range(N):
#    x[n]=math.cos(2*math.pi*3*n/N)
# 
# t1=time.time()
# X=fft(x)
# t2=time.time()
# print('% 10d point fft takes %10.2f sec' %(N, t2-t1))
# 
# dftplot(x,X)