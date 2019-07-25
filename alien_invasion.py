import sys

import pygame

import game_functions as gf
from background import Background
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from pygame.sprite import Group


def run_game():

    pygame.init()

    # new Settings's Object to config use
    all_settings = Settings()

    screen = pygame.display.set_mode(
        [all_settings.screen_width, all_settings.screen_height])

    pygame.display.set_caption('war_plane')

    # create ship
    ship = Ship(all_settings, screen)
    # create many bullets
    bullets = Group()
    # create alien
    alien = Alien(all_settings, screen)
    # collect many alines
    aliens = Group()
    # create statistics
    stats = GameStats(all_settings)

    # create button
    play_button = Button(all_settings, screen, "Play")
    # create score
    score_board = Scoreboard(all_settings, screen, stats)
    # create background's iamge
    bgc = Background(screen)

    gf.create_fleet(all_settings, screen, aliens, ship)

    # start game
    while True:

        gf.check_events(ship, all_settings, screen,
                        bullets, stats, play_button, aliens, score_board)

        if stats.game_active:
            ship.update()

            gf.update_bullets(bullets, aliens, all_settings,
                              screen, ship, stats, score_board)

            gf.update_aliens(aliens, all_settings, ship,
                             stats, screen, bullets, score_board)

        gf.update_screen(all_settings, screen, ship,
                         bgc, bullets, alien, aliens, play_button, stats, score_board)


run_game()
