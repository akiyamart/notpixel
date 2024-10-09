from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def menu():
    builder = InlineKeyboardBuilder()

    buttons = [
        {"text": "👨🏻‍💻 Чат с ИИ", "callback_data": "chat_ai"},
        {"text": "🤖 Боты", "callback_data": "bot_ferm"},
    ]

    for button in buttons: 
        builder.add(
            InlineKeyboardButton(**button)
        )
    
    builder.adjust(1, 1)

    return builder.as_markup()
    

def back_to_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👈 Вернуться в меню", callback_data="menu")
            ]
        ]
    )

