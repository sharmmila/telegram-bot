from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        "Link 🔗",
        callback_data="reference_link"
    )
    # reference_list_button = InlineKeyboardButton(
    #     "Reference list",
    #     callback_data="reference_list"
    # )

    markup.add(reference_link_button)
    # markup.add(reference_list_button)
    return markup