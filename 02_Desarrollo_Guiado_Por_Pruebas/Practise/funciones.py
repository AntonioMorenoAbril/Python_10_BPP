import math 

# Function 1: Autoincrement  

def autoIncrement(limit):
    try:
        limit = int(limit)
        x = 0
        start = 1
        increment = 1
        autoIncrement_list = []
        while x <limit:
            if x == 0:
                x = start
            else:
                x += increment 
            autoIncrement_list.append(x)
        return len(autoIncrement_list)
                    
    except Exception as e:
        return(f"Error {e}, It must be an integer")  

# Function 2: Remainder
def remainder(x,y):
    if y == 0:
        raise ZeroDivisionError ("Not possible divide by 0")
        
    else:
        rem =  x % y
        return rem
        
# Function 3: Squarre root
def squarreRoot(x):
    if x < 0:
        raise Exception ("Not possible negative values")
    else:
        squrt = math.sqrt(x)
        return squrt
