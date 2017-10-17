from ArvoreBMais import *
from copy import deepcopy



def inserirNaArvore(no, entrada, novaentradafilha, qtdCampos):
    dividiuRaizPrimeiraVez = False
    global salvaRaiz


    if(no.raiz):
        salvaRaiz = no
    if not ( no.folha):
        if (entrada[0] < no.indices[0]):
            # print("Entrei no 1ª IF")
            # print(no)
            no.indices.sort()
            novaentradafilha = inserirNaArvore(no.entradas[0], entrada, novaentradafilha, qtdCampos)


        #print("Tamanho: ",(len(no.indices)))
        if(novaentradafilha == None):
            for i in range ((len(no.indices)-1)):
           # print("Entrada: ",entrada[0])
            #print("Indice[i]",no.indices[i])
            #print("Indice[i+1]",no.indices[(i+1)])
            #print(no.indices)




                if(entrada[0] >= no.indices[i] and entrada[0] < no.indices[i+1]):

                #print("Entrei no 3ª IF")
                #print("Chave: ",entrada[0])
                #print("Indices[i-1]: ",no.indices[i-1])
               # print("Indices[i] ",no.indices[i])
                #print("Quant De Indices: ",len(no.indices))
                #print("Tamanho da entrada",len(no.entradas))
               # print(no.entradas[i])



                    no.indices.sort()
                    novaentradafilha = inserirNaArvore(no.entradas[i],entrada, novaentradafilha,qtdCampos)
                    break
            # elif (len(no.indices)==2 and entrada[0] > no.indices[i]):

                # print("Entrei no 3ª IF")
                # print("Chave: ",entrada[0])
                # print("Indices[i-1]: ",no.indices[i-1])
                # print("Indices[i] ",no.indices[i])
                # print("Quant De Indices: ",len(no.indices))
                # print("Tamanho da entrada",len(no.entradas))
                # print(no.entradas[i])



                # no.indices.sort()
                # novaentradafilha = inserirNaArvore(no.entradas[i + 1], entrada, novaentradafilha, qtdCampos)
                # break
        if ( entrada[0] >= no.indices[(len(no.indices)-1) and novaentradafilha == None]):
        # print("Entrei no 2ª IF")
        # print(no)
         no.indices.sort()
        novaentradafilha = inserirNaArvore(no.entradas[(len(no.indices))], entrada, novaentradafilha, qtdCampos)

       # for i in range ((len(no.entradas))):
            #print("Entradas na Pagina: ",i," ",no.entradas[i].entradas)

        if(type(novaentradafilha) == noArvore):

                novaentradafilha = None

        #print(novaentradafilha)
        if (novaentradafilha == None):
           # print("Sai da Iteração")
            #print(salvaRaiz)
            return salvaRaiz

        else:
            if((not no.verificaSeNoInternoEncheu())):
               # print("Entrei no else if not")
               # print(novaentradafilha)

                no.indices.append(novaentradafilha[0])
                no.entradas.append(novaentradafilha[1])
                no.indices.sort()
                #print(len(no.entradas))
                novaentradafilha = None
                return salvaRaiz

            else:
                no2 = noArvore(qtdCampos)
                no2.folha = False
                no.folha = False
                for i in range(int((len(no.indices)/2)),(len(no.indices))):
                    no2.indices.append(no.indices[i])
                    no2.indices.sort()
                for i in range(int((len(no.entradas) / 2)), (len(no.entradas))):
                    no2.entradas.append(no.entradas[i])
                for i in range(len(no2.indices)):
                    no.indices.remove(no2.indices[i])
                    no.indices.sort()
                for i in range(len(no2.indices)):
                    no.entradas.remove(no2.entradas[i])
                print("Dividi No Interno")
                novaentradafilha = ((min(no2.indices)),no2)
                if (no.raiz):


                    #print("Passei Aqui")
                    novoNo = noArvore(qtdCampos)
                    novoNo.indices.append(novaentradafilha[0])
                    novoNo.entradas.append(no)
                    novoNo.entradas.append(novaentradafilha[1])
                    novoNo.raiz = True
                    novoNo.folha = False
                    no.raiz = False
                    #print(novoNo)

                    return novoNo
                return novaentradafilha
    if(no.folha):

        if not(no.verificaSePaginaFolhaEncheu()):
            no.entradas.append(entrada)
            no.entradas.sort()
            #print(no.entradas)
            novaentradafilha = None
            #print("Entrei no if not")
            if (dividiuRaizPrimeiraVez == False):
                return no
            else:
                return novaentradafilha

        else:
            folhaNo = noArvore(qtdCampos)

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
                folhaNo.entradas.sort()
            for i in range(len(folhaNo.entradas)):
                no.entradas.remove(folhaNo.entradas[i])
            no.entradas.sort()
            novaentradafilha = (menorChave,folhaNo)
            if(no.raiz):
                novaRaiz = noArvore(qtdCampos)
                Altura = 1
                print("Altura", Altura)
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
