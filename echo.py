import math
import cmath
import MyModule as mm
import numpy as np
import scipy.io.wavfile as sw

fs,x=sw.read('Libai.wav')
# mm.dftplot(x,x)
'''h=1.0 at 0, 0.2 at 25000, 0.02 at 50000'''
'''y[n]=1x[n]+0.2x[n-25000]+0.02x[n-50000]'''
echolen=25000
numofecho=3
Nfft=2**18
Nfilter=2**17
'''hlen=echolen*numofecho+1'''

hecho=np.zeros((Nfilter),dtype=float)
hecho[0]=1.0
hecho[1*echolen]=0.2
hecho[2*echolen]=0.04
hecho[3*echolen]=0.008

yiffted=mm.convlong(x,hecho,Nfft)
sw.write('Libaiecho.wav',fs,yiffted)

#h=np.array([1.0]+[0.0]*(25000-1)+[0.2]+[0.0]*(25000-1)+[0.02]+[0]*(len(x)-50000-1))
#y=mm.ifft(mm.fft(x)*mm.fft(h))
#y=mm.convlong(x,h,)



# x=np.array([1,2,3,0,1,-1,0,0])
# h=np.array([3,1,4,2,0,0,0,0])
# y=mm.conv(x,h)
# X=mm.fft(x)
# H=mm.fft(h)
# y1=mm.ifft(X*H)
# 
# delta=np.zeros((32))
# delta[0]=1.0
# mm.dftplot(delta,mm.fft(delta)



# x=np.array([1,2,3,4,4,3,2,1])
# h=np.array([2,1,2])
# y=np.array(mm.conv(x,h))
# x1=np.array([1,2,3,4])
# x2=np.array([0,0,0,0,4,3,2,1])
# y1=mm.conv(x1,h)
# y2=mm.conv(x2,h)
# yall=np.array(y1+[0]*(len(y2)-len(y1)))+np.array(y2)