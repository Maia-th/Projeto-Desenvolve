package com.gerenciamento.biblioteca.Model;

public class Autor extends Pessoa {
    private String nacionalidade;

    public Autor(String nome, Livro[] livros, String nacionalidade) {
        super(nome, livros);
        this.nacionalidade = nacionalidade;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public Livro[] getObrasPublicadas() {
        return livros;
    }

    public void setLivros(Livro[] livros) {
        this.livros = livros;
    }

    public Livro[] getObrasPublicadasPorGeneros(String genero) {
        Livro[] obrasPorGenero = new Livro[livros.length];
        int count = 0;
        for (Livro livro : livros) {
            if (livro.getGenero().equals(genero)) {
                obrasPorGenero[count] = livro;
                count++;
            }
        }
        return obrasPorGenero;
    }
}
