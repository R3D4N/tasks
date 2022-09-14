def main():
    countries=input("Paises separados por coma: ")
    lstCountries=set(countries.split(","))
    # borra los espacios innecesario de cada elemento
    lastList=list(map(noEspacio,lstCountries))
    lastList.sort()
    for item in lastList:
        print(item,end=", ")

def noEspacio(item="a"):
    return item.lstrip()

if __name__=="__main__":
    main()
