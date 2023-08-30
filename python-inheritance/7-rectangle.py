class BaseGeometry():
    """BaseGeometry class"""
    def __init__(self,) -> None:
        pass

    @property
    def area(self):
        """a getter"""
        return self.__area
    
    @area.setter
    def area(self,area):
        """a setter"""
        self.__area = area 
    
    def integer_validator(self,name,value):
        """an integer validator"""
        name
        if not isinstance(value,int):
            raise TypeError (name + " must be an integer")
        
        if value <= 0:
            raise ValueError (name +" must be greater than 0")
        
class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self,width,height):
        """initialization of rectangle"""
        self.__width=width
        self.__height=height
        area= width * height

        super().integer_validator(width,height)
        x='[Rectangle] ' + str(width) +'/'+str(height)+'\n'
        y= str(area)
        print(x + y)

       


