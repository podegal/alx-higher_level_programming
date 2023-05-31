#!/usr/bin/python3
""" Defines a Node class and a SinglyLinkedList class
"""


class Node:
    """ Node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initialize the node attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrives the data value"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Set the data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives next_node value"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node value"""
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list"""
    def __init__(self):
        """ Initialize the singly linky list"""
        self.__head = None

    def __str__(self):
        """Makes the singly linked list printable"""
        slList = ""
        prnt = self.__head

        while prnt:
            slList += str(prnt.data)
            if prnt.next_node:
                slList += "\n"
            prnt = prnt.next_node
        return (slList)

    def sorted_insert(self, value):
        """Sorts an insert a new node to the corresponding
        position"""

        prnt = self.__head
        while prnt:
            if prnt.data > value:
                break
            prev = prnt
            prnt = prnt.next_node
        new_node = Node(value, prnt)
        if prnt == self.__head:
            self.__head = new_node
        else:
            prev.next_node = new_node
