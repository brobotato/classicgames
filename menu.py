import pygame

from gameengine import GameEngine
from gamestate import GameState


class MenuState(GameState):

    def __init__(self):
        super(MenuState, self).__init__()

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

    def update(self):
        super().update(50)

    def draw(self):
        GameEngine.display_data(400, 125, "Classic Games in Python", GameEngine.font, (255, 255, 255))
        super().draw()
