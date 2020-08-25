import sys

import pygame

from bullet import Bullet

from time import sleep

from alien import Alien

from random import randint


# events's functions
def check_events(ship, all_settings, screen, bullets, stats, play_button, aliens, score_board):

    # event's trigger
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, all_settings, bullets, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # stats, play_button, mouse_x, mouse_y, alines, bullets, all_settings, screen, ship
            check_play_button(stats, play_button, mouse_x, mouse_y,
                              aliens, bullets, all_settings, screen, ship, score_board)


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, all_settings, screen, ship, score_board):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # reset game's all settings
        all_settings.initialize_dynamic_settings()

        # hide mouse
        pygame.mouse.set_visible(False)

        stats.reset_stat()
        stats.game_active = True

        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(all_settings, screen, aliens, ship)
        ship.center_ship()


def check_keydown_events(event, ship, all_settings, bullets, screen):
    if event.key == pygame.K_RIGHT:
        # right move
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(event, all_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


# screen's object function
def update_screen(ai_settings, screen, ship, bgc, bullets, alien, aliens, play_button, stats, score_board):

    screen.fill(ai_settings.bg_color)

    bgc.background()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    aliens.draw(screen)

    score_board.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


# create bullets's functions
def update_bullets(bullets, aliens, all_settings, screen, ship, stats, score_board):
    bullets.update()
    check_bullet_alien_collisions(
        all_settings, screen, ship, aliens, bullets, stats, score_board)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            # print(bullet)
            bullets.remove(bullet)


def fire_bullet(event, all_settings, screen, ship, bullets):
    if len(bullets) < all_settings.bullet_allowed:
        new_bullet = Bullet(all_settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(all_settings, screen, ship, aliens, bullets, stats, score_board):
    collisions = pygame.sprite.groupcollide(
        bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += all_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_heigh_score(stats, score_board)

    # check aliens is null?
    if len(aliens) == 0:
        bullets.empty()
        all_settings.increase_speed()

        # level up
        stats.level += 1
        score_board.prep_level()

        create_fleet(all_settings, screen, aliens, ship)


# aliens's create functions
def create_fleet(all_settings, screen, aliens, ship):
    alien = Alien(all_settings, screen)
    number_rows = get_number_rows(
        all_settings, ship.rect.width, ship.rect.height)

    # print('number_rows:', number_rows)
    for row_number in range(number_rows):
        number_aliens_x = get_number_aliens_x(all_settings, alien.rect.width)
        for alien_number in range(number_aliens_x):
            create_alien(all_settings, screen, aliens,
                         alien_number, row_number)


# return aliens's number
def get_number_aliens_x(all_settings, alien_width):
    available_space_x = all_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    number_aliens_x = randint(1, number_aliens_x)
    print('random_int:', number_aliens_x)
    return number_aliens_x


def get_number_rows(all_settings, ship_height, alien_height):
    available_space_y = (all_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(all_settings, screen, aliens, alien_number, number_row):
    alien = Alien(all_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_row
    aliens.add(alien)


def check_fleet_edges(all_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(all_settings, aliens)
            break


def update_aliens(aliens, all_settings, ship, stats, screen, bullets, score_board):
    check_fleet_edges(all_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(all_settings, stats, screen, ship,
                 aliens, bullets, score_board)

    check_aliens_bottom(all_settings, stats, screen, ship, aliens, bullets)


def change_fleet_direction(all_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += all_settings.fleet_drop_speed
    all_settings.fleet_direction *= -1


# stats
def ship_hit(all_settings, stats, screen, ship, aliens, bullets, score_board):

    if stats.ships_left > 0:
        stats.ships_left -= 1

        score_board.prep_ships()

        # clear aliens and bullets's collections
        aliens.empty()
        bullets.empty()

        create_fleet(all_settings, screen, aliens, ship)
        ship.center_ship()

        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(all_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(all_settings, stats, screen, ship, aliens, bullets)
            break


# scoreboard's functions
def check_heigh_score(stats, score_board):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()
