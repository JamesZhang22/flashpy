import sys, random
from utils.button import Button
from utils import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flashpy")
icon_img = pygame.image.load("images\cards (1).png")
pygame.display.set_icon(icon_img)

# First screen start button
start_button = Button(300, 450, 300, 100, GREEN, 50, "START", BLACK)

# Main app buttons
add_button = Button(10, 80, 100, 200, GRAY, 0, None, BLACK, "images/add.png")
test_button = Button(700, 5, 80, 40, CYAN, 45, "Test", BLACK)
main_buttons = [add_button, test_button]

# add card buttons
q_button = Button(240, 200, 410, 50, GRAY, 30, '', BLACK)
a_button = Button(240, 300, 410, 50, GRAY, 30, '', BLACK)
done_button = Button(400, 380, 100, 40, GREEN, 30, "Done", BLACK)
add_card_buttons = [q_button, a_button, done_button]

# flashcards
question_answer = {}
flashcards = []

main_flashcard = FlashCard(100, 120, 700, 400, '', '')

# arrows
right_arrow = Button(820, 268, 64, 64, CYAN, 1, None, BLACK, "images/right-arrow.png")
left_arrow = Button(16, 268, 64, 64, CYAN, 1, None, BLACK, "images\left-arrow.png")

# close test
close_test = Button(375, 535, 150, 50, RED, 30, "RETURN", "BLACK")

# Drawing Functions
def draw_start(screen):
    screen.fill(CYAN)

    font = get_font_bold(100)
    text_surface = font.render("FLASHPY", True, BLACK)
    screen.blit(text_surface, (285, 50))

    start_img = pygame.image.load("images\cards.png")
    screen.blit(start_img, (310, 130))

    start_button.draw(screen)

    pygame.display.update()


def draw_main(screen, card):
    screen.fill(CYAN)

    font = get_font_bold(45)
    text_surface = font.render("Your Cards", True, BLACK)
    screen.blit(text_surface, (30, 10))

    pygame.draw.line(screen, BLACK, (0, 50), (900, 50), 3)

    for button in main_buttons:
        button.draw(screen)

    for flashcard in flashcards:
        flashcard.draw(screen)

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

    pygame.display.update()


def draw_test(screen, finish):
    screen.fill(CYAN)

    font = get_font_bold(45)
    text_surface = font.render("Test", True, BLACK)
    screen.blit(text_surface, (420, 10))
    pygame.draw.line(screen, BLACK, (0, 50), (900, 50), 3)

    right_arrow.draw(SCREEN)
    left_arrow.draw(SCREEN)
    main_flashcard.draw(screen)

    if finish:
        close_test.draw(SCREEN)

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

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            start_button.is_hover(pos)

        draw_start(SCREEN)


def main():
    on = True
    clock = pygame.time.Clock()
    add_card = False
    q_pressed = False
    a_pressed = False
    finish = False
    test = False
    index = 0

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
                    elif button.text == "Test" and button.clicked(pos):
                        index = 0
                        finish = False
                        question_answer_keys = list(question_answer.keys())
                        random.shuffle(question_answer_keys)
                        main_flashcard.question = question_answer_keys[index]
                        main_flashcard.answer = question_answer[question_answer_keys[index]]

                        test = True
                if finish:
                    if close_test.clicked(pos):
                        test = False

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
                        elif add_card_button.y == 380 and add_card_button.clicked(pos):
                            question_answer[q_button.text] = a_button.text
                            if len(flashcards) > 6:
                                y_val = 300
                                x_val = 110 * (len(flashcards) - 7) + 10 
                            else:
                                x_val = 110 * len(flashcards) + 120 
                                y_val = 80
                            new_card = FlashCard(x_val, y_val, 100, 200, q_button.text, a_button.text)
                            flashcards.append(new_card)
                            q_button.text = ''
                            a_button.text = ''
                            add_card =  False

            if test:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    main_flashcard.is_clicked(pos)
                    if right_arrow.clicked(pos) and index >= len(question_answer_keys) - 1:
                        main_flashcard.question = main_flashcard.answer = "Finished!"
                        finish = True
                    elif right_arrow.clicked(pos) and index < len(question_answer_keys) - 1:
                        index += 1
                        main_flashcard.question = question_answer_keys[index]
                        main_flashcard.answer = question_answer[question_answer_keys[index]]
                    elif left_arrow.clicked(pos) and 0 < index < len(question_answer_keys):
                        index -= 1
                        main_flashcard.question = question_answer_keys[index]
                        main_flashcard.answer = question_answer[question_answer_keys[index]]

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

            if event.type == pygame.MOUSEMOTION and not add_card:
                pos = event.pos
                for flashcardz in flashcards:
                    flashcardz.is_hover(pos)
                for main_button in main_buttons:
                    main_button.is_hover(pos)
                
        if q_pressed:
            q_button.color = DARK_GRAY
            a_button.color = GRAY
        elif a_pressed:
            a_button.color = DARK_GRAY
            q_button.color = GRAY
        else:
            q_button.color = GRAY
            a_button.color = GRAY
        
        if test:
            draw_test(SCREEN, finish)
        elif not test:
            draw_main(SCREEN, add_card)


if __name__ == "__main__":
    start()