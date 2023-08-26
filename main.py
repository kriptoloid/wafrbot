import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import tokenbot
from handlers import handle_message, cmd_start

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tokenbot)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Регистрация обработчиков
dp.register_message_handler(cmd_start, commands=["start"])
dp.register_message_handler(handle_message)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
