import re

from aiogram import types, Dispatcher

import const
from config import bot
from keyboards.profile import profile_keyboard, my_profile_keyboard
from database.bot_db import Database
from database import sql_queries
from database.async_database import AsyncDatabase
import random


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.select_profile(tg_id=call.from_user.id)

    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['bio'],
                    age=profile['age'],
                    married=profile['married'],
                    gender=profile['gender'],
                    hobbies=profile['hobbies'],
                    location=profile['location']
                ),
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have not registered, please register to view ur profile"
        )


async def random_profile_call(call: types.CallbackQuery):
    if call.message.caption.startswith("Nickname"):
        await call.message.delete()
    db = AsyncDatabase()
    profiles = await db.execute_query(
        query=sql_queries.SELECT_LEFT_JOIN_PROFILE_QUERY,
        params=(
            call.from_user.id,
            call.from_user.id,
        ),
        fetch='all'
    )
    print(profiles)
    if profiles:
        random_profile = random.choice(profiles)

        with open(random_profile['PHOTO'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=random_profile['NICKNAME'],
                    bio=random_profile['BIO'],
                    age=random_profile['AGE'],
                    married=random_profile['MARRIED'],
                    gender=random_profile['GENDER']
                ),
                reply_markup=await profile_keyboard(tg_id=random_profile['TELEGRAM_ID'])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have viewed all profiles, come later"
        )


async def detect_like_call(call: types.CallbackQuery):
    owner = re.sub("like_", "", call.data)
    db = Database()

    db.insert_like_profile(
        owner=owner,
        liker=call.from_user.id
    )
    await random_profile_call(call=call)


async def detect_dislike_call(call: types.CallbackQuery):
    owner = re.sub("dis", "", call.data)
    db = Database()

    db.insert_dislike_profile(
        owner=owner,
        disliker=call.from_user.id
    )
    await random_profile_call(call=call)

def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        random_profile_call,
        lambda call: call.data == "random_profile"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        detect_dislike_call,
        lambda call: "dis" in call.data
    )