# a menor quantidade de moedas possiveis para um troco with conda

def minTroco(troco):
    moedas_troco = [1,5,10,25,50]
    troco_list = []
    num_moedas = 0
    i = 4
    
    while i >= 0:
        if sum(troco_list) == troco:
            break
        while troco - moedas_troco[i] >= 0 :
            troco = troco - moedas_troco[i]
            troco_list.append(moedas_troco[i])
            num_moedas+=1        
        i-=1
    print(f"Number of coins: {num_moedas}\nList of change: {troco_list}")

minTroco(91)