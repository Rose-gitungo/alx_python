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
        if not isinstance(width,int):
            raise TypeError ("width must be an integer")
        
        if width <= 0 :
            raise ValueError(' weight must be > 0')
        
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
        if not isinstance(height,int):
            raise TypeError (" height must be an integer")
        
        if height <= 0 :
            raise ValueError(' height must be > 0')
        
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
        if not isinstance(x,int):
            raise TypeError (("x must be an integer"))
        
        if x < 0 :
            raise ValueError( 'x must be >= 0')
        
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
        if not isinstance(y,int):
            raise TypeError (" y must be an integer")
        
        if y < 0 :
            raise ValueError ("y must be >= 0")
        
        self.__y = y    

    def area(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__width * self.__height
    
    def display(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        for _ in range(self.__height):
            print('#'*self.__width)
        
    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x,self.y,self.width,self.height)

    def display(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print('#'*self.__width+'$'*self.__x)

    def update(self,*args):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if args:
            attributes = ['id','width','height','x','y']

            for i, value in enumerate(args):
                setattr(self,attributes[i],value)

    def update(self,*args,**kwargs):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if args:
            attributes = ['id','width','height','x','y']

            for i, value in enumerate(args):
                setattr(self,attributes[i],value)
            else:
                for key,value in kwargs.items():
                    setattr(self,key,value)

            
   

