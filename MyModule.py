import math
import matplotlib.pyplot as plt
import numpy as np
import cmath
import time


def conv(h, x):
    y = [0] * (len(x) + len(h) -1)
    for n in range(len(y)):
        for k in range(len(h)):
            if(n - k >= 0 and n - k < len(x)):
                y[n] = y[n] + x[n-k] * h[k];
    return (y);
    '''conv(x,h)=ifft(fft(x)*fft(h)), if len(y)<=len(x) and len(h)'''
    
def cconv(x, h):
    '''circular convolution'''
    N=len(x)
    y = np.zeros(N,dtype=complex)
    for i in range(N):
        y[i]=0+0j
        for k in range(N):
            y[i] = y[i] + x[(i-k+N)%N] * h[k];
    return (y);
    

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
    Xdb=[0,0]*N
    
    for i in range(len(X)):
        Xreal[i]=X[i].real
        Ximag[i]=X[i].imag
        Xamp[i],Xphase[i]=cmath.polar(X[i])
        if Xamp[i]<1e-10:
            Xphase[i]=0
        if Xamp[i] !=0.0:
            Xdb[i]=20*cmath.log10(Xamp[i])

        
    f,axarr=plt.subplots(3,2)
    f.suptitle('figtitle')
    axarr[0,0].plot(x,'o-')
    axarr[0,1].plot(Xdb,'o-')
    axarr[1,0].plot(Xreal,'o-')
    axarr[2,0].plot(Ximag,'o-')
    axarr[1,1].plot(Xamp,'o-')
    axarr[2,1].plot(Xphase,'o-')
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
    
def ifftnoscale(X):
    N=len(X)
    if (N==1):
        x=X
    else:
        halfN=N//2
        Xeven=np.zeros((halfN),dtype=complex)
        Xodd=np.zeros((halfN),dtype=complex)
        for i in range(halfN):
            Xeven[i]=X[2*i]
            Xodd[i]=X[2*i+1]
        xeven=ifftnoscale(Xeven)
        xodd=ifftnoscale(Xodd)
        x=np.zeros((N),dtype=complex)
        for m in range(N):
            x[m]=xeven[m % halfN]+xodd[m %halfN]*cmath.exp(1j*2*math.pi*m/N)
    return(x)
    
def ifft(X):
    x=ifftnoscale(X)
    N=len(x)
    for i in range(N):
        x[i]=x[i]/N
    return(x)
    
    
def fft2d(f):
    (Nr,Nc)=f.shape
    F=np.zeros((Nr,Nc),dtype=complex)
    for m in range(Nr):
        F[m,:]=fft(f[m,:])
    for n in range(Nc):
        F[:,n]=fft(F[:,n])
    return(F)

def ifft2d(F):
    (Nr,Nc)=F.shape
    f=np.zeros((Nr,Nc),dtype=complex)
    for m in range(Nr):
        f[m,:]=ifft(F[m,:])
    for n in range(Nc):
        f[:,n]=ifft(f[:,n])
    return(f)

def shift(Img):
    (Nr, Nc) = Img.shape
    Imgshift = np.zeros((Nr,Nc), dtype=complex)
    for i in range(Nr):
        for j in range(Nc):
            Imgshift[i,j] = Img[(i+Nr//2) % Nr, (j+Nc//2) % Nc]
    return(Imgshift)
    
def trim(Img, radius):
    (Nr, Nc) = Img.shape
    for i in range(Nr):
        for j in range(Nc):
            if (((i-Nr//2)**2 + (j-Nc//2)**2) > radius**2):
                Img[i,j] = 0.0 +0.0j
    return(Img)
    
def convlong(x,h,Nfft):
    '''convolute a long signal segment by segment'''
    Nsegment=Nfft-len(h)
    hseq=np.zeros((Nfft))
    hseq[:len(h)]=h[:]
    Hseq=fft(hseq)
    yiffted=np.zeros((len(x)+Nfft),dtype=x.dtype)
    for s in range(len(x)//Nsegment+1):
        xseq=np.zeros((Nfft))
        if (s+1)*Nsegment<=len(x):
            reallen=Nsegment
        else:
            reallen=len(x)-s*Nsegment
        xseq[:reallen]=x[s*Nsegment:s*Nsegment+reallen]
        Xseq=fft(xseq)
        seqiffted=ifft(Hseq*Xseq)
        l=s*Nsegment
        r=l+len(seqiffted)
        yiffted[l:r]=yiffted[l:r]+seqiffted[:]
    return(yiffted)