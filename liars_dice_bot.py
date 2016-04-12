# coding=UTF8
__author__ = 'daedaluschan'

import sys, time
import telepot
from telepot.delegate import per_chat_id, create_open

from datetime import date
from types import *
from enum import Enum
import re
from random import randint

from liars_dice_config import *
from liars_dice_script import *
from liars_dice_game import LiarsDiceGame, DiceOutcome, Player
from liars_dice_util import chkNConv

all_games = {}
group_index = {}

class ConverType(Enum):
    nothing = 1

def genNewRoomNumber():
    return randint(game_room_starts, game_room_ends)

class LiarsDiceBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(LiarsDiceBot, self).__init__(seed_tuple, timeout)
        self._convert_type = ConverType.nothing
        print(u'constructor is being called')

    def create_game(self, msg):
        print(u'new game now')
        content_type, chat_type, _chat_id = telepot.glance2(msg)
        game_id = genNewRoomNumber()
        while game_id in all_games:
            game_id = genNewRoomNumber()
        print(u'new game with game id: ' + chkNConv(game_id.__str__()))
        if chat_type == 'group' or chat_type == 'supergroup':
            all_games[game_id] = LiarsDiceGame(game_id=game_id,
                                           host_id=msg['from']['id'],
                                           group_id=msg['chat']['id'])
            group_index[msg['chat']['id']] = game_id
        else:
            all_games[game_id] = LiarsDiceGame(game_id=game_id,
                                           host_id=msg['from']['id'],
                                           group_id=0)

        all_games[game_id].player_list.append(Player(msg['from']['id']), msg['from']['first_name'])
        start_url = telegram_base_url + bot_name + '?start=' + game_id.__str__()
        self.sender.sendMessage(text=bot_invite_player % (msg['from']['first_name'], bot_name, start_url))

    def on_message(self, msg):
        print(u'on_message() is being called')
        flavor = telepot.flavor(msg)

        # normal message
        if chkNConv(flavor) == u'normal':
            content_type, chat_type, _chat_id = telepot.glance2(msg)
            print('Normal Message:', content_type, chat_type, _chat_id, '; message content: ', msg)

            if content_type == 'text':
                if self._convert_type == ConverType.nothing:
                    if chkNConv(msg['text']) == u'/start':
                        self.sender.sendMessage(text=bot_starting_script)
                    elif chkNConv(msg['text']) == u'/newgame':
                        self.create_game(msg=msg)
        else:
            raise telepot.BadFlavor(msg)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(LiarsDiceBot, timeout=120)),])
print('Listening ...')
bot.notifyOnMessage(run_forever=True)
