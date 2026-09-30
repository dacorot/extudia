from services.gestor import GestorTareas
from utils.helpers import mostrar_menu, pedir_datos_tarea

def main():
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo, descripcion, prioridad = pedir_datos_tarea()
            gestor.agregar_tarea(titulo, descripcion, prioridad)
            print("Tarea agregada correctamente.")
            
        elif opcion == "2":
            gestor.listar_tareas()
            
        elif opcion == "3":
            gestor.listar_tareas()
            try:
                indice = int(input("Numero de tarea a completar: ")) - 1
                gestor.completar_tarea(indice)
                print("Tarea completada.")
            except ValueError:
                print("Debe ingresar un número válido.")
                
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida.")
            
if __name__ == "__main__":
    main()