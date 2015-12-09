import math
import matplotlib.pyplot as plt
import numpy as np
import cmath
import scipy.io.wavfile
import pylab

fs1,y1=scipy.io.wavfile.read('gtr-nylon22.wav')

#x=y1[0000:8256]

N=1024
sb=60000
se=sb+N
x=y1[sb:se]
X=fft(x)

dftplot(x,X[0:32])
#plt.plot(y1)
#plt.show