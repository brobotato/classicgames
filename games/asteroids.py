import pygame
import utils
import math
import random

from gameengine import GameEngine
from gamestate import GameState


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['ship']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = 0
        self.acceleration = 0
        self.warp = 0
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['ship']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = 0
        
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['ship']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.size = size
        self.angle = 0

class Asteroids(GameState):

    def __init__(self):
        super(Asteroids, self).__init__()
        self.ship = Ship(GameEngine.display_width / 2, GameEngine.display_height / 2)

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEngine.quit()
        keypresses = pygame.key.get_pressed()        
        if keypresses[pygame.K_LEFT] != 0:
            self.ship.angle = (self.ship.angle+5)%360
        if keypresses[pygame.K_RIGHT] != 0:
            self.ship.angle = (self.ship.angle-5)%360
        if keypresses[pygame.K_UP] != 0:
            self.ship.acceleration = 6
        if self.ship.warp == 0 and (keypresses[pygame.K_LSHIFT] != 0 or keypresses[pygame.K_RSHIFT] != 0):
            self.ship.warp = 20
            self.ship.rect.x = random.randint(0,GameEngine.display_width)
            self.ship.rect.y = random.randint(0,GameEngine.display_height)
            
    def update(self):
        self.ship.rect.x -= self.ship.acceleration*math.sin(math.radians(self.ship.angle))
        self.ship.rect.y -= self.ship.acceleration*math.cos(math.radians(self.ship.angle))
        self.ship.acceleration = max(self.ship.acceleration - .1,0)
        self.ship.warp = max(self.ship.warp - .5,0)
        if self.ship.rect.x > GameEngine.display_width:
            self.ship.rect.x = 0
        if self.ship.rect.x < 0:
            self.ship.rect.x = GameEngine.display_width
        if self.ship.rect.y > GameEngine.display_height:
            self.ship.rect.y = 0
        if self.ship.rect.y < 0:
            self.ship.rect.y = GameEngine.display_height
        super().update(50)

    def draw(self):
        GameEngine.game_display.fill((0,0,0))
        GameEngine.game_display.blit(utils.rot_center(self.ship.image, self.ship.angle), (self.ship.rect.x, self.ship.rect.y))
        super().draw()
