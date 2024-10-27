package com.gerenciamento.biblioteca;
import org.junit.Test;
import static org.junit.Assert.*;

public class AutorTest {

    @Test
    public void testGetNacionalidade() {
        Livro[] livros = new Livro[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertEquals("Brasileiro", autor.getNacionalidade());
    }

    @Test
    public void testGetObrasPublicadas() {
        Livro[] livros = new Livro[2];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertArrayEquals(livros, autor.getObrasPublicadas());
    }

    @Test
    public void testSetLivros() {
        Livro[] livros1 = new Livro[2];
        Livro[] livros2 = new Livro[3];
        Autor autor = new Autor("João", livros1, "Brasileiro");
        autor.setLivros(livros2);
        assertArrayEquals(livros2, autor.getObrasPublicadas());
    }

    @Test
    public void testGetNome() {
        Livro[] livros = new Livro[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertEquals("João", autor.getNome());
    }

    @Test
    public void testSetNome() {
        Livro[] livros = new Livro[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        autor.setNome("Maria");
        assertEquals("Maria", autor.getNome());
    }

    @Test
    public void testGetLivros() {
        Livro[] livros = new Livro[2];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertArrayEquals(livros, autor.getLivros());
    }

    @Test
    public void testSetLivrosFromPessoa() {
        Livro[] livros1 = new Livro[2];
        Livro[] livros2 = new Livro[3];
        Autor autor = new Autor("João", livros1, "Brasileiro");
        autor.setLivros(livros2);
        assertArrayEquals(livros2, autor.getLivros());
    }
}