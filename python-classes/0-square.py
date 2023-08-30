""""python3 -c 'print(__import__("my_module").__doc__)'"""
class Square():
    """"python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    size=""
    def __init__(self,size) -> None:   
        self.size=size
        
my_square = Square(89)
print(type(my_square))
print(my_square.__dict__)

