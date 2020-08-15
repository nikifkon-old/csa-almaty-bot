import os
from distutils.util import strtobool

import dotenv

dotenv.load_dotenv()


class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    USE_POLLING = bool(strtobool(os.getenv("USE_POLLING", "False")))
    PUBLIC_KEY = os.getenv("PUBLIC_KEY", None)

    HOST = os.getenv("HOST")
    WEBHOOK_PATH = "/webhook/" + TELEGRAM_TOKEN
    WEBHOOK_URL = f"{HOST}{WEBHOOK_PATH}"

    WEBAPP_HOST = "0.0.0.0"
    WEBAPP_PORT = os.getenv("WEBAPP_PORT", 8000)
    WEBHOOK_PORT = os.getenv("PORT", 8001)

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
