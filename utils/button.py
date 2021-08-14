from .settings import *

class Button:
    def __init__(self, x, y, w, h, color, font_size, text = None, text_color = BLACK, image = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.font_size = font_size
        self.text = text
        self.text_color = text_color
        self.image = image
        self.hover = False

    def draw(self, screen):
        if self.image == "images/add.png":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0, 10)
        elif self.image != "images/add.png":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

        if self.hover and self.text == "START":
            self.color = LIGHT_GREEN
        elif not self.hover and self.text == "START":
            self.color = GREEN

        if self.hover and self.image == "images/add.png":
            self.color = DARK_GRAY
        elif not self.hover and self.image == "images/add.png":
            self.color = GRAY
        
        if self.text:
            myfont = get_font_bold(self.font_size)
            text_surface = myfont.render(self.text, True, self.text_color)
            screen.blit(text_surface, (self.x + self.w / 2 - text_surface.get_width() / 2, self.y + self.h / 2 - text_surface.get_height() / 2))
        
        if self.image:
            self.image_load = pygame.image.load(self.image)
            screen.blit(self.image_load, (self.x + (self.w - self.image_load.get_width()) / 2, self.y + (self.h - self.image_load.get_height()) / 2))

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.w):
            return False

        if not (y >= self.y and y <= self.y + self.h):
            return False
        
        return True

    def is_hover(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.w):
            self.hover = False

        elif not (y >= self.y and y <= self.y + self.h):
            self.hover = False
        
        else:
            self.hover = True