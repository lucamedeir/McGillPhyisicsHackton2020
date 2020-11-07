import numpy as np
import matplotlib.pyplot as plt

def _fig2rgb_array(fig):
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    size = fig.canvas.get_width_height()
    return buf,size

def our_function(fig,ax,t,w):
    '''return an image'''

    x = np.linspace(0, 4*np.pi, 1000)
    phase = x+t*w

    ax.plot(x, np.cos(phase))
    ax.plot(x, np.sin(phase))

    return _fig2rgb_array(fig)
