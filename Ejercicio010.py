# -*- coding: utf-8 -*-
"""
Created on Thu May 4 10:29:36 2023

@author: jmrod
"""

def sumaMatrices(matriz1, matriz2): # Mediante len creamos una función y definimos como serán las matrices
   
    n1 = len(matriz1)
    m1 = len(matriz1[0])
    n2 = len(matriz2)
    m2 = len(matriz2[0])


    if n1 != n2 or m1 != m2: # Mediante este if visualizamos si las dimensiones son compatibles. Si no, devuelve un none
        return None

    
    operacion = [] # Se crea la matriz para almacenar la suma y se define la operación suma devolviendo el resultado.
    for i in range(n1):
        fila_suma = []
        for j in range(m1): 
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        operacion.append(fila_suma)

    return operacion


matriz1 = [[2, 3, 6], [2,4, 3]] # Definimos la lista numero 1 = matriz 1
matriz2 = [[4, 7, 1], [1, 2, 4]] # Definimos la lista numero 2 = matriz 2

resultado = sumaMatrices(matriz1, matriz2)

if resultado is None: 
    print("Las dimensiones no son las mismas, por ello no es posible la suma de ambas.") # Mostramos mensaje si las dimensiones no son las mismas.
else:
    print("El resultado de la suma es:") # Mostramos la matriz resultante de la suma de ambas.
    for fila in resultado:
        print(fila)
