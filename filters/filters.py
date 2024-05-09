from aiogram import Router
from aiogram.types import Message

router = Router()


def is_price_filter(message: Message) -> bool:
    try:
        if message.text.isdigit():
            if int(message.text) > 0:
                return True
    except AttributeError:
        pass


calc_cats = ['shoes', 'coats', 'pants', 'jackets', 'accessories', 'bags', 'underware']
