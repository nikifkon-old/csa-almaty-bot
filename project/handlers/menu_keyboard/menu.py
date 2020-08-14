from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from project.bot import dp
from project.keyboards import get_main_menu_keyboard, get_keyboard_by_category_text_or_404
from project.services import get_question_or_404
from project.utils import BACK_TO_MENU_TEXT


class Menu(StatesGroup):
    wait_for_category = State()
    wait_for_question = State()


@dp.message_handler(lambda message: message.text == BACK_TO_MENU_TEXT, state="*")
async def bot_cancel(message: types.Message):
    """
    BACK_TO_MENU_TEXT handler
    """
    await Menu.first()
    keyboard = get_main_menu_keyboard()
    await message.reply("Возврашаю в главное меню", reply_markup=keyboard)


async def entry(message: types.Message):
    keyboard = get_main_menu_keyboard()
    await message.answer("Выбирите категорию:", reply_markup=keyboard)
    await Menu.wait_for_category.set()


async def choose_category(message: types.Message, state: FSMContext):
    keyboard = get_keyboard_by_category_text_or_404(message.text)
    if keyboard is None:
        await message.reply("Пожалуйста, выберите категорию, используя клавиатуру ниже.")
        return
    await state.update_data(category=message.text.lower())

    await Menu.wait_for_question.set()
    await message.answer("Теперь выберите Вопрос:", reply_markup=keyboard)


async def choose_question(message: types.Message, state: FSMContext):
    question = get_question_or_404(message.text)
    if question is None:
        await message.reply("Пожалуйста, выберите вопрос, используя клавиатуру ниже.")
        return
    await message.reply(question.answer)
    await Menu.wait_for_question.set()
