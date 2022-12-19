#Importando a biblioteca OS
import os
from Carro import *
from Moto import *
from Bicicleta import *

#Função para exibir o menu de seleção
def menu():
    os.system('cls')
    print("-----------MENU-----------\n")
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
        print("NOVO CARRO")

        print("\nMarca do carro")
        marca_carro = input("Digite aqui: ")

        print("\nModelo do carro")
        mod_carro = input("Digite aqui: ")

        print("\nCor do carro")
        cor_carro = input("Digite aqui: ")

        print("\nVelocidade do carro")
        vel_carro = int(input("Digite aqui: "))

        carro = Carro(marca_carro, mod_carro, cor_carro, str(vel_carro))
        lista_carro.append(carro)
        print("\nVeiculo adicionado!\n")
        os.system('pause')

    elif selc_veic == "2":
        os.system('cls')
        print("NOVA MOTO")

        print("\nMarca da moto")
        marca_moto = input("Digite aqui: ")

        print("\nModelo da moto")
        mod_moto = input("Digite aqui: ")

        print("\nCor da moto")
        cor_moto = input("Digite aqui: ")

        print("\nVelocidade da moto")
        vel_moto = int(input("Digite aqui: "))

        moto = Moto(marca_moto, mod_moto, cor_moto, str(vel_moto))
        lista_moto.append(moto)
        print("\nVeiculo adicionado!\n")
        os.system('pause')

    elif selc_veic == "3":
        os.system('cls')
        print("NOVA BICICLETA")

        print("\nMarca da Bicicleta")
        marca_bike = input("Digite aqui: ")

        print("\nDigite o modelo da bicicleta")
        mod_bici = input("Digite aqui: ")

        print("\nDigite a cor da bicicleta")
        cor_bici = input("Digite aqui: ")

        bicicleta = Bicicleta(marca_bike, mod_bici, cor_bici)
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
        print("INFO. CARRO\n")
        try:
            if len(lista_carro) == 0:
                print("Nao ha carros adicionados!\n")
                os.system('pause')
            elif len(lista_carro) > 0:
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
        print("INFO. MOTO\n")
        try:
            if len(lista_moto) == 0:
                print("Nao ha motos adicionadas\n")
                os.system('pause')
            elif len(lista_moto) > 0:
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
        print("INFO. BICICLETA\n")
        try:
            if len(lista_bicicleta) == 0:
                print("Nao ha bicicletas adicionadas!\n")
                os.system('pause')
            elif len(lista_bicicleta) > 0:
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
            if len(lista_carro) == 0:
                print("Nao ha carros adicionados!\n")
                os.system('pause')
            elif len(lista_carro) > 0:
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
            if len(lista_moto) == 0:
                print("Nao ha motos adicionadas!\n")
                os.system('pause')
            elif len(lista_moto) > 0:
                for moto in lista_moto:
                    print(f"- {moto}")
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
            if len(lista_bicicleta) == 0:
                print("Nao ha bicicletas adicionadas!\n")
                os.system('pause')
            elif len(lista_bicicleta) > 0:
                for bike in lista_bicicleta:
                    print(f"- {bike}")
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
    print("\nCARROS: " + str(len(lista_carro)))
    if len(lista_carro) == 0:
        print("Nao ha carros adicionados!")
    elif len(lista_carro) > 0:
        for carro in lista_carro:
            print(f"{carro}")

    print("\nMOTOS: " + str(len(lista_moto)))
    if len(lista_moto) == 0:
        print("Nao ha motos adicionadas!")
    elif len(lista_moto) > 0:
        for moto in lista_moto:
            print(f"{moto}")

    print("\nBICICLETAS: " + str(len(lista_bicicleta)))
    if len(lista_bicicleta) == 0:
        print("Nao ha bicicletas adicionadas!")
    elif len(lista_bicicleta) > 0:
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