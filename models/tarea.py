from datetime import datetime

class Tarea:
    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def marcar_completada(self):
        self.completada = True
        
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion
        }
        
    @staticmethod
    def from_dict(data):
        tarea = Tarea(data["titulo"], data["descripcion"], data["prioridad"])
        tarea.completada = data["completada"]
        tarea.fecha_creacion = data["fecha_creacion"]
        return tarea
