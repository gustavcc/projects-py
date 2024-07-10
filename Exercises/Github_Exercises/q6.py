import math
sequence = []
H = 30
C = 50
values = [x for x in input('numbers: ').split(',')]

for D in values:
    Q = round(math.sqrt((2*C*float(D)/H)))  
    sequence.append(str(Q))
print(','.join(sequence))