# ACTIVIDAD 1.1

# Importamos python debugger
# import pdb
# pdb.set_trace()

#Method 1: Compresion de lista
# Creamos lista
list_example = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
max_1 = [max(i) for i in list_example]
print(max_1)



#Method 2: Usando map
# max_2 = list(map(lambda x: max(x), list_example))
# print(max_2)

# ACTIVIDAD 1.2

list_random = [1,4,5,6,10,20,33,22,54,65]

primos = list(filter(lambda x: x%2 != 0, list_random))
print(primos)