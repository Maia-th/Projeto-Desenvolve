import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Date;

public class EmprestimoTest {

    @Test
    public void testEmprestimoCriadoComSucesso() {
        LivroTest livro = new LivroTest("Titulo", new Autor("Autor"), "Genero");
        UsuarioTest usuario = new UsuarioTest("Usuario", new LivroTest[]{}, 25, new Emprestimo[]{});
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
        LivroTest livro = new LivroTest("Titulo", new Autor("Autor"), "Genero");
        livro.setDisponivel(false);
        UsuarioTest usuario = new UsuarioTest("Usuario", new LivroTest[]{}, 25, new Emprestimo[]{});
        Date dataRetirada = new Date();
        Date dataDevolucao = new Date(dataRetirada.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 dias depois

        Emprestimo emprestimo = new Emprestimo(dataRetirada, dataDevolucao, livro, usuario);

        assertNull(emprestimo.getDataRetirada());
        assertNull(emprestimo.getDataDevolucao());
        assertNull(emprestimo.getLivro());
        assertNull(emprestimo.getUsuario());
    }
}