# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class BuildingTable:
    def __init__(self, material: str, tools: list):
        #Валидация аргументов конструктора
        if material not in ['Дерево', 'Металл', 'Пластик', 'Стекло']:
            raise ValueError('material должен быть либо деревом, либо металлом, либо пластиком, либо стеклом')

        if not all(isinstance(tool, str) for tool in tools):
            raise ValueError('tools должны представлять собой список строк')

        self.material = material  # Основной материал таблицы, например, "Дерево"
        self.tools = tools  # Список инструментов, например, ["Пила", "Молоток", "Гвозди"]


    def cut_material(self, dimensions: tuple)->None:
        """
        Разрезает материал на куски в соответствии с заданными размерами.
        :agr dimensions: Кортеж с размерами, на которые нужно разрезать материал
        Пример:
        >>> table_builder = BuildingTable('Дерево', ['Пила', 'Молоток', 'Гвозди'])
        >>> table_builder.cut_material((120, 60, 75))
        :return: None
        """
        ...


    def assemble_table(self)->None  :
        """
        Раскладывает нарезанные кусочки на столе.

        :return: None

        """
        ...


    def polish_and_finish(self)->None:
        """
        Полирует стол и наносит последние штрихи.
        :return: None
        """
        ...




if __name__ == "__main__":
    doctest.testmod()
