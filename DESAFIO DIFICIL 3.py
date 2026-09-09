alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o escriba 'salir'): ")

    if nombre.lower() == "salir":
        break

    alumno = {"nombre": nombre}
    alumnos.append(alumno)

print("Cantidad de alumnos creados:", len(alumnos))
print("Alumnos:", alumnos)