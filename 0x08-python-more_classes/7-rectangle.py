#!/usr/bin/python3
"""Defines a Rectangle class
"""


class Rectangle:
    """Define a rectangle
       attributes:
           width: positive integer (private)
           height: positive integer (private)
           number_of_instances: positive integer (public)
           print_symbol: any type (public)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a new instance of the rectangle
           Args:
               width: width
               height: height
           Returns:
                  None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value of the width
           Args:
               value: value to be set
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value fo the heigth
           Args:
               value: value to be set
           Returns:
                  None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """evaluate the area of the rectangle
           Returns:
                  area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Evaluate the perimeter of the rectangle
           Returns:
                  perimiter
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """get the string representation of a rectangle
           Returns:
                  string with print_symbol attribute
        """

        rep = ""

        if self.__height == 0 or self.width == 0:
            return (rep)
        for i in range(self.__height):
            rep += str(self.print_symbol) * self.__width + '\n'

        return (rep[:-1])

    def __repr__(self):
        """get the string representation of a rectangle
           object
           Return:
                 that string representation
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """prints message when a rectangle object is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
