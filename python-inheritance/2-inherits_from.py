"""
Function that returns true if object is an instance of a class that inherited a specified class.
"""
def inherits_from(obj,a_class):
    """
    Checks whether object is an instance of a class that inherited content in a specied class.

    Args:
         obj: instance of a class
        a_class: an inherited class or a  specified class

    Return:
         bool: True if obj is an instance of a_class,False otherwise.
    """
    if isinstance(obj,a_class) and type(obj) is not a_class:
        return True
    else:
        return False