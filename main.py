import pygame
import time
from turingmachine import TuringMachine

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

# Definition of the Turing machine with custom symbols
tm = TuringMachine(
    # f(x) = x^2
    tape=" 1111",
    blank_symbol=" ",
    initial_state="q0",
    final_states={"h"},
    transition_function={ # TODO: FIXME
        ("q0",  " "): ("q1",  " ", "R"), # 1
        ("q1",  " "): ("h",   " ", "L"), # 2
        ("q1",  "1"): ("q2",  "*", "R"), # 3
        ("q2",  "1"): ("q2",  "1", "R"), # 4 a
        ("q2",  "#"): ("q2",  "#", "R"), # 4 b
        ("q2",  " "): ("q3",  "#", "L"), # 5
        ("q2",  " "): ("q15", " ", "L"), # 6
        ("q3",  "1"): ("q3",  "1", "L"), # 7 a
        ("q3",  "#"): ("q3",  "#", "L"), # 7 b
        ("q3",  "*"): ("q4",  "*", "R"), # 8
        ("q4",  "1"): ("q5",  "2", "R"), # 9
        ("q5",  "1"): ("q5",  "1", "R"), # 10
        ("q5",  "#"): ("q6",  "#", "R"), # 11
        ("q6",  "#"): ("q6",  "#", "R"), # 12
        ("q6",  " "): ("q7",  "x", "L"), # 13
        ("q7",  "1"): ("q7",  "1", "L"), # 14 a
        ("q7",  "x"): ("q7",  "x", "L"), # 14 b
        ("q7",  "#"): ("q7",  "#", "L"), # 14 c
        ("q7",  "2"): ("q8",  "2", "R"), # 15
        ("q8",  "1"): ("q9",  "2", "R"), # 16
        ("q8",  "#"): ("q10", "-", "R"), # 17
        ("q9",  " "): ("q7",  "1", "L"), # 18
        ("q9",  "1"): ("q9",  "1", "R"), # 19 a
        ("q9",  "x"): ("q9",  "x", "R"), # 19 b
        ("q9",  "#"): ("q9",  "#", "R"), # 19 c
        ("q10", "1"): ("q10", "1", "R"), # 20 a
        ("q10", "x"): ("q10", "x", "R"), # 20 b
        ("q10", "#"): ("q10", "#", "R"), # 20 c
        ("q10", " "): ("q11", "#", "L"), # 21
        ("q11", "1"): ("q20", "1", "L"), # 22 a
        ("q11", "#"): ("q20", "#", "L"), # 22 b
        ("q11", "x"): ("q21", "x", "R"), # 23
        ("q12", "x"): ("q2",  "*", "R"), # 24
        ("q12", "#"): ("q8",  "#", "S"), # 25
        ("q15", "1"): ("q15", "1", "L"), # 26
        ("q15", " "): ("h",   " ", "S"), # 27
        ("q20", "-"): ("q12", "-", "R"), # 28
        ("q20", "1"): ("q20", "1", "L"), # 29 a
        ("q20", "x"): ("q20", "x", "L"), # 29 b
        ("q20", "#"): ("q20", "#", "L"), # 29 c
        ("q21", "#"): ("q22", " ", "L"), # 30
        ("q22", "2"): ("q22", "1", "L"), # 31 a
        ("q22", "x"): ("q22", "1", "L"), # 31 b
        ("q22", "*"): ("q22", "1", "L"), # 31 c
        ("q22", "#"): ("q22", "1", "L"), # 31 d
        ("q22", "-"): ("q22", "1", "L"), # 31 e
        ("q22", " "): ("h",   " ", "S"), # 32
    },
    tape_symbols={"1", "2", "x", "*", "#", "-", " "},  # Define the tape symbols
    # 2 == 1°, * == x°, - == #°     # TODO: redefine
)

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
'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_tape(tm)
    pygame.display.flip()

    if not tm.step():
        running = False

    time.sleep(0.5)

pygame.quit()
'''

tm.run()
print("Final Tape:", tm.get_tape())
print("\nTransitions Log:")
tm.print_transitions_log()