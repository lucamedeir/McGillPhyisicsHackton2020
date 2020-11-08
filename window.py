import sys,pygame
import matplotlib.pyplot as plt

class Label:
    def __init__(self,font,name, value,x,y,editable=True,is_int=False):
        self._font = font
        self._edit_mode = False
        self._name = name
        self._value = value
        self._edit_mode_value = str(value)
        self._x = x
        self._is_int = is_int
        self._y = y
        self._editable = editable

        self.render_and_update()

    def remove_edit_mode_value(self):
        if len(self._edit_mode_value)>0:
            self._edit_mode_value = self._edit_mode_value[:-1]
            self.render_and_update()

    def update_edit_mode_value(self,text):
        self._edit_mode_value += text
        self.render_and_update()

    def update_value(self,newvalue):
        self._value = newvalue
        self._textstring = self._name + ": " + str(self._value)
        self.render_and_update()

    def enter_edit_mode(self):
        if self._editable:
            self._edit_mode = True
            self.render_and_update()

    def quit_edit_mode(self):
        self._edit_mode = False
        if not self._is_int:
            self._value = float(self._edit_mode_value)
        else:
            self._value = int(self._edit_mode_value)
        self.render_and_update()

    def get_rect(self):
        return self._rect

    def get_text(self):
        return self._surface,self._rect

    def get_name(self):
        return self._name

    def render_and_update(self):

        if self._edit_mode:
            self._textstring = self._name + ": " + self._edit_mode_value
            surface = self._font.render(self._textstring, True, [0, 0, 0],[0,255,0])
        elif self._editable:
            self._textstring = self._name + ": " + str(self._value)
            surface = self._font.render(self._textstring, True, [255, 0, 0],[255,255,255])
        else:
            self._textstring = self._name + ": " + str(self._value)
            surface = self._font.render(self._textstring, True, [0, 0, 0],[255,255,255])
        rect = surface.get_rect()
        rect.x = self._x
        rect.y = self._y

        self._surface = surface
        self._rect = rect

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

def finish_all_edit_modes(textlist):
    for label in textlist:
        if label._edit_mode:
            label.quit_edit_mode()

def check_if_label_was_clicked(pygame,textlist):
    finish_all_edit_modes(textlist)
    for label in textlist:
        if label.get_rect().collidepoint(pygame.mouse.get_pos()):
            label.enter_edit_mode()
            print("Click on text: ",label.get_name())

def update_in_edit_mode_label(textlist,key):
    for label in textlist:
        if label._edit_mode:
            label.update_edit_mode_value(key)

def remove_in_edit_mode_label(textlist):
    for label in textlist:
        if label._edit_mode:
            label.remove_edit_mode_value()

def handle_events(pygame,textlist):
    '''Handle all interface events'''
    update_variables = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_RETURN:
                finish_all_edit_modes(textlist)
                print("Return clicked")
            elif event.key == pygame.K_u:
                update_variables = True
            elif event.key == pygame.K_0 or \
                 event.key == pygame.K_1 or \
                 event.key == pygame.K_2 or \
                 event.key == pygame.K_3 or \
                 event.key == pygame.K_4 or \
                 event.key == pygame.K_5 or \
                 event.key == pygame.K_6 or \
                 event.key == pygame.K_7 or \
                 event.key == pygame.K_8 or \
                 event.key == pygame.K_9 or \
                 event.key == pygame.K_PERIOD:
                    print("Clicked: ",event.unicode)
                    update_in_edit_mode_label(textlist,event.unicode)

            elif event.key == pygame.K_BACKSPACE:
                remove_in_edit_mode_label(textlist)
                print("clicked backspace")
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
    return update_variables

def render_text(screen,textlist):
    for label in textlist:
        surface,rect = label.get_text()
        screen.blit(surface,rect)

def clear_screen(pygame,):
    screen =  pygame.display.get_surface()
    screen.fill([255,255,255])

def render(pygame,textlist,data,size):
    '''Render the string buffer of the image to the window'''



    screen =  pygame.display.get_surface()

    plot = pygame.image.fromstring(data, size, "RGB")
    plotrect = plot.get_rect()
    screen.blit(plot, plotrect)

    render_text(screen,textlist)

    pygame.display.flip()
