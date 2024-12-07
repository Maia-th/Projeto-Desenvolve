package com.gerenciamento.biblioteca.Model;

import java.util.ArrayList;
import java.util.List;

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
        List<Livro> obrasPorGenero = new ArrayList<>();
        for (Livro livro : livros) {
            if (livro.getGenero().equals(genero)) {
                obrasPorGenero.add(livro);
            }
        }
        return obrasPorGenero.toArray(new Livro[0]);
    }
}