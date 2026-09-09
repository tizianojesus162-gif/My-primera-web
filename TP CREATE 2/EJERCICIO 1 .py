# Pedimos los datos del alumno
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el DNI: "))
promedio = float(input("Ingrese el promedio: "))

# Creamos el diccionario con los datos
alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "dni": dni,
    "promedio": promedio
}

# Mostramos el diccionario
print("Datos del alumno:")
print(alumno)