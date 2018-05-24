import math
import random
import time

import pygame

import games.menu
from gameengine import GameEngine
from gamestate import GameState


class Apple():
    def __init__(self):
        self.x = random.randint(0, 39)
        self.y = random.randint(0, 29)

    def reseed(self, snake):
        x, y = random.randint(0, 39), random.randint(0, 29)
        if [x, y] in snake:
            self.reseed(snake)
        else:
            self.x, self.y = x, y


class Snake(GameState):

    def __init__(self):
        super(Snake, self).__init__()
        self.snake = [[19, 15], [20, 15], [20, 15], [20, 15]]
        self.direction = 180
        self.apple = Apple()
        self.score = 0
        GameEngine.change_mode(640, 480)
        GameEngine.change_caption("Snake")

    def exit(self):
        GameEngine.change_mode(GameEngine.display_width, GameEngine.display_height)
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
        if keypresses[pygame.K_UP] != 0:
            if self.direction != 90:
                self.direction = -90
        if keypresses[pygame.K_LEFT] != 0:
            if self.direction != 0:
                self.direction = 180
        if keypresses[pygame.K_RIGHT] != 0:
            if self.direction != 180:
                self.direction = 0
        if keypresses[pygame.K_DOWN] != 0:
            if self.direction != -90:
                self.direction = 90

    def update(self):
        gameover = False
        self.score = len(self.snake) - 4
        for index, s in enumerate(self.snake[-1:0:-1]):
            s[0], s[1] = [self.snake[len(self.snake) - 2 - index][0], self.snake[len(self.snake) - 2 - index][1]]
        self.snake[0][0] += int(math.cos(math.radians(self.direction)))
        self.snake[0][1] += int(math.sin(math.radians(self.direction)))
        if self.snake[0] == [self.apple.x, self.apple.y]:
            self.snake.append([self.snake[-1][0], self.snake[-1][1]])
            self.apple.reseed(self.snake)
        for s in self.snake[1:]:
            if s == self.snake[0]:
                gameover = True
        if 0 <= self.snake[0][0] < 40 and 0 <= self.snake[0][1] < 30:
            pass
        else:
            gameover = True
        if gameover == True:
            GameEngine.display_data(320, 220, "Game Over!", GameEngine.font, (255, 255, 255))
            super().draw()
            time.sleep(1)
            GameEngine.display_data(320, 260 + 20,
                                    "Your score was: " + str(self.score), GameEngine.font, (255, 255, 255))
            super().draw()
            time.sleep(2)
            self.exit()
            GameEngine.change_state(games.menu.Menu())
        super().update(15)

    def draw(self):
        GameEngine.game_display.fill((0, 0, 0))
        for s in self.snake:
            GameEngine.game_display.blit(GameEngine.sprite_dict['block'], (s[0] * 16, s[1] * 16))
        GameEngine.game_display.blit(GameEngine.sprite_dict['block'], (self.apple.x * 16, self.apple.y * 16))
        super().draw()
