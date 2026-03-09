import doctest


class Porsche:
    """
    Класс, представляющий автомобиль марки Porsche.
    """

    def __init__(self, model: str, max_speed: int, mileage: float):
        """
        Создание и подготовка объекта "Автомобиль Porsche"

        :param model: Модель автомобиля (например, "911 Turbo")
        :param max_speed: Максимальная скорость (км/ч)
        :param mileage: Пробег (км)

        Примеры:
        >>> car = Porsche("911 Turbo", 330, 15000.5)
        """
        if not isinstance(model, str) or not model.strip():
            raise TypeError("Модель должна быть непустой строкой")
        self.model = model.strip()

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть целым числом")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег должен быть числом (int или float)")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self.mileage = float(mileage)

    def start_engine(self) -> str:
        """
        Запуск двигателя автомобиля.

        :return: Сообщение о запуске двигателя

        Примеры:
        >>> car = Porsche("Cayenne", 250, 5000)
        >>> car.start_engine()
        """
        ...

    def accelerate(self, speed_increase: int) -> None:
        """
        Увеличение скорости автомобиля.

        :param speed_increase: На сколько км/ч увеличить скорость
        :raise ValueError: Если увеличение скорости не положительное

        Примеры:
        >>> car = Porsche("Panamera", 280, 12000)
        >>> car.accelerate(20)
        """
        if not isinstance(speed_increase, int):
            raise TypeError("Увеличение скорости должно быть целым числом")
        if speed_increase <= 0:
            raise ValueError("Увеличение скорости должно быть положительным")
        ...

    def get_info(self) -> str:
        """
        Получение информации об автомобиле.

        :return: Строка с моделью, максимальной скоростью и пробегом

        Примеры:
        >>> car = Porsche("Macan", 230, 8000)
        >>> car.get_info()
        """
        ...


class Iphone17:
    """
    Класс, представляющий смартфон iPhone 17.
    """

    def __init__(self, color: str, memory_gb: int, battery_level: int):
        """
        Создание и подготовка объекта "iPhone 17"

        :param color: Цвет корпуса
        :param memory_gb: Объем памяти в ГБ (128, 256, 512)
        :param battery_level: Уровень заряда батареи (0-100)

        Примеры:
        >>> phone = Iphone17("черный", 256, 85)
        """
        if not isinstance(color, str) or not color.strip():
            raise TypeError("Цвет должен быть непустой строкой")
        self.color = color.strip()

        if not isinstance(memory_gb, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if memory_gb not in (128, 256, 512):
            raise ValueError("Объем памяти должен быть 128, 256 или 512 ГБ")
        self.memory_gb = memory_gb

        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда должен быть целым числом")
        if not 0 <= battery_level <= 100:
            raise ValueError("Уровень заряда должен быть от 0 до 100")
        self.battery_level = battery_level

    def make_call(self, contact: str) -> str:
        """
        Совершение звонка контакту.

        :param contact: Имя контакта
        :return: Сообщение о звонке

        Примеры:
        >>> phone = Iphone17("синий", 128, 50)
        >>> phone.make_call("Мама")
        """
        if not isinstance(contact, str) or not contact.strip():
            raise TypeError("Имя контакта должно быть непустой строкой")
        ...

    def charge(self, minutes: int) -> None:
        """
        Зарядка телефона.

        :param minutes: Время зарядки в минутах
        :raise ValueError: Если время зарядки не положительное

        Примеры:
        >>> phone = Iphone17("золотой", 512, 10)
        >>> phone.charge(30)
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть целым числом")
        if minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным")
        ...

    def check_storage(self) -> dict:
        """
        Проверка состояния памяти.

        :return: Словарь с занятой и свободной памятью (условно)

        Примеры:
        >>> phone = Iphone17("серебристый", 256, 100)
        >>> phone.check_storage()
        """
        ...


class Book:
    """
    Класс, представляющий книгу (литературу).
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Создание и подготовка объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1869)
        """
        if not isinstance(title, str) or not title.strip():
            raise TypeError("Название должно быть непустой строкой")
        self.title = title.strip()

        if not isinstance(author, str) or not author.strip():
            raise TypeError("Автор должен быть непустой строкой")
        self.author = author.strip()

        if not isinstance(year, int):
            raise TypeError("Год издания должен быть целым числом")
        if year < 1000 or year > 2030:
            raise ValueError("Год издания должен быть в диапазоне 1000-2030")
        self.year = year

    def get_description(self) -> str:
        """
        Получение описания книги.

        :return: Строка с названием, автором и годом издания

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 1949)
        >>> book.get_description()
        """
        ...

    def is_old(self, current_year: int) -> bool:
        """
        Проверка, является ли книга старой (возраст > 50 лет).

        :param current_year: Текущий год
        :return: True, если книга старше 50 лет, иначе False

        Примеры:
        >>> book = Book("Евгений Онегин", "Александр Пушкин", 1833)
        >>> book.is_old(2024)
        """
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть целым числом")
        ...

    def read(self, pages: int) -> str:
        """
        Чтение указанного количества страниц.

        :param pages: Количество страниц для прочтения
        :return: Сообщение о прочитанных страницах

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        >>> book.read(50)
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        ...


if __name__ == "__main__":
    doctest.testmod(verbose=True)