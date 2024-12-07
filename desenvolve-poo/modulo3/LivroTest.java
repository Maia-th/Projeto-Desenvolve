import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LivroTest {

    @Test
    public void testLivroCriadoComSucesso() {
        Autor autor = new Autor("Autor");
        Livro livro = new Livro("Titulo", autor, "Genero");

        assertEquals("Titulo", livro.getTitulo());
        assertEquals(autor, livro.getAutor());
        assertEquals("Genero", livro.getGenero());
        assertTrue(livro.isDisponivel());
    }

    @Test
    public void testSetDisponivel() {
        Livro livro = new Livro("Titulo", new Autor("Autor"), "Genero");
        livro.setDisponivel(false);

        assertFalse(livro.isDisponivel());
    }

    @Test
    public void testValidarEmprestimo() {
        Livro livro = new Livro("Titulo", new Autor("Autor"), "Genero");
        livro.validarEmprestimo(); // Deve imprimir "Livro disponivel para emprestimo."

        livro.setDisponivel(false);
        livro.validarEmprestimo(); // Deve imprimir "O livro nao esta disponivel"
    }
}