import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""

        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score (it should never be reset)
        self._read_high_score()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def _read_high_score(self):
        """Read the current high score from a file."""

        try:
            with open('C:/Users/Marko/Desktop/Miloš/PYTHON/Alien Invasion/high_score.json') as f:
                hs = json.load(f)

        except ValueError or FileNotFoundError:
            hs = None
        

        if hs:
            self.high_score = hs
        else:
            self.high_score = 0
