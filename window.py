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

    return font.render(text, True, [0, 0, 0],[255,255,255])

def render_text(screen,font,textlist):
    for text in textlist:
        textstring,text_x,text_y = text
        text = get_surface_text(font,textstring)
        textrect = text.get_rect()
        textrect.x = text_x
        textrect.y = text_y
        screen.blit(text, textrect)

def render(pygame,font,textlist,data,size):
    '''Render the string buffer of the image to the window'''



    screen =  pygame.display.get_surface()

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen.blit(plot, plotrect)

    render_text(screen,font,textlist)

    pygame.display.flip()
