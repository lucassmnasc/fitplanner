# GRUPO 8: Matheus Trajano de Freitas, Luiz Henrique de Andrade Rodrigues, Mariana de Melquiades Melo, Lucas Silva Moreira do Nascimento, Arthur Santana de Andrade e Ricardo Amorim Bayma

import os
import js

def print(texto):
    div = js.document.getElementById("output")
    if div:
        div.innerText = div.innerText + "\n" + str(texto) if div.innerText and div.innerText != "Atualizações aparecerão aqui..." else str(texto)

def meu_input(prompt_text=""):
    val = js.prompt(prompt_text)
    return val if val is not None else ""

def adicionar(event=None):
    nome = js.document.getElementById("nome").value
    tipo = js.document.getElementById("tipo").value
    exercicios_raw = js.document.getElementById("exercicios").value

    if not nome or not tipo or not exercicios_raw:
        print("Preencha todos os campos antes de adicionar!")
        return

    dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: {exercicios_raw}"

    with open('treino.txt', 'a') as arquivo:
        arquivo.write(dados_treino + '\n')

    js.document.getElementById("nome").value = ""
    js.document.getElementById("tipo").value = ""
    js.document.getElementById("exercicios").value = ""

    print(f"Treino '{nome}' adicionado com sucesso! :D")

def listar(event=None):
    if not os.path.exists('treino.txt'):
        print('Ainda não há treinos cadastrados! :(')
        return

    with open('treino.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) == 0:
        print('Ainda não há treinos cadastrados! :(')
    else:
        print('Lista de Treinos')
        for linha in linhas:
            print(linha.strip())

def atualizar(treino_antigo, treino_novo):
    if not os.path.exists('treino.txt'):
        print('Arquivo não encontrado.')
        return

    with open('treino.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        if linhas[i].strip() == treino_antigo:
            linhas[i] = treino_novo + '\n'
            with open('treino.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print("Treino atualizado com sucesso!")
            return

    print('Treino não encontrado.')

def excluir(treino_alvo):
    if not os.path.exists('treino.txt'):
        print('Arquivo não encontrado.')
        return

    with open('treino.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    novas_linhas = [l for l in linhas if l.strip() != treino_alvo]

    if len(novas_linhas) == len(linhas):
        print('Treino não encontrado.')
        return

    with open('treino.txt', 'w') as arquivo:
        arquivo.writelines(novas_linhas)

    print('Treino removido com sucesso.')

def treino_js():
    if not os.path.exists('treino.txt'):
        open('treino.txt', 'w').close()
    with open('treino.txt', 'r') as f:
        return f.read()

def adicionar_wrapper(event=None):
    adicionar()
    js.window.atualizarDropdowns()

def listar_wrapper(event=None):
    listar()

def atualizar_wrapper(treino_antigo, treino_novo):
    atualizar(str(treino_antigo), str(treino_novo))
    js.window.atualizarDropdowns()

def excluir_wrapper(treino_param):
    excluir(str(treino_param))
    js.window.atualizarDropdowns()

js.window.py_adicionar = adicionar_wrapper
js.window.py_listar = listar_wrapper
js.window.py_atualizar = atualizar_wrapper
js.window.py_excluir = excluir_wrapper
js.window.py_treino_js = treino_js

if not os.path.exists('treino.txt'):
    open('treino.txt', 'w').close()