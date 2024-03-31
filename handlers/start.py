import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot, MEDIA_DESTINATION
from const import START_MENU_TEXT
from database import bot_db, sql_quries
from keyboards.start_menu import start_menu_keyboard
from database.async_database import AsyncDatabase


async def start_menu(message: types.Message):
    print(message)
    db = AsyncDatabase()
    await db.execute_query(
        query=sql_quries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            None,
            0
        ),
        fetch='none'
    )

    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link("start", payload=command[1])
        owner = db.execute_query(
             query=sql_quries.SELECT_USER_BY_LINK_QUERY,
             params=(link,),
             fetch='one'
         )

        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="U can not use ur own link!!"
            )
            return
        # try:
        #         db.insert_reference_user(
        #             owner=owner['telegram_id'],
        #             reference=message.from_user.id
        #         )
        #         db.update_owner_balance(
        #             tg_id=owner['telegram_id']
        #         )
        #     except sqlite3.IntegrityError:
        #         await bot.send_message(
        #             chat_id=message.from_user.id,
        #             text="U have used this link"
        #         )
        #     return

    with open(MEDIA_DESTINATION + "bot-pic.webp", 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_menu_keyboard()
        )




def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )