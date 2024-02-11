class Car:

    '''
    Реализация класса "Автомобиль"
    '''

    def __init__(self, _name: str = None, horsepower: int = None,
                 weight: int = None) -> None:
        '''
        Создание и подготовка к работе объекта "Автомобиль"

        :param _name: Полное название автомобиля
        :param horsepower: Мощность автомобиля в лошадиных силах
        :param weight: Масса автомобиля в килограммах

        Примеры:
        >>> car = Car('Toyota Corolla', 67, 1030)
        '''
        self.name = _name if _name else "Неизвестный автотмобиль"
        self.hp = horsepower if horsepower else 0
        self.weight = weight if weight else 0
    
    def __str__(self) -> str:
        return f'Автомобиль {self.name} мощностью {self.hp} л.с. и весом {self.weight} кг.'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.hp}, {self.weight})'
    
    def get_description(self) -> str:
        '''
        Возвращает описание автомобиля, полученное через web API.

        :return: Строковое описание автомобиля
        '''
        pass

    def get_unique_feature(self) -> str:
        '''
        Возвращает уникальную особенность автомобиля, в зависимости от его типа

        :return: Строковое описание особенности автомобиля
        '''
        return None if self.name == "Неизвестный автотмобиль" else self.name
                

class LightCar(Car):

    '''
    Реализация класса "Легковой автомобиль"
    '''

    def __init__(self, _name: str = None, horsepower: int = None,
                 weight: int = None, trunk_volume: float = None) -> None:
        '''
        Создание и подготовка к работе объекта "Легковой автомобиль"

        :param _name: Полное название автомобиля
        :param horsepower: Мощность автомобиля в лошадиных силах
        :param weight: Масса автомобиля в килограммах
        :param trunk_volume: Объем багажного отделения в литрах

        Примеры:
        >>> light_car = LightCar('Toyota Corolla', 67, 1030, 150)
        '''
        super().__init__(_name, horsepower, weight)
        self.trunk_volume = trunk_volume if trunk_volume else 0.0
    
    def __str__(self) -> str:
        return f'Легковой автомобиль {self.name} мощностью {self.hp} л.с.' + \
               f'и весом {self.weight} кг. с объемом багажника {self.trunk_volume} литров.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.hp}, {self.weight}, {self.trunk_volume})'

    def get_description(self) -> str:
        '''
        Возвращает описание автомобиля, полученное через web API.

        :return: Строковое описание автомобиля
        '''
        return super().get_description()

    def get_unique_feature(self) -> str:
        '''
        Возвращает уникальную особенность автомобиля, в зависимости от его типа

        Причина перегрузки метода: другая особенность

        :return: Строковое описание особенности автомобиля
        '''
        return f'Объем багажника {self.trunk_volume} м3.'
                

class Truck(Car):

    '''
    Реализация класса "Грузовой автомобиль"
    '''

    def __init__(self, _name: str = None, horsepower: int = None,
                 weight: int = None, load_capacity: int = None) -> None:
        '''
        Создание и подготовка к работе объекта "Грузовой автомобиль"

        :param _name: Полное название автомобиля
        :param horsepower: Мощность автомобиля в лошадиных силах
        :param weight: Масса автомобиля в килограммах
        :param load_capacity: Максимальная грузоподъемность в килограммах

        Примеры:
        >>> truck = Truck('Kamaz 6310', 435, 14150, 11500)
        '''
        super().__init__(_name, horsepower, weight)
        self.load_capacity = load_capacity if load_capacity else 0
    
    def __str__(self) -> str:
        return f'Грузовой автомобиль {self.name} мощностью {self.hp} л.с.' + \
                f'и весом {self.weight} кг. с грузоподъемностью {self.load_capacity} кг.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.hp}, {self.weight}, {self.load_capacity})'

    def get_description(self) -> str:
        '''
        Возвращает описание автомобиля, полученное через web API.

        :return: Строковое описание автомобиля
        '''
        return super().get_description()

    def get_unique_feature(self) -> str:
        '''
        Возвращает уникальную особенность автомобиля, в зависимости от его типа

        Причина перегрузки метода: другая особенность

        :return: Строковое описание особенности автомобиля
        '''
        return f'Грузоподъемность {self.load_capacity} кг.'
                