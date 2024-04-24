import re #biblioteca regex

while True:
    dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    dia_semana = input(f"\nInsira o dia da semana (Segunda - Sábado)\nEx: Terça\n:").capitalize().strip()
    semana_separado=re.split("[ -]", dia_semana)
    print(semana_separado)
    correct = False
    if (semana_separado[0] in dia) or ((semana_separado[0] in dia) and (semana_separado[1] == 'feira')):
        correct = True
    if correct:
        print(correct)
        break
    else:
        print("incorreto")
