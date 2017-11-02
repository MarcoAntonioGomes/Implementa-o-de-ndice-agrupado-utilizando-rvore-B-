


#Função para encontrar no nó pai um irmão que tenha chave extras para distribuir com irmão que esta com chaves abaixo do mínimo
def encontraRIrmaoChavesExtras(NoPai):
    for i in range(len(NoPai.entradas)):
        if not (NoPai.entradas[i].verificaSeNoInternoMinimo()):
            return NoPai.entradas[i]
    return None

def encontraRIrmaoEntradasExtras(NoPai):
    for i in range(len(NoPai.entradas)):
        if not (NoPai.entradas[i].verificaSePaginaFolhaCapacidadeMinima()):
            return tuple(NoPai.entradas[i],NoPai.indices[i-1])
        return None



#Função para redistribuir as chaves entre os irmão afim de manter a estrutura da árvore
#Os parâmetros N e S são nós irmãos
def redistribuirChavesInternas(N,S):
    mediana = int(N.ocupacaoMaxima/2)



    for i in range(mediana,(len(S.indices))):
        indiceARemover = S.indices[i]
        ponteiroARemover = S.entradas[i+1]
        N.indices.append(indiceARemover)
        N.indices.sort();
        N.entradas.insert((no.indices.index(indiceARemover) + 1),ponteiroARemover)
        S.indices.remove(indiceARemover)
        S.entradas.remove(ponteiroARemover)

#Função para intercalar, juntar duas páginas, que estão com chaves abaixo ou no mínimo da quntidade estabelecida
#Os parâmetros N e M são nós irmãos, chaveDeDivisão é a chave no pai que da acesso aos duas páginas filhas irmãs
#Para intercalar deve se descer do pai a chaveDeDivisão para a nova página abaixo que esta unificando os dois irmãos antigos
def intercalarChavesInternas(N,M,chaveDeDivisao):


    N.indices.append(ChaveDeDivisao)
    entradaAMover = M.entradas[0]
    N.entradas.append(entradaAMover)
    for i in range((len(M.indices))):
        indiceAMover = M.indices[i]
        entradaAMover = M.entradas[i+1]
        N.indices.append(indiceAMover)
        N.entradas.append(entradaAMover)


def redistribuirEntradasFolhas(N,S):

    qtdDeEntradasExtras = len(S.entradas)
    if not (S.verificaSePaginaFolhaCapacidadeMinima()):
        for i in range(qtdDeEntradasExtras):

            entradaARemover = S.entradas[i]
            N.entradas.append(entradaARemover)
            S.entradas.remove(entradaARemover)

    novaChaveDeAcessoNoPai = S.entradas[0][0]
    return novaChaveDeAcessoNoPai

def intercalarEntradasFolha(N,M):

    #print("Estou Intercalando as Folhas")
    qtdDeEntradas = len(M.entradas)

    for i in range(qtdDeEntradas):
        entradaAMover = M.entradas[i]
        N.entradas.append(entradaAMover)

    N.proximo = M.proximo

"""
Função para remoção de registros da árvore 

Parâmetros

ponteiropai - nó da árvore que é pai de outros nós subsequentes na subarvore, usado para acesso ao irmão para intercalação de página e redistribuição de registros ou chaves 
entre os nós irmãos (A variável esta com nome de ponteiro devido ao pseudocódigo do Ramakrishan que trabalha com ponteiros, mas que aqui é somente a referência do objeto) 

entrada - chave do registro a ser removido

ponteirono - Inicialmente nó raiz da árvore, depois vai sendo alterado recursivamente conforme a busca pela página folha para remoção acontece.

entradafilhaantiga - usada para realizar as devidas alterações nos nós pais quando duas páginas forem intercaladas ou quando houver redistribuição de chaves ou registros

"""

