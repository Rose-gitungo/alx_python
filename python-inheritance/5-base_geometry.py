class BaseGeometry():
    """base geometry class"""
    
    def __init__(self) -> None:
        """empty class"""
        pass

    def area(self):
        """area class"""
        raise Exception ("area() is not implemented")
    
    def integer_validator(self,name,value):
        """integer validator """
        name
        if not isinstance(value,int):
            raise TypeError (name + " must be an integer")
        if value <=0:
            raise ValueError (name +" must be greater than 0")