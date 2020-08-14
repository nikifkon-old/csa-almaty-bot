from aiogram import types

from project.keyboards import get_main_menu_keyboard
from project.bot import bot
from project.handlers.menu_keyboard import entry


async def bot_help(message: types.Message):
    """
    /help command handler
    """
    await entry(message)
