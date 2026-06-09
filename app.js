let treinoSelecionadoGlobal = "";

window.exibirNoOutput = function(texto) {
    const divOutput = document.getElementById("output");
    if (divOutput.innerText === "As atualizações do sistema aparecerão aqui..." || divOutput.innerText === "") {
        divOutput.innerText = texto;
    } else {
        divOutput.innerText += "\n" + texto;
    }
};

window.atualizarDropdowns = function() {
    if (!window.py_treino_js) return;

    const conteudo = window.py_treino_js();
    
    const selectAtualizar = document.getElementById("treino_select");
    const selectExcluir = document.getElementById("excluir_select");

    selectAtualizar.innerHTML = "";
    selectExcluir.innerHTML = "";

    if (!conteudo || conteudo.trim() === "") {
        return; 
    }

    const treinos = conteudo.split("\n").filter(linha => linha.trim() !== "");

    treinos.forEach(texto => {
        if(texto.includes("Treino:")) {
            const opt1 = document.createElement("option");
            opt1.value = texto;
            opt1.innerText = texto;
            selectAtualizar.appendChild(opt1);

            const opt2 = document.createElement("option");
            opt2.value = texto;
            opt2.innerText = texto;
            selectExcluir.appendChild(opt2);
        }
    });
};

window.adicionar_click = function() {
    document.getElementById("output").innerText = "";
    window.py_adicionar();
    
    document.getElementById("ex_nome").value = "";
    document.getElementById("ex_series").value = "";
    document.getElementById("ex_reps").value = "";
    document.getElementById("ex_carga").value = "";
};

window.listar_click = function() {
    document.getElementById("output").innerText = "";
    window.py_listar();
};

window.carregar_treino_click = function() {
    treinoSelecionadoGlobal = document.getElementById("treino_select").value;
    if (!treinoSelecionadoGlobal) {
        document.getElementById("output").innerText = "Selecione um treino válido.";
        return;
    }

    try {
        const partes = treinoSelecionadoGlobal.split(" | ");
        const nome = partes[0].replace("Treino: ", "");
        const tipo = partes[1].replace("Tipo: ", "");
        const exercicios = partes[2].replace("Exercícios: ", "");

        document.getElementById("edit_nome").value = nome;
        document.getElementById("edit_tipo").value = tipo;
        document.getElementById("edit_exercicios").value = exercicios;
        document.getElementById("output").innerText = "Dados carregados abaixo.";
    } catch(e) {
        document.getElementById("edit_nome").value = treinoSelecionadoGlobal;
        document.getElementById("output").innerText = "Dados carregados abaixo.";
    }
};

window.atualizar_click = function() {
    if (!treinoSelecionadoGlobal) {
        document.getElementById("output").innerText = "Não há treinos carregados para atualizar.";
        return;
    }

    const nome = document.getElementById("edit_nome").value;
    const tipo = document.getElementById("edit_tipo").value;
    const exercicios = document.getElementById("edit_exercicios").value;

    let treinoNovo = `Treino: ${nome} | Tipo: ${tipo} | Exercícios: ${exercicios}`;

    document.getElementById("output").innerText = "";
    window.py_atualizar(treinoSelecionadoGlobal, treinoNovo);

    document.getElementById("edit_nome").value = "";
    document.getElementById("edit_tipo").value = "";
    document.getElementById("edit_exercicios").value = "";
    treinoSelecionadoGlobal = "";
};

window.excluir_click = function() {
    const treinoAlvo = document.getElementById("excluir_select").value;
    if (!treinoAlvo) {
        document.getElementById("output").innerText = "Selecione um treino para excluir.";
        return;
    }
    document.getElementById("output").innerText = "";
    window.py_excluir(treinoAlvo);
};
