import sys,pygame
from window import *
from physics import *
import numpy as np



def main(argv):
    pygame,fig,ax = create_window("McGill Physics Hackaton 2020",640,480)

    t = 0
    dt = 0.001
    w = 2*np.pi*20

    while 1:
        data,size = our_function(fig,ax,t,w)
        t += dt

        handle_events(pygame)
        render(pygame,data,size)

        ax.clear()


if __name__ == "__main__":
    main(sys.argv)
