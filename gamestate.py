import pygame

pygame.init()


class GameState:

    def __init__(self):
        pass

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self):
        pass

    @staticmethod
    def update(ticks):
        pygame.time.Clock().tick(ticks)

    @staticmethod
    def draw():
        pygame.display.update()
