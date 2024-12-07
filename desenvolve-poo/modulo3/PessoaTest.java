import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PessoaTest {

    @Test
    public void testPessoaCriadaComSucesso() {
        Livro livro = new Livro("Titulo", new Autor("Autor"), "Genero");
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
        Livro livro = new Livro("Titulo", new Autor("Autor"), "Genero");
        Livro[] livros = {livro};
        pessoa.setLivros(livros);

        assertArrayEquals(livros, pessoa.getLivros());
    }
}