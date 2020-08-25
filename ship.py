import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, all_settings, screen):

        super(Ship, self).__init__()

        self.screen = screen
        self.all_settings = all_settings

        # create ship and set x,y in screen
        self.image = pygame.image.load('./images/plane.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put ship in screen's center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # move sign
        self.moving_right = False
        self.moving_left = False

        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        # blit in screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.all_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.all_settings.ship_speed_factor
        if self.moving_top and self.rect.centery > self.rect.height:
            self.rect.centery -= self.all_settings.ship_speed_factor
        if self.moving_bottom and int(self.rect.centery + self.rect.height / 2) < self.screen_rect.height:
            self.rect.centery += self.all_settings.ship_speed_factor

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
