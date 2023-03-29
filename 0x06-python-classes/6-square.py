#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2023  Alx-Software Engineering Class, batch 11
#           Repository: alx-higher_level_programming
#           Directory: 0x06-python-classes
# -----------------------------------------------------------
"""Square Class.
This module contains a class that defines a square.
Usage Example:
    Square = __import__('6-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Defines the blueprint of a square.
    Attribute:
        size (int): An integer representing the object size.
        position (int, int): The position of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size private attribute value.
        Validates the assignment of the size private attribute.
        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sets the position private attribute value.
        Validates the assignment of the position private attribute.
        Arg:
            value: the value to be set
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Displays the square object with # character"""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
