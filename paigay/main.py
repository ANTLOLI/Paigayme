# import the pygame module, so you can use it
import pygame
from game import game_loop
from general_info import *
from surfaces import *

# define a main function
def main():
    pygame.init()


    # Logo loliu
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    #pygame.display.set_caption("minimal program")
     
    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        if room == ["game"]:
            game_loop()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        draw_surfaces()
        pygame.display.flip()
main()