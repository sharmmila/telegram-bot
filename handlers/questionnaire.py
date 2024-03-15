from aiogram import types, Dispatcher

import database.sql_quries
from config import bot
from keyboards.questionnaire import questionnaire_keyboard
from handlers.group_actions import check_ban

async def questionnaire_start_call(call:types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=' check ban? ',
        reply_markup= await questionnaire_keyboard()
    )

async def check_ban_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=' check ban'
    )
    await check_ban(tg_id=call.message.from_user.id)

def register_questionnaire_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start_call,
        lambda call: call.data == 'start_questionnaire',
        check_ban_call,
        lambda call: call.data == 'check_ban')










