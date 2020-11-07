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

    return pygame,font,fig,ax

def handle_events(pygame):
    '''Handle all interface events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

def get_surface_text(font,text):
    '''return a surface from a text from a string list'''

    return font.render(text, True, [0, 0, 0])

def render(pygame,font,textlist,data,size):
    '''Render the string buffer of the image to the window'''
    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()


    text = get_surface_text(font,textlist[0])
    textrect = text.get_rect()

    screen =  pygame.display.get_surface()
    screen.blit(plot, plotrect)
    screen.blit(text, textrect)
    pygame.display.flip()
