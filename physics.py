import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sint
from numpy.linalg import solve

def _fig2rgb_array(fig):
    '''Convert plot in figure to a string buffer'''
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    size = fig.canvas.get_width_height()
    return buf,size

def plot_data(fig,ax,X,Y):
    '''Convert data to a string buffer'''
    ax.plot(X, Y)
    return _fig2rgb_array(fig)

def psi0(X,x0,sigma,k):
    return np.exp(-np.power(X-x0,2)/2/sigma**2)*np.exp(1j*k)

def process_data_real(t,dt,N,L,dx,x0,A,sigma,k,psi,X,I,U_I):

    a1 = 1 + 1j*dt/dx**2/2
    a2 = -1j*dt/dx**2/4
    b1 = 1-1j*dt/dx**2/2
    b2 = 1j*dt/dx**2/4

    Y = psi

    # boundaries conditions: Infinite wall at the borders
    Y[0] = 0
    Y[-1] = 0

    W = a1*I+a2*U_I
    P = b1*I+b2*U_I
    v = P@Y

    Y = solve(W,v)

    return Y

def process_data(t,w,A):


    X = np.linspace(0, 40*np.pi, 1000)
    phase = X+t*w

    Y = A*(1/t) * np.exp((-(X-w*t)**2)/(10*t**2))

    #Y = np.cos(phase)

    return X,Y
