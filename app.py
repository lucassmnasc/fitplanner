# GRUPO 8: Matheus Trajano de Freitas, Luiz Henrique de Andrade Rodrigues, Mariana de Melquiades Melo, Lucas Silva Moreira do Nascimento, Arthur Santana de Andrade e Ricardo Amorim Bayma

import js

def py_treino_js():
    conteudo = js.localStorage.getItem('treino_txt')
    if conteudo is None:
        return ""
    return conteudo

def adicionar():
    try:
        nome = js.document.getElementById("nome").value
        tipo = js.document.getElementById("tipo").value
        exf = js.document.getElementById("ex_nome").value
        ser = int(js.document.getElementById("ex_series").value)
        rep = int(js.document.getElementById("ex_reps").value)
        carga = int(js.document.getElementById("ex_carga").value)

        dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "
        dados_treino += f"[{exf}: {ser} ser X {rep} rep: {carga}] "

        calorias_ex = (ser * 1) * 50
        dados_treino += f"| Calorias estimadas: {calorias_ex} kcal"

        conteudo_atual = py_treino_js()
        novo_conteudo = conteudo_atual + dados_treino + '\n'
        
        js.localStorage.setItem('treino_txt', novo_conteudo)
        js.exibirNoOutput("Treino e Exercício armazenados com sucesso!")
        js.atualizarDropdowns()
        
    except ValueError:
        js.exibirNoOutput("Erro: Digite números válidos para Séries, Repetições e Carga.")
    except Exception:
        js.exibirNoOutput("Erro inesperado ao salvar os dados.")

def listar():
    conteudo = py_treino_js()
    if not conteudo.strip():
        js.exibirNoOutput('Nenhum treino foi cadastrado ainda.')
        return

    treinos = conteudo.split('\n')
    js.exibirNoOutput('Listar treino:')
    for treino in treinos:
        if treino.strip():
            js.exibirNoOutput(treino.strip())

def atualizar(treino_antigo, treino_novo):
    conteudo = py_treino_js()
    treinos = conteudo.split('\n')

    if "Exercícios:" in treino_novo and "kcal" not in treino_novo:
        qtd_exercicios = treino_novo.count('[')
        if qtd_exercicios == 0:
            qtd_exercicios = 1
            
        calorias_atualizadas = (3 * qtd_exercicios) * 50
        treino_novo += f" | Calorias estimadas: {calorias_atualizadas} kcal"

    encontrado = False
    for i in range(len(treinos)):
        if treinos[i].strip() == treino_antigo.strip():
            treinos[i] = treino_novo
            encontrado = True
            break

    if encontrado:
        novo_conteudo = '\n'.join(treinos)
        js.localStorage.setItem('treino_txt', novo_conteudo)
        js.exibirNoOutput("Treino atualizado e calorias recalculadas!")
        js.atualizarDropdowns()
    else:
        js.exibirNoOutput("Treino não encontrado para atualização.")

def excluir(treino_alvo):
    conteudo = py_treino_js()
    treinos = conteudo.split('\n')

    encontrado = False
    for i in range(len(treinos)):
        if treinos[i].strip() == treino_alvo.strip():
            treinos.pop(i)
            encontrado = True
            break

    if encontrado:
        novo_conteudo = '\n'.join(treinos)
        js.localStorage.setItem('treino_txt', novo_conteudo)
        js.exibirNoOutput('Treino removido com sucesso!')
        js.atualizarDropdowns()
    else:
        js.exibirNoOutput('Treino não encontrado!')

def treino_recomendado_python(tipo_treino):
    tipo = tipo_treino.upper()
    dados_treino = ""
    
    if tipo == "SUPERIORES":
        superiores = [
            {"exercicio": "Supino Reto","series": 3, "reps":"8-12"},
            {"exercicio": "Triceps Corda","series": 3, "reps":"8-12"},
            {"exercicio": "Puxada Frontal","series": 3, "reps":"8-12"}
        ]
        dados_treino = f"Treino: Recomendado do Sistema | Tipo: {tipo} | Exercícios: "
        for i in superiores:
            dados_treino += f"[{i['exercicio']}: {i['series']} ser X {i['reps']} rep: 0] "
            
        qtd_exercicios = len(superiores)
        calorias_rec = (3 * qtd_exercicios) * 50
        dados_treino += f"| Calorias estimadas: {calorias_rec} kcal"
                
    elif tipo == "INFERIORES":
        inferiores = [
            {"exercicio": "Agachamento livre","series": 3, "reps":"8-12"},
            {"exercicio": "Leg press","series": 3, "reps":"8-12"},
            {"exercicio": "Mesa flexora","series": 3, "reps":"8-12"}
        ]
        dados_treino = f"Treino: Recomendado do Sistema | Tipo: {tipo} | Exercícios: "
        for i in inferiores:
            dados_treino += f"[{i['exercicio']}: {i['series']} ser X {i['reps']} rep: 0] "

        qtd_exercicios = len(inferiores)
        calorias_rec = (3 * qtd_exercicios) * 50
        dados_treino += f"| Calorias estimadas: {calorias_rec} kcal"

    if dados_treino != "":
        conteudo_atual = py_treino_js()
        js.localStorage.setItem('treino_txt', conteudo_atual + dados_treino + '\n')
        js.exibirNoOutput(f"Treino recomendado de {tipo} adicionado com sucesso!")
        js.atualizarDropdowns()

def calcular_calorias():
    conteudo = py_treino_js()
    linhas = conteudo.split('\n')
    total_calorias = 0
    
    for linha in linhas:
        partes = linha.split('|')
        for p in partes:
            if "kcal" in p:
                valor_calorias = float(p.replace("kcal", "").replace("Calorias estimadas:", "").strip())
                total_calorias += valor_calorias
                
    js.exibirNoOutput(f"Total de calorias acumuladas: {total_calorias} kcal")

def limpar_tudo():
    js.localStorage.removeItem('treino_txt')
    js.exibirNoOutput("Dados do sistema resetados.")
    js.atualizarDropdowns()


js.window.py_treino_js = py_treino_js
js.window.py_adicionar = adicionar
js.window.py_listar = listar
js.window.py_atualizar = atualizar
js.window.py_excluir = excluir
js.window.py_treino_recomendo = treino_recomendado_python
js.window.py_calcular_calorias = calcular_calorias
js.window.py_limpar_tudo = limpar_tudo
