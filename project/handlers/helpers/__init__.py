from aiogram import Dispatcher

from .start import bot_start
from .help import bot_help


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["start"], state="*")
    dp.register_message_handler(bot_help, commands=["help"], state="*")
