from datetime import datetime

class Relatorio:
  def __init__(self, id, tipo, dataEntrada, visitantes=0):
    if not isinstance(dataEntrada, datetime):
      

    self.__id = id
    self.__tipo = tipo
    self.__dataEntrada = dataEntrada
    self.__dataSaida = None
    self.__Visitantes = visitantes

  def get_idRelatorio(self):
    return self.__id

  def get_tipoRelatorio(self):
    return self.__tipo

  def get_dataEntrada(self):
    return self.__dataEntrada

  def get_dataSaida(self):
    return self.__dataSaida

  def get_quantVisitantes(self):
    return self.__Visitantes

  def exibirRelatorio(self):
    print(f"ID: {self.__id}")
    print(f"Tipo: {self.__tipo}")
    print(f"Entrada: {self.__dataEntrada.strftime('%Y-%m-%d %H:%M:%S')}")
    if self.__dataSaida:
      print(f"Saída: {self.__dataSaida.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
      print(f"Visitantes: {self.__Visitantes}")
    print("Exibição finalizada")

  def registrar_saida(self, dataSaida):
    if not isinstance(dataSaida, datetime):
      raise TypeError("A data de saída é um objeto datetime")
    self.__dataSaida = dataSaida
