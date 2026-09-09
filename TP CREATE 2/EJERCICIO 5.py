# Ejercicio 5: Módulo Create Definitivo

def registrar_nuevo_alumno():
    # Pedimos los datos básicos
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    try:
        # Pedimos los datos numéricos
        dni = int(input("Ingrese el DNI: "))
        edad = int(input("Ingrese la edad: "))

        # Creamos el diccionario
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "edad": edad
        }

        # Abrimos el archivo para agregar el nuevo alumno
        with open("alumnos.txt", "a") as archivo:
            archivo.write(str(alumno) + "\n")

        print("Alumno registrado correctamente.")

    except ValueError:
        # Se ejecuta si se ingresan letras en DNI o edad
        print("Error: el DNI y la edad deben ser números.")


# Llamamos a la función
registrar_nuevo_alumno()