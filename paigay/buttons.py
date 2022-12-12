from re import I
import pygame
from general_info import *
from surfaces import *

class Button:
    image=""
    available=True

    def __init__(self, x, y, command, image,text):
        self.x=x
        self.y=y
        self.command=command
        self.image=pygame.image.load(image)
        self.text=text
    
    def interaction(self):
        if self.available == True:
            left, middle, right = pygame.mouse.get_pressed()

            if self.image.get_rect().collidepoint(pygame.mouse.get_pos()):
                if left:
                    self.command()
    
    def draw_self(self):
        buttons.blit(self.image, (self.x, self.y))

        text_image = main_font.render(self.text, False, (0, 0, 0))
        texts.blit(text_image, (self.x, self.y))
    
    def execute_self(self):
        self.interaction()
        self.draw_self()
