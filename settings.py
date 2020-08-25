class Settings():

    # all settings's class
    def __init__(self):
        # screen's settings
        self.screen_width = 600
        self.screen_height = 875
        self.bg_color = (230, 230, 230)

        # ship's settinfs
        self.ship_limit = 3

        # bullet's settings
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # aline's settings
        self.fleet_drop_speed = 10

        # speed's settings
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 5

        self.fleet_direction = 1

        # point
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
