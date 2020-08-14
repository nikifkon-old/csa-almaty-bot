from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.types import ParseMode

from config import Config

bot = Bot(token=Config.TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
storage = RedisStorage2(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    password=Config.REDIS_PASSWORD
)
dp = Dispatcher(bot, storage=storage)
