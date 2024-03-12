from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    comedy_button = InlineKeyboardButton(
        'Comedy😂',
        callback_data='comedy'
    )
    fantasy_button = InlineKeyboardButton(
        'Fantasy🪄',
        callback_data='fantasy'
    )
    markup.add(fantasy_button)
    markup.add(comedy_button)
    return markup
async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    sad_films_button = InlineKeyboardButton(
        'Sad films😓',
        callback_data='sad films'
    )
    romcom_button = InlineKeyboardButton(
        'Romcoms💞',
        callback_data='romcoms'
    )
    markup.add(sad_films_button)
    markup.add(romcom_button)
    return markup
async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    horror_movies_button = InlineKeyboardButton(
        'horror_movies',
        callback_data='horror_movies'
    )
    historyc_movies_button = InlineKeyboardButton(
        'historyc_movies',
        callback_data='historyc_movies'
    )

    markup.add(horror_movies_button)
    markup.add(historyc_movies_button)
    return markup