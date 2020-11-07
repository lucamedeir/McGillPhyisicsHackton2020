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

def enter_edit_mode():
    pass

def check_if_label_was_clicked(pygame,textlist):
    for _,rect,id in textlist:
        if rect.collidepoint(pygame.mouse.get_pos()):
            print("Click on text: ",id)


def handle_events(pygame,textlist):
    '''Handle all interface events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
                print("You're moving the mouse to the right")
            elif event.rel[1] > 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
                print("You're moving the mouse down")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("You pressed the left mouse button")
                check_if_label_was_clicked(pygame,textlist)
            elif event.button == 3:
                print("You pressed the right mouse button")
        elif event.type == pygame.MOUSEBUTTONUP:
            print("You released the mouse button")

def get_surface_text(font,text,id):
    '''return a surface from a text from a string list'''
    textstring,x,y = text
    surface = font.render(textstring, True, [0, 0, 0],[255,255,255])
    rect = surface.get_rect()
    rect.x = x
    rect.y = y
    return surface,rect,id


def render_text(screen,font,textlist):
    for text,rect,_ in textlist:
        screen.blit(text, rect)

def render(pygame,font,textlist,data,size):
    '''Render the string buffer of the image to the window'''



    screen =  pygame.display.get_surface()

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen.blit(plot, plotrect)

    render_text(screen,font,textlist)

    pygame.display.flip()
