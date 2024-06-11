number = int(input('Numero\n:'))
fatorial = 1

print(f'{number}! = ',end='')
for i in range(number,0,-1):
    if i == 1:
        print(i,'= ',end='')
    else:
        print(i,' x ',end='')
    fatorial *= i
print(fatorial)