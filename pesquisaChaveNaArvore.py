from ArvoreBMais import *

def pesquisarNaArvore(Arvore,chave):
    global pagina
    if(Arvore.folha):
        for i in range((len(Arvore.entradas))):
            #print(Arvore.entradas[i])
            print("Chave",chave," == Indice ",Arvore.entradas[i][0])
            if(chave == Arvore.entradas[i][0]):
                return entrada[i]
        return None
    else :

        if (chave < Arvore.indices[0]):

            return pesquisarNaArvore(Arvore.entradas[0], chave)

        for i in range ((len(Arvore.indices)-1)):


                if(chave >= Arvore.indices[i] and chave < Arvore.indices[i+1]):


                    return pesquisarNaArvore(Arvore.entradas[i],chave)


        if (chave >= Arvore.indices[(len(Arvore.indices)-1)]):
            return pesquisarNaArvore(Arvore.entradas[(len(Arvore.indices))], chave)