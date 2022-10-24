#Recebe as variáveis
Cod01 = int(input())
ndp01 = int(input())
valuni01 = float(input())

Cod02 = int(input())
ndp02 = int(input())
valuni02 = float(input())

#Calcula o valor total
total = ndp01*valuni01 + ndp02*valuni02

#Imprime o valor 
print(f'VALOR A PAGAR: R$ {total:.2f}')