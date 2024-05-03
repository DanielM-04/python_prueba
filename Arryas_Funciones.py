#array=[1,2,3,4,5]
l = ["Camila", "Juan", "Gabirel", "Ana", "Daniel"]
#for i in range (0,4,1):
#    print("number ",i,letras[i])
a = False


def imprimir():
    for i in range(0, 5, 1):
        print(l[i])

def buscar(r):
    for i in range(0, 5, 1):
        if l[i] == r:
            print("Posicion", i)
            a = True
            break
    else:
        print("No se encuentra")

imprimir()
leer = str(input("Ingrese el nombre que quiere buscar-> "))
buscar(leer)


