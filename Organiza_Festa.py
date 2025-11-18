def sugestao(tipo_de_evento,num_de_convidados):
    orcamento_total = 0

    sugestoes = f"\n=-=-=-= Sugestões para {tipo} =-=-=-=\n"

    if tipo_de_evento == "casamento":

        preco_por_pessoa = 70
        total_do_buffet = preco_por_pessoa * num_de_convidados
        sugestoes += f"\nBuffet para casamanto R${preco_por_pessoa} por pessoa"
        sugestoes += f"\nTotal do buffet para {num_de_convidados} convidados: R${total_do_buffet}"

        sugestoes += "\nCARDÁPIO:\nMassa: Fettuccine, Penne, Raviole\nProteína: Carne, Peixe, Ave\nSobremessas: Petit gateau, Crème Brûlée, Macaron"
        orcamento_total += total_do_buffet
        
        
        sugestoes += "\nDecoração: flores (cor à sua preferencia), iluminação suave, velas, serviço à americana e uma mesa para os familiares dos noivos"
        orcamento_total += 4000

        sugestoes += "\nCabine de fotos, Um Violinista (Para a Cerimônia), Banda ao vivo e DJ (Para a Festa)"
        orcamento_total += 1500


        sugestoes += "\nFotógrafo Profissional"
        orcamento_total += 1200

    
    elif tipo_de_evento == "aniversário":
        festa = input("O aniversário é para criança ou adulto: ").lower()
        preco_por_pessoa = 30
        total_do_buffet = preco_por_pessoa * num_de_convidados

        sugestoes += f"\nBuffet R${preco_por_pessoa} por pessoa"
        sugestoes += f"\nTotal do Buffet: R${total_do_buffet}"
        orcamento_total += total_do_buffet

        if festa == "criança":
            sugestoes += "\CARDÁPIO:\nSalgados: Coxinha, Bolinha de Queijo, Enroladinho de Salsicha\nDoces: Brigadeiro, Beijinho, Surpresa de Uva\nBebidas: Água, Refrigerantes, Sucos\nLanches: Mini pizzas, Mini hamburguer, Cachorro Quente"
            orcamento_total += 2000

            sugestoes += "\nDecoração infantil: Balões, Painiés temáticos"
            orcamento_total += 1500

            sugestoes += "\nBrincadeira: Brinquedos, Mágico"
            orcamento_total += 1500
            
            sugestoes += "\nLancherinha com o tema estampado"
            orcamento_total += 500

            return sugestoes, orcamento_total

        elif festa == "adulto":
            sugestoes += "\CARDÁPIO:\nEntrada: Tábua Simples, Amendoin, Torradinhas com patês\nSalgados: coxinha, Kibe, Risoles\nPrato Quente: Strogonoff, Massas\nBebidas: Refrigerante, Água, Destilados"
            orcamento_total += 2000

            sugestoes += "\nDecoração Elegante"
            orcamento_total += 1000

            sugestoes += "\nMúsica Ao vivo"
            orcamento_total += 600

            return sugestoes, orcamento_total

    elif tipo_de_evento == "reunião":
        preco_por_pessoa = 30
        total_do_buffet = preco_por_pessoa * num_de_convidados

        sugestoes += f"\nBuffet R${preco_por_pessoa} por pessoa"
        sugestoes += f"\nTotal do Buffet R${total_do_buffet}"
        orcamento_total += total_do_buffet

        sugestoes += "\CARDÁPIO:\nBebidas: Café, Suco Natural, Água\nSalgados: Sanduíches Naturais, Pão de Queijo, Folhados\nDoces: Bolo, Biscoitos, Frutas"
        orcamento_total += 500

        sugestoes += "\nDecoração: Mesas com toalhas, Flores de mesa, Guardanapos, Jarras e Pratos"
        orcamento_total += 500

    return sugestoes, orcamento_total
    
