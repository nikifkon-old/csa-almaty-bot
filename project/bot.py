from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.types import ParseMode

from config import Config

# For flask sessions
# try:
#     loop = asyncio.get_event_loop()
# except RuntimeError:
#     loop = asyncio.new_event_loop()

bot = Bot(token=Config.TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
# storage = RedisStorage(
#     host=Config.REDIS_HOST,
#     port=Config.REDIS_PORT,
#     password=Config.REDIS_PASSWORD,
# )
dp = Dispatcher(bot)
# , storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
