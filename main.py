from aiogram import executor, Dispatcher
from config import dp
from handlers import (
   start,
   questionnaire,
)

start.register_start_handler(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)

from database import bot_db
async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup
    )

