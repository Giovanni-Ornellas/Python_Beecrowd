A, B, C = input().split() #Recebe inputs e splita as entradas com " "
A, B, C = int(A),int(B),int(C) #Modifica de string para int 

Maior = (A+B+abs(A-B))//2 # / gera uma divisão float e // gera uma divisão truncada

Maior = (C+Maior+abs(C-Maior))//2


print(f'{Maior} eh o maior')