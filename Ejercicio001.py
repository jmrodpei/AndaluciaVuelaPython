# -*- coding: utf-8 -*-
"""
Created on Tue May 2 17:08:11 2023

@author: jmrod
"""

numero1 = int(input("Introduce el primer número: ")) # Pide primer número a usuario
numero2 = int(input("Introduce el segundo número: ")) # Pide segundo número a usuario
numero3 = int(input("Introduce el tercer número: ")) # Pide tercer número a usuario



if numero1 >= numero2 and numero1 >= numero3: # Utilizamos bucles para comparar los números introducidos y hallar el número máximo.
    max_num = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    max_num = numero2
else:
    max_num = numero3

if numero1 <= numero2 and numero1 <= numero3: # Utilizamos bucles para comparar los números introducidos y hallar el número mínimo.
    min_num = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    min_num = numero2
else:
    min_num = numero3


print("El número máximo es:", max_num) # Muestra por pantalla el número máximo
print("El número mínimo es:", min_num) # Muestra por pantalla el número mínimo
