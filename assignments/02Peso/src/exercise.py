def main():
    #escribe tu código abajo de esta línea
    actual = float(input("Dame el peso inicial: "))
    final = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    resultado = (actual - final) / meses
    print("Lo que debes bajar por mes es: " + str(resultado))



if __name__ == '__main__':
    main()
