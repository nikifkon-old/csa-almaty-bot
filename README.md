# Installation

```
cp .env.example .env
python project
```

# Models

## Question
- text
- answer
- category_id

## Category
- text

# Services

## `list_categories() -> List[Category]`
## `get_questions_in_category(category) -> List[Question]`
## `get_question(question_text) -> str`
## `find_questions(query) -> List[Question]`


# Keyboards

## `get_main_menu_keyboard()`
## `get_questions_list_keyboard(category_name)`
## `get_search_result_keyboard(query)`
## `get_back_to_searh_result_or_categories_keyboard()`
## `get_question_not_found_keyboard()`

# Script

-> при /start пользователь выводиться приветственное сообщение. Предлагается выбрать вопрос с помощью клавиатуры. Отображается Клавиатура: "Категории".
-> пользователь кликает по категории. Бот выводит клавиатуру: "Вопросы в категории"
-> пользователь кликает по вопросу, тогда бот возвращает ответ
Если пользователь не нашел нужного вопроса, он может нажать кнопку назад для возвращения в главное меню

-> в главном меню есть кнопка "Поиск"
-> При нажатии пользователю предоставляется возможность ввести поисковой запрос. Результаты поиска отображаются на клавиатуре
-> Если не было найдено совпадений, бот отправляет клавиатуру с кнопками: "Попробовать ещё раз" и "Вернуться к списку категорий", логика которых очевидна
-> Пользователь кликает на нужный вопрос. Бот присылает ответ. И показывает клавиатуру с кнопками: "Вернуться к категориям", "Вернуться к результатам поиска", логика которых очевидна

-> Если боту не удалось распознать команду или выбрано что-то несуществующее, вместо ошибки будет произведен поиск