# from aiogram import types, Dispatcher
# from config import bot
# from keyboards.scraper import scraper_keyboard
# from scraper.async_scraper import AsyncNewsScraper, AsyncMoviesScraper
# from database.async_database import AsyncDatabase
# from database import sql_queries
#
#
# async def news_menu_call(call: types.CallbackQuery):
#      await bot.send_message(
#         chat_id=call.from_user.id,
#         text='u can read news or new find movies',
#
#     reply_markup=await scraper_keyboard())
#
#
# async def news_call(call: types.CallbackQuery):
#     db = AsyncDatabase
#     news=AsyncNewsScraper()
#     links=news.get_pages()
#     for link in links:
#         db.execute_query(sql_queries.INSERT_ASYNC_NEWS_QUERY, params=(None, link), fetch="none")
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=link,
#             reply_markup=await scraper_keyboard()
#         )
#
# async def movies_call(call: types.CallbackQuery):
#     db = AsyncDatabase()
#     movies=AsyncMoviesScraper()
#     links=movies.get_pages()
#     for link in links:
#         db.execute_query(sql_quries.INSERT_ASYNC_MOVIES_QUERY, params=(None, link), fetch="none")
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=link,
#             reply_markup=await scraper_keyboard()
#         )
# def register_async_scraper_handlers(dp: Dispatcher):
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