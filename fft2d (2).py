import math 
import cmath
import matplotlib.pyplot as plt
import numpy as np
import imageio
import MyModule as mm

def fft2d(f):
    (Nr, Nc) = f.shape
    F = np.zeros((Nr, Nc), dtype=complex)
    for m in range(Nr):
        F[m,:] = mm.fft(f[m,:])
    for n in range(Nc):
        F[:,n] = mm.fft(F[:,n])
    return(F)
    
def ifft2d(F):
    (Nr, Nc) = F.shape
    f = np.zeros((Nr, Nc), dtype=complex)
    for m in range(Nr):
        f[m,:] = mm.ifft(F[m,:])
    for n in range(Nc):
        f[:,n] = mm.ifft(f[:,n])
    return(f)
        

imgTemp = imageio.imread('catblackwhite.png')
img = imgTemp[0:512, 0:512]
Img = fft2d(img)

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

Imgshift = shift(Img)
ImgLow = trim(Imgshift, 50)
Img = shift(ImgLow)

(Nr, Nc) = Img.shape
ImgMag = np.zeros((Nr, Nc), dtype = float)
ImgPhase = np.zeros((Nr, Nc), dtype = float)
for m in range(Nr):
    for n in range(Nc):
        ImgMag[m,n], ImgPhase[m,n] = cmath.polar(Imgshift[m,n])


imageio.imwrite('catReconstructed.png', ifft2d(Img))
        

