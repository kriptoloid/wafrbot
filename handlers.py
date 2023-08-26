from aiogram import types
from utils import get_user_info

async def handle_message(message: types.Message):
    userinfo = get_user_info(message.from_user)

    await bot.send_message(
        myuserid,
        f"User <a href='tg://user?id={message.from_user.id}'>{userinfo}</a> send you message:\n{message.text}",
        parse_mode='HTML'
    )

    await message.answer("Ok, the message was delivered successfully")

async def cmd_start(message: types.Message):
    await message.answer("Hello, write your message and I will send it to the boss.")
