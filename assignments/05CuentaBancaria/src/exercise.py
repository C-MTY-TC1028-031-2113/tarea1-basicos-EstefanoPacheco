def main():
    #escribe tu código abajo de esta línea
    anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    cheques = float(cheques * 13)
    cons = egresos + cheques
    pros = anterior + ingresos 
    resultado = pros - cons
    final = float(resultado - (resultado*0.075))
    final = round(final, 5)
    print("El saldo final de la cuenta es: " + str(final))



if __name__ == '__main__':
    main()
