import json

archivo_datos = "datos_estudiantes.json"

def cargar_datos():
    try:
        with open(archivo_datos, "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {}
    return datos

def guardar_datos(datos):
    with open(archivo_datos, "w") as file:
        json.dump(datos, file)

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    matematicas = float(input("Ingrese la nota de matemáticas: "))
    ciencias = float(input("Ingrese la nota de ciencias: "))
    historia = float(input("Ingrese la nota de historia: "))
    promedio = (matematicas + ciencias + historia) / 3

    estudiante = {
        'nombre': nombre,
        'apellido': apellido,
        'notas': {
            'matematicas': matematicas,
            'ciencias': ciencias,
            'historia': historia,
        },
        'promedio': promedio
    }

    return estudiante

def buscar_estudiantes(nombre_buscar, datos):
    encontrados = []
    for estudiante in datos.values():
        if estudiante['nombre'].lower() == nombre_buscar.lower():
            encontrados.append(estudiante)
    return encontrados

def mostrar_estudiantes(datos):
    if not datos:
        print("No hay estudiantes registrados")
    else:
        print("\nListado de estudiantes:")
        for estudiante in datos.values():
            print(f"{estudiante['nombre']} {estudiante['apellido']}")
            print(f"Notas: Matemáticas: {estudiante['notas']['matematicas']}, Ciencias: {estudiante['notas']['ciencias']}, Historia: {estudiante['notas']['historia']}")
            print(f"Promedio: {estudiante['promedio']:.2f}\n")

def main():
    print("Bienvenido al sistema de registro de estudiantes")

    datos = cargar_datos()

    while True:
        print("\n1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Mostrar estudiantes")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            estudiante = registrar_estudiante()
            datos[f"{estudiante['nombre']} {estudiante['apellido']}"] = estudiante
            guardar_datos(datos)
            print(f"Estudiante {estudiante['nombre']} registrado con éxito")

        elif opcion == "2":
            nombre_buscar = input("Ingrese el nombre del estudiante: ")
            encontrados = buscar_estudiantes(nombre_buscar, datos)
            if encontrados:
                print(f"Se encontraron estudiantes con el nombre '{nombre_buscar}':")
                for estudiante in encontrados:
                    print(f"{estudiante['nombre']} {estudiante['apellido']}")
                    print(f"Notas: Matemáticas: {estudiante['notas']['matematicas']}, Ciencias: {estudiante['notas']['ciencias']}, Historia: {estudiante['notas']['historia']}")
                    print(f"Promedio: {estudiante['promedio']:.2f}\n")
            else:
                print(f"No se encontraron estudiantes con el nombre '{nombre_buscar}'")

        elif opcion == "3":
            mostrar_estudiantes(datos)

        elif opcion == "4":
            print("¡Adiós!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

    print("Gracias por utilizar el sistema.")

if __name__ == "__main__":
    main()
