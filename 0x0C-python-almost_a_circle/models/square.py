#!/usr/bin/python3
'''almost circle module'''


from models.rectangle import Rectangle

class Square(Rectangle):
    '''square inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width
    
    @size.setter
    def size(self, value):
        ''' size setter'''
        self.width = value
    
    def update(self, *args, **kwargs):
        '''updates the attributes value'''
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]
        if not args:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        ''' dictionary representation of a Square'''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        ''' string reperesentation the object'''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
