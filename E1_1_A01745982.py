import numpy as np

#Identificacion de numeros primo
def id_primo(n):
    for i in range(2,n):
        if(n%i)==0:
            return False
    return True

#Generacion de lista de n numeros primos
def list_primo(n):
    list=[]
    c=2
    while len(list)<n:
        if id_primo(c):
            list.append(c)
        c+=1
    return list

#Generacion de Matriz y suma de elementos en diagonal superior
sum=0
m=int(input("Introducir dimensión 𝑚 de una matriz [𝑚 >= 3]: "))
if m<3: 
    print("La dimensión 𝑚 debe ser mayor o igual a 3")
else:
    ar=np.array(list_primo(m**2)).reshape(m,m)
    print("\nMatriz", m, "x", m, "de números primos:\n")
    for row in range(m):
        line=''
        for col in range(m):
            st=str(ar[row][col])
            if col>=row:
                sum+=ar[row][col]
            line+=(str(ar[row][col])+' '*(len(max(st))*4-len(st)))
        print(line)
    print("\nSuma de todos los elementos en y por encima de la diagonal principal: ",sum,"\n")