from rich.console import Console
from rich.layout import Layout

console = Console()

def mostrar_layout_basico(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto usando um layout básico.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["header"].update("[bold magenta]Cabeçalho[/bold magenta]")
    layout["main"].update(texto)
    layout["footer"].update("[bold magenta]Rodapé[/bold magenta]")
    console.print(layout)

def mostrar_layout_colunas(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto usando um layout de colunas.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    layout = Layout()
    layout.split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    layout["left"].update(texto)
    layout["right"].update("[bold magenta]Painel Direito[/bold magenta]")
    console.print(layout)