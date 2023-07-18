# HORA DA XEPA - GLOBAL SOLUTION - PYTHON



def menu():
    try:
        print("\n Seja bem vindo ao programa de combate a fome e agricultura sustentável Hora da Xepa!!!")
        print("1 - Sobre o projeto.")
        print("2 - Ajude nossa causa!! Faça uma doação")
        print("3 - Finalizar doações")
        print("4 - Descubra como as IA's contribuem para um cultivo mais sustentável.")
        print("5- Saiba quais são as melhores culturas para se cultivar de acordo com o clima da sua região.")
        print("6 - Sair.")
    except ValueError:
        print("Opção inválida")    
    return int(input("Escolha uma opção: "))

def doacao():
    try:
        tipo = int(input("\n Você pode contribuir doando algum alimento ou uma pequena quantia de dinheiro \n(1) Alimento não perecível. \n(2) Dinheiro. \n Qual é sua escolha? \n R: "))
        if tipo == 1:
            doar_alimento()
        elif tipo == 2:
            doar_dinheiro()
    except ValueError:
        print("Opção inválida")

cesta = []
qtd_itens = []
valor_doado = []
resumo = []

def doar_alimento():
    try:
        categoria = int(input("\n Aceitamos vários tipos de alimentos não perecívies: \n (1) Empacotados \n (2) Enlatados \n (3) Líquidos \n Qual opção deseja conferir? \n R: "))
        if categoria == 1:
            pacotes()
        elif categoria == 2:
            enlatados()
        elif categoria == 3:
            liquidos()

    except ValueError:
        print("Opção inválida")

def pacotes():
        try:
            print("\n Alimento embalados/empacotados: ")
            print("(1) Arroz")
            print("(2) Feijão")
            print("(3) Sal")
            print("(4) Açucar")
            print("(5) Frinha de trigo")
            print("(6) Achocolatado em pó")
            print("(7) Macarrão")
            print("(8) Café")
            print("(9) Biscoitos")
            print("(10) Leite em pó")
            resposta_empacotados = int(input("\n Qual das opções você escolhe? \n R: "))
        except ValueError:
            print("Opção inválida")

        if resposta_empacotados == 1:
            try:
                quantidade_arroz = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_arroz <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Arroz")
            qtd_itens.append(quantidade_arroz)
            resumo.append(f"Arroz: {quantidade_arroz} pacotes" )

        elif resposta_empacotados == 2:
            try:
                quantidade_feijao = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_feijao <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Feijão")
            qtd_itens.append(quantidade_feijao)
            resumo.append(f"Feijão: {quantidade_feijao} pacotes" )

        elif resposta_empacotados == 3:
            try:
                quantidade_sal = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_sal <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Sal")
            qtd_itens.append(quantidade_sal)
            resumo.append(f"Sal: {quantidade_sal} pacotes" )

        elif resposta_empacotados == 4:
            try:
                quantidade_acucar = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_acucar <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Açúcar")
            qtd_itens.append(quantidade_acucar)
            resumo.append(f"Açúcar: {quantidade_acucar} pacotes" )

        elif resposta_empacotados == 5:
            try:
                quantidade_farinha = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_farinha <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Farinha de trigo")
            qtd_itens.append(quantidade_farinha)
            resumo.append(f"Farinha de trigo: `{quantidade_farinha} pacotes")

        elif resposta_empacotados == 6:
            try:
                quantidade_achocolatado = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_achocolatado <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Achocolatado em pó")
            qtd_itens.append(quantidade_achocolatado)
            resumo.append(f"Achocolatado em pó: {quantidade_achocolatado} pacotes" )

        elif resposta_empacotados == 7:
            try:
                quantidade_macarrao = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_macarrao <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Macarrão")
            qtd_itens.append(quantidade_macarrao)
            resumo.append(f"Macarrão: {quantidade_macarrao} pacotes" )

        elif resposta_empacotados == 8:
            try:
                quantidade_cafe = int(input("Quantas unidades deseja doar? \n R: "))
                if quantidade_cafe <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Café")
            qtd_itens.append(quantidade_cafe)
            resumo.append(f"Café: {quantidade_cafe} pacotes" )

        elif resposta_empacotados == 9:
            try:
                quantidade_biscoitos = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_biscoitos >= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Biscoitos")
            qtd_itens.append(quantidade_biscoitos)
            resumo.append(f"Biscoitos: {quantidade_biscoitos} pacotes" )

        elif resposta_empacotados == 10:
            try:
                quantidade_leite_po = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_leite_po <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado iválido")
            except  Exception:
                print("Quantidade inválida.")
            cesta.append("Leite em pó")
            qtd_itens.append(quantidade_leite_po)
            resumo.append(f"Leite em pó: {quantidade_leite_po} pacotes" )

