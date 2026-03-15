class Car:
    """
    Базовый класс, представляющий автомобиль.

    Атрибуты:
        make (str): Марка автомобиля (только для чтения).
        model (str): Модель автомобиля (только для чтения).
        year (int): Год выпуска (только для чтения).
        _engine_running (bool): Состояние двигателя (защищённый атрибут).
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация автомобиля.

        Аргументы:
            make: Марка.
            model: Модель.
            year: Год выпуска.
        """
        self._make = make
        self._model = model
        self._year = year
        self._engine_running = False  # двигатель заглушен

    @property
    def make(self) -> str:
        """Возвращает марку автомобиля (только для чтения)."""
        return self._make

    @property
    def model(self) -> str:
        """Возвращает модель автомобиля (только для чтения)."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска (только для чтения)."""
        return self._year

    def start_engine(self) -> None:
        """
        Запускает двигатель.

        Двигатель можно запустить только если он ещё не запущен.
        В реальном классе здесь была бы проверка и изменение состояния.
        """
        if not self._engine_running:
            self._engine_running = True
            print(f"{self.make} {self.model}: двигатель запущен")
        else:
            print(f"{self.make} {self.model}: двигатель уже работает")

    def stop_engine(self) -> None:
        """
        Останавливает двигатель.

        Двигатель можно остановить только если он запущен.
        """
        if self._engine_running:
            self._engine_running = False
            print(f"{self.make} {self.model}: двигатель остановлен")
        else:
            print(f"{self.make} {self.model}: двигатель уже заглушен")

    def get_info(self) -> str:
        """
        Возвращает:
            str: Строка с маркой, моделью и годом.
        """
        return f"{self.make} {self.model}, {self.year} г."

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return self.get_info()

    def __repr__(self) -> str:
        """Официальное строковое представление для воссоздания объекта."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class PassengerCar(Car):
    """
    Класс легкового автомобиля, наследующий Car.

    Дополнительный атрибут:
        seats (int): Количество пассажирских мест.
    """

    def __init__(self, make: str, model: str, year: int, seats: int) -> None:
        """
        Инициализация легкового автомобиля.

        Аргументы:
            make: Марка.
            model: Модель.
            year: Год выпуска.
            seats: Количество мест (целое положительное число).
        """
        super().__init__(make, model, year)
        # Присваиваем через свойство для проверки (хотя сеттер не реализован, можно напрямую)
        self._seats = seats

    @property
    def seats(self) -> int:
        """Количество мест (только для чтения)."""
        return self._seats

    def get_info(self) -> str:
        """
        Перегруженный метод: добавляет информацию о количестве мест.

        Причина перегрузки: для легкового автомобиля важно указывать пассажировместимость.
        """
        base_info = super().get_info()
        return f"{base_info}, мест: {self.seats}"

    def __repr__(self) -> str:
        """Перегружен для включения дополнительного атрибута seats."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r}, seats={self.seats!r})"


class Truck(Car):
    """
    Класс грузового автомобиля, наследующий Car.

    Дополнительный атрибут:
        cargo_capacity (float): Грузоподъёмность в тоннах.
    """

    def __init__(self, make: str, model: str, year: int, cargo_capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        Аргументы:
            make: Марка.
            model: Модель.
            year: Год выпуска.
            cargo_capacity: Грузоподъёмность (положительное число).
        """
        super().__init__(make, model, year)
        self._cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self) -> float:
        """Грузоподъёмность (только для чтения)."""
        return self._cargo_capacity

    def get_info(self) -> str:
        """
        Перегруженный метод: добавляет информацию о грузоподъёмности.

        Причина перегрузки: для грузового автомобиля важно указывать грузоподъёмность.
        """
        base_info = super().get_info()
        return f"{base_info}, грузоподъёмность: {self.cargo_capacity} т"

    def __repr__(self) -> str:
        """Перегружен для включения дополнительного атрибута cargo_capacity."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r}, cargo_capacity={self.cargo_capacity!r})"


if __name__ == "__main__":
    # Пример использования
    car = Car("Porsche 911", "Turbo S", 2016)
    print(car)                     # __str__
    print(repr(car))                # __repr__
    car.start_engine()              # унаследованный метод
    car.stop_engine()

    print("-" * 30)

    passenger = PassengerCar("Honda", "Civic", 2021, 5)
    print(passenger)                # перегруженный __str__ (через get_info)
    print(repr(passenger))           # перегруженный __repr__
    passenger.start_engine()         # унаследован от Car
    passenger.stop_engine()

    print("-" * 30)

    truck = Truck("УАЗ", "Патриот", 2005, 7)
    print(truck)                     # перегруженный __str__
    print(repr(truck))                # перегруженный __repr__
    truck.start_engine()              # унаследован
    truck.stop_engine()