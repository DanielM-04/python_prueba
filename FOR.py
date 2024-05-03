#codigo que genere la tabla de multiplicar de un numero

print("Taller 21 de febrero")

a= int(input("Escriba un Numero -> "))
for c in range(1,11):
    b=a*c
    print(a,"X",c,"=",b)


#******************
for a in range(1,11):
    print("    Tabla del ",a)
    for b in range(1,11):
        c=a*b
        print(a,"x",b,"=",c)


#******

i=1
for a in range(1,6):
    i=a*i
    print (a,"",i)

