class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return (self._size)

    @size.setter
    def size(self, value):
        """Set the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the current area of the square"""
        return (self._size ** 2)

    def my_print(self):
        """Print the square with the # character"""
        if self._size == 0:
            print("")
        else:
            for i in range(self._size):
                print("#" * self._size)
