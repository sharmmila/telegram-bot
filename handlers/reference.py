from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot
from database.bot_db import Database
from keyboards.reference import reference_menu_keyboard
import const
import binascii
import os


async def reference_menu_call(call: types.CallbackQuery):
    db = Database()
    user_info = db.select_reference_user_info(tg_id=call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=const.REFERENCE_MENU_TEXT.format(
            user=call.from_user.first_name,
            balance=user_info['balance'],
            count=user_info['count'],
        ),
        reply_markup=await reference_menu_keyboard()
    )


async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.select_user(tg_id=call.from_user.id)
    print(user)
    if user['link']:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ur old link {user['link']}"
        )
    else:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        db.update_user_link(link=link, tg_id=call.from_user.id)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ur new link {link}"
        )


async def reference_list_call(call: types.CallbackQuery):
    db = Database()
    user = db.select_user(tg_id=call.from_user.id)
    table = db.select_reference_user_info(tg_id=call.from_user.id)
    if user in table:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ur reference list {db.select_reference_list(tg_id=call.from_user.id)}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"U doesnt have any references yet"
        )

def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == "reference_menu"
    )
    dp.register_callback_query_handler(
        reference_link_call,
        lambda call: call.data == "reference_link"
    )
    dp.register_callback_query_handler(
        reference_list_call,
        lambda call: call.data == "reference_list"
    )