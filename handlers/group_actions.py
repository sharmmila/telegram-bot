from aiogram import types, Dispatcher
from aiogram.types import Update, CallbackQuery

import database.sql_quries
from config import bot
from profanity_check import predict_prob
from database.bot_db import Database


async def chat_message(message: types.Message):
    db = Database()
    ban_word_predict_prob = predict_prob([message.text])
    print(ban_word_predict_prob)

    if ban_word_predict_prob > 0.6:
        ban_user = db.select_ban_user(
            tg_id=message.from_user.id
        )

        if not ban_user:
            db.insert_ban_user(
                tg_id=message.from_user.id
            )
        elif ban_user['count'] >= 3:
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
        else:
            db.update_ban_count(
                tg_id=message.from_user.id
            )

        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'User: {message.chat.first_name}\n'
                 f'Dont curse in this group otherwise we will banned you'
        )


def register_group_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(
        chat_message
    )

async def check_ban(tg_id):
    db = Database()
    await db.select_ban_user(tg_id=tg_id)
    if tg_id not in db.select_ban_user(tg_id=tg_id):
        print('you are safe!')
    else:
        print('you have fouls!')