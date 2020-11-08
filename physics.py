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
    plt.xlim(420,580)
    return _fig2rgb_array(fig)

def psi0(X,x0):
    return np.exp(-np.power(X-x0,2)/10)*np.exp(1j*2*np.pi*4)

def process_data_real(t,dt,N,L,dx,x0,A,psi,X):


    if t == 0:
        Y = A*psi0(X,x0)
    else:
        Y = psi

    Laplaciano = np.convolve(Y,np.array([1,-2,1]) /dx**2)
    dY = 1j*Laplaciano[1:N+1]/2 # -V*psi

    Y = Y + dt*dY
    return Y

def process_data(t,w,A):


    X = np.linspace(0, 40*np.pi, 1000)
    phase = X+t*w

    Y = A*(1/t) * np.exp((-(X-w*t)**2)/(10*t**2))

    #Y = np.cos(phase)

    return X,Y