def enlatados():
        try:
            print("Alimentos enlatados:")
            print("(1) Atum")
            print("(2) Sardinha")
            print("(3) Milho")
            print("(4) Ervilha")
            print("(5) Molho de tomate")
            respostas_enlatados = int(input("\n Qual das opções você escolhe? \n R: "))
        except ValueError:
            print("Opção inválida")
        if respostas_enlatados == 1:
            try:
                quantidade_atum = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_atum <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida.")
            cesta.append("Atum")
            qtd_itens.append(quantidade_atum)
            resumo.append(f"Atum")

        elif respostas_enlatados == 2:
            try:
                quantidade_sardinha = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_sardinha <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Sardinha")
            qtd_itens.append(quantidade_sardinha)
            resumo.append(f"Sardinha: {quantidade_sardinha} latas")

        elif respostas_enlatados == 3:
            try:
                quantidade_milho = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_milho <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Milho")
            qtd_itens.append(quantidade_milho)
            resumo.append(f"Milho: {quantidade_milho} latas")

        elif respostas_enlatados == 4:
            try:
                quantidade_ervilha = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_ervilha <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Ervilha")
            qtd_itens.append(quantidade_ervilha)
            resumo.append(f"Ervilha: {quantidade_ervilha} latas")

        elif respostas_enlatados == 5:
            try:
                quantidade_molho = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_molho <= 0:
                    raise Exception
            except ValueError:
                    print("Valor informado inválido")
            except Exception:
                    print("Quantidade inválida")
            cesta.append("Molho de tomate")
            qtd_itens.append(quantidade_molho)
            resumo.append(f"Molho: {quantidade_molho} latas")

def liquidos():
        try:
            print("Líquidos: ")
            print("(1) Água")
            print("(2) Sucos")
            print("(3) Leite")
            print("(4) Óleo de girassol")
            print("(5) Azeite")
            resposta_liquidos = int(input("\n Qual das opções você escolhe?"))
        except ValueError:
            print("Opção inválida")
        if resposta_liquidos == 1:
            try:
                quantidade_agua = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_agua <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Água")
            qtd_itens.append(quantidade_agua)
            resumo.append(f"Água: {quantidade_agua} unidades.")
        
        if resposta_liquidos == 2:
            try:
                quantidade_sucos = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_sucos <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Suco")
            qtd_itens.append(quantidade_sucos)
            resumo.append(f"Suco: {quantidade_sucos} unidades.")

        elif resposta_liquidos == 3:
            try:
                quantidade_leite = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_leite <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Leite")
            qtd_itens.append(quantidade_leite)
            resumo.append(f"Leite: {quantidade_leite} caixas.")

        elif resposta_liquidos == 4:
            try:
                quantidade_oleo = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_oleo <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Óleo de girassol")
            qtd_itens.append(quantidade_oleo)
            resumo.append(f"Óleo de girassol: {quantidade_oleo} unidades.")

        elif  resposta_liquidos == 5:
            try:
                quantidade_azeite = int(input("\n Quantas unidades deseja doar? \n R: "))
                if quantidade_azeite <= 0:
                    raise Exception
            except ValueError:
                print("Valor informado inválido")
            except Exception:
                print("Quantidade inválida")
            cesta.append("Azeite")
            qtd_itens.append(quantidade_azeite)
            resumo.append(f"Azeite: {quantidade_azeite} garrafas.")



