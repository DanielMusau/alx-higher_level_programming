#!/usr/bin/python3
"""This module contains a class that defines a Node
for a singly linked list.
"""


class Node:
    """ This is a class that defines a node."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter. """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter. """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ next node getter. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Next node setter. """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Class that defines linked list. """
    def __str__(self):
        """ string representation. """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """ Initialization. """
        self.__head = None

    def sorted_insert(self, value):
        """ Insert node. """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
