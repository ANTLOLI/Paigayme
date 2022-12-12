import pygame
from game_rooms import *
from general_info import *
from buttons import Button
from functools import partial

# Constantes
def demo():
   pass

w, h = pygame.display.get_surface().get_size()

# Criando botões
buttons = [
    Button(w-300,h-300, demo, 'imgs/button.png', ''),
    Button(w-500,h-600, demo, 'imgs/button.png', ''),
    Button(w-700,h-300, demo, 'imgs/button.png', ''),
    Button(w-500,h-150, demo, 'imgs/button.png', ''),
]

contact_texts = ['direita', 'cima', 'esquerda', 'baixo']

initialized = False

def go_to_room(game_room):
    for i, button in enumerate(buttons):
        contact = game_room.contacts[i]
        button.text = '' if contact == '' else contact_texts[i]
        button.command = demo() if contact == '' else partial(go_to_room, game_room)

def initialize_game():
    go_to_room(maze[starting_pos[0]][starting_pos[1]])

def game_loop():
    global initialized
    if initialized == False:
        initialized = True
        initialize_game()

    # Drawing buttons
    for button in buttons:
        button.execute_self()