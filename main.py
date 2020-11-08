import sys,pygame
from window import *
from physics import *
import numpy as np




def main(argv):
    pygame,font,fig,ax = create_window("McGill Physics Hackaton 2020",1240,480)

    t = 0
    dt = 0.0001
    x0 = 20*np.pi
    A = 1
    w = 2*np.pi*20
    N = 10000
    L = 40*np.pi
    dx = L/N

    variablelist = [t,A,w,dt,N,L,x0,dx]

    textlist = [Label(font,'t',round(variablelist[0],3),0,0,False),
                Label(font,'A',variablelist[1],700,0),
                Label(font,'w',round(variablelist[2],2),700,20),
                Label(font,'dt',variablelist[3],700,40),
                Label(font,'N',variablelist[4],700,60),
                Label(font,'L',variablelist[5],700,80),
                Label(font,'x0',variablelist[6],700,100),
                Label(font,'dx',variablelist[7],700,120,False)]


    Y = np.zeros(N)


    while 1:

        textlist[0].update_value(round(t,3))
        X,Y = process_data_real(t,dt,N,L,dx,x0,A,Y)
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
