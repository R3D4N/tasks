class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def mostrarDatos(self):
        print("Los datos de este coche son: ")
        print(self.color,self.ruedas,self.puertas,self.velocidad,self.cilindrada)

auto=Coche("azul",4,2,100,30)
auto.mostrarDatos()