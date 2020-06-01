from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_fabric_consumption(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def some_parameter(self):
        pass

    @abstractmethod
    def some_parameter(self):
        pass


class Coat(Clothes):
    def __init__(self, some_parameter):
        self.some_parameter = some_parameter
        self.result = round(self.some_parameter / 6.5 + 0.5, 2)
        super().__init__()

    @property
    def some_parameter(self):
        return self.__size

    @some_parameter.setter
    def some_parameter(self, some_parameter):
        if isinstance(some_parameter, str):
            print('Size parameter have to be a number')
        elif some_parameter < 20 or some_parameter > 60:
            print('We produce only sizes from 20 to 60')
        elif (isinstance(some_parameter, int) or isinstance(some_parameter, float)) and (20 <= some_parameter <= 60):
            self.__size = some_parameter

    @property
    def get_fabric_consumption(self):
        return self.result

    def __str__(self):
        return f"Consumption of fabric for coat making {self.result}"


class Suit(Clothes):
    def __init__(self, some_parameter):
        self.some_parameter = some_parameter
        self.result = round(2 * self.some_parameter + 0.3, 2)
        super().__init__()

    @property
    def some_parameter(self):
        return self.__height

    @some_parameter.setter
    def some_parameter(self, some_parameter):
        if isinstance(some_parameter, int) or isinstance(some_parameter, float):
            self.__height = some_parameter
        else:
            print('Height parameter have to be a number')

    @property
    def get_fabric_consumption(self):
        return self.result

    def __str__(self):
        return f"Consumption of fabric for suit making  {self.result}"


try:
    coat1 = Coat(45)
    # cause of using @ property decorator can use method as object handling usual point notation
    coat1_fabric = coat1.get_fabric_consumption
    suit1 = Suit(32)
    # cause of using @ property decorator can use method as object handling usual point notation
    suit1_fabric = suit1.get_fabric_consumption
    print(coat1, suit1, sep='\n')
    print(f'Final result of fabric consumption: {round(coat1_fabric + suit1_fabric, 2)}')
except AttributeError as a:
    print(a)