def doar_dinheiro():
    try:
        valor = float(input("\n Para doações em dinheiro, aceitamos valores a partir de R$5,00. \n Digite o valor que deseja doar: \n R: "))
        if valor < 5:
            raise Exception
    except ValueError:
        print("Valor inválido")
    except Exception:
        print("ERRO: Nós só aceitamos doações a partir de R$5,00 (reais)")
    if valor >= 5:
        valor_doado.append(f"R${valor}0")
        resumo.append(f"Você está doando R${valor}0")

def cesta_doacao():
    print("Essa é sua cesta de doações:")
    print(resumo)
    finalizar = int(input("Deseja finalizar as doações e enviar sua cesta? \n (1) SIM \n (2) NÃO \n R: "))
    if finalizar == 1:
        finalizar_doacao()
    elif finalizar == 2:
        menu()



def finalizar_doacao():
    try:
        print("(1) Alimento ")
        print("(2) Alimento e/ou Dinheiro")
        tipo = int(input("O que deseja enviar? \n R: "))
        match tipo:
            case 1:
                print("Para finalizar precisamos de algumas informações suas: ")
                nome = input("Informe seu nome: ")
                rg = input("Informe seu RG: ")
                email = input("Informe um endereço de email para contato: ")
                telefone = input("Informe um número de telefone para contato: ")
                endereco = input("Informe seu endereço: ")

                print("Comprovante:")
                print(f"Nome: {nome}")
                print(f"RG: {rg}")
                print(f"E-mail: {email}")
                print(f"Telefone: {telefone}")
                print(f"Endereço: {endereco}")
                print("\n Doação realizada com sucesso!! Em breve um de nosso veículos fará a retirada dos itens no endereço informado.")
                print("\n Obrigado pela sua contribuição. Volte sempre!!")
                
            case 2:
                print("Para finalizar precisamos de algumas informações suas: ")
                nome = input("Informe seu nome: ")
                rg = input("Informe seu RG: ")
                email = input("Informe um endereço de email para contato: ")
                telefone = input("Informe um número de telefone para contato: ")
                endereco = input("Informe seu endereço: ")
                cpf = int(input("Informe seu CPF: "))


                
                print("\nDepósitos podem ser feitos via Pix ou depósito bancário:")
                print("Nossa Chave: XXXXXXXXXXXXXXXX")
                print("Nossa conta:")
                print("Banco: (Nome do banco \n Agência: XXXX \n Conta: XXXXXXX")

                deposito = int(input("\n (1) Pix \n (2) Depósito bancário \n Selecione a forma de depósito: \n R: "))
                match deposito:
                    case 1:
                        print("\nComprovante: ")
                        print(f"Nome: {nome}")
                        print(f"RG: {rg}")
                        print(f"E-mail: {email}")
                        print(f"Telefone: {telefone}")
                        print(f"Endereço: {endereco}")
                        print(f"Doações: \n {resumo}")
                        print("\n Obrigado pela sua contribuição. Volte sempre!!")

                    case 2: 
                        print("\nComprovante: ")
                        print(f"Nome: {nome}")
                        print(f"RG: {rg}")
                        print(f"E-mail: {email}")
                        print(f"Telefone: {telefone}")
                        print(f"Endereço: {endereco}")
                        print(f"CPF: {cpf}")
                        print(f"Doações: \n {resumo}")
                        print("\n Obrigado pela sua contribuição. Volte sempre!!")
    except ValueError:
        print("Opção inválida.")
      

    


