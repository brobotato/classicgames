import pygame

pygame.init()


def create_image(sprite_name):
    return pygame.image.load('resources/{0}.png'.format(sprite_name))


def rot_center(image, angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite
