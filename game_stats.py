class GameStats():

    def __init__(self, all_settings):
        self.all_settings = all_settings

        self.reset_stat()

        self.game_active = False

        self.high_score = 0

    def reset_stat(self):
        self.ships_left = self.all_settings.ship_limit
        self.score = 0
        self.level = 1
