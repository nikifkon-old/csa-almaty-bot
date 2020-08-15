from aiogram import types

from project.handlers.menu import entry


async def bot_help(message: types.Message):
    """
    /help command handler
    """
    await entry(message)
