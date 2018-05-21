import pygame

from gameengine import GameEngine
from gamestate import GameState


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameEngine.sprite_dict['ship']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


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

    def update(self):
        super().update(50)

    def draw(self):
        GameEngine.game_display.blit(self.ship.image, (self.ship.rect.x, self.ship.rect.y))
        super().draw()
