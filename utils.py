import pygame

pygame.init()


def create_image(sprite_name):
    return pygame.image.load('resources/{0}.png'.format(sprite_name))


def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
