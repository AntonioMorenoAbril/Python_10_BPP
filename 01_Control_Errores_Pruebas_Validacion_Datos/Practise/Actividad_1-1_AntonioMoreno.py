class MiExcepcion(Exception):
    pass

def dameEntero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero > 10:
                raise MiExcepcion("El número no puede ser mayor a 10.")
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            
        except MiExcepcion as e:
            print("Error:", e)

# Ejemplo de uso
numero_ingresado = dameEntero()
print("El número entero ingresado es:", numero_ingresado)
    
    
    