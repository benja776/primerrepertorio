def sumar(a,b):
    return a+b

while True:
    try:
        n1 = int(input("ingrese valor: "))
        n2 = int(input("ingrese segundo valor: "))
        break
    except:
        print("ingrese valores enteros: ")

print(sumar(n1,n2))