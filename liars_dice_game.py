from enum import Enum
from datetime import datetime

class DiceOutcome(Enum):
    One=1
    Two=2
    Three=3
    Four=4
    Five=5
    Six=6

class GameType(Enum):
    GroupInitiated = 1
    PrivateInitiated = 2


class Player:
    def __init__(self, player_id, player_name):
        self._play_id = player_id
        self.player_name = player_name

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value):
        self._play_id = value

    @property
    def player_name(self):
        return self._player_name

    @player_name.setter
    def player_name(self, value):
        self._player_name = value


class LiarsDiceGame:
    def __init__(self, game_id, host_id, group_id):
        self.game_id = game_id
        self.host_id = host_id
        self.group_id = group_id
        if self.group_id == 0:
            self.game_type = GameType.PrivateInitiated
        else:
            self.game_type = GameType.GroupInitiated
        self.create_time = datetime.now()
        self.player_list = []

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

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    @property
    def game_type(self):
        return self._game_type

    @game_type.setter
    def game_type(self, value):
        self.game_type = value

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value

    @property
    def player_list(self):
        return self._player_list

    @player_list.setter
    def player_list(self, value):
        self.player_list = value
