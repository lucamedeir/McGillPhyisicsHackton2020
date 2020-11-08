import sys,pygame
import matplotlib.pyplot as plt

class Label:
    def __init__(self,font,name, value,x,y):
        self._font = font
        self._edit_mode = False
        self._name = name
        self._value = value
        self._x = x
        self._y = y

        self._textstring = name + ": " + str(value)

        surface,rect = self.render()
        self._surface = surface
        self._rect = rect

    def update_value(self,newvalue):
        self._value = newvalue
        self._textstring = self._name + ": " + str(self._value)
        surface,rect = self.render()
        self._surface = surface
        self._rect = rect

    def get_rect(self):
        return self._rect

    def get_text(self):
        return self._surface,self._rect

    def get_name(self):
        return self._name

    def render(self):
        if self._edit_mode:
            surface = self._font.render(self._textstring, True, [0, 0, 255],[255,255,255])
        else:
            surface = self._font.render(self._textstring, True, [0, 0, 0],[255,255,255])
        rect = surface.get_rect()
        rect.x = self._x
        rect.y = self._y

        return surface,rect

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
    for label in textlist:
        if label.get_rect().collidepoint(pygame.mouse.get_pos()):
            print("Click on text: ",label.get_name())


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

def render_text(screen,textlist):
    for label in textlist:
        surface,rect = label.get_text()
        screen.blit(surface,rect)

def render(pygame,textlist,data,size):
    '''Render the string buffer of the image to the window'''



    screen =  pygame.display.get_surface()

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen.blit(plot, plotrect)

    render_text(screen,textlist)

    pygame.display.flip()
