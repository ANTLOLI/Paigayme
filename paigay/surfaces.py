import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenW, screenH = screen.get_width(), screen.get_height()

print(screenW, screenH)

surfaces = []
for i in range(0, 3):
    surfaces.append(pygame.Surface((screenW, screenH)).convert_alpha())

background, buttons, texts = surfaces

def draw_surfaces():
    for surf in surfaces:
        screen.blit(surf, (0, 0))
    for surf in surfaces:
        surf.fill(0)
    
    background.fill(0)