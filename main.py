import pygame
import time
from machines.x_squared import tm

visualization_choice = input("Do you want to execute the program with pygame visualization? (y/n): ")

if visualization_choice.lower() == "n":

    tm.run()
    print("\nFinal Tape:", tm.get_tape())
    print("\nTransitions Log:")
    tm.print_transitions_log()
    exit()

elif visualization_choice.lower() == "y":

    # Pygame initialization
    pygame.init()

    # Window dimensions
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 200
    TAPE_CELL_SIZE = 40
    TAPE_HEIGHT = 50

    # Window creation
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Turing Machine Visualization')

    # Function to draw the tape
    def draw_tape(tm):
        tape = tm.get_tape()
        head_position = tm.get_head_position()

        for i, symbol in enumerate(tape):
            cell_color = (255, 255, 255) if i != head_position else (255, 0, 0)
            pygame.draw.rect(screen, cell_color, (i * TAPE_CELL_SIZE, TAPE_HEIGHT, TAPE_CELL_SIZE, TAPE_CELL_SIZE))
            text = font.render(symbol, True, (0, 0, 0))
            screen.blit(text, (i * TAPE_CELL_SIZE + 15, TAPE_HEIGHT + 10))

    # Main loop
    font = pygame.font.Font(None, 36)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))
        draw_tape(tm)
        pygame.display.flip()

        #if not tm.step():
        #    running = False

        tm.step()

        time.sleep(0.05)

    pygame.quit()

else:
    print("Invalid input.")