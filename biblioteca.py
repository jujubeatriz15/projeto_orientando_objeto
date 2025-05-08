class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def comer(self):
        if self.comendo == True:
            print(f"{self.nome} ja esta comendo")
        elif self.dormindo == True:
            print(f"{self.nome} ja esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} ja esta falando")
        else:
            print(f"E {self.nome} começou a rangar")
            self.comer == True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} ja esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} ja esta falando")
        elif self.comendo == True:
            print(f"{self.nome} ja esta comendo")
        else:
            print(f"E {self.nome} começou a mimir")
            self.dormir == True

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} ja esta falando")
        elif self.comendo == True:
            print(f"{self.nome} ja esta comendo")
        elif self.dormindo == True:
            print(f"{self.nome} ja esta dormindo")
        else:
            print(f"E {self.nome} começou a tagarelar")
            self.falar == True

class Conta():
    def __init__(self, numero, deposito, nome, tipo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0
        self.status_conta = False
        self.deposito = False


    def ativarConta(self):
        if self.status_conta == True:
            print("sua conta ja esta ativa")
        elif self.status_conta == False:
                self.status_conta = True

    def status_contaa(self):
        if self.status_conta == True:
            print("conta ativada")
        else:
            print("conta desarivada")

    def depositar(self):
        if self.deposito