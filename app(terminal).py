import os
os.system('cls')


def adicionar():    #CREATE
    try:
        nome = input("nome do treino: ")
        tipo = input("tipo de treino: ")
        ex = int(input(f"quantas exercicios terá o treino {nome}?: "))

        dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

        for i in range(ex):
            exf = input(f"qual o exercicio {i+1}: ")
            rep = int(input(f"quantas repetições terá o exercicio {i+1}:"))
            dados_treino += f"[{exf}: {rep} rep] "

        with open('treino.txt', 'a') as arquivo:
            arquivo.write(dados_treino + '\n')

        print("Treino adicionado com sucesso!")

    except ValueError:
        print("Erro: digite um número válido para a quantidade de exercícios ou repetições.")
    except PermissionError:
        print("Erro: sem permissão para gravar no arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


def listar():   #READ
    try:
        arquivo = open('treino.txt', 'r')
        treinos = arquivo.readlines()
        arquivo.close()

        if len(treinos) == 0:
            print('Nenhum treino foi cadastrado ainda.')

        else:
            print('Listar treino:')
            for i in range(len(treinos)):
                print(treinos[i].strip())

    except FileNotFoundError:
        print("Nenhum treino encontrado!")
    except PermissionError:
        print("Erro: sem permissão para ler o arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


def atualizar():  # UPDATE
    try:
        treino = input("Digite o nome do treino que deseja atualizar: ")

        arquivo = open('treino.txt', 'r')
        treinos = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for i in range(len(treinos)):

            if treino in treinos[i]:

                print("\nDigite os novos dados do treino:")

                nome = input("Nome do treino: ")
                tipo = input("Tipo de treino: ")
                ex = int(input(f"Quantos exercícios terá o treino {nome}?: "))

                dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

                for j in range(ex):
                    exf = input(f"Qual o exercício {j+1}: ")
                    rep = int(input(f"Quantas repetições terá o exercício {j+1}: "))
                    dados_treino += f"[{exf}: {rep} rep] "

                treinos[i] = dados_treino + "\n"
                encontrado = True
                break

        if encontrado:
            arquivo = open('treino.txt', 'w')

            for treino_atualizado in treinos:
                arquivo.write(treino_atualizado)

            arquivo.close()

            print("Treino atualizado com sucesso!")

        else:
            print("Treino não encontrado.")

    except ValueError:
        print("Erro: digite um número válido para a quantidade de exercícios ou repetições.")
    except FileNotFoundError:
        print("Nenhum arquivo encontrado!")
    except PermissionError:
        print("Erro: sem permissão para acessar o arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


def treino_recomendado():
    try:
        print("TIPOS DE TREINO\nSUPERIORES\nINFERIORES")
        tipo = input("tipo de treino: ").upper()
        if tipo == "SUPERIORES":
            superiores = [
                {"exercicio": "Supino Reto","series": 3, "reps":"8-12"},
                {"exercicio": "Supino Inclinado","series": 3, "reps":"8-12"},
                {"exercicio": "Voador","series": 3, "reps":"8-12"},
                {"exercicio": "Triceps Testa","series": 3, "reps":"8-12"},
                {"exercicio": "Triceps Corda","series": 3, "reps":"8-12"},
                {"exercicio": "Triceps Pulley","series": 3, "reps":"8-12"},
                {"exercicio": "Puxada Frontal","series": 3, "reps":"8-12"},
                {"exercicio": "Remada Baixa","series": 3, "reps":"8-12"},
                {"exercicio": "Pulldown(polia)","series": 3, "reps":"8-12"},
                {"exercicio": "Rosca Martelo com Halteres","series": 3, "reps":"8-12"},
                {"exercicio": "Rosca Scott","series": 3, "reps":"8-12"},
                {"exercicio": "Rosca Direta com Barra","series": 3, "reps":"8-12"},
            ]

            nome = "Recomendado do Sistema"
            dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

            for i in superiores:
                dados_treino += f"\n[{i['exercicio']}: {i['series']} x {i['reps']}]"
            with open('treino.txt', 'a') as arquivo:
                arquivo.write(dados_treino + '\n')

            print("Treino recomendado adicionado com sucesso!")

        elif tipo == "INFERIORES":
            inferiores = [
                {"exercicio": "Agachamento livre","series": 3, "reps":"8-12"},
                {"exercicio": "Leg press","series": 3, "reps":"8-12"},
                {"exercicio": "Agachamento Bulgaro","series": 3, "reps":"8-12"},
                {"exercicio": "Mesa flexora","series": 3, "reps":"8-12"},
                {"exercicio": "Cadeira Abdutora","series": 3, "reps":"8-12"},
                {"exercicio": "Gemeos(pé/sentado)","series": 4, "reps":"12-15"},
            ]

            nome = "Recomendado do Sistema"
            dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercicios: "

            for i in inferiores:
                dados_treino += f"\n[{i['exercicio']}: {i['series']}x{i['reps']}]"

            with open('treino.txt', 'a') as arquivo:
                arquivo.write(dados_treino + '\n')

            print("Treino recomendado adicionado com sucesso!")

        else:
            print("Tipo de treino inválido. Escolha SUPERIORES ou INFERIORES.")

    except PermissionError:
        print("Erro: sem permissão para gravar no arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


def excluir():       #DELETE
    try:
        treino = input("Digite o treino que deseja excluir: ")
        arquivo = open('treino.txt', 'r')
        treinos = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for i in range(len(treinos)):
            if treino in treinos[i].strip():
                treinos.pop(i)

                arquivo = open('treino.txt', 'w')
                for linha in treinos:
                    arquivo.write(linha)
                arquivo.close()

                print('Treino removido com sucesso!')
                encontrado = True
                break

        if not encontrado:
            print('Treino não encontrado.')

    except FileNotFoundError:
        print("Nenhum arquivo encontrado!")
    except PermissionError:
        print("Erro: sem permissão para acessar o arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


def metas():
    try:
        goals = []

        print("1 - adicionar metas")
        print("2 - visualizar metas")
        print("3 - finalizar/excluir metas")

        acao = int(input("adicionar ou visualizar metas? "))
        if acao == 1:
            while True:
                goal = input("definir metas (. para encerrar): ")
                if goal == ".":
                    break
                goals.append(goal)
                with open("treino.txt", "a") as arquivo:
                    arquivo.write(goal + '\n')

        elif acao == 2:
            with open("treino.txt", "r") as arquivo:
                print(arquivo.read())

        elif acao == 3:
            with open("treino.txt", "r") as arquivo:
                goals = arquivo.readlines()

            print("\nSuas metas atuais:")
            for i in range(len(goals)):
                print(f"{i + 1} - {goals[i].strip()}")

            finish = input("\nQual meta deseja remover? ")

            meta_encontrada = False
            for i in range(len(goals)):
                if goals[i].strip() == finish:
                    goals.pop(i)
                    meta_encontrada = True

                    with open("treino.txt", "w") as arquivo:
                        for meta in goals:
                            arquivo.write(meta)

                    print("Meta finalizada/excluída com sucesso!")
                    break

            if not meta_encontrada:
                print("Meta não encontrada.")

        else:
            print("Opção inválida. Escolha entre 1 e 3.")

    except ValueError:
        print("Erro: digite um número válido para escolher a ação.")
    except FileNotFoundError:
        print("Nenhum arquivo encontrado!")
    except PermissionError:
        print("Erro: sem permissão para acessar o arquivo.")
    except OSError as e:
        print(f"Erro ao acessar o arquivo: {e}")


while True:
    try:
        print('\n1 - Adicionar treino')
        print('2 - Listar treinos')
        print('3 - Atualizar treinos')
        print('4 - Excluir treinos')
        print('5 - Administrar Metas')
        print('6 - Treino recomendado')
        print('7 - Sair')

        opcao = int(input('Escolha as opções entre 1-7: '))

        if opcao == 1:
            adicionar()

        elif opcao == 2:
            listar()

        elif opcao == 3:
            atualizar()

        elif opcao == 4:
            excluir()

        elif opcao == 5:
            metas()

        elif opcao == 6:
            treino_recomendado()

        elif opcao == 7:
            break

        else:
            print("Opção inválida. Escolha entre 1 e 7.")

    except ValueError:
        print("Erro: digite um número válido para escolher a opção.")
