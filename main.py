import sys,pygame
from window import *
from physics import *
import numpy as np




def main(argv):
    pygame,font,fig,ax = create_window("McGill Physics Hackaton 2020",1240,480)

    t = 0
    dt = 0.01
    A = 2
    w = 2*np.pi*20
    N = 1000

    textlist = [Label(font,'t',round(t,3),0,0),
                Label(font,'A',round(A),700,0),
                Label(font,'w',round(w,2),700,20),
                Label(font,'dt',dt,700,40),
                Label(font,'N',N,700,60)]


    Y = np.zeros(N)
    dx = 40*np.pi/N
    while 1:

        textlist[0].update_value(round(t,3))
        X,Y = process_data_real(t,dt,Y)
        t += dt
        Amp = np.real(np.conj(Y)*Y)
        Y = Y/np.sqrt(np.sum(Amp*dx))
        Amp = Amp/np.sum(Amp*dx)
        plot,size = plot_data(fig,ax,X,Amp)

        handle_events(pygame,textlist)
        render(pygame,textlist,plot,size)

        ax.clear()
        clear_screen(pygame)


if __name__ == "__main__":
    main(sys.argv)
