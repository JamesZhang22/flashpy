from .settings import *

class FlashCard:
    def __init__(self, x, y, w, h, question, answer):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.question = question
        self.answer = answer
        self.text = question
        self.color = RED
        self.hover = False
        self.clicked = False

    def draw(self, screen):
        if self.hover:
            self.color = YELLOW
            self.text = self.answer
        elif not self.hover:
            self.color = RED
            self.text = self.question

        if self.clicked:
            self.color = YELLOW
            self.text = self.answer
        elif not self.clicked:
            self.color = RED
            self.text = self.question

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0, 10)

        myfont = get_font_bold(45)
        text_surface = myfont.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.x + self.w / 2 - text_surface.get_width() / 2, self.y + self.h / 2 - text_surface.get_height() / 2))

    def is_hover(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.w):
            self.hover = False

        elif not (y >= self.y and y <= self.y + self.h):
            self.hover = False
        
        else:
            self.hover = True

    def is_clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.w):
            self.clicked = False

        elif not (y >= self.y and y <= self.y + self.h):
            self.clicked = False
        
        else:
            self.clicked = True
