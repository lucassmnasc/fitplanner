<div align="center">
🏋️ FitPlanner
Sistema de Gerenciamento de Treinos

📋 Sobre o Projeto
O FitPlanner é um sistema de gerenciamento de treinos que permite ao usuário cadastrar, visualizar, atualizar e excluir seus planos de treino de forma simples e intuitiva. O projeto conta com duas versões: uma interface web rodando no navegador via PyScript, e uma versão de terminal em Python puro.

Projeto desenvolvido pelo Grupo 8:
Matheus Trajano de Freitas, Luiz Henrique de Andrade Rodrigues, Mariana de Melquiades Melo, Lucas Silva Moreira do Nascimento, Arthur Santana de Andrade e Ricardo Amorim Bayma.


🚀 Funcionalidades

➕ Adicionar treino — cadastre nome, tipo e exercícios de um treino
📋 Listar treinos — visualize todos os treinos salvos
✏️ Atualizar treino — edite os dados de um treino existente
🗑️ Excluir treino — remova um treino da lista
💻 Versão terminal — interface via linha de comando com menu interativo


🗂️ Estrutura do Projeto
fitplanner/
├── index.html           # Interface web principal (usa PyScript)
├── app.py               # Lógica do backend em Python (versão web)
├── app.js               # Funções auxiliares JavaScript (dropdowns, eventos)
├── style.css            # Estilização da interface web
├── app(terminal).py     # Versão completa para rodar no terminal
└── Academia_FitPlanner.png  # Imagem do projeto

🛠️ Tecnologias Utilizadas
TecnologiaUsoPythonLógica de CRUD e manipulação de arquivo treino.txtPyScriptExecução do Python diretamente no navegadorJavaScriptComunicação entre a interface HTML e o PythonHTML/CSSEstrutura e estilização da interface web

▶️ Como Executar
Versão Web

Clone o repositório:

bash   git clone https://github.com/lucassmnasc/fitplanner.git

Abra o arquivo index.html em um navegador moderno.

⚠️ O PyScript requer conexão com a internet para carregar suas dependências. Não funciona abrindo o arquivo localmente via file:// em alguns navegadores — use um servidor local se necessário:



bash   python -m http.server 8000
Depois acesse http://localhost:8000 no navegador.
Versão Terminal

Certifique-se de ter o Python 3 instalado.
Execute:

bash   python "app(terminal).py"

Navegue pelo menu usando as opções numéricas:

   1 - Adicionar treino
   2 - Listar treinos
   3 - Atualizar treinos
   4 - Excluir treinos
   5 - Administrar Metas
   6 - Treino recomendado
   7 - Sair

📁 Armazenamento
Os treinos são salvos localmente no arquivo treino.txt, criado automaticamente na primeira execução. Cada treino ocupa uma linha no seguinte formato:
Treino: <nome> | Tipo: <tipo> | Exercícios: <exercício>: <repetições>, ...

📌 Requisitos

Python 3.x (para a versão terminal)
Navegador moderno com suporte a ES Modules (para a versão web)
Conexão com a internet (para carregar o PyScript na versão web)


<div align="center">
Feito com 💪 por Grupo 8
</div>
