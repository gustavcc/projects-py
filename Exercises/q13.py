frase = input('frase: ')
letters = 0
digits = 0

for letra in frase:
    if letra.isdigit():
        digits+=1
    elif 'a' <= letra.lower() <= 'z':
        letters+=1
    else:
        pass
print(f'LETTERS: {letters}\nDIGITS: {digits}')