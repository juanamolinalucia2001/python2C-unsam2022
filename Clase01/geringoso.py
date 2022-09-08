#Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
palabra=input("Ingrese palabra que desea en geringoso: ")
palabraGeringoso=''

for letra in palabra:
    if letra=="a" or letra=="A":
        palabraGeringoso = palabraGeringoso + "apa"

    elif letra=="e" or letra=="E":
        palabraGeringoso = palabraGeringoso + "epe"

    elif letra=="i" or letra=="I":
        palabraGeringoso = palabraGeringoso + "ipi"

    elif letra=="o" or letra=="O":
        palabraGeringoso = palabraGeringoso + "opo"

    elif letra=="u" or letra=="U":
        palabraGeringoso = palabraGeringoso + "upu"

    else:
        palabraGeringoso = palabraGeringoso + letra

print("Palabra en geringoso:", palabraGeringoso)
