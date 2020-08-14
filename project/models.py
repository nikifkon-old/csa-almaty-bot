from dataclasses import dataclass


@dataclass
class Question:
    text: str
    answer: str
    category_name: str  # TODO: id


@dataclass
class Category:
    name: str
