from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception("The car cannot fly")  # that's bad
