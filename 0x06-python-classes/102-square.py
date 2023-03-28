#!/usr/bin/python3

class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int or float): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with the given size."""
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Returns True if the area of this square is equal to the area of the other square."""
        if isinstance(other, Square):
            return self.size == other.size
        return NotImplemented

    def __ne__(self, other):
        """Returns True if the area of this square is not equal to the area of the other square."""
        if isinstance(other, Square):
            return self.size != other.size
        return NotImplemented

    def __lt__(self, other):
        """Returns True if the area of this square is less than the area of the other square."""
        if isinstance(other, Square):
            return self.size < other.size
        return NotImplemented

    def __le__(self, other):
        """Returns True if the area of this square is less than or equal to the area of the other square."""
        if isinstance(other, Square):
            return self.size <= other.size
        return NotImplemented

    def __gt__(self, other):
        """Returns True if the area of this square is greater than the area of the other square."""
        if isinstance(other, Square):
            return self.size > other.size
        return NotImplemented

    def __ge__(self, other):
        """Returns True if the area of this square is greater than or equal to the area of the other square."""
        if isinstance(other, Square):
            return self.size >= other.size
        return NotImplemented
