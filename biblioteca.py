#Classe Pessoa
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

#Classe Conta
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
<<<<<<< HEAD

#Classe Animal
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
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} latiu pra burro porque queria brincar")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"{self.nome} mugiu pra burro")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def Guinchar(self):
        print(f"{self.nome} guinchou fofamente")

#Classe Ingresso
class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O valor do ingresso é {self.valor}")
class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5
    def imprimiValor(self, valor):
        print(f"O valor do ingresso Vip é {self.valor}")

#Classe forma
class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super(). __init__(self)
    def calculaArea(self, base, altura):
        self.area = base * altura
        print(f"A area do retangulo é: {self.area}")
    def calculaPerimetro(self, base, altura):
        self.perimetro = 2*(base + altura)
        print(f"O perimetro do retangulo é: {self.perimetro}")

#Class Atleta
class Atleta():
    def __init__(self, aposentado, peso):
        self.aposentado = False
        self.peso = False
    def aposentar(self):
        print(f"O atleta de aposentou")
    def aquecer(self):
        print(f"O atleta se aqueceu")
class Corredor(Atleta):
    def Correr(self):
        print(f"O Atleta está corredor como o Usain Bolt")
class Nadador(Atleta):
    def Nadar(self):
        print(f"O Atleta está nadando como um peixe")
class Ciclista(Atleta):
    def Pedalar(self):
        print(f"O Atleta está andando na sua bike maneira")
=======
>>>>>>> c9209785a5a450ff2152238f92a589dfecebf990

