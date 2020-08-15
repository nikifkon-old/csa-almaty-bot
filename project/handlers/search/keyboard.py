from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from project.keyboards import (get_back_to_searh_result_or_categories_keyboard, get_question_not_found_keyboard,
                               get_search_result_keyboard)
from project.services import get_question_or_404


class Search(StatesGroup):  # TODO: Move to another folder
    wait_for_query = State()  # When user start searching
    wait_for_question = State()  # When user got search results
    after_not_found = State()  # When user type query but no question was found
    after_get_question = State()  # Whne user click to the question


async def entry(message: types.Message):
    """
    Entry point for search module
    hen user click to button with text ~project.utils.OPEN_SEARCH
    """
    await ask_query(message)


# wait_for_query
async def handle_query(message: types.Message, state: FSMContext):
    """
    When user typed query to search
    """
    keyboard = get_search_result_keyboard(message.text)
    if keyboard is None:
        return await not_found(message)
    await state.update_data(query=message.text)

    return await ask_question(message, keyboard=keyboard)


async def ask_query(message: types.Message):
    """
    Ask user to type query
    When user click to button with text ~project.utils.TRY_SEARCH_AGAIN or from `entry` point
    """
    await message.answer("Введите свой запрос:", reply_markup=None)
    await Search.wait_for_query.set()


async def not_found(message: types.Message):
    """
    Display an error
    When questions not found
    """
    await message.reply("Ничего не найдено", reply_markup=None)
    return await ask_after_not_found(message)


# not_found
async def back_to_search_again(message: types.Message, state: FSMContext):
    """
    When user click to button with text ~project.utils.TRY_SEARCH_AGAIN
    """
    return await ask_query(message)


async def ask_after_not_found(message: types.Message):
    """
    Ask user to choose next step
    When questions not found
    """
    keyboard = get_question_not_found_keyboard()
    await message.answer("Выберите дальнейшее действие, использую клавиатуру ниже.", reply_markup=keyboard)
    await Search.after_not_found.set()


async def handle_invalid_not_found_option(message: types.Message, state: FSMContext):
    """
    When button from keyboard ~project.keyboards.get_question_not_found_keyboard not clicked
    """
    await message.answer("Невозможное действиие", reply_markup=None)
    return await ask_after_not_found(message)


# wait_for_question
async def handle_question(message: types.Message, state: FSMContext):
    """
    Handle getting question from search result
    """
    question = get_question_or_404(message.text)
    if question is None:
        return await invalid_question(message, state=state)
    await message.reply(question.answer)

    return await ask_after_get_question(message)


async def ask_question(message: types.Message, state: FSMContext = None, keyboard=None):
    """
    Display search result and ask for choose one of question
    :param keybaord: (optional) keyboard with search result (see ~project.keyboards.get_search_result_keyboard)
    :param FSMContext state: (optional) aiogram state
    but either keyboard or state must passed
    """
    if keyboard is None:
        if state is not None:
            data = await state.get_data()
            try:
                query = data["query"]
            except KeyError:
                return await ask_query()
            keyboard = get_search_result_keyboard(query)
        else:
            raise ValueError("Must specify either state or keyboard")  # TODO: get state manually

    await message.answer("Выберите вопрос, используя клавиатуру ниже.", reply_markup=keyboard)
    await Search.wait_for_question.set()


async def invalid_question(message: types.Message, state: FSMContext):
    """
    When user`s typed question does not exist
    """
    await message.reply("Такого вопроса не существует", reply_markup=None)
    return await ask_question(message, state=state)


# after_get_question
async def back_to_search(message: types.Message, state: FSMContext):
    """
    Back user to search result
    When he see question answer
    """
    return await ask_question(message, state=state)


async def ask_after_get_question(message: types.Message):
    """
    Ask user to next step after showing question answer
    """
    keyboard = get_back_to_searh_result_or_categories_keyboard()
    await message.answer("Выберите дальнейшее действие, использую клавиатуру ниже.", reply_markup=keyboard)
    await Search.after_get_question.set()


async def handle_invalid_after_get_question_option(message: types.Message, state: FSMContext):
    """
    When button from keyboard ~project.keyboards.get_back_to_searh_result_or_categories_keyboard not clicked
    """
    await message.reply("Невозможное действиие", reply_markup=None)
    return await ask_after_get_question(message)
