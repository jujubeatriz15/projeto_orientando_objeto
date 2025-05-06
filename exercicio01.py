from biblioteca import Pessoa

aluno01 = Pessoa("julia", 22, 103)
print(f"{aluno01.nome} tem {aluno01.idade} anos e {aluno01.peso} kilos.")

aluno01.falar()
aluno01.comer("cachorro quente")
aluno01.dormir()
