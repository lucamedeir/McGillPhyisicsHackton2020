import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sint

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

def psi0(X):
    return np.exp(-np.power(X-20*np.pi,2)/10)*np.exp(1j)

def process_data_real(t,dt,N,psi):
    X = np.linspace(0,40*np.pi,N)
    dx = 40*np.pi/N

    if t == 0:
        Y = psi0(X)
    else:
        Y = psi

    Laplaciano = np.zeros(N,dtype=np.complex)
    Laplaciano = np.convolve(psi,np.array([1,-2,1]) /dx**2)


    Y = Y+1j*Laplaciano[1:N+1]/2*dt
    return X,Y

def process_data(t,w,A):


    X = np.linspace(0, 40*np.pi, 1000)
    phase = X+t*w

    Y = A*(1/t) * np.exp((-(X-w*t)**2)/(10*t**2))

    #Y = np.cos(phase)

    return X,Y
