package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Autor;
import com.gerenciamento.biblioteca.Model.Livro;

public class AutorTest {

    @Test
    public void testAutorCriadoComSucesso() {
        Livro livro = new Livro("Titulo", null, "Genero");
        Livro[] livros = {livro};
        Autor autor = new Autor("Nome", livros, "Nacionalidade");

        assertEquals("Nome", autor.getNome());
        assertArrayEquals(livros, autor.getLivros());
        assertEquals("Nacionalidade", autor.getNacionalidade());
    }

    @Test
    public void testSetNome() {
        Autor autor = new Autor("Nome", new Livro[]{}, "Nacionalidade");
        autor.setNome("Novo Nome");

        assertEquals("Novo Nome", autor.getNome());
    }

    @Test
    public void testSetLivros() {
        Autor autor = new Autor("Nome", new Livro[]{}, "Nacionalidade");
        Livro livro = new Livro("Titulo", autor, "Genero");
        Livro[] livros = {livro};
        autor.setLivros(livros);

        assertArrayEquals(livros, autor.getLivros());
    }

    @Test
    public void testGetObrasPublicadasPorGeneros() {
        Livro livro1 = new Livro("Titulo1", null, "Genero1");
        Livro livro2 = new Livro("Titulo2", null, "Genero2");
        Livro livro3 = new Livro("Titulo3", null, "Genero1");
        Livro[] livros = {livro1, livro2, livro3};
        Autor autor = new Autor("Nome", livros, "Nacionalidade");

        Livro[] obrasPorGenero = autor.getObrasPublicadasPorGeneros("Genero1");

        assertEquals(2, obrasPorGenero.length);
        assertEquals(livro1, obrasPorGenero[0]);
        assertEquals(livro3, obrasPorGenero[1]);
    }
}