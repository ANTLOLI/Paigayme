import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()
surfaces = []
for i in range(0, 3):
    surfaces.append(pygame.Surface((w, h)))

background, buttons, texts = surfaces

def draw_surfaces():
    for surf in surfaces:
        screen.blit(surf, (0, 0))