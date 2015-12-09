import math
import matplotlib.pyplot as plt
import numpy as np

def conv(h, x):
    y = [0] * (len(x) + len(h) -1)
    for n in range(len(y)):
        for k in range(len(h)):
            if(n - k >= 0 and n - k < len(x)):
                y[n] = y[n] + x[n-k] * h[k];
    return (y);
    
N = 64;
h = [0.0, 0.0, 2.0, 1.5, 1.0, 0.5, 0, 0, 0]

shift = 20
scale = 0.1
rec = [0] * N
for i in range(len(h)):
    rec[i + shift] = rec[i + shift] + scale * h[i]
    
x= [0] * N
for i in range(len(x)):
    x[i] = rec[i] + np.random.random_sample()/10 - 0.05
    
y = conv(x, h)
plt.plot(h)
plt.plot(x)
plt.plot(y)

        