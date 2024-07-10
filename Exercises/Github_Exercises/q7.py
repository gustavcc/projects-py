numbers = [n for n in input('Number: ').split(',')]
print(numbers)
X = int(numbers[0])
Y = int(numbers[1])
print(X,Y)

matriz = [[0 for col in range(Y)] for row in range(X)]



for row in range(X):
    for col in range(Y):
        matriz[row][col] = row*col
print(matriz)