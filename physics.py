import numpy as np
import matplotlib.pyplot as plt

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

def process_data(t,w,A):
    X = np.linspace(0, 40*np.pi, 1000)
    phase = X+t*w

    Y = A*(1/t) * np.exp((-(X-w*t)**2)/(10*t**2))

    #Y = np.cos(phase)

    return X,Y
