#Lista que vai armazenar as motos
lista_moto = []

#Criando a classe de veículo: Moto
class Moto:
    marca_moto = ""
    modelo_moto = ""
    cor_moto = ""
    vel_max_moto = 0
    def __init__(self, marca_moto, modelo_moto, cor_moto, vel_max_moto):
        self.marca = marca_moto
        self.modelo = modelo_moto
        self.cor = cor_moto
        self.vel_max = vel_max_moto

    def infoMoto(self):
        print(f"Marca: {self.marca}")
        print("Modelo.....:" + " " + self.modelo)
        print("Cor.......:" + " " + self.cor)
        print("Vel. Max..:" + " " + self.vel_max)