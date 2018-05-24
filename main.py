import pygame

import gameengine
import games

pygame.init()

game = gameengine.GameEngine(800, 600, 'Classic Games in Python')
menu = games.Menu()

game.change_state(menu)

while game.running():
    game.handle_events()
    game.update()
    game.draw()
