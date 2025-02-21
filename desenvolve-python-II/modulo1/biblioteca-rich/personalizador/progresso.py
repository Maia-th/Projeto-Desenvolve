from rich.console import Console
from rich.progress import Progress

console = Console()

def mostrar_barra_progresso(texto: str, isArquivo: bool) -> None:
    """
    Exibe uma barra de progresso com texto.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    with Progress() as progress:
        task = progress.add_task("[green]Processando...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
        console.print(texto)

def mostrar_spinner(texto: str, isArquivo: bool) -> None:
    """
    Exibe um spinner com texto.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    with console.status("[bold green]Carregando...") as status:
        console.print(texto)