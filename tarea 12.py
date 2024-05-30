N=[]
with open('D:\\Python\\p.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(linea.strip())
#Tarea separar por espacios, leer numero por numero.
#Para ello se utiliza split
with open('D:\\Python\\p.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        numeros = linea.strip().split()
        for numero in numeros:
            print(numero)
            N.append(numero)
    

if N:
    first_number = N[0]
    print(f"{first_number}, primer numero")
else:
    print("La línea está vacía o no contiene números")