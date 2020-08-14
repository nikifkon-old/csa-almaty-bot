from aiogram import types

from project.handlers.menu_keyboard import entry


async def bot_start(message: types.Message):
    """
    /start command handler
    """
    await entry(message)
