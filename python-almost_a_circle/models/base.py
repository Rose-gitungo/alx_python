"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
class Base:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    __nb_objects = 0

    def __init__(self, id= None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if id != None:
            id ==None
            self.id=id
        else:
            Base.__nb_objects +=1
            self.id=Base.__nb_objects
            