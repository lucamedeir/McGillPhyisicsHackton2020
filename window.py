import sys,pygame
import matplotlib.pyplot as plt

def create_window(title,width,height):
    pygame.init()

    size = width, height

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(title)

    fig, ax = plt.subplots()

    return pygame,fig,ax

def handle_events(pygame):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

def render(pygame,data,size):
    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen =  pygame.display.get_surface()

    screen.blit(plot, plotrect)
    pygame.display.flip()
