#!/usr/bin/python3
"""Square Class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiatlizing Squares"""
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = None
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
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) > 3:
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        obj_dictionary = {'id': self.id, 'size': self.__size, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
