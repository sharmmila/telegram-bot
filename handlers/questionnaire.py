from aiogram import types, Dispatcher
from config import bot
from keyboards.questionnaire import questionnaire_keyboard

async def questionnaire_start_call(call:types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=' Comedy😂 or Fantasy🪄 ?',
        reply_markup= await questionnaire_keyboard()
    )

async def comedy_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Poor things"'
    )

async def fantasy_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Harry Potter"'
    )


async def questionnaire_2_start_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=' Sad films😓 or Romcoms💞 ?',
        reply_markup=await questionnaire_keyboard()
    )

async def sad_films_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Titanic"')

async def romcom_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Anyone but you"')

async def questionnaire_3_start_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=' Horror movies🙈 or Historyc movies ?',
        reply_markup=await questionnaire_keyboard()
    )

async def horror_movies_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Black mirror"')

async def historyc_movies_call(call:types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Cool! You can watch "Openhaimmer"')

def register_questionnaire_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start_call,
        lambda call: call.data == 'start_questionnaire')
    dp.register_callback_query_handler(
        comedy_call,
        lambda call: call.data == 'comedy')
    dp.register_callback_query_handler(
        fantasy_call,
        lambda call: call.data == 'fantasy')
    dp.register_callback_query_handler(
        sad_films_call)

def register_questionnaire_handlers(dp: Dispatcher):
        dp.register_callback_query_handler(
            questionnaire_2_start_call,
        lambda call: call.data == 'sad films')
        dp.register_callback_query_handler(
        romcom_call,
        lambda call: call.data == 'romcoms')


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_3_start_call,
        lambda call: call.data == 'historyc_movies')
    dp.register_callback_query_handler(
        horror_movies_call,
        lambda call: call.data == 'horror_movies')


