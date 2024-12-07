package test.java.com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import main.java.com.gerenciamento.biblioteca.Model.*;
import main.java.com.gerenciamento.biblioteca.Interface.PublicavelInterface;

public class EstrategiaPublicacaoTest {

    @Test
    public void testPublicacaoLivro() {
        Autor autor = new Autor("Jessica Felix", new Livro[0], "Brasileira", false);
        Livro livro = new Livro("Java for Beginners", autor, "Tecnologia");
        EstrategiaPublicacaoLivro estrategiaLivro = new EstrategiaPublicacaoLivro(livro);

        autor.setEstrategiaPublicacao(estrategiaLivro);
        autor.publicar(); // Deve imprimir "Publicando livro: Java for Beginners"
    }

    @Test
    public void testPublicacaoArtigo() {
        Autor autor = new Autor("Jessica Felix", new Livro[0], "Brasileira", false);
        Artigo artigo = new Artigo("Entendendo Compiladores", autor, "tecnologia", true);
        EstrategiaPublicacaoArtigo estrategiaArtigo = new EstrategiaPublicacaoArtigo(artigo);

        autor.setEstrategiaPublicacao(estrategiaArtigo);
        autor.publicar(); // Deve imprimir "Publicando artigo: Entendendo Compiladores"
    }
}