import sys
from utils.button import Button
from utils import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flashpy")
icon_img = pygame.image.load("images\cards (1).png")
pygame.display.set_icon(icon_img)

# First screen start button
start_button = Button(300, 450, 300, 100, GREEN, 50, "START", WHITE)

# Main app buttons
add_button = Button(30, 100, 100, 200, GRAY, 0, None, BLACK, "images/add.png")
main_buttons = [add_button]

# Drawing Functions
def draw_start(screen):
    screen.fill(CYAN)

    font = get_font_bold(100)
    text_surface = font.render("FLASHPY", True, WHITE)
    screen.blit(text_surface, (285, 50))

    start_img = pygame.image.load("images\cards.png")
    screen.blit(start_img, (310, 130))

    start_button.draw(screen)

    pygame.display.update()


def draw_main(screen):
    screen.fill(CYAN)

    font = get_font_bold(45)
    text_surface = font.render("Your Cards", True, WHITE)
    screen.blit(text_surface, (30, 10))
    pygame.draw.line(screen, WHITE, (0, 50), (900, 50), 3)

    pygame.display.update()


# Game Loops
def start():
    on = True
    clock = pygame.time.Clock()

    while on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if start_button.clicked(pos):
                main()

        draw_start(SCREEN)


def main():
    on = True
    clock = pygame.time.Clock()

    while on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for button in main_buttons:
                    if button.clicked(pos):
                        print(1)

        draw_main(SCREEN)

if __name__ == "__main__":
    start()