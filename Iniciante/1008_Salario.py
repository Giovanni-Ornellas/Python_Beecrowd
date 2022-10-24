#Recebe as variáveis
num_do_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

#Calcula salário
salary = horas_trabalhadas*valor_por_hora

#Imprime o número do funcionário e o salário
print(f'NUMBER = {num_do_funcionario}')
print(f'SALARY = U$ {salary:.2f}')