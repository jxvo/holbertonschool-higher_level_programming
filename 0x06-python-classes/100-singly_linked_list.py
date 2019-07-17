#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns private attr"""
        return self.__data

    @data.setter
    def data(self, value):
        """validates and sets private attr"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """simple initialization"""
        self.__head = None

    def __str__(self):
        """return string to stdout one node value per line, C-style"""
        node = self.__head
        list_lines = []
        while node is not None:
            list_lines.append(node.data)
            node = node.next_node
        return '\n'.join(str(idx) for idx in list_lines)

    def sorted_insert(self, value):
        """insert node into list sorted by numerical value, C-style"""
        if self.__head is not None:
            node = self.__head
            temp_node = None
            while node is not None and node.data <= value:
                temp_node = node
                node = node.next_node
            new_node = Node(value, node)
            if temp_node is None:
                self.__head = new_node
            else:
                temp_node.next_node = new_node
        else:
            self.__head = Node(value, None)
