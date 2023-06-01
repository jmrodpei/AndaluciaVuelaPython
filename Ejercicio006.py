# -*- coding: utf-8 -*-
"""
Created on Wed May 3 10:22:14 2023

@author: jmrod
"""


def NumeroPrimo(numero): #Escribimos una función que valore si es primo o no el número pasado por parámetro posteriormente.
   
    if numero <= 1: # Si el número es menor o igual a 1, no puede ser número primo.
        return False 

    for i in range(2, numero // 2 + 1): 
        if numero % i == 0:
            return False

    return True
numero = 33; #Definimos el valor del número. 

if NumeroPrimo(numero):
    print(f"El número {numero} SI es primo")
else:
    print(f"El número {numero} NO es primo")
