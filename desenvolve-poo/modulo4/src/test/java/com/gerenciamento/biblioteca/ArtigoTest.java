package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Artigo;
import com.gerenciamento.biblioteca.Model.Autor;
import com.gerenciamento.biblioteca.Model.Livro;

public class ArtigoTest {

    @Test
    public void testArtigoCriadoComSucesso() {
        Autor autor = new Autor("Jessica Felix", new Livro[0], "Brasileira", false);
        Artigo artigo = new Artigo("Entendendo Compiladores", autor, "tecnologia", true);

        assertEquals("Entendendo Compiladores", artigo.getTitulo());
        assertEquals(autor, artigo.getAutor());
        assertEquals("tecnologia", artigo.getGenero());
        assertTrue(artigo.isPublicado());
    }
}