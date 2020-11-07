import sys,pygame
from window import *
from physics import *

def main(argv):
    pygame.init()

    size = width, height = 640, 480

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("McGill Physics Hackaton 2020")



    while 1:
        data,size = our_function()
        plot = pygame.image.fromstring(data, size, "RGB")
        plotrect = plot.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(plot, plotrect)
        pygame.display.flip()

if __name__ == "__main__":
    main(sys.argv)
