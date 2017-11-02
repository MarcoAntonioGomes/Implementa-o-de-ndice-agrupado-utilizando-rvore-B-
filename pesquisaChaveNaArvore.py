from ArvoreBMais import *
"""
Busca por igualdade
Parâmetros
Arvore - nó raiz da árvore a se realizar a busca
chave - chave a se buscar
 
"""
def pesquisarNaArvore(Arvore,chave):
    global pagina
    if(Arvore.folha): # Se for folha, busca a entrada de dados que tem chave de busca desejada
        for i in range((len(Arvore.entradas))):

            print("Chave",chave," == Indice ",Arvore.entradas[i][0])
            if(chave == Arvore.entradas[i][0]):
                return Arvore.entradas[i] #Retorna o registro encontrado
        return None #Se não encontrar, retorna nulo
    else :
        #Busca recursivamente a página folha que contém a chave de busca
        if (chave < Arvore.indices[0]):

            return pesquisarNaArvore(Arvore.entradas[0], chave)

        for i in range ((len(Arvore.indices)-1)):


                if(chave >= Arvore.indices[i] and chave < Arvore.indices[i+1]):


                    return pesquisarNaArvore(Arvore.entradas[i+1],chave)


        if (chave >= Arvore.indices[(len(Arvore.indices)-1)]):
            return pesquisarNaArvore(Arvore.entradas[(len(Arvore.indices))], chave)