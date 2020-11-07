import sys,pygame
import matplotlib.pyplot as plt

def create_window(title,width,height):
    '''Create the window '''
    pygame.init()

    size = width, height

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)

    fig, ax = plt.subplots()
    font = pygame.font.Font(pygame.font.get_default_font(), 14)

    screen.fill([255, 255, 255])
    pygame.display.update()

    return pygame,font,fig,ax

def handle_events(pygame):
    '''Handle all interface events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

def get_surface_text(font,text):
    '''return a surface from a text from a string list'''
    textstring,x,y = text
    surface = font.render(textstring, True, [0, 0, 0],[255,255,255])
    rect = surface.get_rect()
    rect.x = x
    rect.y = y
    return surface,rect


def render_text(screen,font,textlist):
    for text,rect in textlist:
        text
        screen.blit(text, rect)

def render(pygame,font,textlist,data,size):
    '''Render the string buffer of the image to the window'''



    screen =  pygame.display.get_surface()

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen.blit(plot, plotrect)

    render_text(screen,font,textlist)

    pygame.display.flip()
