"""
Module containing an integer validator.
"""
class BaseGeometry():
    """
    A base class in a Geometry-related field.
    """
    
    def __init__(self) -> None:
        """
        empty class
        """
        pass

    def area(self):
        """
        Function that calculates area.

        Raise:
        Exception: Always raises an exception "area() is not implemented.
        """
        raise Exception ("area() is not implemented")
    
    def integer_validator(self,name,value):
        """
        Function that validates integers.

        Args;
            name: assumed to be always a string.
            value: integer to be validated.
        """
        name
        if not isinstance(value,int):
            raise TypeError (name + " must be an integer")
        
        if value <=0:
            raise ValueError (name +" must be greater than 0")
        
class Rectangle(BaseGeometry):
    """
    A class rectangle that inherits from BasGeometry.
    """

    def __init__(self,width,height):
        """
        an initializaion class

        Args:
            width: width of rectangle
            height:heigth of rectangle
        """

        self.integer_validator("width",width)
        self.integer_validator("height",height)

        self.__width=width
        self.__height=height

       

