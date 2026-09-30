def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Salir")
    
def pedir_datos_tarea():
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    return titulo, descripcion, prioridad