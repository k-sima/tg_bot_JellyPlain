from aiogram.types import CallbackQuery


def calc_by_categories(callback: CallbackQuery, price: str):
    s = int(price)
    exchange = 14.2  # настраивать курс
    mrkup = 0  # настраивать наценку
    if callback.data == 'shoes':
        return int(s * exchange * 1.0 + mrkup + 3500)
    if callback.data == 'coats':
        return int(s * exchange * 1.25 + mrkup)
    if callback.data == 'pants':
        return int(s * exchange * 1.3 + mrkup)
    if callback.data == 'jackets':
        return int(s * exchange * 1.25 + mrkup)
    if callback.data == 'accessories':
        return int(s * exchange * 1.15 + mrkup)
    if callback.data == 'bags':
        return int(s * exchange * 1.2 + mrkup)
    if callback.data == 'underware':
        return int(s * exchange * 1.2 + mrkup)
