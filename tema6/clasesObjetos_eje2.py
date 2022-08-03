class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def mostrarNota(self):
        result=f"Alumno {self.nombre}, tiene la nota {self.nota} y "
        if self.nota<=10:
            result+="desaprobo"
        else:
            result+="aprobo"
        print(result)

estudiante=Alumno("angelo",11)
estudiante.mostrarNota()