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

def psi0(X,x0):
    return np.exp(-np.power(X-x0,2)/10)*np.exp(1j)

def dydx():
    pass

def rungeKuttaStep(x0,y0,h):
    k1 = h * dydx(x0, y0)
    k2 = h * dydx(x0 + 0.5 * h, y0 + 0.5 * k1)
    k3 = h * dydx(x0 + 0.5 * h, y0 + 0.5 * k2)
    k4 = h * dydx(x0 + h, y0 + k3)
    return x0+h, y0 + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

def process_data_real(t,dt,N,L,dx,x0,A,psi):
    X = np.linspace(0,L,N)

    if t == 0:
        Y = A*psi0(X,x0)
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
