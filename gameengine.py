import os

import pygame

import utils

pygame.init()


class GameEngine:
    states = []
    run = False
    display_width = 0
    display_height = 0
    font = None
    clock = None
    game_display = None
    sprite_dict = None

    @staticmethod
    def __init__(width, height, caption):
        GameEngine.states = []
        GameEngine.run = True

        GameEngine.display_width = width
        GameEngine.display_height = height

        GameEngine.font = pygame.font.Font("resources/vgaoem.fon", 15)
        GameEngine.clock = pygame.time.Clock()
        GameEngine.sprite_dict = {filename[:-4]: utils.create_image(filename[:-4]) for filename in
                                  os.listdir('resources') if filename[-4:] == '.png'}

        pygame.display.set_mode((GameEngine.display_width, GameEngine.display_height))
        pygame.display.set_caption(caption)

        GameEngine.game_display = pygame.display.get_surface()

    @staticmethod
    def change_state(state):
        if not GameEngine.states:
            GameEngine.states.append(state)
        else:
            GameEngine.states[-1].exit()
            GameEngine.states[-1] = state

    @staticmethod
    def pause_state(state):
        if not GameEngine.states:
            pass
        else:
            GameEngine.states[-1].pause()
            GameEngine.states.append(state)

    @staticmethod
    def resume_state():
        if not GameEngine.states:
            pass
        else:
            GameEngine.states = GameEngine.states[:-1]
            GameEngine.states[-1].resume()

    @staticmethod
    def handle_events():
        GameEngine.states[-1].handle_events()

    @staticmethod
    def update():
        GameEngine.states[-1].update()

    @staticmethod
    def draw():
        GameEngine.states[-1].draw()

    @staticmethod
    def running():
        return GameEngine.run

    @staticmethod
    def display_data(x, y, data, font, color):
        data_text = font.render("{0}".format(data), True, color)
        GameEngine.game_display.blit(data_text,
                                     (x - data_text.get_rect().width / 2, y - data_text.get_rect().height / 2))

    @staticmethod
    def quit():
        pygame.quit()
        quit()
