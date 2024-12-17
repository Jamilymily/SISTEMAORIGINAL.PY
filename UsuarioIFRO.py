import time
from abc import ABC

class UsuarioIFRO(ABC):
  def __init__(self,nome,cpf, matricula, senha):
    self.__nome= nome
    self.__cpf=cpf
    self.__matricula = matricula
    self.__senha=senha

  def get_nome(self):
    return self.__nome 

  def get_cpf(self):
    return self.__cpf

  def get_matricula(self):
    return self.__matricula

  def get_senha(self):
    return self.__senha

# método para criar senha com tratamento de exceção

  def criar_senha (self):
    try:
      self.__senha = int(input("Digite sua senha: "))
      print("Senha criada com sucesso")
      return self.__senha
    except ValueError:
      print("Erro, digite apenas numeros para criar a senha.")
      return self.criar_senha()
    
# método para alterar senha com tratamento de exceção

  def set_senha(self):
    try:
      nova_senha = int(input("Digite sua nova senha:"))
      self.__senha = nova_senha
      print("Senha alterada.")
    except ValueError:
      print("Erro, digite apenas numeros para a nova senha")
      self.set_senha()  

