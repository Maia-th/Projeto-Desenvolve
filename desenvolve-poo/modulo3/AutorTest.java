import org.junit.Test;
import static org.junit.Assert.*;

public class AutorTest {

    @Test
    public void testGetNacionalidade() {
        LivroTest[] livros = new LivroTest[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertEquals("Brasileiro", autor.getNacionalidade());
    }

    @Test
    public void testGetObrasPublicadas() {
        LivroTest[] livros = new LivroTest[2];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertArrayEquals(livros, autor.getObrasPublicadas());
    }

    @Test
    public void testSetLivros() {
        LivroTest[] livros1 = new LivroTest[2];
        LivroTest[] livros2 = new LivroTest[3];
        Autor autor = new Autor("João", livros1, "Brasileiro");
        autor.setLivros(livros2);
        assertArrayEquals(livros2, autor.getObrasPublicadas());
    }

    @Test
    public void testGetNome() {
        LivroTest[] livros = new LivroTest[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertEquals("João", autor.getNome());
    }

    @Test
    public void testSetNome() {
        LivroTest[] livros = new LivroTest[0];
        Autor autor = new Autor("João", livros, "Brasileiro");
        autor.setNome("Maria");
        assertEquals("Maria", autor.getNome());
    }

    @Test
    public void testGetLivros() {
        LivroTest[] livros = new LivroTest[2];
        Autor autor = new Autor("João", livros, "Brasileiro");
        assertArrayEquals(livros, autor.getLivros());
    }

    @Test
    public void testSetLivrosFromPessoa() {
        LivroTest[] livros1 = new LivroTest[2];
        LivroTest[] livros2 = new LivroTest[3];
        Autor autor = new Autor("João", livros1, "Brasileiro");
        autor.setLivros(livros2);
        assertArrayEquals(livros2, autor.getLivros());
    }
}