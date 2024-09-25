class Livro {
  constructor(titulo, autor, quantidade) {
    this.titulo = titulo;
    this.autor = autor;
    this.quantidade = quantidade;
  }
}

var estoque = [];

adicionarLivro("O Senhor dos Anéis", "J.R.R. Tolkien", 10);
adicionarLivro("Harry Potter", "J.K. Rowling", 5);
adicionarLivro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 3);

listarLivros();

removerLivro("Harry Potter");

listarLivros();

atualizarQuantidade("O Senhor dos Anéis", 20);

listarLivros();

function adicionarLivro(titulo, autor, quantidade) {
    for (item of estoque) {
        if (item.titulo == titulo) {
            console.log("Livro já cadastrado");
            return;
        }
    }

    let livro = new Livro(titulo, autor, quantidade);
    estoque.push(livro);
}

function removerLivro(titulo) {
    for (let i = 0; i < estoque.length; i++) {
        if (estoque[i].titulo == titulo) {
            estoque.splice(i, 1);
            console.log("Livro removido");
            return;
        }
    }
    console.log("Livro não encontrado");
}

function atualizarQuantidade(titulo, novaQuantidade) {
    for (item in estoque){
        if (estoque[item].titulo == titulo) {
            estoque[item].quantidade = novaQuantidade;
            console.log("Quantidade atualizada");
            return;
        }
    }
    console.log("Livro não encontrado");
}

function listarLivros() {
    for (item of estoque) {
        console.log("Título: " + item.titulo + " Autor: " + item.autor + " Quantidade: " + item.quantidade);
    }
}