from ArvoreBMais import *

def pesquisaIntervaloArvore(Arvore,chaveinicial, chavefinal):

    if(Arvore.folha):

        for i in range((len(Arvore.entradas))):
             #print(Arvore.entradas[i])
            #print("Chave",chave," == Indice ",Arvore.entradas[i][0])
            if (chaveinicial == Arvore.entradas[i][0]):
                j = i
                break
        while(chaveinicial <= Arvore.entradas[j][0] and Arvore.entradas[j][0] < chavefinal):
            print(Arvore.entradas[j])
           # print("Entradas: ",Arvore.entradas)
            j += 1
            #print("j:",j,"len: ",len(Arvore.entradas))
            if(j == (len(Arvore.entradas))):
                j = 0
                Arvore = Arvore.proximo
                #print("Arvore prox: ",Arvore.entrada[j])

        return None
    else :

        if (chaveinicial< Arvore.indices[0]):

            return  pesquisaIntervaloArvore(Arvore.entradas[0], chaveinicial,chavefinal)

        for i in range ((len(Arvore.indices)-1)):


                if(chaveinicial >= Arvore.indices[i] and chaveinicial < Arvore.indices[i+1]):


                    return  pesquisaIntervaloArvore(Arvore.entradas[i+1],chaveinicial,chavefinal)


        if (chaveinicial >= Arvore.indices[(len(Arvore.indices)-1)]):
            return  pesquisaIntervaloArvore(Arvore.entradas[(len(Arvore.indices))], chaveinicial,chavefinal)