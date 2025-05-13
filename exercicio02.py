from biblioteca import Conta

usuario = Conta(1234, 50, "julia", "corrente")

usuario.ativarConta()
usuario.ativarConta()
usuario.VerificacaoSaldo()
usuario.depositar(100)
usuario.sacar(50)
usuario.VerificacaoSaldo()
usuario.desativarConta()
usuario.sacar(50)
usuario.VerificacaoSaldo()
usuario.desativarConta()