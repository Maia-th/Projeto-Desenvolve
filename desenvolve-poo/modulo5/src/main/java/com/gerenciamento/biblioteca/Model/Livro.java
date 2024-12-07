package com.gerenciamento.biblioteca.Model;

public class Livro {
    private String titulo;
    private Autor autor;
    private String genero;
    private boolean disponivel;

    public Livro(String titulo, Autor autor, String genero) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.disponivel = true;
    }

    public String getTitulo() {
        return titulo;
    }

    public Autor getAutor() {
        return autor;
    }

    public String getGenero() {
        return genero;
    } 

    public Boolean isDisponivel () {
        return disponivel;
    }

    public void setDisponivel(Boolean disponivel) {
        this.disponivel = disponivel;
    }

    public void validarEmprestimo() {
        if (disponivel) {
            System.out.println("Livro disponivel para emprestimo.");
        } else {
            System.out.println("O livro nao esta disponivel");
        }
    }
}
