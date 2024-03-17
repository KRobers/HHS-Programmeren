import ctypes # importeert CTypes
class Settings():

    def __init__(self):
        # Krijg de systeembreedte en hoogte
        user = ctypes.windll.user32
        breedte = user.GetSystemMetrics(0)
        hoogte = user.GetSystemMetrics(1)

        # Controleer of de systeembreedte en -hoogte groter zijn dan 1200 en 800
        if breedte > 1200 and hoogte > 800:
            self.screen_width = breedte
            self.screen_height = hoogte

        # Gebruik de minimale  breedte en hoogte als fallback
        else:
            self.screen_width = 1200
            self.screen_height = 800

        # Stel de achtergrondkleur in
        self.bg_color = (0, 0, 0)
