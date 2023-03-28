#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        """ Initializes a new Node object with data and
         a reference to the next Node object in the list """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets the value of the data attribute """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Sets the value of the data attribute if it is an integer,
        otherwise raises a TypeError exception """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets the reference to the next Node object in the list """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Sets the reference to the next Node object in the list
        if it is None or a Node object, otherwise raises a TypeError exception """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """ Initializes a new SinglyLinkedList object with
        a None value for the head attribute """
        self.head = None

    def __str__(self):
        """ Returns a string representation of the SinglyLinkedList object,
        with each node's data value on a separate line """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return ("\n".join(nodes))

    def sorted_insert(self, value):
        """ Inserts a new Node object with the specified value into the
        correct sorted position in the SinglyLinkedList object """
        new_node = Node(value)
        if self.head is None:
            """ If the SinglyLinkedList object is empty,
            the new Node object becomes the head """
            self.head = new_node
        elif self.head.data > value:
            """ If the new Node object's data value is less than the head's
            data value, the new Node object becomes the new head """
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                """ Traverse through the SinglyLinkedList object to find
                the correct position for the new Node object """
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
