from academia_funcoes import * # importando as funções que criamos
import os
import json # importa os aquivos onde vão ser armazenados as informações

while True:

    clientes_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/clientes.json"
    avaliacoes_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/avaliacoes.json"
    exercicios_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/lista_exercicios.json"


    if not os.path.isfile(clientes_json):
        with open(clientes_json, 'w') as arquivo1:
            arquivo1.write('{}')
    with open(clientes_json,"r",encoding="utf8") as arquivo:
        clientes = {}
        cliente = json.load(arquivo)
        clientes = cliente

    if not os.path.isfile(avaliacoes_json):
        with open(avaliacoes_json, 'w') as arquivo2:
            arquivo2.write('{}')
    with open(avaliacoes_json,"r",encoding="utf8") as arquivo:
        avaliacoes = {}
        avaliacao = json.load(arquivo)
        avaliacoes = avaliacao

    if not os.path.isfile(exercicios_json):
        with open(exercicios_json, 'w') as arquivo3:
            arquivo3.write('{}')
    with open(exercicios_json,"r",encoding="utf8") as arquivo:
        lista_exercicios = {}
        lista = json.load(arquivo)
        lista_exercicios = lista

    os.system("cls")
    opcao = menu() # mostra o menu de opções

    if opcao == 1: # função dadastrar é usada

        id_cliente = str(1+int(list(clientes.keys())[-1])) if len(clientes) != 0 else '1'
        id_avaliacao = str(1+int(list(avaliacoes.keys())[-1])) if len(avaliacoes) != 0 else '1'
        id_lista_exercicio = str(1+int(list(lista_exercicios.keys())[-1])) if len(lista_exercicios) != 0 else '1'


        print(cadastrar(clientes, avaliacoes, lista_exercicios, id_cliente, id_avaliacao, id_lista_exercicio, clientes_json, avaliacoes_json, exercicios_json))
        print("\nAperte uma tecla para retornar...")
        input()
    elif opcao == 2: # função editar é usada
        print(editar(clientes, avaliacoes, lista_exercicios, clientes_json, avaliacoes_json, exercicios_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 3: # função excluir é usada
        print(excluir(clientes, avaliacoes, lista_exercicios, clientes_json, avaliacoes_json, exercicios_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 4: # função pesquisar é usada
        print(pesquisar(clientes, avaliacoes, lista_exercicios, clientes_json, avaliacoes_json, exercicios_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 5: # função listar é usada
        print(listar(clientes, avaliacoes, lista_exercicios, clientes_json, avaliacoes_json, exercicios_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 6: # função relatório é usada
        print(relatorio(clientes, avaliacoes, lista_exercicios, clientes_json, avaliacoes_json, exercicios_json))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 0: # opção que encerra o programa
        os.system('cls')
        print(f"\n{'- '*30}")
        print("-"*60) # deixar bunito
        print("\nFim do programa -> sentiremos sua falta :(\n")
        print("-"*60) # deixar bunito
        print(f"{'- '*30}")
        break
    else: # caso for escolhido uma opção errada
        print("Rosponda corretamente: dentre as opções 1 ao 7")