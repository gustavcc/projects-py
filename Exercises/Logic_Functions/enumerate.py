'''A função enumerate() retorna o comprimento de 
um objeto iterável enquanto itera sobre seus 
itens. Portanto, ao imprimir cada item no tipo
de dados iterável, ele gera simultaneamente seu
índice.'''

'''start= permite decidir por onde a lista irá começar'''

fruits = ['grape', 'apple', 'manga']
for indice, value in enumerate(fruits, start=1):
    print(indice,'->',value, end='\n')


'''como seria'''

print('-'*30)

for i in range(len(fruits)):
    print(i,'->',fruits[i])