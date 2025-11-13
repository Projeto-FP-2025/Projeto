import os
from datetime import datetime

print("[1] Adicionar um novo evento")
print("[2] Visualizar um evento")
print("[3] Editar um evento")
print("[4] Excluir um evento")

print("="*20)
opc = int(input("digite uma opção: "))
print("="*20)

if opc == 1:
    nome_do_arquivo = input("Digite o nome do arquivo(colocar .txt): ")
    with open(nome_do_arquivo, 'a',encoding='utf8') as arquivo:
        tipo = input("Digite o tipo do evento: ")
        arquivo.write(tipo + '\n')

        data = input("Digite a data do evento (dd/mm/aaaa): ")
        arquivo.write(data + '\n')

        local = (input("Digite o local do evento: "))
        arquivo.write(local + '\n')

        orcamento = input("Digite o orçamento do evento: ")
        arquivo.write(orcamento + '\n')

    print("evento cadastrada com sucesso!")

elif opc == 2:
    nome_do_arquivo = input("Qual arquivo vc quer visualizar: ")
    try:
        with open(nome_do_arquivo,'r',encoding='utf8') as arquivo:
            tipo = arquivo.readline().strip()
            data = arquivo.readline().strip()
            local = arquivo.readline().strip()
            orcamento = arquivo.readline().split()

            print(f"Tipo de Evento: {tipo}")
            print(f"Data do Evento: {data}")
            print(f"Local do Evento: {local}")
            print(f"Orçamento do Evento: {orcamento}")

            from datetime import date

            dia,mes,ano = map(int,data.split("/"))
            dia_do_evento = date(ano,mes,dia)

            hoje = date.today()

            restam = (dia_do_evento - hoje).days
        with open (nome_do_arquivo,'a',encoding='utf8') as arquivo:
            if restam > 0:
                print(f"Faltam {restam} dias para o evento")
                arquivo.write(f"Faltam {restam} dias para o evento")

            elif restam == 0:
                print(f"O evento é Hoje")
                arquivo.write(f"O evento é Hoje")
            
            else:
                print(f"O evento ja passou há {-restam} dias")
                arquivo.write(f"O evento ja passou há {-restam} dias")

    except FileNotFoundError:
        print("arquivo não encontrado.")

elif opc == 3:
    nome_do_arquivo = input("Qual arquivo vc quer editar: ")
    try:
        with open(nome_do_arquivo, 'a',encoding='utf8') as arquivo:
            tipo = input("Digite o tipo do evento: ")
            arquivo.write(tipo)

            data = input("Digite a data do evento (dd/mm/aaaa): ")
            arquivo.write(data)

            local = (input("Digite o local do evento: "))
            arquivo.write(local)

            orcamento = input("Digite o orçamento do evento: ")
            arquivo.write(orcamento)

            print("Arquivo editado")
    except FileNotFoundError:
        print("Arquivo nao existe")

elif opc == 4:
    nome_do_arquivo = input("Digite o nome do arquivo que deseja apagar: ")
    os.remove(nome_do_arquivo)
    print("Arquivo excluido com sucesso!")
    
    #if para caso n encontre o arquivo


elif opc == 5:
    nome_de_arquivo = input("Informe o nome da festa que voce quer adicionar um item:")
    try:
        with open(nome_de_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        for i, linha in enumerate(linhas):    #enumerate vai guardar a linha em que o orcamento esta para uso futuro
            if linha.startswith("Orçamento:"):
                orcamento_atual = float(linha.split(":")[1].strip())  #split vai dividar o ORCAMENTO e o VALOR e o strip tira espacos em branco
                indice_orcamento = i
                break
        else:
            print("Voce nao tem orcamento restante.")
            exit()
        
        item = input("Digite o nome do item")
        valor = float(input("Digite o custo do item"))

        novo_orcamento = orcamento_atual - valor
        linhas[indice_orcamento] = f"Orcamento: {novo_orcamento}\n"

        linhas.append(f"- {item}: R$ {valor}\n")

        with open(nome_de_arquivo, "w") as arquivo:
            arquivo.writelines(linhas)

        print(f"Item {item} adicionado com sucesso! Novo orcamento: R${novo_orcamento:.2f}")

    except FileNotFoundError:
        print("Nao foi possivel encontrar o arquivo.")
else:
    print("Opca invalida.")