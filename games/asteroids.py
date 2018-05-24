import math
import random
import time

import pygame

import utils
from gameengine import GameEngine
import games.menu
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
        self.firing = 0
        self.bullets = []


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['bullet']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = angle


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['asteroid']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = angle
        self.size = size


class Asteroids(GameState):

    def __init__(self):
        super(Asteroids, self).__init__()
        self.ship = Ship(GameEngine.display_width / 2, GameEngine.display_height / 2)
        self.asteroids = []
        self.time = 0
        self.score = 0
        GameEngine.change_caption("Asteroids")

    def exit(self):
        GameEngine.change_caption("Classic Games in Python")

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
            self.ship.angle = (self.ship.angle + 5) % 360
        if keypresses[pygame.K_RIGHT] != 0:
            self.ship.angle = (self.ship.angle - 5) % 360
        if keypresses[pygame.K_UP] != 0:
            self.ship.acceleration = 6
        if self.ship.firing == 0 and keypresses[pygame.K_SPACE] != 0:
            self.ship.firing = 4
            self.ship.bullets.append(Bullet(self.ship.rect.x + 15, self.ship.rect.y + 17, self.ship.angle))
        if self.ship.warp == 0 and (keypresses[pygame.K_LSHIFT] != 0 or keypresses[pygame.K_RSHIFT] != 0):
            self.ship.warp = 20
            self.ship.rect.x = random.randint(0, GameEngine.display_width)
            self.ship.rect.y = random.randint(0, GameEngine.display_height)

    def update(self):
        self.ship.rect.x -= self.ship.acceleration * math.sin(math.radians(self.ship.angle))
        self.ship.rect.y -= self.ship.acceleration * math.cos(math.radians(self.ship.angle))
        self.ship.acceleration = max(self.ship.acceleration - .1, 0)
        self.ship.warp = max(self.ship.warp - .5, 0)
        self.ship.firing = max(self.ship.firing - .5, 0)
        if self.ship.rect.x > GameEngine.display_width:
            self.ship.rect.x = 0
        if self.ship.rect.x < 0:
            self.ship.rect.x = GameEngine.display_width
        if self.ship.rect.y > GameEngine.display_height:
            self.ship.rect.y = 0
        if self.ship.rect.y < 0:
            self.ship.rect.y = GameEngine.display_height
        if random.randint(0, 100) > 97:
            if random.random() > 0.5:
                if random.random() > 0.5:
                    self.asteroids.append(
                        Asteroid(0, random.randint(0, GameEngine.display_height), random.randint(0, 360), 3))
                else:
                    self.asteroids.append(
                        Asteroid(GameEngine.display_width, random.randint(0, GameEngine.display_height),
                                 random.randint(0, 360), 3))
            else:
                if random.random() > 0.5:
                    self.asteroids.append(
                        Asteroid(random.randint(0, GameEngine.display_width), 0, random.randint(0, 360), 3))
                else:
                    self.asteroids.append(
                        Asteroid(random.randint(0, GameEngine.display_width), GameEngine.display_height,
                                 random.randint(0, 360), 3))
        for bullet in self.ship.bullets:
            bullet.rect.x -= 9 * math.sin(math.radians(bullet.angle))
            bullet.rect.y -= 9 * math.cos(math.radians(bullet.angle))
            if bullet.rect.x < 0 or bullet.rect.x > GameEngine.display_width:
                self.ship.bullets.remove(bullet)
            elif bullet.rect.y < 0 or bullet.rect.y > GameEngine.display_height:
                self.ship.bullets.remove(bullet)
            else:
                for asteroid in self.asteroids:
                    if abs(bullet.rect.x - asteroid.rect.x) < 12.5 * asteroid.size and abs(
                            bullet.rect.y - asteroid.rect.y) < 12.5 * asteroid.size:
                        self.score = int(self.score + 300 / asteroid.size)
                        try:
                            self.asteroids.remove(asteroid)
                        except ValueError:
                            pass
                        try:
                            self.ship.bullets.remove(bullet)
                        except ValueError:
                            pass
                        if asteroid.size > 1:
                            self.asteroids += [
                                Asteroid(asteroid.rect.x, asteroid.rect.y, random.randint(0, 360), asteroid.size - 1),
                                Asteroid(asteroid.rect.x, asteroid.rect.y, random.randint(0, 360), asteroid.size - 1)]
        for asteroid in self.asteroids:
            asteroid.rect.x -= 4 / asteroid.size * math.sin(math.radians(asteroid.angle))
            asteroid.rect.y -= 4 / asteroid.size * math.cos(math.radians(asteroid.angle))
            if asteroid.rect.x > GameEngine.display_width:
                asteroid.rect.x = 0
            if asteroid.rect.x < 0:
                asteroid.rect.x = GameEngine.display_width
            if asteroid.rect.y > GameEngine.display_height:
                asteroid.rect.y = 0
            if asteroid.rect.y < 0:
                asteroid.rect.y = GameEngine.display_height
            if abs(self.ship.rect.x - asteroid.rect.x) < 15 * asteroid.size and abs(
                    self.ship.rect.y - asteroid.rect.y) < 15 * asteroid.size:
                GameEngine.display_data(GameEngine.display_width / 2, GameEngine.display_height / 2 - 20, "Game Over!",
                                        GameEngine.font, (255, 255, 255))
                super().draw()
                time.sleep(1)
                GameEngine.display_data(GameEngine.display_width / 2, GameEngine.display_height / 2 + 20,
                                        "Your score was: " + str(self.score), GameEngine.font, (255, 255, 255))
                super().draw()
                time.sleep(2)
                self.exit()
                GameEngine.change_state(games.menu.Menu())
        super().update(50)

    def draw(self):
        GameEngine.game_display.fill((0, 0, 0))
        GameEngine.game_display.blit(utils.rot_center(self.ship.image, self.ship.angle),
                                     (self.ship.rect.x, self.ship.rect.y))
        for bullet in self.ship.bullets:
            GameEngine.game_display.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
        for asteroid in self.asteroids:
            GameEngine.game_display.blit(
                pygame.transform.scale(asteroid.image, (25 * asteroid.size, 25 * asteroid.size)),
                (asteroid.rect.x, asteroid.rect.y))
        GameEngine.display_data(100, 20, self.score, GameEngine.font, (255, 255, 255))
        super().draw()
