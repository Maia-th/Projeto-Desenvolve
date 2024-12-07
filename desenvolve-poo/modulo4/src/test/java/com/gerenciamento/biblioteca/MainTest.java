package com.gerenciamento.biblioteca;

import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import static org.junit.Assert.*;

public class MainTest {

    @Test
    public void testMain() {
        // Redireciona a saída do console para um ByteArrayOutputStream
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        // Executa o método main
        Main.main(new String[]{});

        // Verifica a saída do console
        String actualOutput = outContent.toString();

        // Verifica se a saída contém as informações esperadas
        assertTrue(actualOutput.contains("Livro: Java for Beginners"));
        assertTrue(actualOutput.contains("Autor: Jessica Felix"));
        assertTrue(actualOutput.contains("Genero: Tecnologia"));
        assertTrue(actualOutput.contains("Usuario: Lucas Rafael"));
        assertTrue(actualOutput.contains("Idade: 25"));
        assertTrue(actualOutput.contains("Data de Retirada:"));
        assertTrue(actualOutput.contains("Data de Devolucao:"));

        // Restaura a saída do console
        System.setOut(originalOut);
    }
}