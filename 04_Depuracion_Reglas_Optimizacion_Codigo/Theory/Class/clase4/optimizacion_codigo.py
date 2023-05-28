#compresión de listas 
cuadrados = []
for i in range(10):
    cuadrados.append(i**2)
    

# nueva_lista = [expresión for elemento in iterable]
'''
nueva_lista: es la lista resultante que se creará a partir de la comprensión.
expresión: es la operación o cálculo que se realizará en cada elemento del iterable.
elemento: es la variable que representa cada elemento del iterable en cada iteración.
iterable: es una secuencia, como una lista, una cadena de texto, una tupla o incluso otro objeto iterable.
'''

cuadrados = [i**2 for i in range(10)]

numeros = [1, 2, 3, 4, 5]

pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
        
pares = [x for x in numeros if x % 2 == 0]

palabras = ["hola", "python", "comprension", "listas"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes) 


#funcion map
#map(funcion, iterable)
'''
función: es la función que deseas aplicar a cada elemento del iterable.
iterable: es una secuencia, como una lista, una tupla o incluso otro objeto iterable.
'''
def cuadrados(x):
    return x**2

cuadrados = lambda x: x**2

cuadrados(2)

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados) 
