#!/usr/bin/python3
"""CLass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Definined Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method that initializes value for rectangle object"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    # height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # x getter and setter
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # y getter and setter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """method that prints a rectangle with sign '#' """
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """a method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """A Public method that assign an argument to all attributes."""
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    if not isinstance(args[i], int):
                        raise TypeError("id must be an integer")
                    if args[i] <= 0:
                        raise ValueError("id must be > 0")
                    self.id = args[i]
                elif i == 1:
                    if not isinstance(args[i], int):
                        raise TypeError("width must be an integer")
                    if args[i] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = args[i]
                elif i == 2:
                    if not isinstance(args[i], int):
                        raise TypeError("height must be an integer")
                    if args[i] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = args[i]
                elif i == 3:
                    if not isinstance(args[i], int):
                        raise TypeError("x must be an integer")
                    if args[i] <= 0:
                        raise ValueError("x must be > 0")
                    self.__x = args[i]
                elif i == 4:
                    if not isinstance(args[i], int):
                        raise TypeError("y must be an integer")
                    if args[i] <= 0:
                        raise ValueError("y must be > 0")
                    self.__y = args[i]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    if value <= 0:
                        raise ValueError("id must be > 0")
                    self.id = value
                elif key == "width":
                    if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                elif key == "height":
                    if not isinstance(value, int):
                        raise TypeError("height must be an integer")
                    if value <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = value
                elif key == "x":
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value <= 0:
                        raise ValueError("x must be > 0")
                    self.__x = value
                elif key == "y":
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value <= 0:
                        raise ValueError("y must be > 0")
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}
        return obj_dictionary
