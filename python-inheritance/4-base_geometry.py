"""
a module containg a class BaseGeomtery
"""
class BaseGeometry():
    """
    A class BaseGeometry
    """
    
    def __init__(self) -> None:
        """
        An initialization function.
        """
        pass

    def area(self):
        """
        Calculates the area.

        Raises:
            Exception: always raisies an exception,"area() is not implemented"
        """
        raise Exception ("area() is not implemented")