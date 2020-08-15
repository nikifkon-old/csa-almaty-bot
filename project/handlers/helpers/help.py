from aiogram import types

from project.handlers.menu_keyboard import entry


async def bot_help(message: types.Message):
    """
    /help command handler
    """
    await entry(message)
