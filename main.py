from ArvoreBMais import *
from inserirNaArvore import *
from random import randint
from pesquisaChaveNaArvore import*

if __name__ == "__main__":

    entrada = list()
    Arvore = noArvore(25)
    Arvore.raiz = True
    Arvore.folha = True
    novaentrada = None
  #  print(Arvore.ocupacaoMaxima)
   # print(Arvore.verificaSePaginaFolhaEncheu())

    cont = 0

    for j in range(10000):

        for i in range(25):
            entrada.append(randint(0,10000))
            if(cont == 0):
                chave = entrada[0]
                cont = cont+1
       # print(entrada)
        #print(entrada[0])
        #print("\n")
        Arvore = inserirNaArvore(Arvore, entrada, novaentrada,25)
        #print(len(Arvore.entradas))
        #print("End",Arvore)
       # print("Endereço",Arvore)
        entrada = list()
        #print(Arvore.ocupacaoMaxima)

    #print(cont)
    #print("Quantidade de chaves inseridas: ",qtdChavesInseridas)
    print(len(Arvore.entradas))
    print((Arvore.indices))
    print("Chave", chave)
    print( pesquisarNaArvore(Arvore,chave))
    entrada = list()
    print("-----------------------INSERINDO NOVO REGISTRO--------------------------------")
    for i in range(25):
        entrada.append(randint(0, 10000))
    Arvore = inserirNaArvore(Arvore, entrada, novaentrada, 25)