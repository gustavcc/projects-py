import json
import os
from colorama import Fore
from time import sleep


def contem_letras(valor):
    for caractere in valor:
        if "a" <= caractere <= "z" or "A" <= caractere <= "Z":
            return True
    return False


def menu():
    print(f"\n{'- '*30}")
    print(f'{"-"*60}\n{" AGENDA ":^60}\n{"-"*60}')
    print(
        """
1 - Cadastrar contato.
2 - Editar um contato.
3 - Excluir um contato.
4 - Pesquisar contato.
5 - Classificar por ordem de contatos cadastrados.
6 - Classificar contatos ordenados pelos nomes.
0 - Encerrar programa."""
    )
    while True:
        opcao = input("\n→ ")
        if opcao:
            return opcao
        else:
            print("\nNão é válido 'Enter' como entrada")


def cadastro(agenda, id_contato, agenda_json):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" CADASTRO ":^60}\n{"-"*60}')
        print(
            """
1 - Continuar para cadastro.
0 - Sair."""
        )
        opcao = input("\n→ ")
        if opcao:
            if opcao == "1":
                while True:
                    nome = input("\nInsira o nome\n→ ").capitalize().strip()
                    if nome:
                        especial = [
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "0",
                            "!",
                            "@",
                            "#",
                            "$",
                            "%",
                            "&",
                            ",",
                            ".",
                            ";",
                        ]
                        diferente = False
                        for letra in nome:
                            if letra in especial:
                                diferente = True
                                break
                        if diferente:
                            print(
                                "\nO nome não pode conter números e caracteres especiais!\n"
                            )
                        else:
                            break
                    else:
                        print("\nNão é válido valor vazio\n")
                while True:
                    endereco = (
                        input(f"\nInsira o endereço de {nome}\n→ ").capitalize().strip()
                    )
                    if endereco:
                        especial = ["!", "@", "#", "$", "%", "&", ",", ".", ";"]
                        diferente = False
                        for letra in endereco:
                            if letra in especial:
                                diferente = True
                                break
                        if diferente:
                            print(
                                "\nO endereço não pode conter caracteres especiais!\n"
                            )
                        else:
                            break
                    else:
                        print("\nNão é válido valor vazio\n")
                resp = "s"
                lista_telefone = []
                while resp[0] in "sS":
                    while True:
                        telefone = input(
                            f"\nInsira o telefone de {nome}\nex: (00)0000-0000\n→ "
                        ).strip()
                        if telefone:
                            if (
                                telefone[0] != "("
                                or telefone[3] != ")"
                                or telefone[8] != "-"
                                or len(telefone) != 13
                                or contem_letras(telefone)
                            ):
                                print(
                                    "\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!"
                                )
                            else:
                                break
                        else:
                            print("\nNão é válido valor vazio\n")
                    lista_telefone.append(telefone)
                    resp = input("\nDeseja adicionar outro telefone? (sim/não)\n→ ")
                agenda[id_contato] = {
                    "nome": nome,
                    "endereço": endereco,
                    "telefone": lista_telefone,
                }
                with open(agenda_json, "w", encoding="utf8") as arquivo:
                    json.dump(agenda, arquivo, indent=4)
                print(Fore.GREEN+"\nContato cadastrado com sucesso...\n"+Fore.RESET)
                sleep(3)
            elif opcao == "0":
                break
            else:
                print("\nEscolha um valor numérico (1 ou 0)!\n")
        else:
            print("\nNão é válido valor vazio\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""


def editar(agenda, agenda_json):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" EDITAR ":^60}\n{"-"*60}')
        print(
            """
1 - Continuar para editar.
0 - Sair."""
        )
        opcao = input("\n→ ")
        if opcao:
            if opcao == "1":
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    while True:
                        os.system("cls")
                        print(
                            f'\n{"-"*60}\n{"CONTATOS":^60}\n{"-"*60}'
                        )  # ! contatos disponíveis
                        for id, contato in agenda.items():
                            print(f"ID: {id} → {contato['nome']}")
                        id = input("\nInsira o ID do contato que desejar\n→ ").strip()
                        if id:
                            if id in agenda.keys():
                                while True:
                                    print(
                                        """
1 - Nome
2 - Endereço
3 - Telefone
0 - Sair"""
                                    )
                                    opcao_editar = (
                                        input(
                                            f'\nInsira o que deseja editar de {agenda[id]["nome"]}\n→ '
                                        )
                                        .lower()
                                        .strip()
                                    )
                                    if opcao_editar:
                                        if (
                                            opcao_editar == "1"
                                            or opcao_editar[0] == "n"
                                        ):
                                            while True:
                                                novo_nome = (
                                                    input("\nInsira o novo nome\n→ ")
                                                    .capitalize()
                                                    .strip()
                                                )
                                                if novo_nome:
                                                    especial = [
                                                        "1",
                                                        "2",
                                                        "3",
                                                        "4",
                                                        "5",
                                                        "6",
                                                        "7",
                                                        "8",
                                                        "9",
                                                        "0",
                                                        "!",
                                                        "@",
                                                        "#",
                                                        "$",
                                                        "%",
                                                        "&",
                                                        ",",
                                                        ".",
                                                        ";",
                                                    ]
                                                    diferente = False
                                                    for letra in novo_nome:
                                                        if letra in especial:
                                                            diferente = True
                                                            break
                                                    if diferente:
                                                        print(
                                                            "\nO nome não pode conter números e caracteres especiais!\n"
                                                        )
                                                    else:
                                                        break
                                                else:
                                                    continue
                                            agenda[id]["nome"] = novo_nome
                                            with open(
                                                agenda_json, "w", encoding="utf-8"
                                            ) as arquivo:
                                                json.dump(agenda, arquivo, indent=4)
                                            print(
                                                f"\nO nome foi alterado com sucesso!\n"
                                            )
                                            sleep(3)
                                            break
                                        if (
                                            opcao_editar == "2"
                                            or opcao_editar[0] == "e"
                                        ):
                                            while True:
                                                novo_endereco = (
                                                    input(
                                                        f"\nInsira o novo endereço de {agenda[id]['nome']}\n→ "
                                                    )
                                                    .capitalize()
                                                    .strip()
                                                )
                                                if novo_endereco:
                                                    especial = [
                                                        "!",
                                                        "@",
                                                        "#",
                                                        "$",
                                                        "%",
                                                        "&",
                                                        ",",
                                                        ".",
                                                        ";",
                                                    ]
                                                    diferente = False
                                                    for letra in novo_endereco:
                                                        if letra in especial:
                                                            diferente = True
                                                            break
                                                    if diferente:
                                                        print(
                                                            "\nO endereço não pode conter caracteres especiais!\n"
                                                        )
                                                    else:
                                                        break
                                                else:
                                                    continue
                                            agenda[id]["endereço"] = novo_endereco
                                            with open(
                                                agenda_json, "w", encoding="utf-8"
                                            ) as arquivo:
                                                json.dump(agenda, arquivo, indent=4)
                                            print(
                                                f"\nO endereço foi alterado com sucesso!\n"
                                            )
                                            sleep(3)
                                            break
                                        if (
                                            opcao_editar == "3"
                                            or opcao_editar[0] == "t"
                                        ):
                                            if len(agenda[id]["telefone"]) > 1:
                                                while True:
                                                    print(
                                                        f"\n{agenda[id]['nome']} possui os seguintes telefones:"
                                                    )
                                                    codigos = []
                                                    for i, numero in enumerate(
                                                        agenda[id]["telefone"]
                                                    ):
                                                        codigos.append(i)
                                                        print(f"Código: {i} - {numero}")
                                                    opcao_telefone = input(
                                                        "\nQuer editar qual telefone? (insira o código)\n→ "
                                                    )
                                                    if opcao_telefone:
                                                        if (
                                                            int(opcao_telefone)
                                                            in codigos
                                                        ):
                                                            novo_telefone = input(
                                                                f"\nInsira o novo telefone de {agenda[id]['nome']}\nex: (00)0000-0000\n→ "
                                                            ).strip()
                                                            while True:
                                                                if novo_telefone:
                                                                    if (
                                                                        novo_telefone[0]
                                                                        != "("
                                                                        or novo_telefone[
                                                                            3
                                                                        ]
                                                                        != ")"
                                                                        or novo_telefone[
                                                                            8
                                                                        ]
                                                                        != "-"
                                                                        or len(
                                                                            novo_telefone
                                                                        )
                                                                        != 13
                                                                        or contem_letras(
                                                                            novo_telefone
                                                                        )
                                                                    ):
                                                                        print(
                                                                            "\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!"
                                                                        )
                                                                    else:
                                                                        break
                                                                else:
                                                                    print(
                                                                        "\nNão é válido valor vazio\n"
                                                                    )
                                                            agenda[id]["telefone"][
                                                                int(opcao_telefone)
                                                            ] = novo_telefone
                                                            with open(
                                                                agenda_json,
                                                                "w",
                                                                encoding="utf-8",
                                                            ) as arquivo:
                                                                json.dump(
                                                                    agenda,
                                                                    arquivo,
                                                                    indent=4,
                                                                )
                                                            print(
                                                                f"\nO telefone foi alterado com sucesso!\n"
                                                            )
                                                            sleep(3)
                                                            break
                                                        else:
                                                            print(
                                                                "\nInsira um código válido\n"
                                                            )
                                                    else:
                                                        print(
                                                            "\nNão é válido valor vazio\n"
                                                        )
                                            else:
                                                while True:
                                                    novo_telefone = input(
                                                        f"\nInsira o novo telefone de {agenda[id]['nome']}\nex: (00)0000-0000\n→ "
                                                    ).strip()
                                                    if novo_telefone:
                                                        if (
                                                            novo_telefone[0] != "("
                                                            or novo_telefone[3] != ")"
                                                            or novo_telefone[8] != "-"
                                                            or len(novo_telefone) != 13
                                                            or contem_letras(
                                                                novo_telefone
                                                            )
                                                        ):
                                                            print(
                                                                "\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!"
                                                            )
                                                        else:
                                                            break
                                                    else:
                                                        print(
                                                            "\nNão é válido valor vazio\n"
                                                        )
                                                agenda[id]["telefone"][
                                                    0
                                                ] = novo_telefone
                                                with open(
                                                    agenda_json, "w", encoding="utf-8"
                                                ) as arquivo:
                                                    json.dump(agenda, arquivo, indent=4)
                                                print(
                                                    f"\nO telefone foi alterado com sucesso!\n"
                                                )
                                                sleep(3)
                                                break
                                            break
                                        if opcao_editar == "0":
                                            break
                                        else:
                                            print("\nInsira um ID válido\n")
                                    else:
                                        print("\nNão é válido valor vazio\n")
                                break
                            else:
                                print("\nEsse contato não existe\n")
                                sleep(3)
                        else:
                            print("\nNão é válido valor vazio\n")
                            sleep(3)
            if opcao == "0":
                break
            else:
                print("\nEscolha um valor numérico (1 ou 0)!\n")
        else:
            print("\nNão é válido valor vazio\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""


def excluir(agenda, agenda_json):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" EDITAR ":^60}\n{"-"*60}')
        print(
            """
1 - Continuar para excluir.
0 - Sair (ou qualquer tecla)."""
        )
        opcao = input("\n→ ").strip()
        if opcao:
            if opcao == "1":
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    while True:
                        os.system("cls")
                        print(
                            f'\n{"-"*60}\n{"CONTATOS":^60}\n{"-"*60}'
                        )  # ! contatos disponíveis
                        for id, contato in agenda.items():
                            print(f"ID: {id} → {contato['nome']}")
                        id = input("\nInsira o ID do contato para excluir\n→ ")
                        if id:
                            if id in agenda.keys():
                                os.system("cls")
                                while True:
                                    resp = input(
                                        Fore.RED
                                        + "\nRealmente deseja excluir"
                                        + Fore.RESET
                                        + f' {agenda[id]["nome"]} '
                                        + Fore.RED
                                        + "da agenda?\n→ "
                                        + Fore.RESET
                                    ).strip()
                                    if resp:
                                        if resp[0] in "Ss":
                                            list_keys = list(agenda.keys())
                                            if id != list_keys[-1]:
                                                agenda.pop(
                                                    id
                                                )  #! se a chave for difente do último id, apaga o id e reescreve os ids
                                                #! seguintes ao que foi excluido (apenas as chaves) e conserva os valores
                                                novo_agenda = {}
                                                for key, value in agenda.items():
                                                    if int(key) > int(id):
                                                        novo_agenda[
                                                            str(int(key) - 1)
                                                        ] = value
                                                    else:
                                                        novo_agenda[key] = value
                                                with open(
                                                    agenda_json, "w", encoding="utf-8"
                                                ) as arquivo:
                                                    json.dump(
                                                        novo_agenda, arquivo, indent=4
                                                    )
                                            else:
                                                agenda.pop(id)
                                                with open(
                                                    agenda_json, "w", encoding="utf-8"
                                                ) as arquivo:
                                                    json.dump(agenda, arquivo, indent=4)
                                            print("\nExcluindo...\n")
                                            sleep(2)
                                            print(
                                                Fore.GREEN
                                                + "\nContato excluido com sucesso!"
                                                + Fore.RESET
                                            )
                                            sleep(2)
                                            break
                                        elif resp[0] in "Nn":
                                            break
                                        else:
                                            print("\nSim ou Não?\n")
                                    else:
                                        print("\nInsira um valor válido\n")
                                break
                            else:
                                print(
                                    Fore.RED
                                    + "\nEsse contato não existe!\n"
                                    + Fore.RESET
                                )
                                sleep(3)
                        else:
                            print("\nInsira um valor válido!\n")
                            sleep(3)
            else:
                break
        else:
            print("\nInsira um caracter válido!\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""


def pesquisar(agenda):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{"PESQUISAR":^60}\n{"-"*60}')
        print(
            """
1 - Pesquisar por ID.
2 - Pesquisar por NOME.
0 - Sair (ou qualquer tecla)."""
        )
        opcao = input("\n→ ").strip()
        if opcao:
            if opcao == "1":
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos para pesquisar!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    while True:
                        os.system("cls")
                        print(
                            f'\n{"-"*60}\n{"CONTATOS":^60}\n{"-"*60}'
                        )  # ! contatos disponíveis
                        for i, contato in agenda.items():
                            print(f"ID: {i} → {contato['nome']}")
                        id = input(
                            "\nInsira o ID do contato para pesquisar\n→ "
                        ).strip()
                        if id:
                            if id in agenda.keys():
                                os.system("cls")
                                for k, v in agenda.items():
                                    if k == id:
                                        print(f'\n{"-"*60}\n{"CONTATO":^60}\n{"-"*60}')
                                        print(
                                            f"Id → {k}\nNome → {v['nome']}\nEndereço → {v['endereço']}"
                                        )
                                        for tel in range(len(v["telefone"])):
                                            print(
                                                f"Telefone {tel+1} → {v['telefone'][tel]}"
                                            )
                                print("-" * 60)
                                print("Aperte uma tecla para retornar...")
                                input()
                                break
                            else:
                                print(
                                    Fore.RED
                                    + "\nEsse contato não existe!\n"
                                    + Fore.RESET
                                )
                                sleep(3)
                        else:
                            print("\nInsira um valor válido!\n")
                            sleep(3)
            elif opcao == "2":
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos para pesquisar!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    while True:
                        os.system("cls")
                        print(
                            f'\n{"-"*60}\n{"CONTATOS":^60}\n{"-"*60}'
                        )  # ! contatos disponíveis
                        for id, contato in agenda.items():
                            print(f"ID: {id} → {contato['nome']}")
                        nome = (
                            input("\nInsira o nome do contato para pesquisar\n→ ")
                            .strip()
                            .capitalize()
                        )
                        if nome:
                            nomes_agenda = []
                            for value in agenda.values():
                                nomes_agenda.append(value["nome"])
                            if nome in nomes_agenda:
                                os.system("cls")
                                for k, v in agenda.items():
                                    if v["nome"] == nome:
                                        print(f'\n{"-"*60}\n{"CONTATO":^60}\n{"-"*60}')
                                        print(
                                            f"Id → {k}\nNome → {v['nome']}\nEndereço → {v['endereço']}"
                                        )
                                        for tel in range(len(v["telefone"])):
                                            print(
                                                f"Telefone {tel} → {v['telefone'][tel]}"
                                            )
                                print("-" * 60)
                                print("Aperte uma tecla para retornar...")
                                input()
                                break
                            else:
                                print(
                                    Fore.RED
                                    + "\nEsse contato não existe!\n"
                                    + Fore.RESET
                                )
                                sleep(3)
                        else:
                            print("\nInsira um valor válido!\n")
                            sleep(3)
            else:
                break
        else:
            print("\nInsira um caracter válido!\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""


def ordem_adcionado(agenda):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{"ORDEM DE ADICIONADOS":^60}\n{"-"*60}')
        print(
            """
1 - Continuar para mostrar.
0 - Sair."""
        )
        opcao = input("\n→ ").strip()
        if opcao:
            if opcao == "1":
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos para pesquisar!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    os.system('cls')
                    for k, v in agenda.items():
                        print(f'\n{"-"*60}\n{v["nome"]:^60}\n{"-"*60}')
                        print(f"\nId → {k}\nEndereço → {v['endereço']}")
                        for tel in range(len(v["telefone"])):
                            print(f"Telefone {tel+1} → {v['telefone'][tel]}")
                    print(f'\n{"-"*60}')
                    print("Aperte uma tecla para retornar...")
                    input()
            else:
                break
        else:
            print("\nInsira um valor válido!\n")
            sleep(3)
    print(f'{"-"*60}\n{"- "*30}')
    return ""

def ordem_abc(agenda):
    while True:
        os.system("cls")
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{"ORDEM ALFABÉTICA":^60}\n{"-"*60}')
        print(
            """
1 - Continuar para mostrar.
0 - Sair."""
        )
        opcao = input("\n→ ").strip()
        if opcao:
            if opcao=='1':
                if not agenda:
                    os.system("cls")
                    print(f'\n{"-"*60}')
                    print(Fore.RED + "Não há contatos para pesquisar!" + Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    os.system('cls')
                    
                    # for key, value in sorted(agenda.items(), key=lambda item: item[1]['nome']):
                    #     ordem_alfabetica = {key: value}
                    
                    ordem_alfabetica = {key: value for key, value in sorted(agenda.items(), key=lambda item: item[1]['nome'])}
                        
                    for k, v in ordem_alfabetica.items():
                        print(f'\n{"-"*60}\n{v["nome"]:^60}\n{"-"*60}')
                        print(f"\nId → {k}\nEndereço → {v['endereço']}")
                        for tel in range(len(v["telefone"])):
                            print(f"Telefone {tel+1} → {v['telefone'][tel]}")
                    print(f'\n{"-"*60}')
                    print("Aperte uma tecla para retornar...")
                    input()
            else:
                break
        else:
            print("\nInsira um valor válido!\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""
