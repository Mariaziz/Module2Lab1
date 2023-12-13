# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Music:
    def __init__(self, Name: str, Genre: str):
        # Валидация аргументов конструктора
        if not isinstance(Name, str):
            raise ValueError('Name должен быть строкой')
        if not isinstance(Genre, str):
            raise ValueError('Genre должен быть строкой')

        self.Name = Name  # Название музыки, например, "In the End"
        self.Genre = Genre  # Название жанра, например, "Рок"

    def add_music(self) -> None:
        """
        Добавляет музыку в плейлист
        :return: None
        """
        ...

    def delete_music(self) -> None:
        """
        Удаляет музыку из плейлиста
        :return: None

        """
        ...

    def share_music(self)->None:
        """
        Поделиться музыкой с другом.
        :arg genre:
        :return: None
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
