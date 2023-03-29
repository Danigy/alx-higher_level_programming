#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2023  Alx-Software Engineering Class, batch 11
#           Repository: alx-higher_level_programming
#           Directory: 0x06-python-classes
# -----------------------------------------------------------
"""
This module contains a class that defines a square.
Usage Example:
    Square = __import__('1-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
