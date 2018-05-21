import pygame

import gameengine
import games

pygame.init()


# rotate an image while keeping its center and size
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


game = gameengine.GameEngine(800, 600, 'Classic Games in Python')
# menu_state = menu.MenuState()
asteroids = games.Asteroids()

# game.change_state(menu_state)
game.change_state(asteroids)

while game.running():
    game.handle_events()
    game.update()
    game.draw()
