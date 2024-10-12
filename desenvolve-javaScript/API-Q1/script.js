const buscar = () =>{
    const user = document.getElementById('buscaUsers').value;

    fetch(`https://api.github.com/users/${user}`)
    .then(response => response.json())
    .then(data => {
        const {id,login,name} = data;

        if(data.message){
            document.getElementById('usersList').innerHTML = `
            <li class="notFound">Usuário não encontrado</li>`;
            return;
        }

        document.getElementById('usersList').innerHTML = `
        <li>ID: ${id}</li>
        <li>Usuario: ${login}</li>
        <li>Nome: ${name}</li>`;
    })
}