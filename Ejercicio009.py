# -*- coding: utf-8 -*-
"""
Created on Wed May 3 19:51:23 2023

@author: jmrod
"""

def matrizEnteros(n, m): #Creamos la función para crear la matrizlista de listas
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            celda = int(input(f"Introduce el valor para la celda ({i}, {j}): "))
            fila.append(celda)
        matriz.append(fila)
    return matriz;


n = 4 # Definimos que la matriz tendra 4 filas.
m = 3 #Definimos que la matriz contendrá 3 columnas.

matriz_resultado = matrizEnteros(n, m) #Mostramos la matriz generada con los valores introducidos por usuario
print("La matriz creada es:")
for fila in matriz_resultado:
    print(fila)
