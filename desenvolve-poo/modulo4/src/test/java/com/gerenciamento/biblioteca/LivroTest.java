package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Autor;
import com.gerenciamento.biblioteca.Model.Livro;

public class LivroTest {

    @Test
    public void testLivroCriadoComSucesso() {
        Autor autor = new Autor("Autor", new Livro[0], "Nacionalidade");
        Livro livro = new Livro("Titulo", autor, "Genero");

        assertEquals("Titulo", livro.getTitulo());
        assertEquals(autor, livro.getAutor());
        assertEquals("Genero", livro.getGenero());
        assertTrue(livro.isDisponivel());
    }

    @Test
    public void testSetDisponivel() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade"), "Genero");
        livro.setDisponivel(false);

        assertFalse(livro.isDisponivel());
    }

    @Test
    public void testValidarEmprestimo() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade"), "Genero");
        livro.validarEmprestimo(); // Deve imprimir "Livro disponivel para emprestimo."

        livro.setDisponivel(false);
        livro.validarEmprestimo(); // Deve imprimir "O livro nao esta disponivel"
    }
}