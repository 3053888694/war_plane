import pygame


class Background():

    def __init__(self, screen):

        self.screen = screen
        self.background_image = pygame.image.load('./images/background.png')
        self.rect = self.background_image.get_rect()

    def background(self):

        self.screen.blit(self.background_image, self.rect)
