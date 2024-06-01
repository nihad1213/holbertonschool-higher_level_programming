#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Class representing a Dog, subclass of Animal."""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """Class representing a Cat, subclass of Animal."""

    def sound(self):
        return "Meow"
