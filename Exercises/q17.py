transaction = [x for x in input(':').split(' ')]
deposito, saque = 0, 0
for i in range(len(transaction)):
    if transaction[i]=='D':
        deposito+=int(transaction[i+1]) 
    elif transaction[i]=='W':
        saque+=int(transaction[i+1]) 
print(f'Deposito: {deposito}, Saque: {saque}, Valor liquido: {deposito-saque}')