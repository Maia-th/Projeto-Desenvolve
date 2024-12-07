package main.java.com.gerenciamento.biblioteca.Model;

import main.java.com.gerenciamento.biblioteca.Interface.PublicavelInterface;

public class EstrategiaPublicacaoLivro implements PublicavelInterface {
    private Livro livro;

    public EstrategiaPublicacaoLivro(Livro livro) {
        this.livro = livro;
    }

    @Override
    public void publicar() {
        System.out.println("Publicando livro: " + livro.getTitulo());
    }
}