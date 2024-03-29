import ctypes
class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""

        #Zorgt voor responsive game die hem automatisch aanpast
        user = ctypes.windll.user32
        breedte = user.GetSystemMetrics(0)
        hoogte = user.GetSystemMetrics(1)

        self.standard_screen_width = 1200
        self.standard_screen_height = 800

        # Controleer of de systeembreedte en -hoogte groter zijn dan 1200 en 800
        if breedte > 1200 and hoogte > 800:
            self.screen_width = breedte
            self.screen_height = hoogte

        # Gebruik de minimale  breedte en hoogte als fallback
        else:
            self.screen_width = self.standard_screen_width
            self.screen_height = self.standard_screen_height

        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        #zorgt ervoor dat afhankelijk van de resolutie de snelheiden hetzelfde blijven met een ratio
        width_ratio = self.screen_width / self.standard_screen_width

        # snelheden worden vermenigvuldigd tegen de ratio
        self.ship_speed = 7 * width_ratio
        self.bullet_speed = 2.5 * width_ratio
        self.alien_speed = 1.0 * width_ratio

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50
        self.alien2_points = 250 #extra puntjes voor alien 2
        self.alien2_chance = 0.05 #percentage kans dat de moeilijkere spawnt.

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien2_points = int(self.alien_points * self.score_scale) #toegevoegd voor alien2 class