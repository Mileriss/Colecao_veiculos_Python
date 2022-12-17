#Importando a biblioteca OS
import os

#Criando a classe de veículo: Carro
class Carro:
    modelo_carro = ""
    marca_carro = ""
    cor_carro = ""
    vel_max_carro = 0
    def __init__(self, modelo_carro, marca_carro, cor_carro, vel_max_carro):
        self.modelo = modelo_carro
        self.marca = marca_carro
        self.cor = cor_carro
        self.vel_max = vel_max_carro

#Criando a classe de veículo: Moto
class Moto:
    modelo_moto = ""
    marca_moto = ""
    cor_moto = ""
    vel_max_moto = 0
    def __init__(self, modelo_moto, marca_moto, cor_moto, vel_max_moto):
        self.modelo = modelo_moto
        self.marca = marca_moto
        self.cor = cor_moto
        self.vel_max = vel_max_moto

#Criando a classe de veículo: Bicicleta
class Bicicleta:
    modelo_bike = ""
    cor_bike = ""
    qtde_rodas_bike = 0
    def __init__(self, modelo_bike, cor_bike, qtde_rodas_bike):
        self.modelo = modelo_bike
        self.cor = cor_bike
        self.qtde_rodas = qtde_rodas_bike

