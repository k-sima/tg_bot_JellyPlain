from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from fsm.fsm_states import FSMFillForm
from lexicon.lexicon import LEXICON
from filters.filters import is_price_filter, calc_cats
from keyboards.calc_kb import calc_keyboard
from keyboards.order_kb import home_keyboard
from service.count_price import calc_by_categories
from database.database import calc_try

router = Router()
PRICE: str  # Цена товара от пользоватля


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "калькулятор"
@router.callback_query(F.data == 'calculator')
async def calculator_press(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text="<b>Введите цену в ЮАНЯХ:</b>")
    await state.set_state(FSMFillForm.fill_price)


# Этот хэндлер сработает после ввода цены
@router.message(is_price_filter, StateFilter(FSMFillForm.fill_price))
async def show_categories_buttons(message: Message, state: FSMContext):
    global PRICE
    PRICE = message.text
    await message.answer(
        text=LEXICON['choose_category'],
        reply_markup=calc_keyboard
    )
    await state.set_state(FSMFillForm.choosing_cat)


# Этот хэндлер сработает после нажатия на инлайн кнопку
@router.callback_query(F.data.in_(calc_cats), StateFilter(FSMFillForm.choosing_cat))
async def show_price(callback: CallbackQuery, state: FSMContext, bot: Bot):
    price = calc_by_categories(callback, PRICE)
    formatted_price = f'{price:,.0f}'.replace(',', '.') + ' руб.'

    await callback.message.answer(
        text=f"{formatted_price}\nЭто окончательная цена с доставкой\n\nЧтобы вернуться в меню нажмите на кнопку",
        reply_markup=home_keyboard
    )

    my_chat_id = '364217467'
    data = callback.data
    user_name = callback.from_user.username
    # отправка инфы о цене и категории админам
    await bot.send_message(
        my_chat_id,
        f"Пользователь @{user_name} \n"
        f"Выбрал категорию: {LEXICON[data]}\nЦена: {price}\nЦена в юанях: {PRICE}"
    )

    # отправка инфы о цене и категории в БД
    await calc_try(user_name, LEXICON[data], price, PRICE)

    await callback.answer()
    await state.clear()
    await callback.message.delete()


# Этот хэндлер сработает если на этапе ввода цены пользователь введет не то
@router.message(StateFilter(FSMFillForm.fill_price))
async def no_state_message(message: Message):
    await message.answer(text=LEXICON['wrong_price_message'])


# Этот хэндлер сработает если на этапе выбора категории товара пользователь начнет что-то писать
@router.message(StateFilter(FSMFillForm.choosing_cat))
async def no_state_message(message: Message):
    await message.answer(text=LEXICON['wrong_category_message'])
