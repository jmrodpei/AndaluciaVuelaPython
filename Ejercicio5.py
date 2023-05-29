# -*- coding: utf-8 -*-
"""
Created on Wed May 3 01:12:16 2023

@author: jmrod
"""




def NumeroPrimo(num):  # Definimos la función que realiza la comprobación del número introducido.
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
   
    return True

num = int(input("Introduce un número positivo por favor: ")) #Se pide que introduzca el usuario un número y se le especifica que sea positivo.

if NumeroPrimo(num): # Visualiza si el número es primo o no primo.
    
    print(f"{num} SI es un número primo")
else:
    print(f"{num} NO es un número primo. Si has introducido un número negativo, debes saber que los números negativos no pueden ser primos")
    