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
        

    def infoBike(self):
        print(f"Marca: {self.marca}")
        print("Modelo.......:" + " " + self.modelo)
        print("Cor..........:" + " " + self.cor)
