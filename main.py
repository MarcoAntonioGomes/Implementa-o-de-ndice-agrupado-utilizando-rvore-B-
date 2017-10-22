from ArvoreBMais import *
from inserirNaArvore import *
from pesquisaChaveNaArvore import*
from pesquisaPorIntervaloArvore import*
from removerDaArvore import*

if __name__ == "__main__":

    arq = open('saida.csv','r')



    entrada = list()
    Arvore = noArvore(25)
    Arvore.raiz = True
    Arvore.folha = True
    novaentrada = None


    for linha in arq:
        valores = linha.split(',')
        if(valores[0] == '+'):
            qtdCampos = (len(valores)-1)
            entrada = list(map(int, valores[1:]))
            Arvore = inserirNaArvore(Arvore, entrada, novaentrada,qtdCampos)
            #print("Inseri, ",entrada)
        elif(valores[0] == '-'):
            chave = int(valores[1])
            #print("Vou Remover: ", chave)
            excluirDaArvore(None, Arvore, chave, None)
            #print("Remove")
    chave = 5857
    print(pesquisarNaArvore(Arvore, chave))
    chave = 1222
    pesquisaIntervaloArvore(Arvore,chave, chave+100)

    arq.close()