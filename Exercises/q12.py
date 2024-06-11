numbers = []

for number in range(1000,3001):
    n = str(number)
    if (int(n[0]) % 2==0) and (int(n[1]) % 2==0) and (int(n[2]) % 2==0) and (int(n[3]) % 2==0):
        numbers.append(n)
print(','.join(numbers))