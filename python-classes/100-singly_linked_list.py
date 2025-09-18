#!/usr/bin/python3
"""This module defines a SinglyLinkedList class."""


class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node with data and the next node.

        Args:
            data (int): Data value of the node.
            next_node (Node, optional): Next node reference."""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the reference to the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """New node inserted into the list in sorted order.

        Args:
            value (int): The data value of the new node to be inserted."""

        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
