import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import MyModule as mm

N=8
mat_idft=np.array([cmath.exp(1j*2*math.pi*m*n/N) for m in range(N) for n in range(N)]).reshape(N,N)#IDFT matrix
mat_dft=np.conjugate(mat_idft)#DFT matrix
mat_idft=mat_idft/N

np.set_printoptions(precision=2, suppress=True)

#np.sum(x2d,axis=0)
#imshow(mat_dft.real)
#plt.colorbar()

x=[1,2,3,4,4,3,2,1]
X=np.linalg.solve(mat_idft,x) #AX=B   order(N**3)

plt.imshow(np.dot(mat_dft,mat_idft).real)
plt.colorbar()