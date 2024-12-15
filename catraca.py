class Catraca:
  def __init__ (self, biometria, cartao, faceID):
    self.__biometria = biometria
    self.__cartao = cartao
    self.faceID = faceID
    
  def get_biometria(self):
    return self.__biometria
    
  def get_cartao(self):
    return self.__cartao
    
  def get_faceID(self):
    self.__faceID
