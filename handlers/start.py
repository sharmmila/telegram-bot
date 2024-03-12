from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards.start_menu import start_menu_keyboard
import sqlite3


async def start_menu(message: types.Message):
    db = bot_db.Database()
    try:
        db.sql_insert_user(
         tg_id=message.from_user.id,
         username=message.from_user.username,
         first_name=message.from_user.first_name,
         last_name=message.from_user.last_name
        )
    except sqlite3.IntegrityError:
        pass

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hello {message.from_user.first_name}',
        reply_markup=await start_menu_keyboard()
    )

def register_start_handler (dp: Dispatcher ):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )