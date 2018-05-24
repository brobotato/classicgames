import pygame

from gameengine import GameEngine
import games.asteroids
import games.snake
from gamestate import GameState


class Menu(GameState):

    def __init__(self):
        super(Menu, self).__init__()

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self):
        pos = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEngine.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
        if 360 < pos[0] < 440 and 395 < pos[1] < 405:
            GameEngine.change_state(games.asteroids.Asteroids())
        elif 360 < pos[0] < 440 and 435 < pos[1] < 445:
            GameEngine.change_state(games.snake.Snake())

    def update(self):
        super().update(50)

    def draw(self):
        GameEngine.game_display.fill((0, 0, 0))
        GameEngine.display_data(400, 125, "Classic Games in Python", GameEngine.font, (255, 255, 255))
        GameEngine.display_data(400, 400, "Asteroids", GameEngine.font, (255, 255, 255))
        GameEngine.display_data(400, 440, "Snake", GameEngine.font, (255, 255, 255))
        super().draw()
