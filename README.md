# 🏋️ FitPlanner — Sistema de Gerenciamento de Treinos

![Python](https://img.shields.io/badge/Python-55.7%25-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-21.5%25-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML-18.8%25-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-4.0%25-1572B6?style=flat&logo=css3&logoColor=white)

---

## 📋 Sobre o Projeto

O **FitPlanner** é um sistema de gerenciamento de treinos que permite ao usuário cadastrar, visualizar, atualizar e excluir seus planos de treino de forma simples e intuitiva. O projeto conta com duas versões: uma interface web rodando no navegador via **PyScript**, e uma versão de terminal em Python puro.

> Projeto desenvolvido pelo **Grupo 8**: Matheus Trajano de Freitas, Luiz Henrique de Andrade Rodrigues, Mariana de Melquiades Melo, Lucas Silva Moreira do Nascimento, Arthur Santana de Andrade e Ricardo Amorim Bayma.

---

## 🚀 Funcionalidades

- ➕ **Adicionar treino** — Cadastre nome, tipo e detalhes do exercício (séries, repetições e carga);
- 📋 **Listar treinos** — Visualize todos os treinos salvos no painel de saída;
- ✏️ **Atualizar treino** — Edite os dados de um treino existente com recalculo automático de calorias;
- 🗑️ **Excluir treino** — Remova treinos específicos do sistema através de menus seletores;
- 🔥 **Cálculo de Gasto Calórico** — Sistema integrado que computa e acumula as calorias estimadas dos seus treinos;
- 💡 **Treinos Recomendados** — Injeção automatizada de rotinas prontas para membros Superiores ou Inferiores;
- 💻 **Versão Terminal** — Interface via linha de comando em Python puro com menu interativo e administração de metas.
---

## 🗂️ Estrutura do Projeto

```
fitplanner/
├── index.html            # Interface web principal (usa PyScript)
├── app.py                # Lógica do backend em Python (versão web)
├── app.js                # Funções auxiliares JavaScript (dropdowns, eventos)
├── style.css             # Estilização da interface web
├── app(terminal).py      # Versão completa para rodar no terminal
└── Academia_FitPlanner.png   # Imagem do projeto
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python** | Lógica de CRUD e manipulação do arquivo `treino.txt` |
| **PyScript** | Execução do Python diretamente no navegador |
| **JavaScript** | Comunicação entre a interface HTML e o Python |
| **HTML/CSS** | Estrutura e estilização da interface web |

---

## ▶️ Como Executar

### Versão Web

1. Clone o repositório:

```bash
git clone https://github.com/lucassmnasc/fitplanner.git
```

2. Abra o arquivo `index.html` em um navegador moderno.

> ⚠️ O PyScript requer conexão com a internet para carregar suas dependências. Caso o navegador bloqueie o arquivo local, use um servidor local:

```bash
python -m http.server 8000
```

Depois acesse `http://localhost:8000` no navegador.

### Versão Terminal

1. Certifique-se de ter o **Python 3** instalado.

2. Execute:

```bash
python "app(terminal).py"
```

3. Navegue pelo menu usando as opções numéricas:

```
1 - Adicionar treino
2 - Listar treinos
3 - Atualizar treinos
4 - Excluir treinos
5 - Administrar Metas
6 - Treino recomendado
7 - Sair
```

---

## 📁 Armazenamento e Persistência

O sistema adota estratégias diferentes dependendo do ambiente de execução:

- **Versão Web:** Os dados são persistidos no navegador do usuário utilizando a API do `localStorage` sob a chave `'treino_txt'`. Isso garante que seus treinos continuem lá mesmo após fechar a aba.
- **Versão Terminal:** Os treinos são salvos localmente em um arquivo físico chamado **`treino.txt`**, gerado na mesma pasta do script.

### Formato do Registro (Web):
```
Treino: <Nome> | Tipo: <Tipo> | Exercícios: [<NomeEx>: <Séries> ser X <Reps> rep: <Carga>] | Calorias estimadas: <Valor> kcal
```

---

## 📌 Requisitos

- Python 3.x (para a versão terminal)
- Navegador moderno com suporte a ES Modules (para a versão web)
- Conexão com a internet (para carregar o PyScript na versão web)

---

Feito com 💪 pelo Grupo 8
