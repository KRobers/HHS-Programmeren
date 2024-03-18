import unittest
from unittest.mock import patch
from settings import Settings

class TestScreenSettings(unittest.TestCase):
    @patch('ctypes.windll.user32.GetSystemMetrics')
    def test_screen_dimensions_greater_than_standard(self, mock_GetSystemMetrics):
        # Verzin waarde
        mock_GetSystemMetrics.side_effect = [
            1600,  # Imitatie systeembreedte
            1000   # Imitatie systeemhoogte
        ]

        # Creëer een instantie van de Settings-class
        settings = Settings()

        # Controleer of de systeembreedte en -hoogte correct zijn ingesteld
        self.assertEqual(settings.screen_width, 1600)
        self.assertEqual(settings.screen_height, 1000)

    @patch('ctypes.windll.user32.GetSystemMetrics')
    def test_screen_fallback_to_standard(self, mock_GetSystemMetrics):
        #verzin waarde
        mock_GetSystemMetrics.side_effect = [
            1000,  # Imitatie systeembreedte
            600    # imitatie systeemhoogte
        ]

        # Creëer een instantie van de Settings-class
        settings = Settings()

        # Controleer of de standaardafmetingen worden gebruikt als de systeembreedte en -hoogte te klein zijn
        self.assertEqual(settings.screen_width, 1200)
        self.assertEqual(settings.screen_height, 800)

if __name__ == '__main__':
    unittest.main()