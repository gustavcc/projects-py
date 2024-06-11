from math import sqrt


'''Você pode usar round() para arredondar o 
resultado de uma operação matemática para 
um número específico de dígitos significativos:'''

calc = sqrt(2)
rounded = round(calc,2)
print(rounded)

'''ou'''

print(f'{calc:.2f}')