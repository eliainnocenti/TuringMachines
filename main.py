import os
import importlib
import pygame
import time

tm = None
machine_input = ''

machine_files = os.listdir('machines')
machine_names = [file[:-3] for file in machine_files if file.endswith('.py')]

while machine_input.lower() == 'list' or machine_input not in machine_names:
    machine_input = input("\nEnter the machine to run or type 'list' to see available machines: ")

    if machine_input.lower() == 'list':
        print("Available machines:", machine_names)
    elif machine_input not in machine_names:
        print(f"No machine named '{machine_input}' found in the 'machines' directory.")
    else:
        machine_module = importlib.import_module(f"machines.{machine_input}")
        create_tm = machine_module.create_tm

        tape_input = input("Enter the tape input (unary): ")
        if not all(char == '1' or char == ' ' for char in tape_input): # TODO: update
            raise ValueError("Invalid input. The tape input must be unary (a string of 1s).")
        tape_input = " " + tape_input
        tm = create_tm(tape_input)

if tm is not None:
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

        # FIXME: add a way to change the window dimensions dinamically

        # Window dimensions
        WINDOW_WIDTH = 1200
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

            tm.step()

            time.sleep(0.05)

        pygame.quit()

    else:
        print("Invalid input.")
