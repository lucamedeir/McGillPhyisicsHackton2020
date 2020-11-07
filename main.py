import sys,pygame
from window import *
from physics import *
import numpy as np


def main(argv):
    pygame,font,fig,ax = create_window("McGill Physics Hackaton 2020",1240,480)

    t = 0.001
    dt = 0.001
    A = 2
    w = 2*np.pi*20

    textlist = [get_surface_text(font,['t: '+ str(round(t,3)),0,0],0),
                get_surface_text(font,['A: '+ str(A),700,0],1),
                get_surface_text(font,['w: '+ str(round(w,2)),700,20],2)]

    while 1:

        textlist[0] = get_surface_text(font,['t: '+ str(round(t,3)),0,0],0)
        X,Y = process_data(t,w,A)
        t += dt
        plot,size = plot_data(fig,ax,X,Y)

        handle_events(pygame,textlist)
        render(pygame,font,textlist,plot,size)

        ax.clear()


if __name__ == "__main__":
    main(sys.argv)
