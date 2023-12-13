# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class DoingHomework:
    def __init__(self, subject: str, deadline: str):
        #Валидация аргументов конструктора
        if not isinstance(subject, str):
            raise ValueError('subject должен быть строкой')

        if not isinstance(deadline, str):
            raise ValueError('deadline должен быть строкой')

        self.subject = subject  #Предмет домашнего задания, например, "Математика"
        self.deadline = deadline  # Крайний срок выполнения домашнего задания, например, "13-12-2023"


    def start_homework(self) -> None:
        """
        #Начинает выполнять указанное домашнее задание.
        :return: None
        """
        ...




    def request_extension(self, new_deadline: str):
        """
       Просит продлить срок выполнения домашнего задания.
        :arg new_deadline: Новый срок сдачи.
        Пример:
        >>> homework = DoingHomework('Физика', '01-12-2023')
        >>> homework.request_extension('10-12-2023')
         """
        ...


if __name__ == "__main__":
    doctest.testmod()
