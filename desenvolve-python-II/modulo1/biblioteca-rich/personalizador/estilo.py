from rich.console import Console

console = Console()

def mostrar_texto_negrito(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto em estilo negrito.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    console.print(f"[bold]{texto}[/bold]")

def mostrar_texto_italico(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto em estilo itálico.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    console.print(f"[italic]{texto}[/italic]")