from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    group_actions,
    registration,
    profile,
    reference,
)
from database import bot_db


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


start.register_start_handler(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handlers(dp=dp)
reference.register_reference_handlers(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )