number=int(input("digite un numero: "))
def isPrime(number):
    if number ==1:
        return False

    if number==2:
        return True
    
    for i in range(3,int(number/2)+1):
        if number%i==0:
            return False
    else:
        return True

if isPrime(number):
    print("es primo")
else:
    print("no es primo")