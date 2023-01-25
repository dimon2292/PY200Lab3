class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, new_author):
        self._author = new_author


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
        super().__repr__()

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"


    @property
    def pages(self):
        return self.pages


    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Неверный тип данных")
        if value < 0:
            raise ValueError("Неверно значение страниц")
        self.pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"


    @property
    def duration(self):
        return self.duration


    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Неверный тип данных")
        if not 0 < value < 1000.0:
            raise ValueError("Неверное число")
        self.duration = value

book1 = PaperBook('efwe', 'efefe', 100)
print(book1.__repr__())