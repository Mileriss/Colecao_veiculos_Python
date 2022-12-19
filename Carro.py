#Lista para armazenar os carros
lista_carro = []

#Criando a classe de veículo: Carro
class Carro:
    marca_carro = ""
    modelo_carro = ""
    cor_carro = ""
    vel_max_carro = 0
    def __init__(self, marca_carro, modelo_carro, cor_carro, vel_max_carro):
        self.marca = marca_carro
        self.modelo = modelo_carro
        self.cor = cor_carro
        self.vel_max = vel_max_carro

    def infoCarro(self):
        print(f"Marca: {self.marca}")
        print("Modelo.....:" + " " + self.modelo)
        print("Cor.......:" + " " + self.cor)
        print("Vel. Max..:" + " " + self.vel_max)