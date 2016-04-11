# coding=UTF8
__author__ = 'daedaluschan'

import sys, time
import telepot
from telepot.delegate import per_chat_id, create_open

from datetime import date
from types import *
from enum import Enum
import re

from liars_dice_script import *
from liars_dice_game import LiarsDiceGame, DiceOutcome
from liars_dice_util import chkNConv

all_games = {}

class ConverType(Enum):
    nothing = 1

class LiarsDiceBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(LiarsDiceBot, self).__init__(seed_tuple, timeout)
        self._convert_type = ConverType.nothing
        print('constructor is being called')

    def on_message(self, msg):
        print('on_message() is being called')
        flavor = telepot.flavor(msg)

        # normal message
        if flavor == 'normal':
            content_type, chat_type, _chat_id = telepot.glance2(msg)
            print('Normal Message:', content_type, chat_type, _chat_id, '; message content: ', msg)

            if self._convert_type == ConverType.nothing:
                if chkNConv(msg['text']) == u'/start':
                    self.sender.sendMessage(text='game start')

        else:
            raise telepot.BadFlavor(msg)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(LiarsDiceBot, timeout=120)),])
print('Listening ...')
bot.notifyOnMessage(run_forever=True)
