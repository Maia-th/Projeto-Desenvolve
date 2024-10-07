var listaTarefas = [];

function Adicionar() {
  const descricaoTarefa = document.getElementById("tarefa").value;

  let tarefa = {
    descricao: descricaoTarefa,
    status: false,
  };

  listaTarefas.push(tarefa);

  const index = listaTarefas.length - 1;
  document.getElementById(
    "checkboxes"
  ).innerHTML += `<div class="novaTarefa"><input type="checkbox" id="tarefa${index}" class="inputCheck" name="tarefa${index}"><label for="tarefa${index}" class="labelNoCheck">${listaTarefas[index].descricao}</label></div>`;

  for (let i = 0; i < listaTarefas.length; i++) {
    document.getElementById(`tarefa${i}`).addEventListener("change", function () {
      if (document.getElementById(`tarefa${i}`).checked) {
        listaTarefas[i].status = true;
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelCheck");
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelNoCheck");
      } else {
        listaTarefas[i].status = false;
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.remove("labelCheck");
        document.getElementById(`tarefa${i}`).nextElementSibling.classList.add("labelNoCheck");
      }
    });
  }
}
