"""
A Function that returns true if object is an instance of , or
if the object is an instance of a class that inherited the specified class.
"""
def is_kind_of_class(obj,a_class):
    """
    Checks whether object is an instance of or if object is an instance of a class that inherited the specified class,returns True
    otherwise False

    Args:
        obj: instance of a class
        a_class: an inherited class or a  specified class

    Return:
         bool: True if obj is an instance of a_class,False otherwise.
    """
    if isinstance(obj,a_class) == True or issubclass(a_class,int)==True:
       __name__ = type(obj)
       return True and __name__
    else:
        return False