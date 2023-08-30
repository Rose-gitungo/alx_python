class BaseGeometry():
    """base geometry class"""
    
    def __init__(self) -> None:
        """an empty"""
        pass

    def area(self):
        """an area class"""
        raise Exception ("area() is not implemented")
    
    def integer_validator(self,name,value):
        """integer validator class"""
        name
        if not isinstance(value,int):
            raise TypeError (name + " must be an integer")
        
        if value <=0:
            raise ValueError (name +" must be greater than 0")
        
class Rectangle(BaseGeometry):

    def __init__(self,width,height):
        """an initializaion class"""
        self.__width=width
        self.__height=height

        super().integer_validator(width,height)


