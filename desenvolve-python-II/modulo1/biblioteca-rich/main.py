import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Formate texto usando a biblioteca rich.")
    parser.add_argument("texto", help="Texto ou caminho do arquivo a ser formatado.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o texto é um caminho de arquivo.")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Módulo a ser usado para formatação.")
    parser.add_argument("-f", "--funcao", choices=["mostrar_layout_basico", "mostrar_layout_colunas", "mostrar_painel_basico", "mostrar_painel_fancy", "mostrar_barra_progresso", "mostrar_spinner", "mostrar_texto_negrito", "mostrar_texto_italico"], required=True, help="Função a ser usada para formatação.")
    
    args = parser.parse_args()
    
    modulo = globals()[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()