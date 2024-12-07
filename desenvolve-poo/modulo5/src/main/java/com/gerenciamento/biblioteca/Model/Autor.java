package com.gerenciamento.biblioteca.Model;

import com.gerenciamento.biblioteca.Interface.PublicavelInterface;
import java.util.ArrayList;
import java.util.List;

public class Autor extends Pessoa {
    private String nacionalidade;
    private boolean isUsuario;
    private PublicavelInterface estrategiaPublicacao;

    public Autor(String nome, Livro[] livros, String nacionalidade, boolean isUsuario) {
        super(nome, livros);
        this.nacionalidade = nacionalidade;
        this.isUsuario = isUsuario;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public boolean isUsuario() {
        return isUsuario;
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

    public void setEstrategiaPublicacao(PublicavelInterface estrategiaPublicacao) {
        this.estrategiaPublicacao = estrategiaPublicacao;
    }

    public void publicar() {
        if (estrategiaPublicacao != null) {
            estrategiaPublicacao.publicar();
        } else {
            System.out.println("Nenhuma estratégia de publicação definida.");
        }
    }
}