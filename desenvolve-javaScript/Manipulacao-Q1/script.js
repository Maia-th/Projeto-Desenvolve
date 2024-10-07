var pessoas = [];

(function() {
    pessoas = JSON.parse(localStorage.getItem('pessoas')) || [];
})();

addEventListener('load', carregaLista());

function Curtir() {
    const nomePessoa = document.getElementById('nome').value;

    if (pessoas.includes(nomePessoa)) {
        alert('Essa pessoa já curtiu.');
        return;
    }

    pessoas.push(nomePessoa);

    localStorage.setItem('pessoas', JSON.stringify(pessoas));

    carregaLista();
}

function carregaLista() {
    const listaCurtidas = document.getElementById('listaCurtidas');
    if (!listaCurtidas) return;

    if (pessoas.length == 1) 
        listaCurtidas.innerText = `${pessoas[0]} curtiu`;
    else if (pessoas.length == 2) 
        listaCurtidas.innerText = `${pessoas[0]} e ${pessoas[1]} curtiram`;
    else 
        listaCurtidas.innerText = `${pessoas[0]}, ${pessoas[1]} e mais ${pessoas.length - 2} pessoas curtiram`;
}

function Limpar() {
    const listaCurtidas = document.getElementById('listaCurtidas');
    localStorage.clear();
    pessoas = [];
    listaCurtidas.innerText = 'Ninguém curtiu';
}