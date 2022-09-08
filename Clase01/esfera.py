#ejercicio 1.13 programa que indique al usuarie que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma.
from math import pi, radians
radio =float(input("Ecriba el radio de la esfera que desea saber su volumen "))
volumen= round(4/3*pi*radio**3,2)
print ('El volumen de la esfera es', volumen)