
class noArvore():
    def __init__(self,m):
        self.m = m
        self.indices = list()
        self.raiz = False
        self.folha = True

    def verificaQuantChaves(self):
        if(len(self.indices)== self.m):
            return True