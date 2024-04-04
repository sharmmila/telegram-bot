# from aiogram import types, Dispatcher
# from config import bot
# from database.bot_db import Database
# async def news_menu_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text='u can read news or new find movies',
#
#     reply_markup=await scraper_keyboard())
#
#
# async def news_call(call: types.CallbackQuery):
#     db = Database()
#     news=NewsScraper()
#     links=news.scrape_data()
#     for link in links:
#         db.insert_news(link)
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=link,
#             reply_markup=await scraper_keyboard()
#         )
#
# async def movies_call(call: types.CallbackQuery):
#     db = Database()
#     movies=MoviesScraper()
#     links=movies.scrape_movies()
#     for link in links:
#         db.insert_movies(link)
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=link,
#             reply_markup=await scraper_keyboard()
#         )
# def register_scraper_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(
#         news_call,
#         lambda call: call.data == "news"
#     )
#     dp.register_callback_query_handler(
#         news_menu_call,
#         lambda call: call.data == "news_menu"
#     )
#     dp.register_callback_query_handler(
#         movies_call,
#         lambda call: call.data == "movies"
#     )