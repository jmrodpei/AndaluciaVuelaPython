# -*- coding: utf-8 -*-
"""
Created on Tue May 2 18:12:18 2023

@author: jmrod
"""


numero1 = int(input("Introduce el primer número entero: ")) # Pide primer número a usuario
numero2 = int(input("Introduce el segundo número entero: ")) # Pide segundo número a usuario



if numero1 % numero2 == 0: # Comprobamos si los números se pueden dividir uno entre otro 
    print(numero1, "divide a", numero2)
elif numero2 % numero1 == 0:
    print(numero2, "divide a", numero1)
else:
    print("Ninguno de los dos números divide al otro") # Si no, los números introducidos no son divisibles entre ellos.
