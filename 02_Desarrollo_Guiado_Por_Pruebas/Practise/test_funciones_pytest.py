import pytest 
from funciones import *

assert autoIncrement(100) == 100
assert autoIncrement(10) == 10
assert autoIncrement("texto") == 0
    
assert remainder(100,10) == 0
assert remainder(17,5) == 2
assert remainder(20,3) == 2

assert squarreRoot(100) == 10
assert squarreRoot(4) == 2
assert squarreRoot(3) == 3

    
    

        