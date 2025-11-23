## Função para sugerir detalhes do evento com base no tipo e número de convidados ##
def sugestao(tipoEvento, convidados):
    orcamento_total = 0
    t = tipoEvento.lower()

    sugestoes = f"\nSugestões para o seu evento de {tipoEvento} com {convidados} convidados:\n"

    if t == "casamento":
        sugestoes += f"\nBuffet de casamanto R$70 por pessoa"
        orcamento_total += 70 * convidados
        sugestoes += "\nCARDÁPIO:\nMassa: Fettuccine, Penne, Raviole\nProteína: Carne, Peixe, Ave\nSobremessas: Petit gateau, Crème Brûlée, Macaron"
        sugestoes += "\nDECORAÇÃO: flores (cor à sua preferencia), iluminação suave, velas, serviço à americana e uma mesa para os familiares dos noivos (R$4000)"
        orcamento_total += 4000
        sugestoes += "\nMUSICA: Um Violinista (Para a Cerimônia), Banda ao vivo e DJ (Para a Festa) (R$1500)"
        orcamento_total += 1500
        sugestoes += "\nFOTOS:Fotógrafo Profissional (Com cabine de fotos) (R$1200)"
        orcamento_total += 1200
        return sugestoes, orcamento_total

    elif t == "aniversário":
        idade = input("O aniversário é para criança ou adulto: ").lower()
        sugestoes += f"\nBuffet de aniversário R$30 por pessoa"
        orcamento_total += 30 * convidados
        if idade == "criança":
            sugestoes += "\nCARDÁPIO:\nSalgados: Coxinha, Bolinha de Queijo, Enroladinho de Salsicha\nDoces: Brigadeiro, Beijinho, Surpresa de Uva\nBebidas: Água, Refrigerantes, Sucos\nLanches: Mini pizzas, Mini hamburguer, Cachorro Quente"
            sugestoes += "\nDECORAÇÃO infantil: Balões, Painiés temáticos (R$1500)"
            orcamento_total += 1500
            sugestoes += "\nBRINCADEIRAS: Brinquedos, Mágico (R$1500)"
            orcamento_total += 1500
            sugestoes += "\nLEMBRANCINHAS: Lancherinha com o tema estampado (R$500)"
            orcamento_total += 500
            return sugestoes, orcamento_total
        elif idade == "adulto":
            sugestoes += "\nCARDÁPIO:\nEntrada: Tábua Simples, Amendoin, Torradinhas com patês\nSalgados: coxinha, Kibe, Risoles\nPrato Quente: Strogonoff, Massas\nBebidas: Refrigerante, Água, Destilados"
            sugestoes += "\nDECORAÇÃO: Elegante (R$1000)"
            orcamento_total += 1000
            sugestoes += "\nMÚSICA: Ao vivo (R$600)"
            orcamento_total += 600
            return sugestoes, orcamento_total

    elif t == "reunião":
        sugestoes += f"\nBuffet R$30 por pessoa"
        orcamento_total += 30 * convidados
        sugestoes += "\nCARDÁPIO:\nBebidas: Café, Suco Natural, Água\nSalgados: Sanduíches Naturais, Pão de Queijo, Folhados\nDoces: Bolo, Biscoitos, Frutas"
        sugestoes += "\nDECORAÇÃO: Mesas com toalhas, Flores de mesa, Guardanapos, Jarras e Pratos (R$500)"
        orcamento_total += 500
        return sugestoes, orcamento_total
    
    elif t == "churrasco":
        sugestoes += f"\nChurrasco R$50 por pessoa"
        orcamento_total += 50 * convidados
        sugestoes += "\nCARDÁPIO:\nCarnes: Picanha, Fraldinha, Linguiça, Frango\nAcompanhamentos: Arroz, Farofa, Vinagrete, Salada\nBebidas: Cerveja, Refrigerante, Água"
        sugestoes += "\nDECORAÇÃO: Toalhas de mesa xadrez, guardanapos coloridos, pratos e copos descartáveis (R$800)"
        orcamento_total += 800
        sugestoes += "\nMÚSICA: Playlist personalizada ou DJ (R$400)"
        orcamento_total += 400
        return sugestoes, orcamento_total
    
    elif t == "batizado":
        sugestoes += f"\nBuffet R$40 por pessoa"
        orcamento_total += 40 * convidados
        sugestoes += "\nCARDÁPIO:\nEntradas: Canapés, Salgadinhos finos\nPrato Principal: Frango ao molho, Massas\nSobremesas: Mini tortas, Docinhos variados\nBebidas: Sucos, Refrigerantes, Água"
        sugestoes += "\nDECORAÇÃO: Cores suaves, Flores delicadas, Itens religiosos (R$1200)"
        orcamento_total += 1200
        sugestoes += "\nMÚSICA: Música ambiente suave (R$300)"
        orcamento_total += 300
        return sugestoes, orcamento_total
    
    elif t == "formatura":
        sugestoes += f"\nBuffet R$60 por pessoa"
        orcamento_total += 60 * convidados
        sugestoes += "\nCARDÁPIO:\nEntradas: Tábua de frios, Salgadinhos variados\nPrato Principal: Carnes nobres, Massas finas\nSobremesas: Doces gourmet, Bolo temático\nBebidas: Coquetéis, Refrigerantes, Água"
        sugestoes += "\nDECORAÇÃO: Tema sofisticado, Iluminação especial, Arranjos florais (R$2000)"
        orcamento_total += 2000
        sugestoes += "\nMÚSICA: Banda ao vivo e DJ (R$1500)"
        orcamento_total += 1500
        return sugestoes, orcamento_total
