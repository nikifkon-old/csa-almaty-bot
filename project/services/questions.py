from fuzzywuzzy import fuzz

from project.models import Question
from project.utils import EXCLAMATION_CHAR, QUESTION_CHAR

from .data import questions_data

questions = [
    Question(
        category_name=f"{EXCLAMATION_CHAR} {item['category_name']}",   # TODO get cat text to func
        text=f"{QUESTION_CHAR} {item['text']}",  # TODO
        answer=item["answer"]) for item in questions_data
]


def find_questions(query: str):
    result = [question for question in questions if fuzz.partial_ratio(query, question.text) > 50]
    return result


def get_questions_in_category(category_name: str):
    result = [question for question in questions if question.category_name == category_name]
    return result


def get_question_or_404(question_text: str):
    if question_text not in [question.text for question in questions]:
        return
    return get_question(question_text)


def get_question(question_text: str):
    result = [question for question in questions if question.text == question_text]
    return result[0]
