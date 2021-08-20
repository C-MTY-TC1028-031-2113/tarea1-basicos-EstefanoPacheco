def main():
    #escribe tu código abajo de esta línea
    mat1 = float(input("Ingresa la calificación de la primera materia: "))
    mat2 = float(input("Ingresa la calificación de la sgunda materia: "))
    mat3 = float(input("Ingresa la calificación de la tercera materia: "))
    mat4 = float(input("Ingresa la calificación de la cuarta materia: "))
    promedio = (mat1 + mat2 + mat3 + mat4)/4
    print("El promedio de tus calificaciones es: " + str(promedio))


if __name__ == '__main__':
    main()
