import json

ARCHIVO_JSON = "estudiantes.json"

#WE LOAD THE JSON FILE AND RETURN THE LIST OF STUDENTS
def cargarDatos():
    try:
        archivo = open(ARCHIVO_JSON, "r", encoding = "utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos ["estudiantes."]
    except: FileNotFoundError
    print("Archivo json no rencontrado.")
    return[]


#WE SAVE THE LIST OF RETURNING STUDENTS IN A JSON FILE
def Guardardatos_estudiantes(estudiantes):
    try:
        archivo = open(ARCHIVO_JSON, "w", encoding = "utf-8")
        json.dump({"estudiantes": estudiantes}, archivo, ensure_ascci=False, indent=4)
        archivo.close()
        print("cambios guardados en el archivo json.")
    except:
        print("error a el guardar archivo json")
    
#WE ONLY REQUEST AND VALIDATE NUMBERS
def pedirNumero(mensaje):
    ejecutando = False
    while not ejecutando:
        try:

            opcion =  input(mensaje).strip()

            if len(opcion) == 0:
                print("este apartado no pyuede estar vacio.")
            if opcion.isalpha():
                print("este apartado no puede contener letras.")
            else:
                ejecutando = True
        except:
            print("Error grave.")
    return opcion

#WE DISPLAY ALL STUDENTS BY GOING THROUGH THE LIST WITH FOR
def mostrarInformacion(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes por mostrar")
    else:
        print("===== Lista De Estudiantes =====")
        for estudiante in estudiantes:
            print(f"ID: {estudiante ['id']} {estudiante ['nombre']} {estudiante ['apellido']} Edad: {estudiante['[edad]']} Ingles: {estudiante['nvlIgles']}")

#WE ARE LOOKING FOR A STUDENT BY THEIR ID
def buscarEstudiantes(estudiantes):
    id_buscar = int(pedirNumero("Ingresa el id que quieras buscar: "))
    encontrado = False
    for estudiantes in estudiantes:
        if estudiantes["id"] == id_buscar:
            print(f"nombre: {estudiantes ['nombre']} apellido: {estudiantes ['apellido']}")
            print(f"edad: {estudiantes ['edad']}")
            print(f"ingles: {estudiantes ['nvlIngles']}")
            encontrado = True
            print("estudiante no encontrado")
        if not encontrado:
            print("estudiante no encontrado")


#We add a new student to the list and save it with the JSON file.
def añadirEstudiante(estudiantes):
    id_nuevo = int(input("Ingrese el id de el estudiante que quiere agregar: "))
    nombre = input("Ingrese el nombre de el estudiante que quiere agregar: ").strip()
    apellido = input("Ingrese el apellido de el estudiante que quiere agregar: ").strip()
    edad = int(input("ingrese el apellido de el estudiante que quiere agregar: "))
    ingles = input("Cual sera su nivel de ingles: ").strip()

    estudiante_nuevo = {
    "id": id_nuevo,
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "nvIngles": ingles
}
    estudiantes.append(estudiante_nuevo)
    Guardardatos_estudiantes(estudiantes)
    print(f"estudiante: '{nombre}' añadido correctamente")


#We delete a student by their ID and save it with the JSON
def eliminarEstudiante(estudiantes):
    id_eliminar = int(input("ingrese el id de la persona que quiere eliminar"))
    encontrado = False
    for estudiante in estudiantes:
        if estudiante["id"] == id_eliminar:
            estudiantes.remove(estudiante)
            Guardardatos_estudiantes(estudiantes)
            print("estudiante eliminado correctamente")
            encontrado = True
            return
        if not encontrado:
            print("estudiante no encontrado")


#We modified a student's data using their ID and saved it in a JSON file.
def modificareEtudiantes(estudiantes):
    id_modificar = int(input("Elegir el id que se quiere modificar."))
    for estudiante in estudiantes:
        if estudiante ['id'] == id_modificar:
            print("dejar en blanco si no quieres modificar a el usuario: ")
            nuevoNombre = input(f"ingrese el nuevo nombre a mofidicar: ({estudiantes ['nombre']}): ")
            nuevaEdad = input(f"ingrese la nueva edad ha modificar: ({estudiantes ['edad']}): ")
            nuevoIngles = input(f"Nuevo ingles ha modificar: ({estudiantes ['nvlIngles']}): ")

            if nuevoNombre != "":
                estudiante ["nombre"] = nuevoNombre
            if nuevaEdad != "":
                estudiante ["edad"] = nuevaEdad
            if nuevoIngles != "":
                estudiante ["nvlIngles"]
                Guardardatos_estudiantes(estudiantes)
                print("Tu estudiante ha sido modificado.")
                return
            print("estudiante no encontrado")


def main():
    estudiantes = cargarDatos()

    ejecutando = True
    while ejecutando:
        print("===== REGISTRO DE ESTUDIANTES =====")
        print("1. MOSTRAR TODO")
        print("2. BUSCAR ESTUDIATE")
        print("3. AÑADIR ESTUDIANTE")
        print("4. ELIMINAR ESTUDIANTE")
        print("5. MODIFICAR ESTUDIANTE")
        print("0. SALIR")

        opcion = pedirNumero("elige un numero de el menu: ")

        if opcion == "1":
            mostrarInformacion(estudiantes)
        elif opcion == "2":
            buscarEstudiantes(estudiantes)
        elif opcion == "3":
            añadirEstudiante(estudiantes)
        elif opcion == "4":
            eliminarEstudiante(estudiantes)
        elif opcion == "5":
            modificareEtudiantes(estudiantes)
        elif opcion == "0":
            print("Hasta luego!")
            ejecutando = False
        else:
            print("opcion no valida")

main()