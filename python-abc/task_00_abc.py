#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal abstract base class"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses to make a sound."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Implementation of the abstract method sound for Dog."""
        return "Woof!"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Implementation of the abstract method sound for Cat."""
        return "Meow!"
