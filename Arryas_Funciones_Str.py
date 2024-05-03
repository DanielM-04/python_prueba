#array=[1,2,3,4,5]

#for i in range (0,4,1):
#    print("number ",i,letras[i])
a=False
l=["Nancy", "Juan","Luis","Miguel","Kaka"] 
def imprimir():
    for i in range (0,5,1):
        print(l[i])
    
def buscar(r):
    global a
    for i in range(0,5,1):
        if(l[i]==r):
            print("Posicion",i)
            a=True
            break
    else:
        print("No se encuentra")
            
imprimir()    
leer=str(input("Ingrese el numero que quiere buscar-> "))
buscar(leer)

