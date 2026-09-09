
# Pedimos los datos del alumno
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el DNI: "))
edad = int(input("Ingrese la edad: "))

# Verificamos si la edad es válida
if edad >= 17 and edad <= 99:
    # Creamos el diccionario
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad
    }

    print("Alumno creado correctamente:")
    print(alumno)

else:
    # Si la edad no es válida, descartamos el registro
    print("Error: la edad debe estar entre 17 y 99 años.")