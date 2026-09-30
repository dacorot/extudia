import json
import os
from models.tarea import Tarea

RUTA_ARCHIVO = "data/tareas.json"

class GestorTareas:
  def __init__(self):
    self.tareas = []
    self.cargar_tareas()
    
  def agregar_tarea(self, titulo, descripcion, prioridad):
    tarea = Tarea(titulo, descripcion, prioridad)
    self.tareas.append(tarea)
    self.guardar_tareas()
    
  def listar_tareas(self):
    if not self.tareas:
        print("No hay tareas registradas. ")
        return
    
    for i, tarea in enumerate(self.tareas, 1):
        estado = "✔" if tarea.completada else "✘"
        print(f"{i}. [{estado}] {tarea.titulo} - Prioridad: {tarea.prioridad}")
        
  def completar_tarea(self, indice):
    if 0 <= indice < len(self.tareas):
        self.tareas[indice].marcar_completada()
        self.guardar_tareas()
    else:
        print("indice inválido")
        
  def guardar_tareas(self):
    os.makedirs("data", exist_ok=True)
    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump([t.to_dict() for t in self.tareas], archivo, indent=4)
        
  def cargar_tareas(self):
    if os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "r") as archivo:
            datos = json.load(archivo)
            self.tareas = [Tarea.from_dict(d) for d in datos]