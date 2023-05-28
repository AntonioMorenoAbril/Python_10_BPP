import pytest

# Definimos funcion a testear
def capital(x):
    return x.capitalize()

# Definimos los test

def test_capital1():
    assert capital("hola") == "Hola"
