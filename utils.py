from aiogram import types

def get_user_info(user: types.User) -> str:
    userinfo = ""

    if user.username:
        userinfo += f"{user.username} "
    elif user.last_name:
        userinfo += f"{user.last_name} "
    elif user.first_name:
        userinfo += f"{user.first_name} "

    return userinfo
