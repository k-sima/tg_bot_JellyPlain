from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON

assortment_b = InlineKeyboardButton(
    text=LEXICON['instruction'],
    callback_data='instruction',
    url='https://telegra.ph/Instrukciya-po-zakazu-s-POIZON-04-23'
)
calculator_b = InlineKeyboardButton(
    text=LEXICON['calculator'],
    callback_data='calculator'
)
reviews_b = InlineKeyboardButton(
    text=LEXICON['reviews'],
    callback_data='reviews',
    url='https://t.me/jellyreview'
)
order_b = InlineKeyboardButton(
    text=LEXICON['order'],
    callback_data='order'
)
write_manager_b = InlineKeyboardButton(
    text=LEXICON['write_manager'],
    callback_data='write_manager',
    url='https://t.me/levmanilo'
)
terms_b = InlineKeyboardButton(
    text=LEXICON['terms'],
    callback_data='terms',
    url='https://telegra.ph/Usloviya-zakaza-04-24'
)
menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[assortment_b],
                     [calculator_b],
                     [terms_b],
                     [order_b],
                     [write_manager_b, reviews_b]]
)
