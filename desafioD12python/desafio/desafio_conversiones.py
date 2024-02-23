import sys

#crear las funciones que serán llamadas a hacer las conversiones
def convertir_sol(peso_chileno, tasa_sol):
    return peso_chileno * tasa_sol
def convertir_peso(peso_chileno, tasa_peso):
    return peso_chileno * tasa_peso
def convertir_dolar(peso_chileno, tasa_dolar):
    return peso_chileno * tasa_dolar

#verifica la cantidad de argumentos
def main():
    if len(sys.argv) != 5:
        print("Ingresar tasas de conversión y monto de peso chileno (clp) a convertir.")
        exit(1)

#datos float que seran ingreados por consola
    try:
        tasa_sol = float(sys.argv[1])
        tasa_peso = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_peso_chileno = float(sys.argv[4])
    except ValueError:
        print("Por favor, ingrese tasas de conversión y el valor en peso chileno válido.")
        exit(1)

#calculo de la conversion e impresion de los valores
    valor_sol = convertir_sol(valor_peso_chileno, tasa_sol)
    valor_peso = convertir_peso(valor_peso_chileno, tasa_peso)
    valor_dolar = convertir_dolar(valor_peso_chileno, tasa_dolar)

    print(f"Valor en soles peruanos: {valor_sol}")
    print(f"Valor en pesos argentinos: {valor_peso}")
    print(f"Valor en dólares norteamericanos: {valor_dolar}")

#se ejecuta solo como principal
if __name__ == "__main__":
    main()