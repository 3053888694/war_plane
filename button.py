import pygame.font


class Button():

    def __init__(self, all_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set button's size and value
        self.width, self.height = 100, 60
        self.button_color = (162, 199, 72)

        self.text_color = (8, 15, 12)
        self.font = pygame.font.SysFont(None, 48)

        # create button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.preg_msg(msg)

    def preg_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
