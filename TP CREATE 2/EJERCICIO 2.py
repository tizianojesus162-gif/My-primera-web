# Creamos una lista vacía para guardar los alumnos
alumnos = []

# Preguntamos cuántos alumnos se quieren registrar
cantidad = int(input("¿Cuántos alumnos desea registrar? "))

# Repetimos el proceso según la cantidad indicada
for i in range(cantidad):
    print("\nAlumno", i + 1)

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el DNI: "))
    promedio = float(input("Ingrese el promedio: "))

    # Creamos el diccionario
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "promedio": promedio
    }

    # Agregamos el alumno a la lista
    alumnos.append(alumno)

# Mostramos todos los alumnos
print("\nLista completa de alumnos:")
print(alumnos)