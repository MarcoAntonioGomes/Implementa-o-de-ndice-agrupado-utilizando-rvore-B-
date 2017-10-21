
class noArvore:

    def __init__(self,qtdCampos):
        self.tamanhoDoBlocoDePaginas = 1000
        self.qtdCampos = qtdCampos
        self.indices = list()
        self.entradas = list()
        self.raiz = False
        self.folha = True
        self.proximo = None
        self.anterior = None
        self.irmao = None
        self.ocupacaoMaxima = int(self.tamanhoDoBlocoDePaginas / (self.qtdCampos * 4))
        self.ocupacaoMinima = int((self.tamanhoDoBlocoDePaginas / 2) / (self.qtdCampos * 4))

    def returnFolha(self):
        return self.folha

    def returnRaiz(self):
        return self.raiz

    def verificaSePaginaFolhaEncheu(self):
            #print("Tam Entradas: ", len(self.entradas)," == Ocupação Maxima",self.ocupacaoMaxima)
            return ((len(self.entradas)) == self.ocupacaoMaxima)

    def verificaSePaginaFolhaCapacidadeMinima(self):
        return ((len(self.entradas)) <= self.ocupacaoMinima)

    def verificaSeNoInternoEncheu(self):
        return ((len(self.indices))==(self.ocupacaoMaxima*self.qtdCampos))

    def verificaSeNoInternoMinimo(self):
        return ((len(self.indices))<=(self.ocupacaoMinima*self.qtdCampos))

    def grauDaArvore(self):
        return (int((self.ocupacaoMaxima*self.qtdCampos) / 2))
