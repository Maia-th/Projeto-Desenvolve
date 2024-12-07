package com.gerenciamento.biblioteca;

import org.junit.Test;
import static org.junit.Assert.*;
import com.gerenciamento.biblioteca.Model.Autor;
import com.gerenciamento.biblioteca.Model.Livro;
import com.gerenciamento.biblioteca.Model.Usuario;
import com.gerenciamento.biblioteca.Model.Emprestimo;
import java.util.Date;

public class EmprestimoTest {

    @Test
    public void testEmprestimoCriadoComSucesso() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero");
        Usuario usuario = new Usuario("Usuario", new Livro[]{}, 25, new Emprestimo[]{});
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date(dataRetirada.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 dias depois

        Emprestimo emprestimo = new Emprestimo(dataRetirada, dataDevolucao, livro, usuario);

        assertEquals(dataRetirada, emprestimo.getDataRetirada());
        assertEquals(dataDevolucao, emprestimo.getDataDevolucao());
        assertEquals(livro, emprestimo.getLivro());
        assertEquals(usuario, emprestimo.getUsuario());
        assertFalse(livro.isDisponivel());
    }

    @Test
    public void testEmprestimoLivroIndisponivel() {
        Livro livro = new Livro("Titulo", new Autor("Autor", new Livro[0], "Nacionalidade",false), "Genero");
        livro.setDisponivel(false);
        Usuario usuario = new Usuario("Usuario", new Livro[]{}, 25, new Emprestimo[]{});
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date(dataRetirada.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 dias depois

        Emprestimo emprestimo = new Emprestimo(dataRetirada, dataDevolucao, livro, usuario);

        assertNull(emprestimo.getDataRetirada());
        assertNull(emprestimo.getDataDevolucao());
        assertNull(emprestimo.getLivro());
        assertNull(emprestimo.getUsuario());
    }
}