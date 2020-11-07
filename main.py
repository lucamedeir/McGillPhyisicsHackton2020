import sys,pygame
from physics import *
import numpy as np

def main(argv):
    pygame.init()

    size = width, height = 640, 480

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("McGill Physics Hackaton 2020")

    fig, ax = plt.subplots()

    t = 0
    dt = 0.001
    w = 2*np.pi

    while 1:
        data,size = our_function(fig,ax,t,w)
        t += dt
        plot = pygame.image.fromstring(data, size, "RGB")
        plotrect = plot.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(plot, plotrect)
        pygame.display.flip()
        ax.clear()


if __name__ == "__main__":
    main(sys.argv)
