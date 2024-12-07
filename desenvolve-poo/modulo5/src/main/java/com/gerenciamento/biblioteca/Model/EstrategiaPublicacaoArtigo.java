package main.java.com.gerenciamento.biblioteca.Model;

import main.java.com.gerenciamento.biblioteca.Interface.PublicavelInterface;

public class EstrategiaPublicacaoArtigo implements PublicavelInterface {
    private Artigo artigo;

    public EstrategiaPublicacaoArtigo(Artigo artigo) {
        this.artigo = artigo;
    }

    @Override
    public void publicar() {
        System.out.println("Publicando artigo: " + artigo.getTitulo());
    }
}