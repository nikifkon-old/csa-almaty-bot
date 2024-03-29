import logging

from aiogram import executor
from aiogram.utils.executor import start_webhook

from config import Config
from project import handlers
from project.bot import bot, dp

logging.basicConfig(level=logging.INFO)


async def on_startup(app):
    logging.info(f"Setting up webhook url: {Config.WEBHOOK_URL}")
    await bot.delete_webhook()
    status = await bot.set_webhook(Config.WEBHOOK_URL)
    if status:
        logging.info("Webhook setting up successfully!")
    else:
        logging.error("Failed to setting up webhook!")


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    # await bot.delete_webhook()  DONT DO THIS!  Heroku app will not awake!
    await bot.set_webhook(Config.HOST)  # Instead set webhook to heroku host, in order to awake it

    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')


if __name__ == '__main__':
    handlers.helpers.setup(dp)
    handlers.menu.setup(dp)
    handlers.search.setup(dp)
    if Config.USE_POLLING:
        executor.start_polling(dp, skip_updates=True)
    else:
        start_webhook(
            dispatcher=dp,
            webhook_path=Config.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=Config.WEBAPP_HOST,
            port=Config.WEBHOOK_PORT,
        )
