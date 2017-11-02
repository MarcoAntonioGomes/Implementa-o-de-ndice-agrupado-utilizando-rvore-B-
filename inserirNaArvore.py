from ArvoreBMais import *

'''
Inserir na árvore B+
Paramêtros:
no - No raiz da árvore 
entrada - registro com n campos
novaentradafilha - Nula inicialmente e depois recebe os filhos dividos para inserção nos nós pais, se for nula depois da inserção de um registro faz com que a função termine 
qtdcampos - Quantidade de campos presente nos registros
'''


def inserirNaArvore(no, entrada, novaentradafilha, qtdCampos):
    dividiuRaizPrimeiraVez = False
    global salvaRaiz


    if(no.raiz):
        salvaRaiz = no
    if not ( no.folha): #Busca recursivamente a Folha adequada  para inserção
        if (entrada[0] < no.indices[0]):

            novaentradafilha = inserirNaArvore(no.entradas[0], entrada, novaentradafilha, qtdCampos)
        if ( entrada[0] >= no.indices[(len(no.indices)-1)]):

            novaentradafilha = inserirNaArvore(no.entradas[(len(no.indices))], entrada, novaentradafilha, qtdCampos)


        else:

            for i in range ((len(no.indices)-1)):


                if(entrada[0] >= no.indices[i] and entrada[0] < no.indices[i+1]):



                    novaentradafilha = inserirNaArvore(no.entradas[i+1],entrada, novaentradafilha,qtdCampos)
                    break





        if(type(novaentradafilha) == noArvore):
                if(novaentradafilha.raiz):
                    salvaRaiz = novaentradafilha #Salva nova raiz
                novaentradafilha = None


        if (novaentradafilha == None):

            return salvaRaiz #Se inseriu corretamente e sem precisar de divisões, sai da função

        else:
            if((not no.verificaSeNoInternoEncheu())):

                #Se o no interno não encheu, posso colocar a chave de acesso para uma pagina subsequente com a referencia para objeto pagina conrrespondente
                #novaentradafilha[0] é igual a uma chave que da acesso a uma pagina
                #novaentradafilha[1] é igual a referencia para um objeto  do tipo nó da árvore

                no.indices.append(novaentradafilha[0])
                no.indices.sort(); # Linhas 56 e 57 garantem que as chaves a as referencias estarão ordenadas
                no.entradas.insert((no.indices.index(novaentradafilha[0])+1),novaentradafilha[1])
                atual = (no.indices.index(novaentradafilha[0]) + 1) #Linhas 58 as 62 foram implementadas, mas não foram utilizadas, será removido posteriormente.

                if(no.irmao != None):

                    no.entradas[len(no.entradas)-1].proximo = no.irmao.entradas[0]

                novaentradafilha = None
                return salvaRaiz

            else:
                #Linhas 68 a 79  fazem o processo de divisão de um nó interno criando um novo nó e removendo 50% das chaves e dos ponteiros  de um nó para o novo no criado.
                no2 = noArvore(qtdCampos)
                no2.folha = False
                no.folha = False
                for i in range(int((len(no.indices)/2)),(len(no.indices))):
                    no2.indices.append(no.indices[i])
                for i in range((int((len(no.entradas) / 2))), (len(no.entradas))):
                    no2.entradas.append(no.entradas[i])
                for i in range(len(no2.indices)):
                    no.indices.remove(no2.indices[i])
                for i in range(1,len(no2.entradas)):
                    no.entradas.remove(no2.entradas[i])
                no.indices.append(novaentradafilha[0]) #Linhas 80 a 82 garantem a ordem das chaves e das referencias para os objetos subsequentes
                no.indices.sort();
                no.entradas.insert((no.indices.index(novaentradafilha[0])+1),novaentradafilha[1])
                if(no.irmao == None): #Atualiza irmãos
                   no.irmao = no2
                else:
                   no2.irmao = no.irmao
                   no.irmao = no2.irmao


                novaentradafilha = ((min(no2.indices)),no2) # Configura a variável novaentradafilha para retorno e inserção no nó pai das novas paginas alteradas e as
                                                            # respectivas chaves
                if (no.raiz): # Linhas 96 a 106 Se o no dividido for raiz, cria se uma nova raiz e atribui os filhos novos



                    novoNo = noArvore(qtdCampos)
                    novoNo.indices.append(novaentradafilha[0])
                    novoNo.entradas.append(no)
                    novoNo.entradas.append(novaentradafilha[1])
                    novoNo.raiz = True
                    novoNo.folha = False
                    no.raiz = False


                    return novoNo
                return novaentradafilha #retorna novaentraafilha para inserção no pai das chaves e paginas divididas
    if(no.folha):

        if not(no.verificaSePaginaFolhaEncheu()):
            # Se a folha não esta cheia, insere normalmente a entrada de dados, registro de dados;
            no.entradas.append(entrada)
            no.entradas.sort() #Garante a ordem das entradas
            novaentradafilha = None #Nulo para retornar, significa que não ouve divisões
            if (dividiuRaizPrimeiraVez == False):
                return no
            else:
                return novaentradafilha

        else:
            #Folha esta cheia, dividi si o no cheio removendo as entradas e colocando as em um novo nó folha
            #Nivel minimo de ocupação em 50%
            folhaNo = noArvore(qtdCampos)
            menorChave = no.entradas[int((len(no.entradas) / 2))][0]
            metadeDasChaves = int((len(no.entradas) / 2))
            totalDasChaves = len(no.entradas)
            for i in range(metadeDasChaves,totalDasChaves):
                folhaNo.entradas.append(no.entradas[i]) #Coloca as entradas do nó antigo no nó novo
                folhaNo.entradas.sort() #Garante a ordenação
            for i in range(len(folhaNo.entradas)):
                no.entradas.remove(folhaNo.entradas[i]) #Remove as entradas do nó antigo
            if(no.proximo == None):
                no.proximo = folhaNo # Atualiza se os nós proximos e anteriores após a divisão
                folhaNo.anterior = no
            else:
                folhaNo.proximo = no.proximo
                no.proximo.anterior = folhaNo
                no.proximo = folhaNo

            novaentradafilha = (menorChave,folhaNo)
            #Caso inicial no qual a raiz é folha e esta cheia, logo a divisão realizada acima precisa ser inserida em uma nova raiz
            if(no.raiz):
                novaRaiz = noArvore(qtdCampos)
                novaRaiz.indices.append(novaentradafilha[0])
                novaRaiz.entradas.append(no)
                novaRaiz.entradas.append(novaentradafilha[1])
                novaRaiz.raiz = True
                novaRaiz.folha = False
                no.raiz = False
                no.folha = True

                no = novaRaiz

                novaentradafilha = None
                dividiuRaizPrimeiraVez = True
                return novaRaiz #Retorna nova raiz criada

            return novaentradafilha #Retorna chave e referencia do objeto pagina criado para ser inserido no nó pai
