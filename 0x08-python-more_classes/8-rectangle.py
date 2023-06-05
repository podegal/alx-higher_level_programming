#!/usr/bin/python3
"""rectangle class definition"""


class Rectangle:
    """defines a rectangle class
    attributes:
           width: positive integer (private)
           height: positive integer (private)
           number_of_instances: positive integer (public)
           print_symbol: any type (public)"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates a new instance of a rectangle
        Args:
               width: width
               height: height
           Returns:
                  None
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance

        Args:
            value (int): the width of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle instance

        Args:
            value (int): the height of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle instance"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the the perimeter of a rectangle instance"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """gets the string representation of a rectangle
           Returns:
                  string with #
        """

        rep = ""

        if self.__height == 0 or self.width == 0:
            return (rep)
        for i in range(self.__height):
            rep += "#" * self.__width + '\n'

        return (rep[:-1])

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle by comparing their areas

        Args:
            rect_1: the first rectangule
            rect_2: the second rectangule

        Raises:
            TypeError: if either rectangles is not an instances of a class
        Rectangle"

        Returns:
            returns the bigger rectangle
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __del__(self):
        """prints a message when an instance of a Rectangle is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


