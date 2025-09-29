#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0
        self._length = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._length:
            value = self._iterable[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def count(self):
        return self._index
