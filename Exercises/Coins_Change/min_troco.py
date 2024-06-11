# a menor quantidade de moedas possiveis para um troco

def dp_change(money, coins):
    # [0,1,2,3,4,5,6,7,8,9]
    # [1,0,0,0,0,0,0,0,0,0] chegar com 0 moedas
    # [0,1,0,0,0,0,0,0,0,0] chegar com 1 moedas
    # [0,0,1,0,0,0,0,0,0,0] chegar com 2 moedas
    
    possibles = [0] * (money + 1)
    possibles[0] = 1
    for i in range(money):
        new_possibles = [0] * (money + 1)
        for j in range(len(possibles)):
            if possibles[j]:
                for coin in coins:
                    if j+coin == money:
                        return f'Numero minimo de moedas: {i + 1}'
                    if j+coin < money:
                        new_possibles[j+coin] = 1
        possibles = new_possibles
coins = [1,5,10,25,50]
print(dp_change(2, coins))