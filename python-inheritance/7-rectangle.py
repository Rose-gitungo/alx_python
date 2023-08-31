"""
A module that inherits BaseGeomtry from 5-base_geometry.
"""
BaseGeometry =__import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits BaseGeomtry.
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

    def __str__(self) -> str:
        """
        Returning a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width,self.__height)

    def area(self):
        """
        function to calculate area.

        Returns:
             self.__height * self.__width
        """
        return self.__height * self.__width
       


