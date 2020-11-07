import numpy as np
import matplotlib.pyplot as plt

def _fig2rgb_array(fig):
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    size = fig.canvas.get_width_height()
    return buf,size

def our_function(fig,ax):
    '''return an image'''

    t = np.linspace(0, 4*np.pi, 1000)

    ax.plot(t, np.cos(t))
    ax.plot(t, np.sin(t))

    return _fig2rgb_array(fig)
