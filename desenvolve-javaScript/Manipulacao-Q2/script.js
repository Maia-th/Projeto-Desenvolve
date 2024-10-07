var listaTarefas = [];

(function () {
  listaTarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
})();

addEventListener("load", carregaLista);

function Adicionar() {
  const descricaoTarefa = document.getElementById("tarefa").value;
  

  var tarefa = {
    descricao: descricaoTarefa,
    status: false,
  };

  listaTarefas.push(tarefa);
  localStorage.setItem("tarefas", JSON.stringify(listaTarefas));
  const index = listaTarefas.length - 1;

  document.getElementById('checkboxes').innerHTML += `<div class="novaTarefa"><input type="checkbox" id="tarefa${index}" class="inputCheck" name="tarefa${index}"><label for="tarefa${index}" class="labelNoCheck">${listaTarefas[index].descricao}</label><button onclick="excluirItem(${index})" class="excluir">X</button></div>`;
  
  observaMudancas();
}

function carregaLista() {
  const checkboxes = document.getElementById('checkboxes');
  if (!checkboxes) return;
  
  for (let i = 0; i < listaTarefas.length; i++){
    checkboxes.innerHTML += `<div class="novaTarefa"><input type="checkbox" id="tarefa${i}" class="inputCheck" name="tarefa${i}"><label for="tarefa${i}" class="labelNoCheck">${listaTarefas[i].descricao}</label><button onclick="excluirItem(${i})" class="excluir">X</button></div>`;

    if(listaTarefas[i].status == true){
      document.getElementById(`tarefa${i}`).setAttribute("checked", "checked");
      document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelCheck");
      document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelNoCheck");
    }
    else{
      document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelCheck");
      document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelNoCheck");
    }
  }

  observaMudancas();
}


function observaMudancas(){
  for (let i = 0; i < listaTarefas.length; i++) {
    const tarefa = document.getElementById(`tarefa${i}`);
    if(!tarefa) return;

    tarefa.addEventListener("change", function () {
      if (document.getElementById(`tarefa${i}`).checked) {
        listaTarefas[i].status = true;
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelCheck");
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelNoCheck");
        localStorage.setItem("tarefas", JSON.stringify(listaTarefas));
      } else {
        listaTarefas[i].status = false;
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelCheck");
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelNoCheck");
        localStorage.setItem("tarefas", JSON.stringify(listaTarefas))
      }
    });
  }
}

function excluirItem(index){
  listaTarefas.splice(index, 1);
  localStorage.setItem("tarefas", JSON.stringify(listaTarefas));
  document.getElementById('checkboxes').innerHTML = '';
  carregaLista();
}