def excluirDaArvore(ponteiropai, ponteirono, entrada, entradafilhaantiga):

    if not (ponteirono.folha):
        #Busca recursivamente a página folha adequada para a remoção do registro

        if (entrada < ponteirono.indices[0]):
            entradafilhaantiga = excluirDaArvore(ponteirono,ponteirono.entradas[0], entrada, entradafilhaantiga)

            for i in range((len(ponteirono.indices) - 1)):

                if (entrada >= ponteirono.indices[i] and chave < ponteirono.indices[i + 1]):
                    entradafilhaantiga = excluirDaArvore(ponteirono,ponteirono.entradas[i + 1], entrada,entradafilhaantiga)

        if (entrada >= ponteirono.indices[(len(ponteirono.indices) - 1)]):
            entradafilhaantiga = excluirDaArvore(ponteirono, ponteirono.entradas[(len(ponteirono.indices))],entrada,entradafilhaantiga)

        if(entradafilhaantiga == None):
            return #Processo de Remoção terminou

        else:
            if(ponteiropai != None):
                ponteiropai.entradas.remove(entradafilhaantiga)
            if not (ponteirono.verificaSeNoInternoEncheu()):
                entradafilhaantiga = None
                return entradafilhaantiga
            elif(encontraRIrmaoChavesExtras(ponteiropai) != None):

                        redistribuirChavesInternas(ponteirono,encontraRIrmaoChavesExtras(ponteiropai)) #Redistribuição para nós internos
                        entradafilhaantiga = None
                        return entradafilhaantiga
            else:
                #Intercalação de Páginas para nós internos
                irmaoADireita = (ponteiropai.entradas[(ponteiropai.entradas.index(ponteirono))+1])
                indiceADireita = ponteiropai.indices[(ponteiropai.entradas.index(ponteirono))]
                intercalarChavesInternas(ponteirono,irmaoADireita,indiceADireita)
                ponteiropai.entradas.remove(irmaoADireita)
                ponteiropai.indices.remove(indiceADireita)
                entradafilhaantiga = None
                return entradafilhaantiga

    if(ponteirono.folha):
        if not (ponteirono.verificaSePaginaFolhaCapacidadeMinima()):
            for i in range((len(ponteirono.entradas))):

                if (entrada == ponteirono.entradas[i][0]): #Verifica se chave de busca é igual a primeira posição da lista que corresponde aos registros, que no caso é a chave
                                                           #Conrrespondente aquele registro
                    ponteirono.entradas.remove( ponteirono.entradas[i]) # Remove registro
                    entradafilhaantiga = None
                    return entradafilhaantiga
        elif(encontraRIrmaoEntradasExtras(ponteiropai) != None): # Se o nó esta na capacidade mínima ou abaixo dela e se tem irmão com registros extras
                                                                 # Realiaza se a redistribuição uniformimente dos registros
            dadosRemove = encontraRIrmaoEntradasExtras(ponteiropai)
            noIrmao = dadosRemove[0]
            chaveDeAcesso = dadosRemove[1]
            chaveDeTrocaNoPai = redistribuirEntradasFolhas(ponteirono,noIrmao)# Chama a função para realizar a redistribuição
            ponteiropai.indices[ponteiropai.indices.index(chaveDeAcesso)] = chaveDeTrocaNoPai # Troca as chaves que dão acesso as páginas para garantir a estrutura da árvore
            entradafilhaantiga = None
            return entradafilhaantiga
        else:
            # Senão há irmãos com  registros extras realiza se a intercalação das páginas folhas
            #Para que a intercalação funcione deve se passar pará o nó referência, as chavés do nó pagina a direita (irmão a direita)
            #O if abaixo inverte os casos para que intercalação funcione quando se esta tentando intercalar um nó referencia e a direita dele não existe mais nós irmãos
            #Logo pega se o nó a esquerda do ultimo e nó a direita fica sendo o ultima nó
            if((len(ponteiropai.entradas)-1) == ponteiropai.entradas.index(ponteirono)): # Verifica se o indice do nó é equivalente ao ultimo nó no pai
                irmaoAEsquerda = ponteiropai.entradas[(ponteiropai.entradas.index(ponteirono)) - 1 ]
                intercalarEntradasFolha(irmaoAEsquerda, ponteirono)
                return irmaoAEsquerda
            else:
                irmaoADireita = ponteiropai.entradas[(ponteiropai.entradas.index(ponteirono))+1]
                intercalarEntradasFolha(ponteirono,irmaoADireita)
                return irmaoADireita




