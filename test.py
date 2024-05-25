import library
import numpy as np
import matplotlib.pyplot as plt

xi,yi = [-1,4,-2,3,1,2],[1,3,2,-2,4,0]
ti = library.compute_t_terms(xi,yi)
T = ti[-1]
N = 1000
t = np.linspace(0,T,N)
x,y = np.zeros_like(t),np.zeros_like(t)

for i in range(N):
    x[i],y[i] = library.newton_interpolation(xi,yi,ti,t[i])
plt.plot(x,y)
plt.plot(xi,yi,'.r')
plt.show()


