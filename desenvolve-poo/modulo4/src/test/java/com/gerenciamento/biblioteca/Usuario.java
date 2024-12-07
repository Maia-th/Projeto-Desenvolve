package com.gerenciamento.biblioteca;

import com.gerenciamento.biblioteca.Model.Livro;
import com.gerenciamento.biblioteca.Model.Emprestimo;

public class Usuario extends Pessoa {
    private int idade;
    private Emprestimo[] historicoEmprestimos;

    public Usuario(String nome, Livro[] livros, int idade, Emprestimo[] historicoEmprestimos) {
        super(nome, livros);
        this.idade = idade;
        this.historicoEmprestimos = historicoEmprestimos;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public Emprestimo[] getHistoricoEmprestimos() {
        return historicoEmprestimos;
    }

    public void setHistoricoEmprestimos(Emprestimo[] historicoEmprestimos) {
        this.historicoEmprestimos = historicoEmprestimos;
    }
}
