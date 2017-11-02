from ArvoreBMais import *
"""
Seleção de registros por intervalo
Arvore -  nó raiz da árvore
chaveinicial - chave de busca inicial
chavefinal - chave de busca final, serve para limitar a busca até uma chave final    

"""


def pesquisaIntervaloArvore(Arvore,chaveinicial, chavefinal):

    if(Arvore.folha): #Se a página folha conter o registro com a chave de busca inicial, o algoritimo percore e exibe os registros até encontrar uma chave
                      # que seja menor ou igual a chave final
        for i in range((len(Arvore.entradas))):

            if (chaveinicial == Arvore.entradas[i][0]): # Lista de Lista
                j = i #Achou o registro com a chave
                break
        while(chaveinicial <= Arvore.entradas[j][0] and Arvore.entradas[j][0] < chavefinal):
            print(Arvore.entradas[j]) #Começa a percorrer as folhas e exibir os registros

            j += 1

            if(j == (len(Arvore.entradas))):
                j = 0
                Arvore = Arvore.proximo #Busca a proxima página folha


        return None
    else :
        # Busca recursivamente a página folha que contém a chave de busca
        if (chaveinicial< Arvore.indices[0]):

            return  pesquisaIntervaloArvore(Arvore.entradas[0], chaveinicial,chavefinal)

        for i in range ((len(Arvore.indices)-1)):


                if(chaveinicial >= Arvore.indices[i] and chaveinicial < Arvore.indices[i+1]):


                    return  pesquisaIntervaloArvore(Arvore.entradas[i+1],chaveinicial,chavefinal)


        if (chaveinicial >= Arvore.indices[(len(Arvore.indices)-1)]):
            return  pesquisaIntervaloArvore(Arvore.entradas[(len(Arvore.indices))], chaveinicial,chavefinal)