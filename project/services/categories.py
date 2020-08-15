from project.models import Category
from project.utils import EXCLAMATION_CHAR

from .data import categories_names

categories = [
    Category(
        name="{prefix} {name}".format(prefix=EXCLAMATION_CHAR, name=name)
    ) for name in categories_names
]


def list_categories():
    return categories
