'''
Script que define o nó da arvoré, tal nó é usado tanto para nó interno quanto para folha

'''
class noArvore:

    def __init__(self,qtdCampos):
        self.tamanhoDoBlocoDePaginas = 1000 # Váriavel que armazena o tamanho do bloco da página, tal parâmetro será alterado para que possar ser utilizado em tempo de execução
        self.qtdCampos = qtdCampos #Quantidade de campos que o registro possuí
        self.indices = list() #Lista para armazenar as chaves de acesso nos nós não folhas, se o nó for folha ela ficará vazia
        self.entradas = list() #Lista para armazenar as referencias para os objetos do tipo nó que serão criados em nós internos, semelhante ao armazenamento de ponteiros em C++
                                # Se o nó for folha, esta lista conterá as entradas de dados, que no caso será outra lista com os campos gerados no gerador de dados sintético
        self.raiz = False
        self.folha = True
        self.proximo = None #variável que quando o nó é folha salva o proximo objeto, conforme a lista duplamente encadeada que acontece nas folhas da arvoré B+
        self.anterior = None # Mesmo caso do proximo, só que para o objeto anterior
        self.irmao = None #Irmao utilizado para facilitar a redistribuição de chaves
        #Abaixo são atribuidos as variáveis ocupaçãoMaxima e ocupaçãoMinima a quantidade de registro Maxima e Minima que as paginas irão suportar
        #O valor 4 é o tamanho do tipo int usado, tal constante será corrigida para que seja passada por parametro para o uso correto do tamanho de inteiro da linguagem
        self.ocupacaoMaxima = int(self.tamanhoDoBlocoDePaginas / (self.qtdCampos * 4))
        self.ocupacaoMinima = int((self.tamanhoDoBlocoDePaginas / 2) / (self.qtdCampos * 4))

    def returnFolha(self):
        return self.folha

    def returnRaiz(self):
        return self.raiz

    def verificaSePaginaFolhaEncheu(self): #Método que verifica se a pagina folha encheu, tal método é utilizado para divisão das páginas folhas na função inserir

            return ((len(self.entradas)) == self.ocupacaoMaxima) #Leva em conta o fato de que nas páginas folhas tem se menos entradas de dados devido ao fato
                                                                 # de que o registro é maior que uma unica chave (Chave = 4 bytes / Entrada de dados = QtdCampos * 4 bytes )
    def verificaSePaginaFolhaCapacidadeMinima(self): #Método que verifica se a página folha esta na capacidade minima ou abaixo dela, método utilizado na função remover
        return ((len(self.entradas)) <= self.ocupacaoMinima)

    def verificaSeNoInternoEncheu(self): # Página interna cabe mais chaves do que as paginas folhas cabem entradas de dados
        return ((len(self.indices))==(self.ocupacaoMaxima*self.qtdCampos))

    def verificaSeNoInternoMinimo(self):
        return ((len(self.indices))<=(self.ocupacaoMinima*self.qtdCampos))

    def grauDaArvore(self): #Método criado para retornar o grau  da árvore
        return (int((self.ocupacaoMaxima*self.qtdCampos) / 2))
