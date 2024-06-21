import csv

# Dicionário global para armazenar usuários
usuarios = {}

# Lista global para armazenar produtos e serviços
produtos_servicos = []

def carregar_usuarios():
    """
    Carrega os usuários do arquivo 'usuarios.csv' para o dicionário global 'usuarios'.
    """
    global usuarios
    try:
        with open('usuarios.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios[row['username']] = {
                    'password': row['password'],
                    'role': row['role']
                }
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Criando novo arquivo.")
        with open('usuarios.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'role'])

def salvar_usuarios():
    """
    Salva os usuários do dicionário global 'usuarios' no arquivo 'usuarios.csv'.
    """
    with open('usuarios.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password', 'role'])
        for username, info in usuarios.items():
            writer.writerow([username, info['password'], info['role']])

def adicionar_usuario(username, password, role):
    """
    Adiciona um novo usuário ao dicionário global 'usuarios' e salva no arquivo.
    Entradas:
    - username (str): Nome de usuário
    - password (str): Senha do usuário
    - role (str): Papel/função do usuário
    """
    if username in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[username] = {'password': password, 'role': role}
        salvar_usuarios()

def listar_usuarios():
    """
    Lista todos os usuários presentes no dicionário global 'usuarios'.
    """
    for username, info in usuarios.items():
        print(f"Usuário: {username}, Role: {info['role']}")

def atualizar_usuario(username, password=None, role=None):
    """
    Atualiza as informações de um usuário existente no dicionário global 'usuarios'.
    Entradas:
    - username (str): Nome de usuário
    - password (str, opcional): Nova senha do usuário
    - role (str, opcional): Novo papel/função do usuário
    """
    if username in usuarios:
        if password:
            usuarios[username]['password'] = password
        if role:
            usuarios[username]['role'] = role
        salvar_usuarios()
    else:
        print("Usuário não encontrado.")

def remover_usuario(username):
    """
    Remove um usuário do dicionário global 'usuarios' e salva a alteração no arquivo.
    Entradas:
    - username (str): Nome de usuário
    """
    if username in usuarios:
        del usuarios[username]
        salvar_usuarios()
    else:
        print("Usuário não encontrado.")

