import random

print(random.random()) 
# aleatorio entre 0 e 1
print('-'*30)
print(random.randint(1,10)) 
# aleatorio inteiro entre os numeros ditos
print('-'*30)
print(random.uniform(1,10)) 
# aleatorio decimal entre os numeros ditos 
print('-'*30)
list = ['azul', 'vermelho', 'amarelo']
print(random.choice(list)) 
# escolhe uma opcao dentro de uma fonte
print('-'*30)
cartas = ['catrat1', 'carta2', 'carta3']
random.shuffle(cartas)
# embaralha as opcoes de uma lista
print(cartas)