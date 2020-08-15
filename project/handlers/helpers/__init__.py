from aiogram import Dispatcher

from .help import bot_help
from .start import bot_start


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["start"], state="*")
    dp.register_message_handler(bot_help, commands=["help"], state="*")
