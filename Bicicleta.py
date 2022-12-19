<<<<<<< HEAD
#Lista que vai armazenas as bicicletas
lista_bicicleta = []

#Criando a classe de veículo: Bicicleta
class Bicicleta:
    marca_bike = ""
    modelo_bike = ""
    cor_bike = ""
    def __init__(self, marca_bike, modelo_bike, cor_bike):
        self.marca = marca_bike
        self.modelo = modelo_bike
        self.cor = cor_bike
        
=======
import os

#Lista que vai armazenas as bicicletas
lista_bicicleta = [["Monark","Verde","4"]]
#Criando a classe de veículo: Bicicleta
class Bicicleta:
    modelo_bike = ""
    cor_bike = ""
    qtde_rodas_bike = 0
    def __init__(self, modelo_bike, cor_bike, qtde_rodas_bike):
        self.modelo = modelo_bike
        self.cor = cor_bike
        self.qtde_rodas = qtde_rodas_bike
>>>>>>> ba743fe4602617482865126b971cc3fdb3cf9306

    def infoBike(self):
        print(f"Marca: {self.marca}")
        print("Modelo.......:" + " " + self.modelo)
        print("Cor..........:" + " " + self.cor)
<<<<<<< HEAD
=======
        print("Qtde. Rodas..:" + " " + self.qtde_rodas)
>>>>>>> ba743fe4602617482865126b971cc3fdb3cf9306
