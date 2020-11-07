import sys, pygame


def run_window(title,data,size):
    pygame.init()

    size = width, height = 640, 480
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(title)

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(plot, plotrect)
        pygame.display.flip()
