from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

direct_b = InlineKeyboardButton(
    text='Перейти в чат с админом',
    callback_data='order',
    url='https://t.me/levmanilo'
)

correct_b = InlineKeyboardButton(
    text="✅Отправить форму",
    callback_data='correct_b'
)
wrong_b = InlineKeyboardButton(
    text='❌Изменить форму',
    callback_data='wrong_b'
)

home_b = KeyboardButton(text='Меню 🏠')

check_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[correct_b], [wrong_b]]
)

home_keyboard = ReplyKeyboardMarkup(keyboard=[[home_b]], resize_keyboard=True, one_time_keyboard=True)

order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[direct_b]]
)

