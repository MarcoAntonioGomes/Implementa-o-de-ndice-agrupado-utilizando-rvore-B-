
class noArvore:

    def __init__(self,qtdCampos):
        self.tamanhoDoBlocoDePaginas = 8000
        self.qtdCampos = qtdCampos
        self.indices = list()
        self.entradas = list()
        self.raiz = False
        self.folha = True
        self.ocupacaoMaxima = (self.tamanhoDoBlocoDePaginas / (self.qtdCampos * 4))
        self.ocupacaoMinima = ((self.tamanhoDoBlocoDePaginas / 2) / (self.qtdCampos * 4))

    def returnFolha(self):
        return self.folha

    def returnRaiz(self):
        return self.raiz

    def verificaSePaginaFolhaEncheu(self):

            return ((len(self.entradas)*self.qtdCampos*4) == self.ocupacaoMaxima)

    def verificaSePaginaFolhaCapacidadeMinima(self):
        return ((len(self.entradas)*self.qtdCampos*4) == self.ocupacaoMinima)

    def verificaSeNoInternoEncheu(self):
        return ((len(self.indices)*4)==(self.ocupacaoMaxima*self.qtdCampos))

    def verificaSeNoInternoMinimo(self):
        return ((len(self.indices)*4)==(self.ocupacaoMinima*self.qtdCampos))

