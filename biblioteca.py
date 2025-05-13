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
        self.deposito = deposito
        self.saldo = 0
        self.limite = 0
        self.status = False



    def ativaConta(self):
        if self.status == True:
            print("sua conta ja esta ativa")
            print("-" * 50)
    def ativarConta(self):
        if self.status == True:
            print("A sua conta ja está ativada")
            print("-" * 50)
        else:
            self.status = True
            print("Conta ja ativa")
            print("-" * 50)

    def depositar(self,valordeposito):
        if self.status == True:
            self.saldo += valordeposito
            print("Valor depositado com sucesso")
            print("-" * 50)
        else:
            print("Conta nao ativa")
            print("-" * 50)

    def VerificacaoSaldo(self):
        if self.saldo == True:
            print(self.saldo)
            print(f"Saldo: {self.saldo}")
            print("-"*50)
        else:
            print("Conta nao ativa")
            print("-"*50)

    def sacar(self,valorsaque):
        if self.status == True:
            self.saldo -= valorsaque
            print("O saque foi efetuado")
            print("-" * 50)
        else:
            print("Conta nao ativa")
            print("-" * 50)

    def desativarConta(self):
        if self.saldo == 0:
            if self.saldo == 0:
                self.status == True
                self.status == False
                print("Conta nao ativa")
                print("-" * 50)
        else:
            print("Conta nao pode ser desativada")

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome} foi comer")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"{self.nome} miou pra burro que nao me deixou dormir")