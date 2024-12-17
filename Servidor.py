
import time
from abc import ABC
from exceptionCPF import *

from UsuarioIFRO import UsuarioIFRO

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
  
  def set_senha(self, novasenha):
    self.__novasenha =("Digite sua nova senha:")
    self.__novasenha = self.__senha
    print("Senha alterada com sucesso")

class Servidor(UsuarioIFRO):
  def __init__ (self,nome,cpf,senha,matricula,departamento):
    super().__init__(nome,cpf,senha,matricula)
    self.__departamento=departamento

  def cadastrar_servidor(self):
    try:
      time.sleep(1)
      print("Cadastro Servidor, dados necessarios:\n\n01-Nome\n02-Matricula\n03 Departamento\n04-CPF\n05-Senha\n\n")
      time.sleep(1)
      self.__nome =input("Digite seu nome:")
      time.sleep(0.5)
      
      while True:
        departamento=input("Digite seu departamento:")
        if len(departamento)<=30:
          self.__departamento=departamento
          break
        else:
          print("Digite novamente:")
          continue
      time.sleep(0.5)
    
#validação de Cpf:
      while True:
        try:
          cpf= input("Digite seu CPF com 11 dígitos:")
          self.__cpf=(cpf)
          if len(str(cpf)) == 11:
            self.__cpf=cpf
            break
          if len(str(cpf)) != 11:
            raise ErrorCPF ("O CPF deve conter exatamente 11 dígitos.")
        except ErrorCPF:
          print("O CPF deve conter exatamente 11 dígitos.")
      time.sleep(0.5)
    
#validação de matrícula:
      while True:    
        matricula = input("Digite sua Matricula com 7 dígitos: ")
        if len(str(matricula)) == 7:
          self.__matricula=matricula
          break
        else:
          print("Matricula inválida tente novamente com apenas 7 digitos:")
          continue
      time.sleep(0.5)
    
#validação de senha
      while True:
        senha= input("Digite sua senha com 4 dígitos: ")
        self.__senha=(senha)
        if len(str(self.__senha))== 4:
          self._senha=senha
          break 
        else:
          print("Senha inválida tente novamente com 4 dígitos:")
    except Exception as e:
      print(f"Ocorreu um ero durante o cadastro: {e}")
    finally:
      print("Finalizando o cadastro...")

  def exibirDados_servidor(self):
    time.sleep(1)
    print("*=*"*6)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\nMatricula: {self.__matricula}\nSenha:{self.__senha}\nDepartamento:{self.__departamento}")
    print("*=*"*6)
  

#Set escolha do usuário para troca de departamento
  def set_departamento(self):
    while True:
      atualiza = input(f"{self.__nome}, deseja atualizar seu departamento?\n\n[A]Sim\n[B]Não\n\nResposta: ")
      if atualiza.upper() == "A":
        novo_departamento= input("Digite seu novo departamento(máximo 30 caracteres):")
        if len(novo_departamento)<= 50:
          self.__departamento=novo_departamento
          print("Departamento atualizado com sucesso.")
          return
        else:
          print("O departamento deve ter no máximo 30 caracteres. Por favor,digite novamente.")
          break
      elif atualiza.upper() == "B":
        print(f"Ok, {self.__nome},você optou por não trocar de departamento")
        break
      else:
        print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")