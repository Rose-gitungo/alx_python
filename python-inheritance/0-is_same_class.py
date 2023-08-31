"""
Writing a Function that returns true if the object is exactly an instance of the specified class,
otheriwse returns False.

"""
def is_same_class(obj,a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj:The object to check.
        a_class: The class to compre against.

    Returns:
    bool: True if obj is an instance of a_class,False otherwise.
    """
    if isinstance(obj,a_class) == True:
         return True
    else:
         return False
