#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2023  Alx-Software Engineering Class, batch 11
#           Repository: alx-higher_level_programming
#           Directory: 0x06-python-classes
# -----------------------------------------------------------
"""Square Class.
This module contains a class that defines a square.
Usage Example:
    Square = __import__('1-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""

class Square:
    """Defines the blueprint of a square.
    Attribute:
        size: An integer indicating the size of the square object.
    """

    def __init__(self, size):
        """An object constructor method.
        Initiatilizes Square with size.
        Arg:
            size: A integer representing object size
        """
        self.__size = size
