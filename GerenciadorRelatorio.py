from Relatorio import Relatorio

class GerenciadorRelatorio:
  def __init__(self):
    self.__relatorio = []

  def adicionar_relatorio(self, relatorio):
    if not isinstance(relatorio, Relatorio):
      raise TypeError("Instância de Relatório")
#O raise é uma exceção, garante que apenas ojetos do tipo 
#Relatorio sejam adicionados a lista.
    self.__relatorio.append(relatorio)

  def lista_relatorio(self, modo=None):
    if not self.__relatorio:
      print("Nenhum Relatório registrado")
      return
    for relatorio in self.__relatorio:
      if modo is None or relatorio.get_tipoRelatorio() == modo:
        relatorio.exibirRelatorio()
