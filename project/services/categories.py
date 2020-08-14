from project.models import Category
from project.utils import EXCLAMATION_CHAR


categories_names = [
    "1. Вопросы по Отделу имущественного найма.",
    "2. Вопросы по Отделу управлению коммунальными активами.",
    "3. Вопросы по Отдел доверительного управления и приватизации."
]


categories = [
    Category(
        name="{prefix} {name}".format(prefix=EXCLAMATION_CHAR, name=name)
    ) for name in categories_names
]


def list_categories():
    return categories