def clima():
    try:
        print("\nÉ importante considerar as condições locais como a duração da estação de crescimento, a disponibilidade de água e o tipo de solo, ao selecionar as culturas mais adequadas para uma determinada região com seu respctivo clima")
        print("Escolha o clima que melhor combine com a região em que você mora:")
        print("(1) Equatorial")
        print("(2) Tropical")
        print("(3) Subtropical")
        print("(4) Temperado")
        print("(5) Semiárido")
        print("(6) Árido")
        print("(7) Subpolar")
        resposta_clima = int(input("\n Qual das opções combina com a sua região?\n R:"))
        match resposta_clima:
            case 1:
                print("\nO clima equatorial é caracterizado por ser quente e úmido ao longo do ano, com chuvas frequentes. Essas condições climáticas favoráveis permitem o cultivo de uma ampla variedade de culturas. \nAqui está uma lista de culturas que podem ser cultivadas no clima equatorial:")
                print("\n1 - Bananas: As bananeiras são bem adaptadas ao clima equatorial, sendo uma cultura importante em várias regiões equatoriais ao redor do mundo.")
                print("\n2 - Café: O café é uma cultura comumente cultivada em áreas equatoriais. Os grãos de café são sensíveis às variações de temperatura e umidade, e as condições equatoriais proporcionam o ambiente ideal para seu cultivo.")
                print("\n3 - Cacau: O cacau é cultivado em muitas áreas equatoriais e é a principal matéria-prima para a produção de chocolate. O clima equatorial, com sua umidade e temperatura constantes, é adequado para o cultivo de árvores de cacau.")
                print("\n4 - Arroz: O arroz é uma cultura alimentar importante e é cultivado em áreas de clima equatorial, onde a água está disponível em abundância. As plantações de arroz requerem uma quantidade significativa de água para crescerem adequadamente.")
                print("\n5 - Milho: O milho é uma cultura versátil que pode ser cultivada em uma ampla gama de climas, incluindo o equatorial. É uma fonte importante de alimento e pode se adaptar às condições quentes e úmidas.")
                print("\n6 - Mandioca: A mandioca é uma cultura básica em muitas regiões equatoriais. Ela é tolerante à seca e pode se desenvolver bem em solos pobres, sendo uma fonte importante de carboidratos.")
                print("\n7 - Frutas tropicais: Muitas frutas tropicais prosperam em climas equatoriais, como abacaxi, manga, maracujá, goiaba, mamão, entre outras. Essas frutas são apreciadas por sua doçura e suculência.")


            case 2:
                print("\nO clima tropical abrange uma ampla gama de condições climáticas, com variações de temperatura e precipitação ao longo do ano. No entanto, em geral, as áreas tropicais são caracterizadas por temperaturas quentes durante todo o ano, com estações chuvosas e secas distintas. \nAqui está uma lista de culturas que podem ser cultivadas em climas tropicais:")
                print("\n1 - Arroz: O arroz é uma cultura importante em regiões tropicais, especialmente em áreas com altos índices de chuva. O cultivo de arroz é amplamente praticado em países como Índia, Tailândia, Vietnã e muitos outros países do Sudeste Asiático.")
                print("\n2 - Milho: O milho é uma cultura versátil que pode ser cultivada em climas tropicais. É uma fonte importante de alimento e pode ser cultivado em várias variedades adaptadas às diferentes condições climáticas.")
                print("\n3 - Feijão: O feijão é uma cultura comum em climas tropicais, pois é adaptado ao calor e à umidade. Diferentes variedades de feijão, como feijão-fradinho, feijão-preto e feijão-manteiga, são cultivadas em várias regiões tropicais.")
                print("\n4 - Mandioca: A mandioca é uma cultura amplamente cultivada em climas tropicais, especialmente em áreas com baixa pluviosidade. É uma fonte importante de carboidratos e pode crescer em solos pobres.")
                print("\n5 - Banana: As bananeiras são adaptadas a climas tropicais, especialmente em áreas com alta umidade. Elas são amplamente cultivadas em várias regiões tropicais ao redor do mundo.")
                print("\n6 - Coco: O coqueiro é uma cultura típica de áreas tropicais, onde pode crescer em solos arenosos e tolerar altas temperaturas. É uma fonte importante de água de coco, óleo de coco e outros produtos.")
                print("\n7 - Abacaxi: O abacaxi é uma fruta tropical cultivada em climas tropicais, conhecida por sua doçura e sabor característico. É cultivado comercialmente em várias partes do mundo.")
                print("\n8 - Frutas cítricas: Frutas como laranja, limão, tangerina e grapefruit são cultivadas em climas tropicais, especialmente em áreas com temperaturas moderadas e umidade adequada.")
                print("\n9 - Pimenta: A pimenta é uma cultura comum em climas tropicais, conhecida por sua variedade de sabores e níveis de pungência. Diferentes tipos de pimenta, como pimenta-do-reino e pimenta-malagueta, são cultivados em áreas tropicais.")
                print("\n10 - Cana-de-açúcar: A cana-de-açúcar é uma cultura importante em climas tropicais, devido à sua tolerância ao calor e à disponibilidade de água. É amplamente cultivada para a produção de açúcar e biocombustíveis.")



            case 3:
                print("\nO clima subtropical é caracterizado por invernos moderadamente frios e verões quentes. Essas condições climáticas proporcionam uma variedade de culturas que podem ser cultivadas com sucesso. \nAqui está uma lista de culturas comuns que podem ser plantadas em climas subtropicais:")
                print("\n1 - Citrus: Frutas cítricas como laranjas, tangerinas, limões e são bem adaptadas a climas subtropicais. Elas são conhecidas por sua doçura e sabor refrescante.")
                print("\n2 - Pêssegos: Pêssegos são frutas de caroço que se dão bem em climas subtropicais, pois necessitam de um período de dormência no inverno para produzir bem. Eles são apreciados por sua polpa suculenta e sabor doce.")
                print("\n3 - Uvas: Algumas variedades de uvas são cultivadas em climas subtropicais, especialmente aquelas adaptadas a temperaturas mais quentes. Elas são usadas para fazer vinhos, sucos e também podem ser consumidas frescas.")
                print("\n4 - Morangos: Morangos podem ser cultivados em climas subtropicais, especialmente durante os meses mais frescos do ano. Eles são apreciados por seu sabor doce e são frequentemente cultivados em sistemas de cultivo protegido.")
                print("\n5 - Kiwi: O kiwi é uma fruta que se dá bem em climas subtropicais, especialmente em áreas com invernos moderados. Essa fruta é conhecida por seu sabor doce e sua textura macia.")
                print("\n6 - Amêndoas: As amêndoas são cultivadas com sucesso em climas subtropicais, onde a exposição ao frio no inverno é necessária para sua produção. Elas são usadas em uma variedade de alimentos e produtos.")
                print("\n7 - Oliveiras: As oliveiras são bem adaptadas a climas subtropicais, com invernos suaves e verões quentes e secos. Elas são cultivadas principalmente por suas azeitonas, que são usadas para a produção de azeite de oliva.")
                print("\n8 - Abacate: O abacateiro é uma árvore que prospera em climas subtropicais, pois requer temperaturas amenas. O abacate é uma fruta muito nutritiva e é usado em saladas, guacamole e outros pratos.")
                print("\n9 - Nozes: Algumas variedades de nozes, como noz-pecã, noz-macadâmia e castanha-de-caju, podem ser cultivadas em climas subtropicais, desde que haja exposição adequada ao frio no inverno.")


            case 4:
                print("\nO clima temperado é caracterizado por estações distintas, com invernos frios e verões moderados. Essas condições climáticas permitem o cultivo de uma ampla variedade de culturas. \nAqui está uma lista de culturas comuns que podem ser plantadas em climas temperados:")
                print("\n1 - Trigo: O trigo é uma cultura de cereais amplamente cultivada em climas temperados. É usado principalmente para a produção de farinha e alimentos derivados, como pão, massas e bolos.")
                print("\n2 - Milho: O milho é uma cultura versátil que pode ser cultivada em climas temperados, desde que a estação de crescimento seja suficientemente longa e quente. É usado para alimentos, ração animal e também na indústria de biocombustíveis.")
                print("\n3 - Batatas: As batatas são amplamente cultivadas em climas temperados. Elas são uma importante fonte de carboidratos e podem ser preparadas de várias maneiras, como cozidas, fritas ou assadas.")
                print("\n4 - Maçãs: As macieiras são cultivadas em climas temperados, onde a mudança sazonal é favorável para a frutificação. Existem muitas variedades de maçãs que podem ser cultivadas em climas temperados, e elas são apreciadas por seu sabor doce e crocante.")
                print("\n5 - Uvas: Vinhedos são comuns em climas temperados, onde as uvas são cultivadas para a produção de vinho, sucos e também podem ser consumidas frescas. Existem variedades específicas de uvas adequadas para diferentes regiões de clima temperado.")
                print("\n6 - Cenouras: As cenouras são raízes comestíveis que crescem bem em climas temperados. Elas são uma fonte de vitaminas e são usadas em uma variedade de pratos culinários.")
                print("\n7 - Repolho: O repolho é um vegetal de folhas que pode ser cultivado em climas temperados. Ele é usado em saladas, sopas, ensopados e outros pratos.")
                print("\n8 - Espinafre: O espinafre é uma verdura que cresce bem em climas temperados. É uma excelente fonte de nutrientes, como ferro e vitaminas, e pode ser usado em saladas, sopas e refogados.")
                print("\n9 - Cebolas: As cebolas são cultivadas em climas temperados e são usadas como tempero em muitos pratos. Elas são conhecidas por seu sabor característico e podem ser armazenadas por um longo período.")
                
            case 5:
                print("\nO clima semiárido é caracterizado por verões quentes e secos, com baixa precipitação pluviométrica. No entanto, mesmo nessas condições desafiadoras, é possível cultivar certas culturas adaptadas à escassez de água. \nAqui está uma lista de culturas comuns que podem ser plantadas em climas semiáridos:")
                print("\n1 - Oliveiras: As oliveiras são árvores resistentes à seca e prosperam em climas semiáridos. Elas são cultivadas principalmente por suas azeitonas, que são usadas para produzir azeite de oliva.")
                print("\n2 - Amendoeiras: Amendoeiras são culturas adequadas para climas semiáridos. Elas têm uma alta tolerância à seca e podem ser cultivadas em solos pobres.")
                print("\n3 - Uvas de vinho: Algumas variedades de uvas de vinho são adaptadas a climas semiáridos, desde que sejam fornecidos sistemas de irrigação adequados. Elas são cultivadas principalmente para a produção de vinho.")
                print("\n4 - Tâmara: As tamareiras são árvores que se dão bem em climas semiáridos, onde a água é escassa. As tâmaras são frutas doces e são amplamente cultivadas em regiões semiáridas.")
                print("\n5 - Milheto: O milheto é um cereal que se adapta bem a climas semiáridos. É utilizado como alimento para animais, mas também é consumido pelos seres humanos em algumas regiões.")
                print("\n6 - Lentilhas: As lentilhas são leguminosas que podem ser cultivadas em climas semiáridos, pois têm uma alta tolerância à seca. Elas são uma fonte importante de proteína vegetal.")
                print("\n7 - Amendoim: O amendoim é uma cultura com boa adaptação a climas semiáridos. É cultivado principalmente por suas sementes, que são uma fonte de gordura e proteína.")
                print("\n8 - Sorgo: O sorgo é um cereal resistente à seca que pode ser cultivado em climas semiáridos. É usado como alimento para animais, mas também pode ser utilizado para a produção de farinha e outros produtos alimentícios.")

            case 6:
                print("\nO clima árido é caracterizado por baixos níveis de precipitação e alta evaporação, tornando a disponibilidade de água um fator limitante para o cultivo. No entanto, algumas culturas adaptadas à escassez de água podem ser cultivadas em climas áridos. \nAqui está uma lista de culturas comuns que podem ser plantadas em climas áridos:")
                print("\n1 - Romã: A romãzeira é uma árvore frutífera que se adapta a climas áridos. Ela requer pouca água e é conhecida por seus frutos saborosos e nutritivos.")
                print("\n2 - Oliveiras: As oliveiras são árvores resistentes à seca e podem ser cultivadas em climas áridos. Elas são cultivadas principalmente por suas azeitonas, que são usadas para produzir azeite de oliva.")
                print("\n3 - Figueiras: As figueiras são árvores que se dão bem em climas áridos. Elas têm uma boa tolerância à seca e podem ser cultivadas em solos pobres.")
                print("\n4 - Uvas de mesa: Algumas variedades de uvas de mesa podem ser cultivadas em climas áridos, desde que sejam fornecidos sistemas de irrigação adequados. Elas são apreciadas por seu sabor doce e são consumidas frescas.")
                print("\n5 - Amendoim: O amendoim é uma cultura resistente à seca que pode ser cultivada em climas áridos. Ele é cultivado principalmente por suas sementes, que são uma fonte de gordura e proteína.")
                print("\n6 - Sorgo: O sorgo é um cereal resistente à seca que pode ser cultivado em climas áridos. É usado como alimento para animais, mas também pode ser utilizado para a produção de farinha e outros produtos alimentícios.")
                print("\n7 - Tâmaras: As tâmaras são frutas secas amplamente cultivadas em climas áridos. Elas têm uma alta tolerância à seca e são uma importante fonte de alimento em regiões áridas.")
        

            case 7:
                print("\nO clima subpolar é caracterizado por invernos longos e extremamente frios, com temperaturas médias abaixo de zero, e verões curtos e frescos. \nDevido às condições climáticas desafiadoras, a variedade de culturas que podem ser cultivadas é limitada. No entanto, existem algumas culturas que podem ser adaptadas a essas condições. \nAqui está uma lista de culturas comuns que podem ser plantadas em climas subpolares:")
                print("\n1 - Cevada: A cevada é um cereal de estação fria que pode ser cultivado em climas subpolares. Ela é usada para a produção de cerveja, ração animal e outros produtos.")
                print("\n2 - Centeio: O centeio é outro cereal que pode ser cultivado em climas subpolares. Ele é utilizado principalmente como alimento para animais, mas também pode ser moído em farinha para fazer pães e outros produtos assados.")
                print("\n3 - Batatas: As batatas são uma cultura que pode ser cultivada em climas subpolares. Elas são uma importante fonte de carboidratos e podem ser armazenadas por um longo período de tempo.")
                print("\n4 - Cenouras: As cenouras são vegetais de raiz que podem ser cultivados em climas subpolares. Elas são ricas em nutrientes e são usadas em uma variedade de pratos culinários.")
                print("\n5 - Beterrabas: As beterrabas são outra cultura de raiz que se adapta a climas subpolares. Elas são usadas em saladas, sopas e outros pratos.")
                print("\n6 - Repolho: O repolho é uma cultura que pode ser cultivada em climas subpolares. Ele é usado em saladas, sopas, ensopados e outros pratos.")
                print("\n7 - Espinafre: O espinafre é uma verdura que cresce bem em climas subpolares. Ele é uma excelente fonte de nutrientes e pode ser usado em saladas, sopas e refogados.")
                print("\n8 - Alho: O alho é uma cultura que pode ser cultivada em climas subpolares. Ele é usado como tempero em muitos pratos culinários.")
                print("\n9 - Bagas: Algumas variedades de bagas, como framboesas e amoras, podem ser cultivadas em climas subpolares. Elas são apreciadas por seu sabor doce e são utilizadas em sobremesas, geleias e sucos.")
                print("\nÉ importante ressaltar que o cultivo de culturas em climas polares requer técnicas avançadas, como o uso de estufas, jardins internos aquecidos e outras formas de proteção contra o frio extremo. \nAlém disso, o fornecimento de luz adequada para as plantas é fundamental, uma vez que os climas polares podem ter longos períodos de escuridão.")
    except ValueError:
        print("Opção inválida")

    


