import math
import matplotlib.pyplot as plt
import numpy as np
import cmath
import time

def real_dft(x):
    N=len(x)
    X=[0+0j]*N
    for m in range(N):
        for n in range(N):
            X[m]=X[m]+x[n]*complex(math.cos(2*math.pi*m*n/N),-1.0*math.sin(2*math.pi*m*n/N))
    return(X)

def complex_dft(x):
    '''complex input DFT'''
    N=len(x)
    X=[0+0j]*N
    for m in range(N):
        for n in range(N):
            X[m]=X[m]+x[n]*cmath.exp(-1j*2*math.pi*m*n/N)
    return(X)
    
def complex_idft(X):
    '''complex input inverse DFT,scaled by 1/N'''
    N=len(X)
    x=[0+0j]*N
    for n in range(N):
        for m in range(N):
            x[n]=x[n]+X[m]*cmath.exp(1j*2*math.pi*m*n/N)
        x[n]=x[n]/N 
    return(x)

def dftplot(x,X):
    N=len(X)
    Xreal=[0.0]*N
    Ximag=[0.0]*N
    Xamp=[0.0]*N
    Xphase=[0.0]*N
    
    for i in range(len(X)):
        Xreal[i]=X[i].real
        Ximag[i]=X[i].imag
        Xamp[i],Xphase[i]=cmath.polar(X[i])
        if Xamp[i]<1e-10:
            Xphase[i]=0

        
    f,axarr=plt.subplots(3,2)
    axarr[0,0].plot(x,'o-')
    axarr[1,0].plot(Xreal,'o-')
    axarr[2,0].plot(Ximag,'o-')
    axarr[1,1].plot(Xamp,'o-')
    axarr[2,1].plot(Xphase,'o-')
    plt.show


# N = 16
# x = [0]*N
# for n in range(N):
#     x[n]=2*math.cos(2*math.pi*2*n/N)+1.5*math.sin(2*math.pi*5*n/N)
#     
#X=real_dft(x)
#dftplot(x,X)   
# t1=time.time()
# X2=complex_dft(x)
# t2=time.time()
# print('% 5d point dft takes %10.2f sec' %(N, t2-t1))
# 
# 
# dftplot(x,X2)
# 
# x3=complex_idft(X2)
# dftplot(x3,X2)

