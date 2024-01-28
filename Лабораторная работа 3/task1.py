class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    @staticmethod
    def is_pages_valid(pages: int) -> bool:
        return type(pages) == int and pages > 0

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if type(value) == int and value > 0:
            self._pages = value
        else:
            raise ValueError("Кол-во страниц должно быть положительным целым числом.")

    def __str__(self):
        return f'{super().__str__()}. Страниц: {self.pages}'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if type(value) in (int, float) and value > 0:
            self._duration = value
        else:
            raise ValueError("Длительность должна быть положительным числом.")

    def __str__(self):
        return f'{super().__str__()}. Продолжительность: {self.duration}'
