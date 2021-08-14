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
add_button = Button(30, 80, 100, 200, GRAY, 0, None, BLACK, "images/add.png")
main_buttons = [add_button]

# add card buttons
q_button = Button(240, 200, 410, 50, GRAY, 30, '', BLACK)
a_button = Button(240, 300, 410, 50, GRAY, 30, '', BLACK)
done_button = Button(400, 380, 100, 40, GREEN, 30, "Done", WHITE)
add_card_buttons = [q_button, a_button, done_button]

# flashcards
question_answer = {}

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


def draw_main(screen, card):
    screen.fill(CYAN)

    font = get_font_bold(45)
    text_surface = font.render("Your Cards", True, WHITE)
    screen.blit(text_surface, (30, 10))

    pygame.draw.line(screen, WHITE, (0, 50), (900, 50), 3)

    for button in main_buttons:
        button.draw(screen)

    if card:
        # transparent
        shape_surf = pygame.Surface(pygame.Rect((0, 0, 900, 600)).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, (0, 0, 0, 127), shape_surf.get_rect())
        screen.blit(shape_surf, (0, 0, 900, 600))

        # card
        pygame.draw.rect(screen, WHITE, (225, 150, 450, 300))

        # labels
        font2 = get_font_bold(30)
        text_surface_q = font2.render("Question", True, BLACK)
        text_surface_a = font2.render("Answer", True, BLACK)
        screen.blit(text_surface_q, (240, 170))
        screen.blit(text_surface_a, (240, 270))

        for button_add in add_card_buttons:
            button_add.draw(screen)
        # question_surface = font2.render(input_q, True, BLACK)
        # answer_surface = font2.render(input_a, True, BLACK)
        # screen.blit(question_surface, (240, 200))
        # screen.blit(answer_surface, (240, 300))

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
    add_card = False
    q_pressed = False
    a_pressed = False

    while on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                q_pressed = False
                a_pressed = False
                for button in main_buttons:
                    if button.image == "images/add.png" and button.clicked(pos):
                        add_card = True

            if add_card:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    q_pressed = False
                    a_pressed = False
                    for add_card_button in add_card_buttons:
                        if add_card_button.y == 200 and add_card_button.clicked(pos):
                            q_pressed = True
                        elif add_card_button.y == 300 and add_card_button.clicked(pos):
                            a_pressed = True

            if event.type == pygame.KEYDOWN:
                if q_pressed:
                    if event.key == pygame.K_BACKSPACE:
                        q_button.text = q_button.text[:-1]
                    else:
                        q_button.text += event.unicode
                elif a_pressed:
                    if event.key == pygame.K_BACKSPACE:
                        a_button.text = a_button.text[:-1]
                    else:
                        a_button.text += event.unicode
            
                

            

        draw_main(SCREEN, add_card)


if __name__ == "__main__":
    start()