package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Livro;
import com.gerenciamento.biblioteca.Model.Pessoa;
import com.gerenciamento.biblioteca.Model.Autor;

public class PessoaTest {

    @Test
    public void testPessoaCriadaComSucesso() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero");
        Livro[] livros = {livro};
        Pessoa pessoa = new Pessoa("Nome", livros);

        assertEquals("Nome", pessoa.getNome());
        assertArrayEquals(livros, pessoa.getLivros());
    }

    @Test
    public void testSetNome() {
        Pessoa pessoa = new Pessoa("Nome", new Livro[]{});
        pessoa.setNome("Novo Nome");

        assertEquals("Novo Nome", pessoa.getNome());
    }

    @Test
    public void testSetLivros() {
        Pessoa pessoa = new Pessoa("Nome", new Livro[]{});
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero");
        Livro[] livros = {livro};
        pessoa.setLivros(livros);

        assertArrayEquals(livros, pessoa.getLivros());
    }
}