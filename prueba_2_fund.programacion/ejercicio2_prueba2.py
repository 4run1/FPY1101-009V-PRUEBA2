# Ejercicio prueba parcial 2

from random import randint

# Solicitar rango numérico
while True:
    try:
        num1 = int(input("Ingrese límite inferior: "))
        num2 = int(input("Ingrese límite superior: "))

        if num1 < num2:
            numero = randint(num1, num2)
            break
        else:
            print("El límite inferior debe ser menor que el superior.")

    except:
        print("Debe ingresar números enteros.")

# Ajustar número para que sea par
if numero % 2 != 0:

    numero += 1

    if numero > num2:
        numero -= 2

# Intento 1
while True:
    try:
        intento1 = int(input("Intente adivinar: "))

        if num1 <= intento1 <= num2:
            break
        else:
            print(f"El número debe estar entre {num1} y {num2}.")

    except:
        print("Debe ingresar un número entero.")

if intento1 == numero:
    print("Felicitaciones, adivinó en el primer intento.")

else:

    if intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # Intento 2
    while True:
        try:
            intento2 = int(input("Intente de nuevo: "))

            if num1 <= intento2 <= num2:
                break
            else:
                print(f"El número debe estar entre {num1} y {num2}.")

        except:
            print("Debe ingresar un número entero.")

    if intento2 == numero:
        print("Felicitaciones, adivinó en su segundo intento.")

    else:

        if intento2 < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        print("Te daré una pista:")

        distancia1 = abs(numero - intento1)
        distancia2 = abs(numero - intento2)

        if distancia1 < distancia2:
            print(f"El número que buscas está más cerca de {intento1} que de {intento2}")

        else:
            print(f"El número que buscas está más cerca de {intento2} que de {intento1}")

        # Intento 3
        while True:
            try:
                intento3 = int(input("Intente la última vez: "))

                if num1 <= intento3 <= num2:
                    break
                else:
                    print(f"El número debe estar entre {num1} y {num2}.")

            except:
                print("Debe ingresar un número entero.")

        if intento3 == numero:
            print("Felicitaciones, pudiste adivinar.")

        else:
            print("Perdiste.")
            print(f"El número era: {numero}")