#Importando a biblioteca OS
import os
from Carro import *
from Moto import *
from Bicicleta import *

#Função para exibir o menu de seleção
def menu():
    os.system('cls')
    print("MENU - Selecione uma opcao\n")
    print("1 - Adicionar novo veiculo")
    print("2 - Info. Veiculo")
    print("3 - Deletar veiculo")
    print("4 - Listar veiculos")
    print("5 - Finalizar programa")
    selc_opcao = input("Digite aqui: ")
    return selc_opcao

#Função para criar novos veiculos
def addVeiculo():
    os.system('cls')
    print("ADICIONAR NOVO VEICULO\n")
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    if selc_veic == "1":
        os.system('cls')
        print("NOVO: CARRO")
        print("\nDigite o modelo do carro")
        mod_carro = input("Digite aqui: ")
        print("\nDigite a marca do carro")
        marca_carro = input("Digite aqui: ")
        print("\nDigite a cor do carro")
        cor_carro = input("Digite aqui: ")
        print("\nDigite a velocidade do carro")
        vel_carro = int(input("Digite aqui: "))
        carro = Carro(mod_carro, marca_carro, cor_carro, str(vel_carro))
        lista_carro.append(carro)
        print("\nVeiculo adicionado!\n")
        os.system('pause')
    elif selc_veic == "2":
        os.system('cls')
        print("NOVO: MOTO")
        print("\nDigite o modelo da moto")
        mod_moto = input("Digite aqui: ")
        print("\nDigite a marca da moto")
        marca_moto = input("Digite aqui: ")
        print("\nDigite a cor da moto")
        cor_moto = input("Digite aqui: ")
        print("\nDigite a cor da moto")
        vel_moto = int(input("Digite aqui: "))
        moto = Moto(mod_moto, marca_moto, cor_moto, str(vel_moto))
        lista_moto.append(moto)
        print("\nVeiculo adicionado!\n")
        os.system('pause')
    elif selc_veic == "3":
        os.system('cls')
        print("NOVO: BICICLETA")
        print("\nDigite o modelo da bicicleta")
        mod_bici = input("Digite aqui: ")
        print("\nDigite a cor da bicicleta")
        cor_bici = input("Digite aqui: ")
        print("\nDigite a quantidade de rodas da bicicleta")
        rodas_bici = int(input("Digite aqui: "))
        bicicleta = Bicicleta(mod_bici, cor_bici, str(rodas_bici))
        lista_bicicleta.append(bicicleta)
        print("\nVeiculo adicionado!\n")
        os.system('pause')
    else:
        print("Algo deu errado...")

#Função para visualizar informações de um veiculo
def infoVeiculo():
    os.system('cls')
    print("INFO. DO VEICULO\n")
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    
    if selc_veic == "1":
        os.system('cls')
        print("INFO. CARRO")
        try:
            for carro in lista_carro:
                print(f"- {carro}")
            print("\nDigite o numero do carro que deseja visualizar a info")
            veic_exib = input("Digite aqui: ")
            os.system('cls')
            print("VISUALIZAR INFO. CARRO\n")
            lista_carro[int(veic_exib)].infoCarro()
            print("\n")
            os.system('pause')
        except:
            print("\nCarro nao existe na lista!\n")
            os.system('pause')
    elif selc_veic == "2":
        os.system('cls')
        print("INFO. MOTO")
        try:
            for moto in lista_moto:
                print(f"- {moto}")
            print("\nDigite o numero da moto que deseja visualizar a info")
            veic_exib = input("Digite aqui: ")
            os.system('cls')
            print("VISUALIZAR INFO. MOTO\n")
            lista_moto[int(veic_exib)].infoMoto()
            print("\n")
            os.system('pause')
        except:
            print("\nMoto nao existe na lista!\n")
            os.system('pause')
    elif selc_veic == "3":
        os.system('cls')
        print("INFO. BICICLETA")
        try:
            for bicicleta in lista_bicicleta:
                print(f"- {bicicleta}")
            print("\nDigite o numero da bicicleta que deseja visualizar a info")
            veic_exib = input("Digite aqui: ")
            os.system('cls')
            print("VISUALIZAR INFO. BICICLETA\n")
            lista_bicicleta[int(veic_exib)].infoBike()
            print("\n")
            os.system('pause')
        except:
            print("\nBicicleta nao existe na lista!\n")
            os.system('pause')

#Função para deletar um veiculo criado anteriormente
def delVeiculo():
    os.system('cls')
    print("DELETAR UM VEICULO\n")
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    if selc_veic == "1":
        try:
            os.system('cls')
            print("DELETAR CARRO")
            print("\nSelecione qual veiculo deseja excluir\n")
            for carro in lista_carro:
                print(f"- {carro}")
            print("\n")
            excl_veic = input("Digite aqui: ")
            del lista_carro[int(excl_veic)]
            print("\nVeiculo deletado!\n")
            os.system('pause')
        except:
            print("\nVeiculo nao existe na lista\n")
            os.system('pause')
    elif selc_veic == "2":
        try:
            os.system('cls')
            print("DELETAR MOTO")
            print("\nSelecione qual veiculo deseja excluir\n")
            for moto in lista_moto:
                print(f"- {lista_moto}")
            print("\n")
            excl_veic = input("Digite aqui: ")
            del lista_moto[int(excl_veic)]
            print("\nVeiculo deletado!\n")
            os.system('pause')
        except:
            print("\nVeiculo nao existe na lista\n")
            os.system('pause')
    elif selc_veic == "3":
        try:
            os.system('cls')
            print("DELETAR BICICLETA")
            print("\nSelecione qual veiculo deseja excluir\n")
            for bike in lista_bicicleta:
                print(f"- {lista_bicicleta}")
            print("\n")
            excl_veic = input("Digite aqui: ")
            del lista_bicicleta[int(excl_veic)]
            print("\nVeiculo deletado!\n")
            os.system('pause')
        except:
            print("\nVeiculo nao existe na lista\n")
            os.system('pause')
    else:
        print("Algo deu errado...")
        os.system('pause')

#Função para exibir todos os veiculos criados
def listarVeiculo():
    os.system('cls')
    print("VEICULOS DISPONIVEIS")
    print("\nCARROS:")
    for carro in lista_carro:
        print(f"{carro}")
    print("\nMOTOS:")
    for moto in lista_moto:
        print(f"{moto}")
    print("\nBICICLETAS:")
    for bike in lista_bicicleta:
        print(f"{bike}")
    
    print("\n")
    os.system('pause')

#Função para finalizar o programa
def finalizarPrograma():
    os.system('cls')
    print("Obrigado por ter utilizado este programa!\n\nFinalizando a aplicação...\n")
    os.system('pause'), os.system('cls')
    exit()

#Condição para exibir o menu de seleção
retorno = menu()
while retorno != "6":
    if retorno == "1":
        addVeiculo()
    elif retorno == "2":
        infoVeiculo()
    elif retorno == "3":
        delVeiculo()
    elif retorno == "4":
        listarVeiculo()
    elif retorno == "5":
        finalizarPrograma()
    retorno = menu()

os.system('cls')