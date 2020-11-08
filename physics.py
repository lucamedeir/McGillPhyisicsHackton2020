import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse.linalg
import scipy.sparse
from numpy.linalg import solve

def _fig2rgb_array(fig):
    '''Convert plot in figure to a string buffer'''
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    size = fig.canvas.get_width_height()
    return buf,size

def plot_data(fig,ax,X,Y,V):
    '''Convert data to a string buffer'''
    ax.plot(X, Y)
    ax.plot(X, V)
    ax.set_xlim(3,7)
    ax.set_ylim(0,120)
    return _fig2rgb_array(fig)

def psi0(X,x0,sigma,k):
    return np.exp(-np.power(X-x0,2)/(2*sigma**2))   *np.exp(1j*k*X)/sigma/np.sqrt(np.pi)

def getLUU2(dt,dx,N,V):
    a = 1j*dt/dx**2

    # From Christoph Wachter 2017 Bachelor Thesis - University of Graz
    o = np.ones(N,np.complex)
    alp = a*o/2
    xi = o+a*o+1j*dt*V/2
    gamma = o-a*o-1j*dt*V/2
    diags =[-1,0,1]
    vecs1 =[-alp,xi,-alp]
    vecs2 =[alp,gamma,alp]
    U1 = scipy.sparse.spdiags(vecs1,diags,N,N)
    U1.tocsc()
    U2 = scipy.sparse.spdiags(vecs2,diags,N,N)
    U2.tocsc()

    LU = scipy.sparse.linalg.splu(U1)

    return LU,U2

def process_data_real(t,dt,N,L,dx,x0,A,sigma,k,Y,X,LU,U2):
    # boundaries conditions: Infinite wall at the borders
    Y[0] = 0
    Y[-1] = 0

    b = U2.dot(Y)
    return LU.solve(b)
