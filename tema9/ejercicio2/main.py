from functools import reduce

def main():
    lista=[1,2,3,4,5,6,7,8,9]
    listaImpar=list(filter(lambda x:x%2!=0,lista))
    sumaImpar=reduce(lambda a,b:a+b,listaImpar)
    print("La suma de ",listaImpar," es ",sumaImpar)


if __name__=="__main__":
    main()