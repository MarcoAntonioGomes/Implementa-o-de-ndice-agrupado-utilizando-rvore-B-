from ArvoreBMais import *
from copy import deepcopy

def inserirNaArvore(no, entrada, novaentradafilha):
    dividiuRaizPrimeiraVez = False
    if(no.raiz):
        salvaRaiz = no
    if not ( no.folha):

        #print("Tamanho: ",(len(no.indices)))
        for i in range ((len(no.indices))):
           # print("Entrada: ",entrada[0])
            #print("Indice[i]",no.indices[i])
            #print("Indice[i+1]",no.indices[(i+1)])
            #print(no.indices)
            if((len(no.indices))==1 and entrada[0] <= no.indices[i]):
               # print("Entrei no 1ª IF")
               # print(no)
                no.indices.append(entrada[0])
                novaentradafilha = inserirNaArvore(no.entradas[i], entrada, novaentradafilha)
                break

            elif((len(no.indices))==1 and entrada[0] >= no.indices[i]):
                #print("Entrei no 2ª IF")
                #print(no)
                no.indices.append(entrada[0])
                novaentradafilha = inserirNaArvore(no.entradas[i+1], entrada,novaentradafilha)
                break

            elif(entrada[0] <= no.indices[i-1] and entrada[0] < no.indices[i]):

                #print("Entrei no 3ª IF")
                #print(i)

               # print(no.entradas[i])
                print("Entradas da Pagina: ",i," ",no.entradas[i].entradas)

                no.indices.append(entrada[0])
                no.indices.sort()
                novaentradafilha = inserirNaArvore(no.entradas[i-1],entrada, novaentradafilha)
                break
        if(type(novaentradafilha) == noArvore):
            novaentradafilha = None

        #print(novaentradafilha)
        if (novaentradafilha == None):
           # print("Sai da Iteração")
            return salvaRaiz

        else:
            if((not no.verificaSeNoInternoEncheu())):
               # print("Entrei no else if not")
               # print(novaentradafilha)
                no.indices.append(novaentradafilha[0])
                no.entradas.append(novaentradafilha[1])
                #print(len(no.entradas))
                novaentradafilha = None
                return salvaRaiz
            else:
                no2 = noArvore(10)
                for i in range(int((len(no.indices)/2)),(len(no.indices))):
                    no2.indices.append(no.indices[i])
                for i in range(int((len(no.entradas) / 2)), (len(no.entradas))):
                    no2.entradas.append(no.entradas[i])
                for i in range(len(no2.indices)):
                    no.indices.remove(no2.indices[i])
                for i in range(len(no2.indices)):
                    no.entradas.remove(no2.entradas[i])

                novaentradafilha = ((min(no2.indices)),no2)
                if (no.raiz):
                    print("Passei Aqui")
                    novoNo = noArvore(10)
                    novoNo.indices.append[novaentradafilha[0]]
                    novoNo.entradas.append(no)
                    novoNo.entradas.append(novaentradafilha[1])
                    novoNo.raiz = True
                    no.raiz = False
                    return novaentradafilha

    if(no.folha):

        if not(no.verificaSePaginaFolhaEncheu()):
            no.entradas.append(entrada)
            #print(len(no.entradas))
            #print(no.entradas[0][0])
            novaentradafilha = None
            #print("Entrei no if not")
            if (dividiuRaizPrimeiraVez == False):
                return no
            else:
                return novaentradafilha

        else:
            folhaNo = noArvore(10)

            menorChave = no.entradas[0][int((len(no.entradas) / 2))]
           # print("------------------------------------------------------------")
            metadeDasChaves = int((len(no.entradas) / 2))
            totalDasChaves = len(no.entradas)
            for i in range(metadeDasChaves,totalDasChaves):
               # print(i,no.entradas[i])
                folhaNo.entradas.append(no.entradas[i])
                if(no.entradas[0][i] < menorChave):
                    menorChave = no.entradas[0][i]
                    #print(menorChave)
            for i in range(len(folhaNo.entradas)):
                no.entradas.remove(folhaNo.entradas[i])
            novaentradafilha = (menorChave,folhaNo)
            if(no.raiz):
                novaRaiz = noArvore(10)

                novaRaiz.indices.append(novaentradafilha[0])
                novaRaiz.entradas.append(no)
                novaRaiz.entradas.append(novaentradafilha[1])
                novaRaiz.raiz = True
                novaRaiz.folha = False
                no.raiz = False
                no.folha = True
                #print("Dividi Raiz")
               # print(novaRaiz)
                #print(no)
                #print(novaRaiz)
                no = novaRaiz
                #print(no)
                novaentradafilha = None
                dividiuRaizPrimeiraVez = True
                return novaRaiz
            #print("Passei no else")
           # print("Novaentradafilha: ",novaentradafilha)
            return novaentradafilha
