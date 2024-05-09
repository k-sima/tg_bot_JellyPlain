from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.menu_kb import menu_keyboard
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from keyboards.order_kb import home_keyboard

router = Router()


# Этот хэндлер сработает после нажатия на /start
@router.message(Command(commands=['start', 'menu']))
async def process_start_command(message: Message, state: FSMContext):
    photo_path = 'jelly_photo.png'
    photo = FSInputFile(photo_path)
    await message.answer_photo(
        photo=photo,
        caption=LEXICON['/start'],
        reply_markup=menu_keyboard
    )
    await state.set_state(default_state)


@router.message(F.text == 'Меню 🏠')
async def process_start_command(message: Message, state: FSMContext):
    photo_path = 'jelly_photo.png'
    photo = FSInputFile(photo_path)
    await message.answer_photo(
        photo=photo,
        caption=LEXICON['/start'],
        reply_markup=menu_keyboard
    )
    await state.set_state(default_state)


# Этот хэндлер сработает если пользователь введет сообщение в меню
@router.message(StateFilter(default_state))
async def no_state_message(message: Message):
    await message.answer(
        text='Я вас не понимаю, выберите кнопку\nДля возврата в меню нажмите на кнопку',
        reply_markup=home_keyboard
    )
