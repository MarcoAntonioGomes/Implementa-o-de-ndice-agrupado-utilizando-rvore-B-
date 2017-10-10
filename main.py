from ArvoreBMais import *
from inserirNaArvore import *
from random import randint

if __name__ == "__main__":
    entrada = list()
    Arvore = noArvore(10)
    Arvore.raiz = True
    Arvore.folha = True
    novaentrada = None
  #  print(Arvore.ocupacaoMaxima)
   # print(Arvore.verificaSePaginaFolhaEncheu())

    for j in range(10000):
        for i in range(10):
            entrada.append(randint(0,10000))
       # print(entrada)
        #print(entrada[0])
        #print("\n")
        Arvore = inserirNaArvore(Arvore, entrada, novaentrada)
        #print("End",Arvore)
       # print("Endereço",Arvore)
        entrada = list()

