class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False
    def falar(self, ):
        print(f"{self.nome} começou a tagarelar")
    def comer(self, comida):
        if self.comendo == True:
            print(f"esta rangando {comida}")
    def dormir(self):
        print(f"{self.nome} começou a mimir")
class Pessoa():
    def __init__(self, nome, idade, peso):