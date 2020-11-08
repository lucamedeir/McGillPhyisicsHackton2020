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

    textlist = [Label(font,'t',round(t,3),0,0),
                Label(font,'A',round(A),700,0),
                Label(font,'w',round(w,2),700,20),
                Label(font,'dt',dt,700,40)]

    while 1:

        textlist[0].update_value(round(t,3))
        X,Y = process_data(t,w,A)
        t += dt
        plot,size = plot_data(fig,ax,X,Y)

        handle_events(pygame,textlist)
        render(pygame,textlist,plot,size)

        ax.clear()
        clear_screen(pygame)


if __name__ == "__main__":
    main(sys.argv)
