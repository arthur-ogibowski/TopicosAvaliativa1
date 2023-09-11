'''
Banco de dados de usuarios com menu, cadastro e impressao, usando funcoes e dicionarios.
'''

import json

# Dicionário para guardar usuários
banco_usuarios = []

'''
Para cadastrar usuarios, usamos um loop para solicitar os dados dos campos,
e um loop infinito para solicitar os dados dos campos opcionais até que o usuário digite "sair".
'''
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}

    # Solicitando dados para os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    # Solicitando dados para campos opcionais até que o usuário digite "sair"
    while True:
        campo = input("Digite um campo ou 'sair' para encerrar: ")
        if campo.lower() == 'sair':
            break
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    banco_usuarios.append(usuario)
    print("Usuário cadastrado.")

'''
Para imprimir usuários, temos im menu com 4 opções: imprimir todos, filtrar por nomes, filtrar por campos e filtrar por nomes e campos.
Caso o usuário escolha a opção 2 ou 4, usamos o *args para receber os nomes dos usuários a serem filtrados.
Caso o usuário escolha a opção 3 ou 4, usamos o **kwargs para receber os campos e valores a serem filtrados.
'''
def imprimir_usuarios(*args, **kwargs):
    opcao = int(input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n"))

    if opcao == 1:
        for usuario in banco_usuarios:
            print(json.dumps(usuario, indent=4))
    elif opcao == 2:
        nomes = args
        for usuario in banco_usuarios:
            if usuario.get("nome") in nomes:
                printjson.dumps(usuario, indent=4))
    elif opcao == 3:
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(json.dumps(usuario, indent=4))
    elif opcao == 4:
        nomes = args
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if usuario.get("nome") in nomes and all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(json.dumps(usuario, indent=4))
    else:
        print("Opção inválida.")

'''
A função principal é onde inicializamos os campos obrigatórios e chamamos o menu.
'''
def main():
    campos_obrigatorios = input("Digite os nomes dos campos separados por vírgula: ").split(",")
    
    while True:
        print("\nMenu:")
        print("1: Cadastrar usuário")
        print("2: Imprimir usuários")
        print("0: Encerrar")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == "2":
            imprimir_usuarios()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
