import os

#Lista que vai armazenar as motos
lista_moto = [["Automatica","Kawasaki","Roxa",230]]

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

    def infoMoto(self):
        print(f"Marca: {self.marca}")
        print("Modelo.....:" + " " + self.modelo)
        print("Cor.......:" + " " + self.cor)
        print("Vel. Max..:" + " " + self.vel_max)