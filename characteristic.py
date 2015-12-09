import math 
import cmath
import numpy as np
import matplotlib.pyplot as plt


N=32
x=[0]*N
cycles1=8.5
cycles2=0
shift=5

for n in range(N):
    x[n]=math.cos(2*math.pi*cycles1*n/N)#+math.cos(2*math.pi*cycles2*n/N)
    
xshifted=x[shift:]+x[0:shift]

X=fft(x)
dftplot(x,X)

#Xshifted=fft(xshifted)
#dftplot(xshifted,Xshifted)