def carregar_produtos_servicos():
    """
    Carrega os produtos e serviços do arquivo 'produtos_servicos.csv' para a lista global 'produtos_servicos'.
    """
    global produtos_servicos
    try:
        with open('produtos_servicos.csv', 'r') as file:
            reader = csv.DictReader(file)
            produtos_servicos = list(reader)
    except FileNotFoundError:
        print("Arquivo de produtos/serviços não encontrado. Criando novo arquivo.")
        with open('produtos_servicos.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['nome', 'tipo', 'preco', 'quantidade'])

def salvar_produtos_servicos():
    """
    Salva os produtos e serviços da lista global 'produtos_servicos' no arquivo 'produtos_servicos.csv'.
    """
    with open('produtos_servicos.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'tipo', 'preco', 'quantidade'])
        for produto in produtos_servicos:
            writer.writerow([produto['nome'], produto['tipo'], produto['preco'], produto['quantidade']])

def adicionar_produto_servico(nome, tipo, preco, quantidade):
    """
    Adiciona um novo produto ou serviço à lista global 'produtos_servicos' e salva no arquivo.
    Entradas:
    - nome (str): Nome do produto/serviço
    - tipo (str): Tipo do produto/serviço
    - preco (str): Preço do produto/serviço
    - quantidade (str): Quantidade disponível do produto/serviço
    """
    produtos_servicos.append({'nome': nome, 'tipo': tipo, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos_servicos()

def listar_produtos_servicos():
    """
    Lista todos os produtos e serviços presentes na lista global 'produtos_servicos'.
    """
    for produto in produtos_servicos:
        print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def atualizar_produto_servico(nome, tipo=None, preco=None, quantidade=None):
    """
    Atualiza as informações de um produto ou serviço existente na lista global 'produtos_servicos'.
    Entradas:
    - nome (str): Nome do produto/serviço
    - tipo (str, opcional): Novo tipo do produto/serviço
    - preco (str, opcional): Novo preço do produto/serviço
    - quantidade (str, opcional): Nova quantidade do produto/serviço
    """
    for produto in produtos_servicos:
        if produto['nome'] == nome:
            if tipo:
                produto['tipo'] = tipo
            if preco:
                produto['preco'] = preco
            if quantidade:
                produto['quantidade'] = quantidade
            salvar_produtos_servicos()
            return
    print("Produto/Serviço não encontrado.")

def remover_produto_servico(nome):
    """
    Remove um produto ou serviço da lista global 'produtos_servicos' e salva a alteração no arquivo.
    Entradas:
    - nome (str): Nome do produto/serviço
    """
    global produtos_servicos
    produtos_servicos = [produto for produto in produtos_servicos if produto['nome'] != nome]
    salvar_produtos_servicos()

def buscar_produto_servico(nome):
    """
    Busca um produto ou serviço na lista global 'produtos_servicos' e exibe suas informações.
    Entradas:
    - nome (str): Nome do produto/serviço
    """
    for produto in produtos_servicos:
        if produto['nome'] == nome:
            print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            return
    print("Produto/Serviço não encontrado.")

def ordenar_produtos_servicos_por_nome():
    """
    Ordena os produtos e serviços pelo nome e exibe a lista ordenada.
    """
    produtos_ordenados = sorted(produtos_servicos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def ordenar_produtos_servicos_por_preco():
    """
    Ordena os produtos e serviços pelo preço e exibe a lista ordenada.
    """
    produtos_ordenados = sorted(produtos_servicos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def main():
    """
    Função principal que gerencia o fluxo do sistema de gerenciamento.
    """
    carregar_usuarios()
    carregar_produtos_servicos()
    
    while True:
        print("\nSistema de Gerenciamento")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos/Serviços")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            while True:
                print("\nGerenciamento de Usuários")
                print("1. Adicionar Usuário")
                print("2. Listar Usuários")
                print("3. Atualizar Usuário")
                print("4. Remover Usuário")
                print("0. Voltar")
                opcao_usuario = input("Escolha uma opção: ")
                
                if opcao_usuario == "1":
                    username = input("Username: ")
                    password = input("Password: ")
                    role = input("Role: ")
                    adicionar_usuario(username, password, role)
                elif opcao_usuario == "2":
                    listar_usuarios()
                elif opcao_usuario == "3":
                    username = input("Username: ")
                    password = input("Novo Password (deixe em branco para não alterar): ")
                    role = input("Novo Role (deixe em branco para não alterar): ")
                    atualizar_usuario(username, password if password else None, role if role else None)
                elif opcao_usuario == "4":
                    username = input("Username: ")
                    remover_usuario(username)
                elif opcao_usuario == "0":
                    break
                else:
                    print("Opção inválida.")

        elif opcao == "2":
            while True:
                print("\nGerenciamento de Produtos/Serviços")
                print("1. Adicionar Produto/Serviço")
                print("2. Listar Produtos/Serviços")
                print("3. Atualizar Produto/Serviço")
                print("4. Remover Produto/Serviço")
                print("5. Buscar Produto/Serviço")
                print("6. Ordenar Produtos/Serviços por Nome")
                print("7. Ordenar Produtos/Serviços por Preço")
                print("0. Voltar")
                opcao_produto = input("Escolha uma opção: ")
                
                if opcao_produto == "1":
                    nome = input("Nome: ")
                    tipo = input("Tipo: ")
                    preco = input("Preço: ")
                    quantidade = input("Quantidade: ")
                    adicionar_produto_servico(nome, tipo, preco, quantidade)
                elif opcao_produto == "2":
                    listar_produtos_servicos()
                elif opcao_produto == "3":
                    nome = input("Nome: ")
                    tipo = input("Novo Tipo (deixe em branco para não alterar): ")
                    preco = input("Novo Preço (deixe em branco para não alterar): ")
                    quantidade = input("Nova Quantidade (deixe em branco para não alterar): ")
                    atualizar_produto_servico(nome, tipo if tipo else None, preco if preco else None, quantidade if quantidade else None)
                elif opcao_produto == "4":
                    nome = input("Nome: ")
                    remover_produto_servico(nome)
                elif opcao_produto == "5":
                    nome = input("Nome: ")
                    buscar_produto_servico(nome)
                elif opcao_produto == "6":
                    ordenar_produtos_servicos_por_nome()
                elif opcao_produto == "7":
                    ordenar_produtos_servicos_por_preco()
                elif opcao_produto == "0":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
