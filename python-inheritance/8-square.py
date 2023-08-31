"""
A mdoule containing class Sqoare that inherits from class Rectangle 7-rectangle.py.
"""
Rectangle =__import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    A class square, inherits from class rectangle.
    """
    def __init__(self,size):
        self.integer_validator("size",size)
        self.__size=size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[square] {}/{}".format(self.__size,self.__size)
        