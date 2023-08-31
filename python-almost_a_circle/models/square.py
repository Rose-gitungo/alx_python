"""python3 -c 'print(__import__("my_module").__doc__)'"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, size, x=0, y=0, id=None):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        """python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width, self.height)
    
    @property
    def size(self):
        """
        Getter for size attributes
        """
        return self.width
    
    @size.setter
    def size(self,value):
        """
        setter for size attributes
        """
        self.width = value
        self.height = value