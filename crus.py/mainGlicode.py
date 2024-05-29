from classesCrudCadastros import crud_cadastro

classeGlicode = crud_cadastro

from classesCrudCadastros import Funcionalidades
classeGlicode2 = Funcionalidades



while True:

    login = 'defoult'
    continuos = 1
    userClass = ''

    while True:
        userFirstAction = str(input('\no que você deseja fazer?\n\n[1] fazer login\n[2] criar usuário\n[3] sair do sistema\n\n')).strip()

        try:
            userFirstAction = int(userFirstAction)

        except:
            print('\nresposta inválida, tente novamente')

        if userFirstAction in (1, 2, 3):
            break

    while True:

        while True:
            match userFirstAction:

                case 1:
                        login = classeGlicode.login()

                        if login == 'defoult':

                            print('\nusuário ou senha incorretos')
                            continuos = classeGlicode2.verificacao_de_prossegimento('continuar tentando', 'retornar ao menu anterior')
                            break

                        else:

                            userClass = classeGlicode.verificação_classe_usuário(login)
                            break

                case 2:
                    classeGlicode.CreateOrdinaryUser()
                    break

                case 3:
                    break

        if continuos == 2 or userFirstAction == 3 or login == 'defoult' or userClass != '':
            break

    if continuos == 2 or userFirstAction == 3:
            break

    if userClass == 'adiministrador':

        while True:
        
            userChoise = classeGlicode.menuFuncionalidadesAdm()

            match userChoise:

                case 1:

                    classeGlicode.CreateAdmUser()

                case 2:

                    verify = classeGlicode.Read()

                    if verify == 2:
                        break

                case 3:

                    classeGlicode.edição_usuário(login)

                case 4:

                    verify = classeGlicode.Delete()

                    if verify == 2:
                        break

            userProceed = classeGlicode2.verificacao_de_prossegimento('a utilizar alguma outra funcionalidade', 'voltar para menu principal')

            if userProceed == 2:
                break

    elif userClass == 'paciente':

        while True:

            user_choise = classeGlicode2.menu_funcionalidades_paciente()

            if user_choise == 9:
                break

            classeGlicode2.match_funcionalidades_pacientes(user_choise, login)

    elif userClass == 'profissional de saúde':

        while True:

            user_choise = classeGlicode.menuFuncionalidadesProfissionalDeSaúde()

            if user_choise == 3:
                break

            match user_choise:

                case 1:

                    menuChoise = classeGlicode.menuPerfilUsuário()

                    classeGlicode.matchPerfilUsuário(menuChoise, login)

                case 2:

                    import json
                    def main():
                            while True:
                                print("\n=== Dicas para um estilo de vida saudável ===")
                                print("1. Exibir dicas")
                                print("2. Adicionar dica")
                                print("3. Atualizar dica")
                                print("4. Excluir dica")
                                print("5. Sair")
                                opcao = input("Selecione uma opção: ")

                                if opcao == "1":
                                    exibir_dicas()
                                elif opcao == "2":
                                    adicionar_dica()
                                elif opcao == "3":
                                    atualizar_dica()
                                elif opcao == "4":
                                    excluir_dica()
                                elif opcao == "5":
                                    print("Saindo...")
                                    break
                                else:
                                    print("Opção inválida. Tente novamente.")
                        # Função para carregar os dados do arquivo JSON
                    def carregar_dicas():
                            try:
                                with open("dicas_saude.json", "r") as file:
                                    dicas = json.load(file)
                            except FileNotFoundError:
                                dicas = []
                            return dicas
                        # Função para exibir todas as dicas
                    def exibir_dicas():
                            dicas = carregar_dicas()
                            if dicas:
                                print("Dicas para um estilo de vida saudável:")
                                print("==========================================")
                                for i, dica in enumerate(dicas, 1):
                                    
                                    print(f"{i}. {dica}")
                                    print("------------------------------------------")
                            else:  
                                print("Nenhuma dica encontrada.")
                        # Função para salvar os dados no arquivo JSON
                    def salvar_dicas(dicas):
                            with open("dicas_saude.json", "w") as file: 
                                json.dump(dicas, file, indent=4) #dump converte arquivos p/ python
                        # Função para adicionar uma nova dica
                    def adicionar_dica():
                            dicas = carregar_dicas()
                            nova_dica = input("Digite a nova dica para um estilo de vida saudável: ")
                            dicas.append(nova_dica) #append para deixar em lista / ADD POR ULTIMO
                            salvar_dicas(dicas)
                            print("Dica adicionada com sucesso.")

                        # Função para atualizar uma dica existente
                    def atualizar_dica():
                            dicas = carregar_dicas()
                            exibir_dicas()
                            indice = int(input("Digite o número da dica que deseja atualizar: ")) - 1
                            if 0 <= indice < len(dicas):
                                nova_dica = input("Digite a nova versão da dica: ")
                                dicas[indice] = nova_dica
                                salvar_dicas(dicas)
                                print("Dica atualizada com sucesso.")
                            else:
                                print("Índice inválido.")

                        # Função para excluir uma dica
                    def excluir_dica():
                            dicas = carregar_dicas()
                            exibir_dicas()
                            indice = int(input("Digite o número da dica que deseja excluir: ")) - 1
                            if 0 <= indice < len(dicas):  # se nao for zero ou maior que o len=tamanho da lista
                                del dicas[indice]
                                salvar_dicas(dicas)
                                print("Dica excluída com sucesso.")
                            else:
                                print("Índice inválido.")


                            main()

                case 3:
                    
                    break

    else:
        pass
