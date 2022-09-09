import operaciones

def main():
    num1=8
    num2=16
    print("numeros:",num1,num2)
    print("suma:",operaciones.sumar(num1,num2))
    print("resta:",operaciones.restar(num1,num2))
    print("division:",operaciones.dividir(num1,num2))
    print("multiplicacion:",operaciones.multiplicar(num1,num2))



if __name__=="__main__":
    main()
