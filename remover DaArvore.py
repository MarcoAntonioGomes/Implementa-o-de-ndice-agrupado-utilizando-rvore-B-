

def excluir(ponteiropai, ponteirono, entrada, entradafilhaantiga):

    if not (ponteirono.folha):


        if (chave < ponteirono.indices[0]):
            entradafilhaantiga = excluir(ponteirono,ponteirono.entradas[0], entrada, entradafilhaantiga)

            for i in range((len(Arvore.indices) - 1)):

                if (chave >= ponteirono.indices[i] and chave < ponteirono.indices[i + 1]):
                    entradafilhaantiga = excluir(ponteirono,ponteirono.entradas[i + 1], entrada,entradafilhaantiga)

        if (chave >= ponteirono.indices[(len(ponteirono.indices) - 1)]):
            entradafilhaantiga = excluir(ponteirono, ponteirono.entradas[(len(ponteirono.indices))],entrada,entradafilhaantiga)

        if(entradafilhaantiga == None):
            return

        else:
            if not (ponteirono.verificaSeNoInternoEncheu()):
                entradafilhaantiga = None
                return entradafilhaantiga
            elif(encontraRIrmaoChavesExtras(ponteiropai) != None):

                        redistribuirChavesInternas(ponteirono,encontraRIrmaoChavesExtras(ponteiropai))
                        entradafilhaantiga = None
                        return entradafilhaantiga
            else:
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

                if (chave == ponteirono.entradas[i][0]):
                    ponteirono.entradas.remove( ponteirono.entradas[i])
                    entradafilhaantiga = None
                    return entradafilhaantiga
        else






def encontraRIrmaoChavesExtras(NoPai):
    for i in range(len(NoPai.entradas)):
        if not (NoPai.entradas[i].verificaSeNoInternoMinimo()):
            return NoPai.entradas[i]
    return None


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

    qtdDeEntradas = len(M.entradas)

    for i in range(qtdDeEntradas):
        entradaAMover = M.entradas[i]
        N.entradas.append(entradaAMover)

    N.proximo = M.proximo