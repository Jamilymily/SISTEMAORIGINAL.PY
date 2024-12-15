class Catraca:
    def __init__(self, biometria, cartao, faceID):
        # Tratamento simples para evitar falhas durante a inicialização
        try:
            self.__biometria = biometria
            self.__cartao = cartao
            self.faceID = faceID
        except Exception as e:
            print(f"Erro ao inicializar a instância: {e}")
            raise

    def get_biometria(self):
        try:
            return self.__biometria
        except Exception as e:
            print(f"Erro ao acessar biometria: {e}")
            raise

    def get_cartao(self):
        try:
            return self.__cartao
        except Exception as e:
            print(f"Erro ao acessar cartão: {e}")
            raise

    def get_faceID(self):
        try:
            return self.faceID
        except Exception as e:
            print(f"Erro ao acessar faceID: {e}")
            raise

    