package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Livro;
import com.gerenciamento.biblioteca.Model.Usuario;
import com.gerenciamento.biblioteca.Model.Emprestimo;
import com.gerenciamento.biblioteca.Model.Autor;
import java.util.Date;

public class UsuarioTest {

    @Test
    public void testUsuarioCriadoComSucesso() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero");
        Livro[] livros = {livro};
        Emprestimo[] historico = {};
        Usuario usuario = new Usuario("Nome", livros, 25, historico);

        assertEquals("Nome", usuario.getNome());
        assertArrayEquals(livros, usuario.getLivros());
        assertEquals(25, usuario.getIdade());
        assertArrayEquals(historico, usuario.getHistoricoEmprestimos());
    }

    @Test
    public void testSetIdade() {
        Usuario usuario = new Usuario("Nome", new Livro[]{}, 25, new Emprestimo[]{});
        usuario.setIdade(30);

        assertEquals(30, usuario.getIdade());
    }

    @Test
    public void testSetHistoricoEmprestimos() {
        Usuario usuario = new Usuario("Nome", new Livro[]{}, 25, new Emprestimo[]{});
        Emprestimo emprestimo = new Emprestimo(new Date(), new Date(), new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero"), usuario);
        Emprestimo[] historico = {emprestimo};
        usuario.setHistoricoEmprestimos(historico);

        assertArrayEquals(historico, usuario.getHistoricoEmprestimos());
    }
}