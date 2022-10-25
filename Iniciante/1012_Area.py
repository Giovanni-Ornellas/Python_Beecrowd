#Recebe o valor de A, B e C
A, B, C = input().split() #Pega um input e separa as entradas (geralmente com " ")
A, B, C = float(A),float(B),float(C) #Modifica de string para float

pi = 3.14159

area_do_triagulo_retangulo = (A*C)/2
area_do_circulo = pow(C,2)*pi
area_do_trapezio = ((A+B)*C)/2
area_do_quadrado = pow(B,2)
area_do_retangulo = A*B

print(f'TRIANGULO: {area_do_triagulo_retangulo:.3f}')
print(f'CIRCULO: {area_do_circulo:.3f}')
print(f'TRAPEZIO: {area_do_trapezio:.3f}')
print(f'QUADRADO: {area_do_quadrado:.3f}')
print(f'RETANGULO: {area_do_retangulo:.3f}')