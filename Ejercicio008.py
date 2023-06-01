# -*- coding: utf-8 -*-
"""
Created on Wed May 3 15:42:25 2023

@author: jmrod
"""

def calculo(entrada1, entrada2, entrada3):
  
    media = (entrada1 + entrada2 + entrada3) / 3   # Calculamos la media de los valores de entrada
    varianza = ((entrada1 - media)**2 + (entrada2 - media)**2 + (entrada3 - media)**2) / 3  # Calculamos la varianza de los valores de entrada
    
    return media, varianza # Se devuelve mediante return los valores obtenidos.

# Definimos tres valores de entrada

entrada1 = 10
entrada2 = 15
entrada3 = 20

media, varianza = calculo(entrada1, entrada2, entrada3)

print(f"el valor de las entradas es; {entrada1}, {entrada2} y {entrada3}")  # Mostramos el valor de las entradas.

print(f"La media de las entradas es: {media}") #Mostramos el valor de la media

print(f"La varianza de las entradas es: {varianza}")  #Mostrados el valor de la varianza
