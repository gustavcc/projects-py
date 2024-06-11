from functools import reduce

def soma(a,b):
    return a+b
lista=[1, 2, 3, 10, 20]
print(reduce(soma, lista))

'''A função reduce() é usada para aplicar 
uma função a uma sequência de elementos
(por exemplo, uma lista) de forma cumulativa,
onde o resultado acumulado é passado para a 
próxima chamada da função.'''

'''Você também pode formatar uma lista de 
strings usando a função reduce():'''

def add_str(a,b):
	return a+' '+b
a = ['Gustavo', 'is', 'a', 'good', 'boy']
print(reduce(add_str, a))