## Função para escolher pacote sem sugestão ##    
def semSugestao():
    print("Escolha o Pacote:")
    print("[1] Pacote Básico (R$ 1000)")
    print("[2] Pacote Completo (R$ 5000)")
    print("[3] Pacote VIP (R$ 10000)")
    try:
        pacote = int(input("Digite o número do pacote desejado: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return "Pacote inválido. Por favor, escolha uma opção válida.", 0
    if pacote == 1:
        return "Pacote Básico (R$ 1000)", 1000
    
    elif pacote == 2:
        return "Pacote Completo (R$ 5000)", 5000
    
    elif pacote == 3:
        return "Pacote VIP (R$ 10000)", 10000
    else:
        return "Pacote inválido. Por favor, escolha uma opção válida.", 0

def indice(linhas, chave):
    for i, linha in enumerate(linhas):
        if linha.lower().startswith(chave.lower()):
            return i
    return None

## importando bibliotecas ##
import os
from datetime import datetime
## menu de operações ##
while True:
    print("=" * 40)
    print("\tOrganiza Festa\t")
    print("=" * 40)
    print("[1] - Adicionar novo evento")
    print("[2] - Visualizar um evento")
    print("[3] - Editar um evento")
    print("[4] - Excluir evento")
    print("[5] - adicionar lista de convidados")
    print("[0] - Sair")
    print("=" * 40)
    try:
        operacao = int(input("Escolha a operação a ser realizada: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    print("=" * 40)
    ## Adicionar novo evento ##
    if operacao == 1:

        nomeArquivo = input("Digite o nome do arquivo(sem espaços): ") + ".txt"
        
        validos = ["- casamento", "- aniversário", "- reunião", "- churrasco", "- batizado", "- formatura"]
        print("Segue a lista de eventos com sugestões pré definidas:")
        for item in (validos):
            print(f"{item}")
            
        ## coletando dados do evento ##
        with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
            tipo = input("Digite o tipo do evento: ").lower()
            arquivo.write("Tipo do evento: " + tipo + "\n")

            data = input("Digite a data do evento (DD/MM/AAAA): ") 
            arquivo.write("Data do evento: " + data + "\n")

            local = input("Digite o local do evento: ")
            arquivo.write("Local do evento: " + local + "\n")

            convidados = int(input("Digite o número de convidados: "))
            arquivo.write("Número de convidados: " + str(convidados) + "\n")

            orcamento = input("Digite o orçamento do evento: R$ ")
            arquivo.write("Orçamento do Evento: R$ " + orcamento + "\n")
            try:
                orcamento = float(orcamento)
            except ValueError:
                print("Por favor, digite um valor numérico válido para o orçamento.")
                continue
            ## verificando orçamento mínimo ##
            if orcamento < 1000:
                print("\nO valor mínimo para contratar um evento é de R$1000")
                continue
        ## sugerindo pacotes ##
        validos = ["casamento", "aniversário", "reunião", "churrasco", "batizado", "formatura"]

        if tipo.lower() not in validos:
            pacote, valor = semSugestao()
            print(pacote)

            with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                diferenca = orcamento - valor

                if diferenca >= 0:
                    print(f"\n====== Evento {pacote} Contratado ======n")
                    print(f"\nVocê terá um saldo restante de R$ {diferenca} após contratar o pacote escolhido.")

                    arquivo.write(f"====== Evento {pacote} Contratado ======\n")
                    arquivo.write(f"Saldo restante após contratar o pacote escolhido: R$ {diferenca}\n")
                else:
                    print(f"\nSeu orçamento não cobre o {pacote}. Faltam R$ {abs(diferenca)} para contratar esse pacote.")
                    arquivo.write(f"\nSeu orçamento não cobre o {pacote}. Faltam R$ {abs(diferenca)} para contratar esse pacote.\n")
                    continue
        ## sugerindo detalhes do evento ##
        else:
            suges, orcamento_total = sugestao(tipo, convidados)
            print(suges)

            if orcamento > orcamento_total:
                with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                    print(f"\nOrçamento Total do Evento: R$ {orcamento_total}")
                    arquivo.write(f"Orçamento Total do Evento: R$ {orcamento_total}\n")

                    valor_final = orcamento - orcamento_total
                    print(f"Saldo restante após contratar os serviços sugeridos: R$ {valor_final}.")
                    arquivo.write(f"Saldo restante após contratar os serviços sugeridos: R$ {valor_final}\n")
            else:
                falta = orcamento_total - orcamento
                print(f"\nSeu orçamento não cobre todas as sugestões. Faltam R$ {falta} para contratar todos os serviços sugeridos.")
                print("Não foi possível adicionar o evento.")
                continue

            querer = input("Deseja usar essas sugestões? (s/n): ").lower()
            if querer == "s":
                orcamento -= orcamento_total

                with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                    arquivo.write("\n====== Sugestão Escolhida: ======\n")
                    arquivo.write(suges + "\n")

                    print("evento cadastrado com sucesso!")

            elif querer == "n":
                pacote, valor = semSugestao()
                print(pacote)

                with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                    diferenca = orcamento - valor

                    if diferenca >= 0:
                        print(f"\n====== Evento {pacote} Contratado ======\n")
                        print(f"\nVocê terá um saldo restante de R$ {diferenca} após contratar o pacote escolhido.")

                        arquivo.write(f"====== Evento {pacote} Contratado ======\n")
                        arquivo.write(f"Saldo restante após contratar o pacote escolhido: R$ {diferenca}\n")
                        orcamento = diferenca
                    else:
                        print(f"\nSeu orçamento não cobre o {pacote}. Faltam R$ {abs(diferenca)} para contratar esse pacote.")
                        arquivo.write(f"\nSeu orçamento não cobre o {pacote}. Faltam R$ {abs(diferenca)} para contratar esse pacote.\n")
                        continue

        ## adicionando tarefas extras ##
        tarefas = input("\nDeseja adicionar mais tarefas ao evento? (s/n): ").lower()

        if tarefas == "s" or tarefas == "sim":
            with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                while True:
                    tarefa = input("\nDigite a tarefa (ou 'f' para finalizar): ")
                    if tarefa.lower() == "f":
                        break
                    else:
                        try:
                            valorTarefa = float(input(f"Quanto {tarefa} irá custar? R$ "))

                        except ValueError:
                            print("Por favor, digite um valor numérico válido para o custo da tarefa.")
                            continue

                        orcamento -= valorTarefa

                        if orcamento >= 0:
                            with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                                arquivo.write("Tarefa extra: " + tarefa + "\n")

                        elif orcamento < 0:
                            print(f"\nOrçamento insuficiente para adicionar a tarefa '{tarefa}'. Você precisa de mais R$ {abs(orcamento)}.")
                            orcamento += valorTarefa
                            continue

            with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                arquivo.write(f"Orçamento restante após tarefas extras: R$ {orcamento}\n")

            print(f"\nTarefas adicionadas com sucesso! (Orçamento restante R$ {orcamento:.2f})")
            print(f"\nEvento {nomeArquivo} adicionado com sucesso!")

    ## Visualizar um evento ##
    elif operacao == 2:
        nome_do_arquivo = input("Qual arquivo vc quer visualizar (sem espaços): ") + ".txt"

        try:
            with open(nome_do_arquivo,'r',encoding='utf8') as arquivo:
                tipo = arquivo.readline().strip()
                data = arquivo.readline().strip()
                local = arquivo.readline().strip()
                convidados = arquivo.readline().strip()
                orcamento = arquivo.readline().strip()

                print(f"{tipo}")
                print(f"{data}")
                print(f"{local}")
                print(f"{convidados}")
                print(f"{orcamento}")

                ## calculando dias restantes ##
                if ": " in data:
                    _, data_str = data.split(": ", 1)

                else:
                    data_str = data
                dia,mes,ano = map(int, data_str.split("/"))

                from datetime import date

                dia_do_evento = date(ano,mes,dia)
                hoje = date.today()
                restam = (dia_do_evento - hoje).days

                if restam > 0:
                    print(f"Faltam {restam} dias para o evento")

                elif restam == 0:
                    print(f"O evento é Hoje")

                else:
                    print(f"O evento ja passou há {-restam} dias")

        except FileNotFoundError:
            print("arquivo não encontrado.")

        except Exception as e:
            print("Erro ao visualizar o arquivo:", e)

    ## Editar um evento ##

    elif operacao == 3:
        try:
            nomeArquivo = input("Qual arquivo vc quer editar (sem espaços): ") + ".txt"
            with open(nomeArquivo, 'r',encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()

            data_indice = indice(linhas, "Data do Evento")
            local_indice = indice(linhas, "Local do Evento")
            convidado_indice = indice(linhas, "Número de Convidados")
            orcamento_indice = indice(linhas, "Orçamento do Evento")

            print("\n====== Evento Atual ======")
            for i in [data_indice, local_indice, convidado_indice, orcamento_indice]:
                if i is not None:
                    print(linhas[i].strip())


            print("\n====== Evento Novo ======")
            print("Aperte Enter para manter o antigo")

            data_nova = input("Digite a NOVA data do Evento: ")
            local_novo = input("Digte o NOVO local do Evento: ")
            convidado_novo = input("Digte a NOVA quantidade de convidados: ")
            orcamento_novo = input("Digite o NOVO orçamento do Evento: ")
            print("=-" * 15)

            if data_nova and data_indice is not None:
                linhas[data_indice] = f"Data do Evento: {data_nova}\n"
            
            if local_novo and local_indice is not None:
                linhas[local_indice] = f"Local do Evento: {local_novo}\n"
            
            if convidado_novo and convidado_indice is not None:
                linhas[convidado_indice] = f"Número de Convidados: {convidado_novo}\n"

            if orcamento_novo and orcamento_indice is not None:
                orcamento_novo = float(orcamento_novo)

                orcamento_antigo_str = linhas[orcamento_indice].split(":")[1].replace("R$", "").strip()
                orcamento_antigo = float(orcamento_antigo_str)

                saldo_antigo = 0.0
                for l in linhas:
                    if "saldo restante" in l.lower():
                        saldo_antigo = float(l.split(":")[1].replace("R$", "").strip())
                
                orcamento_total = orcamento_antigo - saldo_antigo
                saldo_novo = orcamento_novo - orcamento_total

                linhas[orcamento_indice] = f"Orçamento do Evento: R$ {orcamento_novo}\n"

                linhas = [l for l in linhas if "saldo restante" not in l.lower()]

                linhas.append(f"Saldo Restante: R$ {saldo_novo}\n")


            with open(nomeArquivo,'w',encoding='utf-8') as arquivo:
                arquivo.writelines(linhas)

            print("\nArquivo editado com sucesso!")

        except FileNotFoundError:
            print("\nArquivo não encontrado")

        except Exception as e:
            print("\nErro ao editar o arquivo:", e)

    ## Excluir um evento ##
    elif operacao == 4:
        try:
            nomeArquivo = input("Digite o nome do arquivo que deseja apagar(sem espaços): ") + ".txt"
            os.remove(nomeArquivo)
            print("\nArquivo excluido com sucesso!")

        except FileNotFoundError:
            print("\nO arquivo não existe!")

        except Exception as e:
            print("\nErro ao excluir o arquivo:", e)
    ## Adicionar lista de convidados ##
    elif operacao == 5:
        listaConvidados = []
        nomeArquivo = input("Em qual evento você gostaria de adicionar a lista de convidados? (sem espaços): ") + ".txt"

        try:
            with open (nomeArquivo, "r", encoding = "utf-8") as c:
                linhas = c.readlines()

            numero = None
            for l in linhas:
                if "Número de convidados" in l:

                    try:
                        numero = int(l.split(":")[-1].strip())

                    except Exception:
                        numero = None
                    break

            if numero is None:
                try:
                    numero = int(input("Quantos convidados você quer adicionar? ").strip())

                except ValueError:
                    print("Número inválido. Operação cancelada.")
                    continue

        except FileNotFoundError:
                print("Arquivo não encontrado.")
                continue
        
        for i in range(numero):
            convidadoNome = input(f"insira o nome do convidado {i+1}:  ".strip())
            listaConvidados.append(convidadoNome)
        listaConvidados.sort()

        try:
            with open(nomeArquivo, "a", encoding = "utf-8") as arquivo:
                arquivo.write("\nLista de convidados:\n")
                arquivo.writelines([f"{nome}\n" for nome in listaConvidados])
                print("Lista de convidados adicionada com sucesso!")

        except Exception as e:
            print("Erro ao escrever no arquivo:", e)

    ## saindo do programa ##
    elif operacao == 0:
        print("Saindo do programa...")
        break

    ## Operação inválida ## 
    else:
        print("Operação inválida. Tente novamente.")
        continue