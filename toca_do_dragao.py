print("""Seja Bem-Vindo a Toca do Dragão!
Onde as Armas e os Equipamentos são forjados sob Fogo Dracônico!""")

print("Você possui um saldo de 300 Moedas de Ouro.")

print("Para primeiro acesso, digite 'usuario' no campo 'Usuário' e '1234' no campo 'Senha'.")

acesso_correto = False

while acesso_correto == False:
    login = input("Qual é o nome de usuário? ")

    senha = input("Qual é a senha? ")

    if login == "usuario":
        if senha == "1234":
            acesso_correto = True
            print("O seu acesso foi autenticado com sucesso!")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não cadastrado!")

produtos = ["Espada de Aço","Arco de Madeira","Escudo Redondo","Lança de Ferro","Armadura de Couro"]
precos = [75, 50, 90, 120, 150]
estoque = [3, 2, 4, 2, 1]
moedas = 300


carrinho = []


finalizar_compra = False

while finalizar_compra == False:
    opcao = input(""" Toca do Dragão
    Selecione uma opção:
    1 - Ver produtos
    2 - Comprar produtos
    3 - Ver carrinho/saldo restante
    4 - Finalizar compra 
    Opção: """)

    if opcao == "1":
        print("""
        Espada de Aço - 75 Moedas de Ouro - Estoque: 3
        Arco de Madeira - 50 Moedas de Ouro - Estoque:2
        Escudo Redondo - 90 Moedas de Ouro - Estoque:4
        Lança de Ferro - 120 Moedas de Ouro - Estoque:2
        Armadura de Couro - 150 Moedas de Ouro - Estoque:1""")
    elif opcao == "2":
        print(""" Produtos Disponíveis:
            1 - Espada de Aço - 75 Moedas de Ouro - Estoque: 3
            2 - Arco de Madeira - 50 Moedas de Ouro - Estoque:2
            3 - Escudo Redondo - 90 Moedas de Ouro - Estoque:4
            4 - Lança de Ferro - 120 Moedas de Ouro - Estoque:2
            5 - Armadura de Couro - 150 Moedas de Ouro - Estoque:1""")
        opcao_menu2 = int(input("Qual produto deseja comprar? "))
        indice_produto = opcao_menu2 - 1

        print(f"Você selecionou: {produtos[indice_produto]}")
        quantidade_menu2 = int(input("Quantas unidades deseja comprar? "))
        if quantidade_menu2 <= estoque[indice_produto] and quantidade_menu2 * precos[indice_produto] <= moedas:
            print(f" {quantidade_menu2} {produtos[indice_produto]} foi adicionado na sua cesta de compras!")
            estoque[indice_produto] = estoque[indice_produto] - quantidade_menu2
            carrinho.append([produtos[indice_produto], quantidade_menu2])
            moedas = moedas - (quantidade_menu2 * precos[indice_produto])
        else:
            print("Não foi possível adicionar o produto ao carrinho. Verifique seu saldo e a disponibilidade em estoque.")

    elif opcao == "3":
        for numero, compras in enumerate(carrinho, 1):
            print(f"{numero} - {compras[0]}, {compras[1]} unidades.")

        print(f"Saldo restante: {moedas} moedas de ouro.")

    elif opcao =="4":
        opcao_finalizar_compra = input("""Deseja finalizar a compra?
        1 - Sim
        2 - Não
        Opção: """)
        if opcao_finalizar_compra == "1":
            print("A sua compra foi feita com sucesso!")

            for numero, compras in enumerate(carrinho, 1):
                print(f"{numero} - {compras[0]}, {compras[1]} unidades.")

            print("Volte sempre, viajante!")
            finalizar_compra = True

        
            


    

            


        
        
        
    



