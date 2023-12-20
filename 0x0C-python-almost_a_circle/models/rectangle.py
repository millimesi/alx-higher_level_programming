#!/usr/bin/python3
'''almost circle module'''


from models.base import Base

class Rectangle(Base):
    ''' Rectangle class inhertis from base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        
        if type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        
    @property
    def width(self):
        ''' width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        ''' width getter'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' width setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        ''' width getter'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' width setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        ''' width getter'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' width setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Displays its selfs'''
        print(self.__y * "\n", end="")
        for _ in range(self.__height):
            print(self.__x * " ", end="")
            for i in range(self.__width):
                if not(i == (self.__width - 1)):
                    print("#", end="")
                else:
                     print("#")

    def update(self, *args, **kwargs):
        '''update using *args'''
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.__width = args[1]
        if num_args >= 3:
            self.__height = args[2]
        if num_args >= 4:
            self.__x = args[3]
        if num_args >= 5:
            self.__y = args[4]
        if not args:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        ''' dictionary representation of a Square'''
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }

    def __str__(self):
        ''' string reperesentation the object'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
