from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON

shoes_b = InlineKeyboardButton(
    text=LEXICON['shoes'],
    callback_data='shoes'
)
coats_b = InlineKeyboardButton(
    text=LEXICON['coats'],
    callback_data='coats'
)
pants_b = InlineKeyboardButton(
    text=LEXICON['pants'],
    callback_data='pants'
)
jackets_b = InlineKeyboardButton(
    text=LEXICON['jackets'],
    callback_data='jackets'
)
accessories_b = InlineKeyboardButton(
    text=LEXICON['accessories'],
    callback_data='accessories'
)
bags_b = InlineKeyboardButton(
    text=LEXICON['bags'],
    callback_data='bags'
)
underware_b = InlineKeyboardButton(
    text=LEXICON['underware'],
    callback_data='underware'
)

calc_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[shoes_b],
                     [coats_b],
                     [pants_b],
                     [jackets_b],
                     [accessories_b],
                     [bags_b],
                     [underware_b],]
)
