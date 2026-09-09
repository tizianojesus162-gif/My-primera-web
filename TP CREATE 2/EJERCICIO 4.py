# Creamos una lista vacía para guardar los alumnos
alumnos = []

while True:
    # Pedimos el DNI
    dni = input("Ingrese el DNI del alumno (o escriba SALIR): ")

    # Comprobamos si el usuario quiere terminar
    if dni.upper() == "SALIR":
        break

    dni = int(dni)

    # Buscamos si el DNI ya existe
    duplicado = False

    for alumno in alumnos:
        if alumno["dni"] == dni:
            duplicado = True
            break

    # Si el DNI ya existe, rechazamos el registro
    if duplicado:
        print("Error: ese DNI ya está registrado.")
        continue

    # Pedimos el resto de los datos
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))

    # Creamos el nuevo alumno
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad
    }

    # Guardamos el alumno
    alumnos.append(alumno)

    print("Alumno registrado correctamente.")

# Mostramos todos los alumnos
print("\nAlumnos registrados:")
print(alumnos)