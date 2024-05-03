array=[1,2,3,4,5]
#letras=["Nancy", "Juan","Luis","Miguel"]
#for i in range (0,4,1):
#    print("number ",i,letras[i])
a=False
def imprimir():
    for i in range (0,5,1):
        print(array[i])
    
def buscar(r):
    for i in range(0,5,1):
        if(array[i]==r):
            print("Posicion",i)
            a=True
            break
    else:
        print("No se encuentra")
            
imprimir()    
leer=int(input("Ingrese el numero que quiere buscar-> "))
buscar(leer)

