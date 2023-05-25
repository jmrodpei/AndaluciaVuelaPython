# -*- coding: utf-8 -*-
"""
Created on Tue May 2 23:21:23 2023

@author: jmrod
"""

numeros = [] # Creamos un array números para contener los números introducidos por el usuario.
contador = 0 # Incializamos un contador a cero

while True:
    
    numero1 = float(input("Introduce un número positivo ó introduce el número 0 para salir): ")) # Pedimos que se introduzca por teclado el/los números.
    
    if numero1 == 0: # Condición que realiza break en caso de que se introduzca el número 0.
        break;
    elif numero1 > 0: # En caso de que el usuario introduzca números negativos, no los tendrá en cuenta.
        numeros.append(numero1)
        contador += 1
        
        if contador == 10: # Condición que limita la cantidad de números introducidos por usuario a 10 números.
            break;
            
if numeros:
    media = sum(numeros) / len(numeros) # Realiza la operación de la media.
    
    print("La media de los números positivos es :", media)
else:
    print("No has introducido números positivos.")
