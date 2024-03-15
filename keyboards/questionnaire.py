from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    check_ban_button = InlineKeyboardButton(
        'Check ban?',
        callback_data='check_ban'
    )

    markup.add(check_ban_button)
    return markup