import numpy as np


def compute_t_terms(xi,yi):
    """This function yields a time sampling for the dots cloud of which coordinates are (xi,yi) couples."""
    N = len(xi)
    ti = np.zeros_like(xi)
    ti[0] = 0
    for i in range(1,N):
        d = np.sqrt((xi[i]-xi[i-1])**2+(yi[i]-yi[i-1])**2)
        ti[i] = ti[i-1] + d
    return ti

def newton_polynomial(t,ti,i):
    """This function evaluates the Newton polynomial in t."""
    N = 1
    if i == 0:
        return N
    else:
        for j in range(i):
            N *= t-ti[j]
        return N
    
def divided_difference(ti,xi,i,j):
    """This function computes the divided differences for indexes from i to j."""
    n = j-i+1
    if n == 1:
        return xi[i]
    elif n == 2:
        return (xi[j]-xi[i])/(ti[j]-ti[i])
    else:
        return (divided_difference(ti,xi,i+1,j)-divided_difference(ti,xi,i,j-1))/(ti[j]-ti[i])
    
def newton_interpolation(xi,yi,ti,t):
    """This function returns the dot corresponding to the value of the interpolating polynomial in t
    according to the Newton method."""
    n = len(xi)
    x,y = 0,0
    for i in range(n):
        x += divided_difference(ti,xi,0,i)*newton_polynomial(t,ti,i)
        y += divided_difference(ti,yi,0,i)*newton_polynomial(t,ti,i)
    return x,y