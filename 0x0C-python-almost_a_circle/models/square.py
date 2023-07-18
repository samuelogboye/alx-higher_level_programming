#!/usr/bin/python3
"""Square Class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiatlizing Squares"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        if id is not None and not isinstance(id, int):
            raise TypeError("id must be an integer")
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = id if id is not None else 0
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    """Setter and Getter"""
    @property
    def size(self):
        """Getting the value of size"""
        return self.__size

    @property
    def x(self):
        """getting the value of x"""
        return self.__x

    @property
    def y(self):
        """Getting the value of y"""
        return self.__y

    """Setter"""
    @size.setter
    def size(self, value):
        """Function that set the value of size conditions to raise
        exceptions"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """A public method that assign attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None:
                    if type(args[0]) != int:
                        raise TypeError("id must be an integer")
                    if args[0] < 0:
                        raise ValueError("id must be >= 0")
                    self.id = args[0]
            if len(args) > 1:
                if not isinstance(args[1], int):
                    raise TypeError("size must be an integer")
                if args[1] <= 0:
                    raise ValueError("size must be > 0")
                self.__size = args[1]
            if len(args) > 2:
                if args[2] < 0:
                    raise ValueError("x must be >= 0")
                if not isinstance(args[2], int):
                    raise TypeError("x must be an integer")
                self.__x = args[2]
            if len(args) > 3:
                if args[3] < 0:
                    raise ValueError("y must be >= 0")
                if not isinstance(args[3], int):
                    raise TypeError("y must be an integer")
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        if type(value) != int:
                            raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    if value <= 0:
                        raise ValueError("size must be > 0")
                    if not isinstance(value, int):
                        raise TypeError("size must be an integer")
                    self.__size = value
                if key == "x":
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    self.__x = value
                if key == "y":
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        obj_dictionary = {'id': self.id, 'size': self.__size, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
