from Relatorio import Relatorio

class GerenciadorRelatorio(Exception):
  def __init__(self):
    self.__relatorio = []

  def adicionar_relatorio(self, relatorio):
    try:
        if not isinstance(relatorio, Relatorio):
          raise TypeError("Instância de Relatório")
        self.__relatorio.append(relatorio)
    except TypeError as e:
      print(f"Tem um Erro:{e}")
      
      def lista_relatorio(self, modo=None):
        if not self.__relatorio:
          print("Nenhum Relatório registrado")
          return
        for relatorio in self.__relatorio:
          if modo is None or relatorio.get_tipoRelatorio() == modo:
            relatorio.exibirRelatorio()
    finally:
     print("Execução da lista concluída")
