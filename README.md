# HORA DA XEPA - GLOBAL SOLUTION - PYTHON - DESCRIÇÃO



O projeto "Hora da Xepa" atua como intermediário entre fornecedores e ONGs, coletando alimentos em boas condições, mas que seriam descartados devido a defeitos estéticos. A coleta é realizada em postos nas feiras, com voluntários e por meio de doações de feirantes e pessoas interessadas em contribuir. O site permite doações de alimentos não perecíveis ou valores em dinheiro. O transporte dos alimentos é feito por caminhões especializados, utilizando inteligência artificial para monitorar em tempo real o estado dos alimentos e tomar ações corretivas para evitar perdas ou avarias. Os alimentos são armazenados em armazéns monitorados por inteligência artificial, que define um limite de estoque de acordo com a demanda, evitando desperdícios e garantindo a qualidade dos alimentos.


O programa desenvolvido aborda o atendimento do usuário no site. O sistema permite o usuário realizar doações de alimentos não perecívies ou uma quantia em dinheiro.

O sistema é composto por um mneu que contém 6 opções, que é chamado dentro de um laço de repetição toda vez que uma operação for finalizada: 

    1 - Sobre o projeto: Mostra uma descrição geral sobre o problema e a solução.
    2 - Fazer doação: Permite que o usuário faça doações de alimentos não perecíveis ou dinheiro.
    3 - Finalizar doações: Permite que o usuário visualize sua cesta de doações e se deseja finalizar.
    4 - Exibe informações sobre o uso de IA na agricultura.
    5 - Exibe uma lista de culturas favoráveis para cultivo de acordo com o clima da região.
    6 - Sair/Encerrar o programa.

    As opções 1 e 4 não chamam nenhuma função. Elas exibem a informação assim que escolhidas.
    As demais opçoes chamam as funções  doacao(), cesta_doacao(), clima(), exit().

    Sobre a funcionalidade Doar:
        - Quando chamada ela permite o usuário escolher entre doações alimentícias e/ou monetárias:
        - Sua funcionalidade é baseada em armazenamento de valores dentro de variáveis e listas.

            - Para doações alimentícias, os sistema permite o usuário escolher entre 3 categorias: Embalados, enlatados e líquidos. Dentro de cada categoria é exibida uma lista com diversos alimentos.
                - O usuário deve selecionar o alimento listado digitando o número que representa o mesmo.
                - Após escolher o alimento, o usuário deve definir a quantidade. A quantidade não pode ser menor ou igual a 0.
                - Após definir a quantidade, o alimento e a quantidade serão armazenados nas listas "cesta" e na lista "qtd_itens"

            - Para doações monetárias, o usuário deve digitar a quantia que deseja doar. O sistema permite apenas valores maiores ou igual a 5, caso contrário o sistema irá gerar um erro e não guardará o valor na lista "valor_doado".

        - Posteriormente ambas doações e suas informações serão armazenadas na lista "resumo".

    Sobre a funcionalidade Finalizar doações:
        - Quando chamada permite o usuário verificar suas escolhas e finalizar. Caso escolha não finalizar o menu é chamado novamente.
        - Caso escolha finalizar, o programa da a escolha de enviar só alimentos e outra para enviar dinheiro ou ambos.

            - Para enviar apenas alimentos, será requisitado ao usuário os seguintes dados: nome, rg, email, telefone e endereço.

            - Para enviar dinheiro ou ambos será rquisitado ao usuário os seguintes dados: nome, rg, email, telefone e endereço, cpf. E o sistema informará as opções de depósito.

            - Após finalizar ambas opções exibirão seus respectivos comprovantes contendo os itens doados, os dados informados e uma mensagem final.

    Sobre a funcionalidade Exibir culturas de acordo com o clima.
        - Permitirá ao usuário escolher entre 7 climas distintos e o sistema exibirá informações de acordo com a escolha.


    Funcionalidade Sair: Encerra o programa.


    ***TODAS AS ESCOLHAS FEITAS NO PROGRAMA SÃO INTERPRETADAS COMO NÚMEROS INTEIROS DE 1 A 10 DEPENDENDO DA QUANTIDADE DE ITENS DE ESCOLHA***

    ***AS VALIDAÇÕES DE INFORMAÇÕES ESTÃO CONCENTRADAS NAS DOAÇÕES, DADOS COMO CPF NÃO ESTÃO SENDO VALIDADOS***

    
