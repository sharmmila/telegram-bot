from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def scraper_keyboard():
    markup = InlineKeyboardMarkup()
    news_button = InlineKeyboardButton(
    "Последние новости",
        callback_data="news"
    )
    movies_button = InlineKeyboardButton(
        "Популярные фильмы",
        callback_data="movies"
    )
    markup.add(news_button)
    markup.add(movies_button)
    return markup