from math import pi

def triangulo(altura,base):
    return altura*base/2

def circulo(radio):
    return (radio**2)*pi

print("el area del triangulo es",triangulo(8,6))
print("el area del circulo es",circulo(10))