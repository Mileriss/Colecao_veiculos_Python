import os

#Lista que vai armazenas as bicicletas
lista_bicicleta = []
#Criando a classe de veículo: Bicicleta
class Bicicleta:
    modelo_bike = ""
    cor_bike = ""
    qtde_rodas_bike = 0
    def __init__(self, modelo_bike, cor_bike, qtde_rodas_bike):
        self.modelo = modelo_bike
        self.cor = cor_bike
        self.qtde_rodas = qtde_rodas_bike

    def infoBike(self):
        print("Modelo..........:" + " - " + self.modelo)
        print("Cor.............:" + " - " + self.cor)
        print("Qtde. Rodas........:" + " - " + self.qtde_rodas)