while True:
    try:
        opcao = menu()

        if opcao == 1:
            print("Sobre o projeto:")
            print("\n Dentre diversos fatores como, pandemias, mudanças climáticas, conflitos e interesses políticos, a distribuição desigual e o desperdício desenfreado de alimentos em nosso país e mundo afora são de longe a principal causa da fome. \n  -> Segundo a FAO, 1,6 bilhões de toneladas de produtos primários – que são matérias primas para outros produtos alimentícios são perdidos ou descartados ao ano. Já o desperdício somente de alimentos chega a  1,3 bilhões de toneladas por ano. \n  -> Quanto a distribuição, é possível concluir que trata-se de uma consequência da pobreza e distribuição de renda. \n Esses fatores fazem com que a comida não chegue para a mesa de todos, uma vez que a produção de alimentos no Brasil por exemplo, é suficiente para a população inteira.")
            print("\n Nosso projeto se chama “Hora da Xepa” e tem o objetivo de coletar alimentos que estão em condições boas para consumo mas que não vão ser comprados, doações de alimento e levar para cozinhas solidarias ou ongs de distribuição de marmitas, nosso papel é fazer o intermédio entre fornecedor e ong.")

        elif opcao == 2:
            tipo = doacao()

        elif opcao == 3:
            cesta_doacao()
            

        elif opcao == 4:
            print("\nA Inteligencia Artificial na agricultura: \nA aplicação da Inteligência Artificial Generativa (IA Generativa) na agricultura tem o potencial de trazer benefícios significativos, permitindo melhorias na produção, monitoramento de cultivos, otimização de recursos e tomada de decisões mais precisas. ")
            print("\nÉ importante ressaltar que a aplicação da IA Generativa na agricultura requer a disponibilidade de dados de qualidade, como dados climáticos, dados genéticos, informações sobre solos e outras variáveis relevantes. \nAlém disso, é necessário adaptar e personalizar as soluções de IA de acordo com as necessidades específicas de cada propriedade agrícola e cultura cultivada.")
            print("\n1 - Geração de cultivos virtuais: A IA Generativa pode ser usada para simular e gerar cultivos virtuais com base em dados agrícolas históricos e modelos de crescimento de plantas. \nEssa simulação virtual permite testar diferentes cenários e condições, como mudanças climáticas, variações de solo e uso de fertilizantes, para otimizar o crescimento das culturas e antecipar possíveis problemas.")
            print("\n2 - Otimização de recursos: A IA Generativa pode ser usada para otimizar o uso de recursos agrícolas, como água, fertilizantes e defensivos agrícolas. \nCom base em dados de sensores e monitoramento em tempo real, a IA pode gerar recomendações precisas sobre a quantidade adequada de recursos a serem aplicados em cada área específica, maximizando a eficiência e minimizando o desperdício.")
            print("\n3 - Melhoria da genética das plantas: A IA Generativa pode ser aplicada para melhorar a genética das plantas, gerando combinações de características desejáveis. \nA IA pode analisar grandes volumes de dados genômicos e fenotípicos para identificar combinações promissoras que resultem em plantas mais resistentes a pragas, tolerantes a condições adversas e com maior produtividade.")
            print("\n4 - Monitoramento de saúde das plantas: A IA Generativa pode ser usada para monitorar a saúde das plantas de forma contínua e automatizada. \nCom base em imagens de drones, câmeras ou sensores de campo, a IA pode identificar sinais precoces de doenças, deficiências nutricionais ou estresse hídrico, permitindo ações rápidas e precisas para minimizar os danos às culturas.")
            print("\n5 - Previsão de colheitas: A IA Generativa pode ser usada para prever a produtividade e o tempo de colheita das culturas com base em dados históricos, condições climáticas atuais e outros fatores relevantes. \nEssas previsões podem ajudar na otimização do planejamento de colheita, armazenamento e logística, garantindo uma melhor gestão da cadeia de suprimentos agrícolas.")
        
        elif opcao == 5:
            clima()

        elif opcao == 6:
            print("Obrigado pela contribuição")
            exit()
        else:
            print("Opção inválida")
    except ValueError:
        print("Valor informado inválido")
    
