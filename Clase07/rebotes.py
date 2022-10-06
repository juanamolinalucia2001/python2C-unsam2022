#Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.
cantidadRebotes=0
altura=100
while cantidadRebotes<10:
    altura=altura*(3/5)
    print(cantidadRebotes,altura)
    cantidadRebotes+=1   