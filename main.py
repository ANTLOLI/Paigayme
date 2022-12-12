# import the pygame module, so you can use it
import pygame
from game_console_code import game_execute
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
        if room[0] == "game":
            game_execute()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            draw_surfaces()

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()