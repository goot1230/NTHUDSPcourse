import math
import cmath
import numpy as np
import imageio
import FFT
import dft

def fft2d(f):
    (Nr,Nc)=f.shape
    F=np.zeros((Nr,Nc),dtype=complex)
    for m in range(Nr):
        F[m,:]=FFT.fft(f[m,:])
    for n in range(Nc):
        F[:,n]=FFT.fft(F[:,n])
    return(F)

def ifft2d(F):
    (Nr,Nc)=F.shape
    f=np.zeros((Nr,Nc),dtype=complex)
    for m in range(Nr):
        f[m,:]=dft.complex_idft(F[m,:])
    for n in range(Nc):
        f[:,n]=dft.complex_idft(f[:,n])
    return(f)

# N=128
# cc=3
# cr=3
# basis2d= np.zeros((N,N),dtype=float)
# for m in range(N):
#     for n in range(N):
#         basis2d[m,n]=math.cos(2*math.pi*cc*n/N)*math.cos(2*math.pi*cr*m/N)
# 
# imageio.imwrite('basis2d.png',basis2d)

img=imageio.imread('lena.png')[256-32:256+32,256-32:256+32]
imageio.imwrite('lenareconstructed.png',ifft2d(fft2d(img)))

