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
    '''Given the parameters return the X and Y data to be plotted'''
    X = np.linspace(0, 4*np.pi, 1000)
    phase = X+t*w
    Y = A*np.cos(phase)

    return X,Y
