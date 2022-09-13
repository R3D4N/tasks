import pickle
objVehiculo=0
class Vehiculo:
    ruedas=0
    color=""
    modelo=""

    def __init__(self,ruedas,color,modelo):
        self.ruedas=ruedas
        self.color=color
        self.modelo=modelo

    def getsData(self):
        print("Este vehiculo tiene")
        print(f"{self.ruedas} ruedas")
        print(f"es de color {self.color}")
        print(f"y su modelo es {self.modelo}.")
    
def serializar():
    firstVehiculo=Vehiculo(4,"amarillo","Toyota")
    stream=open("data.bin","wb")
    pickle.dump(firstVehiculo,stream)
    stream.close()

def deserializar():
    global objVehiculo
    stream=open("data.bin","rb")
    objVehiculo=pickle.load(stream)
    stream.close()

deserializar()
print(objVehiculo.getsData())

