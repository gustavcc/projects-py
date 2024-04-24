import json
from funcoes import *
import os

while True:

    agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Python_Projects™/Agenda/agenda.json'

    if not os.path.isfile(agenda_json):
        # Se o arquivo não existe, crie-o
        with open(agenda_json, 'w') as arquivo:
            arquivo.write('{}')
            
    with open(agenda_json,"r",encoding="utf8") as arquivo:
        agenda = {}
        arquivo_json = json.load(arquivo)
        agenda = arquivo_json

    os.system("cls")
    opcao = menu()
    os.system("cls")
    if opcao == '1':
        
        id_contato = str(1+int(list(agenda.keys())[-1])) if len(agenda) != 0 else '1'

        cadastro(agenda, id_contato, agenda_json)
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '2':
        editar(agenda,agenda_json)
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '3':
        print(excluir(agenda,agenda_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '4':
        pesquisar(agenda)
        print("Aperte uma tecla para retornar...")
        input()
        
    elif opcao == '5':
        ordem_adcionado(agenda)
        print("Aperte uma tecla para retornar...")
        input()
        
    elif opcao == '6':
        ordem_abc(agenda)
        print("Aperte uma tecla para retornar...")
        input()
        
    elif opcao == '0':
        print(f'{"-"*60}\n{"- "*30}')
        print("\n\nFim do programa!\n\n")
        print(f'{"- "*30}\n{"-"*60}')
        break
    else:
        print("\nResponda de acordo com as opções: 1 ao 6, ou 0\n")
        continue