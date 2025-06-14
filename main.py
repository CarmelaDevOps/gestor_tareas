# main.py
from datetime import datetime
import os

TAREAS_PATH = "tareas.txt"
LOG_PATH = "logs/log.txt"

def guardar_log(texto):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as archivo:
        archivo.write(f"{datetime.now()} - {texto}\n")

def cargar_tareas():
    if not os.path.exists(TAREAS_PATH):
        return []
    with open(TAREAS_PATH, "r") as f:
        return [linea.strip() for linea in f.readlines()]

def guardar_tareas(tareas):
    with open(TAREAS_PATH, "w") as f:
        for tarea in tareas:
            f.write(tarea + "\n")

def mostrar_menu():
    print("\n1. Ver tareas\n2. Agregar tarea\n3. Eliminar tarea\n4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tareas = cargar_tareas()
            print("\nTareas actuales:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            guardar_log("Consultó las tareas")
        elif opcion == "2":
            nueva = input("Escribe la nueva tarea: ")
            tareas = cargar_tareas()
            tareas.append(nueva)
            guardar_tareas(tareas)
            guardar_log(f"Agregó tarea: {nueva}")
        elif opcion == "3":
            tareas = cargar_tareas()
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            num = input("Número de tarea a eliminar: ")
            if num.isdigit() and 1 <= int(num) <= len(tareas):
                eliminada = tareas.pop(int(num)-1)
                guardar_tareas(tareas)
                guardar_log(f"Eliminó tarea: {eliminada}")
            else:
                print("Número inválido.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

