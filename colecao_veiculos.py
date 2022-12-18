#Importando a biblioteca OS
import os
from Carro import *
from Moto import *
from Bicicleta import *

def menu():
    print("MENU - Selecione uma opcao\n\n")
    print("1 - Adicionar novo veiculo")
    print("2 - Info. Veiculo")
    print("3 - Deletar veiculo")
    print("4 - Listar veiculos")
    print("5 - Finalizar programa")

def addVeiculo():
    os.system('cls')
    print("Adicionar novo veiculo\n\n")
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    if selc_veic == "1":
        os.system('cls')
        print("Digite o modelo do carro\n")
        mod_carro = input("Digite aqui: ")
        print("Digite a marca do carro\n")
        marca_carro = input("Digite aqui: ")
        print("Digite a cor do carro\n")
        cor_carro = input("Digite aqui: ")
        print("Digite a velocidade do carro\n")
        vel_carro = int(input("Digite aqui: "))
        carro = Carro(mod_carro, marca_carro, cor_carro, str(vel_carro))
        lista_carro.append(carro)
        print("\n\nVeiculo adicionado!")
    elif selc_veic == "2":
        os.system('cls')
        print("Digite o modelo da moto\n")
        mod_moto = input("Digite aqui: ")
        print("Digite a marca da moto\n")
        marca_moto = input("Digite aqui: ")
        print("Digite a cor da moto\n")
        cor_moto = input("Digite aqui: ")
        print("Digite a cor da moto\n")
        vel_moto = int(input("Digite aqui: "))
        moto = Moto(mod_moto, marca_moto, cor_moto, str(vel_moto))
        lista_moto.append(moto)
        print("\n\nVeiculo adicionado!")
    elif selc_veic == "3":
        os.system('cls')
        print("Digite o modelo da bicicleta\n")
        mod_bici = input("Digite aqui: ")
        print("Digite a cor da bicicleta\n")
        cor_bici = input("Digite aqui: ")
        print("Digite a quantidade de rodas da bicicleta\n")
        rodas_bici = int(input("Digite aqui: "))
        bicicleta = Bicicleta(mod_bici, cor_bici, str(rodas_bici))
        lista_bicicleta.append(bicicleta)
        print("\n\nVeiculo adicionado!")
    else:
        print("Algo deu errado...")

def infoVeiculo():
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    if selc_veic == "1":
        for carro in lista_carro:
            print(f"- {carro}")
    elif selc_veic == "2":
        for moto in lista_moto:
            print(f"- {moto}")
    elif selc_veic == "3":
        for bike in lista_bicicleta:
            print(f"- {bike}")
    else:
        print("Algo deu errado...")

def delVeiculo():
    selc_veic = input("Selecione o tipo de veiculo: \n1 - Carro\n2 - Moto\n3 - Bicicleta\nDigite aqui: ")
    if selc_veic == "1":
        try:
            print("Selecione qual veiculo deseja excluir")
            print(f"- {lista_carro}")
            excl_veic = input("Digite aqui: ")
            del lista_carro[int(excl_veic)]
            print("Veiculo deletado!")
        except:
            print("Veiculo nao existe na lista")
    elif selc_veic == "2":
        try:
            print("Selecione qual veiculo deseja excluir")
            print(f"- {lista_moto}")
            excl_veic = input("Digite aqui: ")
            del lista_moto[int(excl_veic)]
            print("Veiculo deletado!")
        except:
            print("Veiculo nao existe na lista")
    elif selc_veic == "3":
        try:
            print("Selecione qual veiculo deseja excluir")
            print(f"- {lista_bicicleta}")
            excl_veic = input("Digite aqui: ")
            del lista_bicicleta[int(excl_veic)]
            print("Veiculo deletado!")
        except:
            print("Veiculo nao existe na lista")
    else:
        print("Algo deu errado...")

def listarVeiculo():
    print("Veiculos adicionados\n\n")
    print("CARROS:")
    for carro in lista_carro:
        print(f"{lista_carro[:]}")
    print("MOTOS:")
    for moto in lista_moto:
        print(f"{lista_moto[:]}")
    print("BICICLETAS:")
    for bike in lista_bicicleta:
        print(f"{lista_bicicleta[:]}")

def finalizarPrograma():
    os.system('cls')
    print("Obrigado por ter utilizado este programa!")
    os.system('pause')
    quit("Finalizando o programa...")