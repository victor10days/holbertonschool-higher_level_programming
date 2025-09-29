#!/usr/bin/python3

from abc import ABC, abstractmethod
import list

class VerboseList(list, ABC):
    @abstractmethod
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    @abstractmethod
    def extend(self, iterable):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    @abstractmethod
    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list.")

    @abstractmethod
    def pop(self, index=-1):
        super().pop(index)
        print(f"Popped item at index {index} from the list.")
