str = input('Name: ')
upper = 0
lower = 0
for letter in str:
    if letter in str.upper():
        upper+=1
    elif letter in str.lower():
        lower+=1
    else:
        pass
print(f'UPPER: {upper}, LOWER: {lower}')