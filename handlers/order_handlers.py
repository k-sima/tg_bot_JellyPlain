from aiogram.fsm.context import FSMContext
from keyboards.order_kb import check_keyboard, home_keyboard
from lexicon.lexicon import LEXICON
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, FSInputFile
from fsm.fsm_states import FSMFillForm
from aiogram.filters import StateFilter

router = Router()


@router.callback_query(F.data == 'order')
async def send_order_example(callback: CallbackQuery, state: FSMContext):
    photo_path = 'order_image.png'
    photo = FSInputFile(photo_path)
    # Заполните форму по примеру
    await callback.message.answer_photo(
        caption=LEXICON['order_form'],
        photo=photo
    )
    await state.set_state(FSMFillForm.message_to_admin)
    await callback.answer()


@router.message(F.text, StateFilter(FSMFillForm.message_to_admin))
async def check_form(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Проверьте правильность данных\n\n{message.text}",
        reply_markup=check_keyboard
    )
    await state.set_state(FSMFillForm.message_to_admin)


@router.callback_query(F.data == 'correct_b', StateFilter(FSMFillForm.message_to_admin))
async def echo_to_admin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    my_chat_id = '364217467'
    lev_chat_id = '1396546330'
    message = callback.message
    user_name = callback.from_user.username
    text = message.text.removeprefix("Проверьте правильность данных\n\n") if message.text else "No text"

    await bot.send_message(
        my_chat_id,
        f"Пользователь @{user_name} \n"
        f"Написал: \n\n{text}"
    )
    await bot.send_message(
        lev_chat_id,
        f"Пользователь @{user_name} \n"
        f"Написал: \n\n{text}"
    )
    await message.answer(
        text=LEXICON['order_sent'],
        reply_markup=home_keyboard
    )
    await state.clear()
    await callback.answer()
    await callback.message.delete()


@router.callback_query(F.data == 'wrong_b', StateFilter(FSMFillForm.message_to_admin))
async def send_order_example(callback: CallbackQuery, state: FSMContext):
    # Заполните форму по примеру
    await callback.message.answer(
        text=LEXICON['order_form']
    )
    await state.set_state(FSMFillForm.message_to_admin)
    await callback.answer()
    await callback.message.delete()


@router.message(StateFilter(FSMFillForm.message_to_admin))
async def check_form(message: Message):
    await message.answer(text=LEXICON['wrong_form_message'])
