def is_kind_of_class(obj,a_class):
    """a function"""
    if isinstance(a_class,int) == True or issubclass(a_class,int):
       __name__ = type(obj)
       return True and __name__
    else:
        return False