import math
import cmath
import numpy as np
import imageio
import MyModule as mm
import time

x=[1,2,3,4]
x1=mm.complex_idft(mm.complex_dft(x))
x2=mm.complex_idft(mm.fft(x))
x3=mm.ifft(mm.complex_dft(x))
x4=mm.ifft(mm.fft(x))

y=[5,6,7,8]
output1=mm.conv(x,y)
output2=mm.ifft(mm.fft(x)*mm.fft(y))


img=imageio.imread('lena.png')#[256-128:256+128,256-128:256+128]

t1=time.time()
imageio.imwrite('lenareconstructed.png',mm.ifft2d(mm.fft2d(img)))

t2=time.time()
print('img ifft takes %10.2f sec' %( t2-t1))

