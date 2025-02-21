from rich.console import Console
from rich.panel import Panel

console = Console()

def mostrar_painel_basico(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto dentro de um painel básico.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    painel = Panel(texto)
    console.print(painel)

def mostrar_painel_fancy(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto dentro de um painel estilizado com bordas e título.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    painel = Panel(texto, title="Painel Estilizado", border_style="bold magenta")
    console.print(painel)