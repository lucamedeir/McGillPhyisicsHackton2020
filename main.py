import sys,pygame
from window import *
from physics import *
import numpy as np




def main(argv):
    pygame,font,fig,ax = create_window("McGill Physics Hackaton 2020",1240,480)

    t = 0
    dt = 0.0001
    x0 = 3
    A = 100
    w = 2*np.pi*20
    N = 1000
    L = 10
    dx = L/N
    sigma = 0.05
    k = 100
    norma = 1

    variablelist = [t,A,w,dt,N,L,x0,dx,sigma,k,norma]

    textlist = [Label(font,'t',variablelist[0],0,0,editable = False),
                Label(font,'A',variablelist[1],700,0),
                Label(font,'w',round(variablelist[2],2),700,20),
                Label(font,'dt',variablelist[3],700,40),
                Label(font,'N',variablelist[4],700,60,is_int=True),
                Label(font,'L',variablelist[5],700,80),
                Label(font,'x0',variablelist[6],700,100),
                Label(font,'dx',variablelist[7],700,120,editable = False),
                Label(font,'sigma',variablelist[8],700,140),
                Label(font,'k',variablelist[9],700,160),
                Label(font,'norma',variablelist[10],0,20,editable = False)]

    X = np.linspace(0,variablelist[5],variablelist[4])

    Y  = psi0(X,x0,sigma,k)

    V = A*np.exp(-np.power(X-5,2)/(2*2**2))
    V[V<9*A/10] = 0
    V[V>9*A/10] = A


    print(dt/dx**2)

    LU,U2 = getLUU2(dt,dx,N,V)

    N = variablelist[4]
    update_variables = False
    while 1:

        if update_variables:
            for id,label in enumerate(textlist):
                if label._editable:
                    variablelist[id] = label._value

            update_variables = False
            N = variablelist[4]
            variablelist[7] = variablelist[5]/N # dx = L/N
            textlist[7].update_value(variablelist[7])
            X = np.linspace(0,variablelist[5],N)
            x0 = variablelist[6]
            sigma = variablelist[8]
            A = variablelist[1]
            V = A*np.exp(-np.power(X-5,2)/(2*0.01**2))
            k = variablelist[9]
            Y  = A*psi0(X,x0,sigma,k)
            variablelist[0] = 0 #t
            dt = variablelist[3]
            dx = variablelist[7]
            LU,U2 = getLUU2(dt,dx,N,V)
            print(dt/dx**2)

        textlist[0].update_value(variablelist[0]) # update time t
        Y = process_data_real(variablelist[0], #t
                                variablelist[3], #dt
                                variablelist[4], #N
                                variablelist[5], #L
                                variablelist[7], #dx
                                variablelist[6], #x0
                                variablelist[1], #A
                                variablelist[7], #sigma
                                variablelist[8], #k
                                Y,X,LU,U2)
        variablelist[0] += variablelist[3] # t+=dt

        Amp = np.real(np.conj(Y)*Y)
        sum = np.sum(Amp*dx)
        variablelist[10] = sum
        textlist[10].update_value(variablelist[10])
        plot,size = plot_data(fig,ax,X,Amp,V)

        update_variables = handle_events(pygame,textlist)

        render(pygame,textlist,plot,size)

        ax.clear()
        clear_screen(pygame)


if __name__ == "__main__":
    main(sys.argv)
