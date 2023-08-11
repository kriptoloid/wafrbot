import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import tokenbot, myuserid

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tokenbot)

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, write your message and I will send it to the boss.")

@dp.message_handler()
async def message(message: types.Message):
    userinfo = ""
    if message.from_user.username != None:
        userinfo += f"{message.from_user.username} "
    elif message.from_user.last_name != None:
        userinfo += f"{message.from_user.last_name} "
    elif message.from_user.first_name != None:
        userinfo += f"{message.from_user.first_name} "
    await bot.send_message(myuserid, f"User <a href='tg://user?id={message.from_user.id}'>{userinfo}</a>send you message:\n{message.text}", parse_mode='HTML')
    await bot.send_message(message.from_user.id, "Ok, the message was delivered successfully")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
