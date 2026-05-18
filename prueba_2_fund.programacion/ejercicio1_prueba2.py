# Ejercicio prueba parcial 1

# Solicitar edad del cliente
while True:
    try:
        edad = int(input("Ingrese su edad: "))

        if edad <= 0:
            print("La edad debe ser mayor que 0.")
        else:
            break

    except:
        print("Error: debe ingresar un número entero.")

# Solicitar tramo del cliente
while True:
    tramo = input("Ingrese el tramo a recorrer (A, B, C o D): ").upper()

    if tramo in ("A", "B", "C", "D"):
        break
    else:
        print("Tramo inválido. Debe ingresar A, B, C o D.")

# Valores fijos
valor_mensual_medicamento = 60000
valor_despacho_domicilio = 8000

# Variables
descuento = 0
descuento_despacho = 0

# Evaluar descuento según edad y tramo
if edad <= 30 and tramo in ("A", "B"):
    descuento = 0.18

elif edad <= 30 and tramo in ("C", "D"):
    descuento = 0.12

elif 31 <= edad <= 60 and tramo in ("A", "B"):
    descuento = 0.12

elif 31 <= edad <= 60 and tramo in ("C", "D"):
    descuento = 0.08

# Evaluar descuento para despacho
if tramo in ("A", "B"):

    if edad >= 55:
        descuento_despacho = 0.15
    else:
        descuento_despacho = 0.10

# Cálculos finales
valor_final_medicamento = int(
    valor_mensual_medicamento -
    (valor_mensual_medicamento * descuento)
)

valor_final_despacho = int(
    valor_despacho_domicilio -
    (valor_despacho_domicilio * descuento_despacho)
)

total = valor_final_medicamento + valor_final_despacho

# Mostrar resultados
print("\n------ RESUMEN DE COMPRA ------")
print(f"Valor medicamento: ${valor_final_medicamento}")
print(f"Valor despacho: ${valor_final_despacho}")
print(f"Total a pagar: ${total}")