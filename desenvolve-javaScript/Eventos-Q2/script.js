var pessoas = [];

function Curtir() {
    const nomePessoa = document.getElementById('nome').value;

    if (pessoas.includes(nomePessoa)) {
        alert('Essa pessoa já curtiu.');
        return;
    }

    pessoas.push(nomePessoa);

    if (pessoas.length == 1) 
        document.getElementById('listaCurtidas').innerText = `${pessoas[0]} curtiu`;
    else if (pessoas.length == 2) 
        document.getElementById('listaCurtidas').innerText = `${pessoas[0]} e ${pessoas[1]} curtiram`;
    else 
        document.getElementById('listaCurtidas').innerText = `${pessoas[0]}, ${pessoas[1]} e mais ${pessoas.length - 2} pessoas curtiram`;
}