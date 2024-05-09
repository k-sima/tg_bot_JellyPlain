from aiogram import Bot, Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup


class FSMFillForm(StatesGroup):
    fill_price = State()
    fill_form = State()
    message_to_admin = State()
    choosing_cat = State()