from typing import Protocol
from abc import ABC, abstractmethod
try:
    from typing import override
except ImportError:
    from typing_extensions import override


class IAnimal(Protocol):
    def get_value(self, corn_cost, hay_cost): ...
    def get_feed_cost(self, corn_cost, hay_cost): ...


class Animal(IAnimal, ABC):
    def __init__(self, name, weight, corn, hay):
        self.__name = name
        self.weight = weight
        self.num_corn = corn
        self.num_haybales = hay

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_value(self, corn_cost, hay_cost):
        pass  # raise NotImplemented

    def get_feed_cost(self, corn_cost, hay_cost):
        return (self.num_corn * corn_cost) + (self.num_haybales * hay_cost)


class Cow(Animal):
    MILK_PRICE_LB = 0.20

    def __init__(self, name, weight, milk, corn, hay):
        super().__init__(name, weight, corn, hay)
        self.milk = milk

    def get_value(self, corn_cost, hay_cost):
        return (self.milk * Cow.MILK_PRICE_LB) - self.get_feed_cost(corn_cost, hay_cost)


class Horse(Animal):
    def __init__(self, name, weight, corn, hay, rides, ride_cost):
        super().__init__(name, weight, corn, hay)
        self.num_rides = rides
        self.ride_cost = ride_cost

    def get_value(self, corn_cost, hay_cost):
        return (self.num_rides * self.ride_cost) - self.get_feed_cost(corn_cost, hay_cost)

    @override
    def get_name(self):
        return super().get_name() + super().get_name()
