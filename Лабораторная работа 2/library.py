BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:

    def __init__(self, id_: int, name: str, pages: int) -> None:
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:

    def __init__(self, books = []):
        self.books = books

    def get_max_book_id(self) -> int:
        # Возвращает максимальный id книги в библиотеке
        return max(self.books, key=lambda x: x.id_).id_
    def get_next_book_id(self) -> int:
        '''
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то возвращает 1.
        Если книги есть, то возвращает идентификатор последней книги увеличенный на 1.
        '''
        return 1 if len(self.books) == 0 else self.get_max_book_id()+1

    def get_index_by_book_id(self, book_id: int):
        '''
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то возвращает индекс из списка.
        Если книги нет, то вызывает ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
        '''
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
