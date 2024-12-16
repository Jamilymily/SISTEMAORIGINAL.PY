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

  def criar_senha (self):
    self.__senha = int(input("Digite sua senha: "))
    return self.__senha
  
  def set_senha(self):
    try:
      novasenha=int(input("Digite sua nova senha"))
      if len(str(novasenha))==4:
        self.__senha=novasenha
        print("Senha alterada com sucesso!!")
      else:
        print("Erro, a senha deve ter 4 dígitos")
    except ValueError:#Vai capturar erro quando a entrada não é um número válido
      print("ERRO: a senha deve ser em número.tente de novo")
    except Exception as e:#Serve para capturar qualquer erro inesperados
      print(f"Ocorreu um erro:{e}")