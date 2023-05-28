def sumar(x,y):
    return x + y

def dividir(x,y):
    if y == 0:
        raise ValueError("No puedes dividir por 0")
    else:
        return x/y