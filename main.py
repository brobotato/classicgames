import pygame

import gameengine
import games

pygame.init()

game = gameengine.GameEngine(800, 600, 'Classic Games in Python')
menu = games.Menu()
asteroids = games.Asteroids()

# game.change_state(menu)
game.change_state(asteroids)

while game.running():
    game.handle_events()
    game.update()
    game.draw()
