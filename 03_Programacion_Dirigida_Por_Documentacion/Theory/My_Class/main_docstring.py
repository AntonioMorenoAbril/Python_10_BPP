# Docstring documentation method

# Simple example: Level 1 
def myFunction():
    """Description of the function."""
    return None

# print(myFunction.__doc__)
help(myFunction)

# More complex example: Level 2

def myFunction1(arg1):
    """Description of the function.
    
    Extended description of the function
    
    Parameters:
    arg1 (int): Description of arg1
    
    Returns:
    int: Description of return value
    
    """
    return arg1

print(myFunction1.__doc__)