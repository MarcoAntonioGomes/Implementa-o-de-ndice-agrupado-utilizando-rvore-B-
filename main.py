from ArvoreBMais import *
from inserirNaArvore import *
from pesquisaChaveNaArvore import*
from pesquisaPorIntervaloArvore import*
from removerDaArvore import*

if __name__ == "__main__":

    arq = open('saida.csv','r')



    entrada = list()
    crieiArvore = False
    novaentrada = None

    print("Inserindo na Arvore...")

    for linha in arq:
        valores = linha.split(',')
        if(valores[0] == '+'):
            qtdCampos = (len(valores)-1)
            if(crieiArvore == False):
                Arvore = noArvore(qtdCampos)
                Arvore.raiz = True
                Arvore.folha = True
                crieiArvore = True
            entrada = list(map(int, valores[1:]))
            Arvore = inserirNaArvore(Arvore, entrada, novaentrada,qtdCampos)
            print("Entrada de dados: ",entrada)
        elif(valores[0] == '-'):

            chave = int(valores[1])
            print("Removendo entrada com Chave: ",chave)
            excluirDaArvore(None, Arvore, chave, None)

    chave = 5857
    print("\n\nBuscando Chave já removida: ",chave,"\n\n ")
    procura = pesquisarNaArvore(Arvore, chave)
    if(procura == None):
        print("Não existe entrada de dados com esta chave\n\n")
    else:
        print("Entrada: ",procura)

    print("Seleção por intervalo...\n\n")
    chave = 1222
    print("Buscando entradas com chave de ", chave, "ate ", chave + 100,"\n\n")
    pesquisaIntervaloArvore(Arvore,chave, chave+100)

    arq.close()