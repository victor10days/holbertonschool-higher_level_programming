#!/usr/bin/python3

from abc import ABC, abstractmethod

class Fish(ABC):
    @abstractmethod
    def swim(self):
        return 'The fish is swimming.'
    
    def habitat(self):
        return "The fish lives in water."
    
class Bird(ABC):
    @abstractmethod
    def fly(self):
        return 'The bird is flying.'
    
    def habitat(self):
        return "The bird lives in the sky."
    
class FlyingFish(Fish, Bird):
    def swim(self):
        return 'The flying fish is swimming.'
    
    def fly(self):
        return 'The flying fish is soaring'
    
    def habitat(self):
        return "The flying fish lives in both water and air."