def sem_sugestao(opc):
    print("Escolha o Pacote:")
    print("[1] Pacote Básico (R$ 1000)")
    print("[2] Pacote Completo (R$ 1500)")
    print("[3] Pacote VIP (R$ 2500)")

    opc = int(input("Digite o número do pacote desejado: "))

    if opc == 1:
        return "Pacote Básico (R$ 1000)", 1000
    
    elif opc == 2:
        return "Pacote Completo (R$ 1500)", 1500
    
    elif opc == 3:
        return "Pacote VIP (R$ 2500)", 2500

import os
from datetime import datetime

print("[1] Adicionar um novo evento")
print("[2] Visualizar um evento")
print("[3] Editar um evento")
print("[4] Excluir um evento")
print("[5] ")

print("="*20)
opc = int(input("digite uma opção: "))
print("="*20)

if opc == 1:
    nome_do_arquivo = input("Digite o nome do arquivo(colocar .txt): ")
    with open(nome_do_arquivo, 'a',encoding='utf8') as arquivo:
        tipo = input("Digite o tipo do evento: ").lower()
        arquivo.write(tipo + '\n')

        data = input("Digite a data do evento (dd/mm/aaaa): ")
        arquivo.write(data + '\n')

        local = (input("Digite o local do evento: "))
        arquivo.write(local + '\n')

        orcamento = int(input("Digite o orçamento do evento: "))
        arquivo.write(str(orcamento) + '\n')

        if orcamento < 1000:
            print("O valor mínimo para contratar um evento é de R$1000")
            exit()
    
    num_de_convidados = int(input("Digite a quantidade de convidados: "))
    s, orcamento_total = sugestao(tipo,num_de_convidados)

    print(s)

    if orcamento > orcamento_total:
            with open (nome_do_arquivo,'a',encoding='utf8') as arquivo:
                print(f"Orçamento final: R${orcamento_total}\n")
                arquivo.write(f"Orçamento final: {orcamento_total}\n")

                valor_final = orcamento - orcamento_total
                arquivo.write(f"O orçamento Restante é R${valor_final}\n")

    else:
        falta = orcamento_total - orcamento
        print(f"O seu orçamento ainda não é o sufuciente")
        print(f"o total da festa é R${orcamento_total}")
        print(f"Faltam R${falta}")
        print("Não foi possível salvar o evento")
        exit()

    querer = input("Deseja usar essas sugestões? [Sim/Não]: ").lower()

    if querer == "sim":
        with open (nome_do_arquivo,'a',encoding='utf8') as arquivo:
            arquivo .write("=-=-=-= Sugestão Escolhida: =-=-=-=\n")
            arquivo.write(s + '\n')
            print("evento cadastrada com sucesso!")


    elif querer == "não":
        texto, valor = sem_sugestao(opc)
        print(texto)

        with open (nome_do_arquivo,'a',encoding='utf8') as arquivo:
            diferenca = orcamento - valor
            if diferenca >= 0:
                print(f"\n=-=-=-= Evento {texto} Contratado =-=-=-=\n")
                print(f"Sobraram R${diferenca}")

                arquivo.write(f"\n=-=-=-= Evento {texto} Contratado =-=-=-=\n")
                arquivo.write(f"Sobraram R${diferenca}")

            else:
                print("Não foi possível contrar o Pacote para o evento")
                print(f"Faltam R${abs(diferenca)} para contratar o evento")

                arquivo.write("Não foi possível contrar o Pacote para o evento")
                arquivo.write(f"Faltam R${abs(diferenca)} para contratar o evento\n")

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

        with open (nome_do_arquivo,'a',encoding='utf8') as arquivo: # perguntar se quer salvar no arquivo ou so quando pedir para visualizar a fesgta
            if restam > 0:
                print(f"Faltam {restam} dias para o evento")
                

            elif restam == 0:
                print(f"O evento é Hoje")
                
            
            else:
                print(f"O evento ja passou há {-restam} dias")
                

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