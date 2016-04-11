from enum import Enum

class DiceOutcome(Enum):
    One=1
    Two=2
    Three=3
    Four=4
    Five=5
    Six=6

class LiarsDiceGame ():
    def __init__(self, game_id, host_id):
        self.game_id = game_id
        self.host_id = host_id

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def group_id(self, value):
        self._game_id = value

    @property
    def host_id(self):
        return self._host_id

    @host_id.setter
    def host_id(self, value):
        self._host_id = value