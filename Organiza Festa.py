import os

print("[1] Adicionar uma nova festa")
print("[2] Visualizar uma festa")
print("[3] Editar uma festa")
print("[4] Excluir uma festa")

print("="*10)
opc = int(input("digite uma opção: "))
print("="*10)

if opc == 1:
    nome_de_arquivo = input("Digite o nome do arquivo(colocar .txt): ")
    with open(nome_de_arquivo, 'w',encoding='utf8') as arquivo:
        tipo = input("Digite o tipo de festa: ")
        arquivo.write(tipo)

        data = input("Digite a data da festa: ")
        arquivo.write(data)

        local = (input("Digite o local da festa: "))
        arquivo.write(local)

        orcamento = input("Digite o orçamento da festa: ")
        arquivo.write(orcamento)

    print("Festa cadastrada com sucesso!")

elif opc == 2:
    nome_de_arquivo = input("Qual arquivo vc quer visualizar: ")
    try:
        with open(nome_de_arquivo,'r',encoding='utf8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("arquivo não encontrado.")

elif opc == 3:
    nome_de_arquivo = input("Qual arquivo vc quer editar: ")
    try:
        with open(nome_de_arquivo, 'w',encoding='utf8') as arquivo:
            tipo = input("Digite o tipo de festa: ")
            arquivo.write(tipo)

            data = input("Digite a data da festa: ")
            arquivo.write(data)

            local = (input("Digite o local da festa: "))
            arquivo.write(local)

            orcamento = input("Digite o orçamento da festa: ")
            arquivo.write(orcamento)

    except FileNotFoundError:
        print("Arquivo nao existe")

elif opc == 4:
    nome_de_arquivo = input("Digite o nome do arquivo que deseja apagar: ")
    os.remove(nome_de_arquivo)
    print("Arquivo excluido com sucesso!")

else:
    print("Arquivo nao encontrado")