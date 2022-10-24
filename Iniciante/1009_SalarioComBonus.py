#Recebe as entradas
nome = input()
salario = float(input())
montante_total = float(input())

#Calcula o total
total = salario+(0.15*montante_total)

#Imprime o total
print(f'TOTAL = R$ {total:.2f}')