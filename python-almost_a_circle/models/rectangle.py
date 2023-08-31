"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
from models.base import Base

class Rectangle(Base):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self,width,height,x=0,y=0,id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__width
    
    @width.setter
    def width(self,width):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
         
        raise: typeError with the message <name of attribute> must be an integer if input is not integer.
        """
        if isinstance(width,int)==False:
            raise TypeError ("width must be an integer")
        else:
            print('OK')
        
        if width <= 0 :
            raise ValueError(' weight must be > 0')
        else:
            print('OK')
        
        self.__width = width

    @property
    def height(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__height
    
    @height.setter
    def height(self,height):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if isinstance(height,int)==False:
            raise TypeError (" height must be an integer")
        else:
            print('OK')
        
        if height <= 0 :
            raise ValueError(' height must be > 0')
        else:
            print('OK')
        
        self.__height = height

    @property
    def x(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__x
    
    @x.setter
    def x(self,x):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if isinstance(x,int)==False:
            raise TypeError (("x must be an integer"))
        else:
            print('OK')
        
        if x < 0 :
            raise ValueError( 'x must be >= 0')
        else:
            print('OK')
        
        self.__x = x

    @property
    def y(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__y
    
    @y.setter
    def y(self,y):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if  isinstance(y,int)==False:
            raise TypeError ("y must be an integer")
        else:
            print('OK')
        
        if y < 0 :
            raise ValueError ("y must be >= 0")
        else:
            print('OK')
        
        self.__y = y    
    
   

