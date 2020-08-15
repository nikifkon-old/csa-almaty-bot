from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from project.keyboards import (get_back_to_searh_result_or_categories_keyboard, get_question_not_found_keyboard,
                               get_search_result_keyboard)
from project.services import get_question_or_404


class Search(StatesGroup):
    wait_for_query = State()
    wait_for_question = State()
    after_not_found = State()
    after_get_question = State()


async def entry(message: types.Message):
    await ask_query(message)


# wait_for_query
async def handle_query(message: types.Message, state: FSMContext):
    keyboard = get_search_result_keyboard(message.text)
    if keyboard is None:
        return await not_found(message)
    await state.update_data(query=message.text)

    return await ask_question(message, keyboard=keyboard)


async def ask_query(message: types.Message):
    await message.answer("Пожалуйста, введите свой запрос.", reply_markup=None)
    await Search.wait_for_query.set()


async def not_found(message: types.Message):
    await message.reply("Ничего не найдено", reply_markup=None)
    return await ask_after_not_found(message)


# not_found
async def handle_back_to_search_again(message: types.Message, state: FSMContext):
    """
    if TRY_SEARCH_AGAIN
    """

    return await ask_query(message)


async def ask_after_not_found(message: types.Message):
    keyboard = get_question_not_found_keyboard()
    await message.answer("Выберите дальнейшее действие, использую клавиатуру ниже.", reply_markup=keyboard)
    await Search.after_not_found.set()


async def handle_invalid_not_found_option(message: types.Message, state: FSMContext):
    await message.answer("Невозможное действиие", reply_markup=None)
    return await ask_after_not_found(message)


# wait_for_question
async def handle_question(message: types.Message, state: FSMContext):
    question = get_question_or_404(message.text)
    if question is None:
        return await invalid_question(message, state=state)
    await message.reply(question.answer)

    return await ask_after_get_question(message)


async def ask_question(message: types.Message, keyboard):
    await message.answer("Пожалуйста, выберите вопрос, используя клавиатуру ниже.", reply_markup=keyboard)
    await Search.wait_for_question.set()


async def invalid_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        query = data["query"]
    except KeyError:
        return await ask_query()

    keyboard = get_search_result_keyboard(query)
    await message.reply("Такого вопроса не существует", reply_markup=None)

    return await ask_question(message, keyboard=keyboard)


# after_get_question
async def handle_after_get_question(message: types.Message, state: FSMContext):
    """
    if BACK_TO_SEARCH_RESULT
    """
    data = await state.get_data()
    try:
        query = data["query"]
    except KeyError:
        return await ask_query()

    keyboard = get_search_result_keyboard(query)
    return await ask_question(message, keyboard=keyboard)


async def ask_after_get_question(message: types.Message):
    keyboard = get_back_to_searh_result_or_categories_keyboard()
    await message.answer("Выберите дальнейшее действие, использую клавиатуру ниже.", reply_markup=keyboard)
    await Search.after_get_question.set()


async def handle_invalid_after_get_question(message: types.Message, state: FSMContext):
    """
    If invalid after_get_get_question
    """
    await message.reply("Невозможное действиие", reply_markup=None)
    return await ask_after_get_question(message)
