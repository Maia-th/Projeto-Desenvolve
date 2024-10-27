package com.gerenciamento.biblioteca;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor("Jessica Felix", new Livro[1], "Brasileira");

        Livro livro = new Livro("Java for Beginners", autor, "Tecnologia");
        Livro[] livros = { livro };
        
        autor.setLivros(livros);

        Usuario usuario = new Usuario("Lucas Rafael", new Livro[0], 25, new Emprestimo[1]);
        
        Emprestimo emprestimo = new Emprestimo(new Date(), new Date(), livro, usuario);
        Emprestimo[] emprestimos = { emprestimo };

        usuario.setHistoricoEmprestimos(emprestimos);

        livro.validarEmprestimo();
        System.out.println("Livro: " + livro.getTitulo());
        System.out.println("Autor: " + livro.getAutor().getNome());
        System.out.println("Genero: " + livro.getGenero());
        System.out.println("Usuario: " + usuario.getNome());
        System.out.println("Idade: " + usuario.getIdade());
        System.out.println("Data de Retirada: " + emprestimo.getDataRetirada());
        System.out.println("Data de Devolucao: " + emprestimo.getDataDevolucao());
    }
}