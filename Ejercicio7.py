# -*- coding: utf-8 -*-
"""
Created on Wed May 3 12:18:52 2023

@author: jmrod
"""


def rango(minimo, maximo):
   
    print(f"El rango es de {minimo} a {maximo}")  # Mostramos el rango al usuario antes de que introduzca la información.

    while True: #Mientras no se cumpla no se cierra el while
        numero = int(input("Introduce un número entero dentro del rango: "))
        
        if minimo <= numero <= maximo: # Si el número introducido se encuentra dentro del rango, se devuelve el valor.
            return numero
        else:
            print("El número introducido no se encuentra del rango.") # Si no se encuentra, se muestra mensaje al usuario con la información


minimo = 1 # Definimos el valor mínimo
maximo = 150 #Definimos el valor máximo
numero_valido = rango(minimo, maximo)
print(f"El número introducido ({numero_valido}) está dentro del rango.")
   