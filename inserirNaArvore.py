def inserirNaArvore(no, entrada, novaentradafilha):
    if not no.folha:

        for i in range ((len(no)-1)):
            if(entrada.chave <= no.indices[i] and entrada.chave < no.indices[i+1]):
                inserirNaArvore(no.entradas[no.indice[i]],entrada, None)



        if (novaentradafilha == None):
            return

        else:
            if((not no.verificaSeNoInternoEncheu())):
                no.indices.appended(novaentradafilha[0])
                no.entradas[novaentradafilha[0]] = novaentradafilha[1]
                novaentradafilha = None
                return
            else:
                no2 = noArvore
                for i in range((len(no.indices)/2),len(no.indices)):
                    no2.indices.appended(no.indices[i])
                    no2.entradas.appended(no.entradas[indice[i]])
                    no.indices.remove(i)
                    no.entradas.remove(i)
                    novaentradafilha = ((min(no2.indices)),no2)
            if (not no.raiz):
                novoNo = noArvore
                novoNo.entradas.appended(no)
                novoNo.entradas.appended(novaentradafilha[1])
                novoNo.raiz = True
                return

    if(no.folha):
        if(not no.verificaSePaginaFolhaEncheu):
            no.entradas.appended(entrada)
            novaentradafilha = None
            return
        else:
            folhaNo = noArvore
            menorChave = no.entradas[0][(len(no.entradas) / 2)]

            for i in range((len(no.entradas) / 2),len(no.entradas)):
                folhaNo.entradas.appended(no.entradas[i])
                if(no.entradas[0][i] < menorChave):
                    menorChave = no.entradas[0][i]
                no.entradas.remove(i)
        novaentradafilha = (menorChave,folhaNo)
        return
