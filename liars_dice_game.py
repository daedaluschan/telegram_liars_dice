class LiarsDiceGame ():
    def __init__(self):
        self.game_id = ''

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def group_id(self, value):
        self._game_id = value