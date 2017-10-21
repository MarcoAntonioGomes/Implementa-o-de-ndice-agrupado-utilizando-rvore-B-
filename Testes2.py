from Testes import*

if __name__ == "__main__":
    NovoTeste = teste()

    NovoTeste.insereValor(10)

    print(NovoTeste.indices)

    alteraIndice(NovoTeste)

    print(NovoTeste.indices)
