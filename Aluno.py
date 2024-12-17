import time
from UsuarioIFRO import UsuarioIFRO
class Aluno(UsuarioIFRO):
  def __init__(self, nome, cpf, matricula, senha, turma):
    super().__init__(nome,cpf,senha, matricula)
    self.__turma=turma

  def get_turma(self):
    return self.__turma

#Função cadastrar Aluno:
  def cadastrar_aluno(self):
    try:
      print("Cadastro Aluno,dados necessários:\n\n01-Nome\n02-Matricula\n03-Turma\n04-CPF\n05-Senha\n\n")
      time.sleep(2)
  
      print("*=*=*"*6)
      self.__nome =str(input("Digite seu nome: "))
      time.sleep(0.5)
    except ValueError:
      print("Apenas letras são aceitas neste campo, tente novamente")

#Condições de validação dos dados do Aluno(a):
    while True:
      turma=input("Digite sua Turma:")
      if len(str(turma))<=30:
        self.__turma=turma
        break
      else:
        print("Digite novamente: ")
      continue
    time.sleep(0.5)
    
#Validação de Identidade:    
    while True:
      cpf=input("Digite seu CPF com 11 dígitos: ")
      if len(str(cpf)) == 11:
        self.__cpf=cpf
        break
      else:
        print("Cpf inválido tente novamente com 11 dígitos:")
        continue
    time.sleep(0.5)
    
#Validação de Matrícula:
    while True:    
      matricula=input("Digite sua Matricula com 13 dígitos:")
      self.__matricula=(matricula)
      if len(str(matricula))==13:
        self.__matricula=matricula
        break
      else:
        print("Matricula inválida tente novamente com 13 dígitos:")
        continue
    time.sleep(0.5)
    
#Validação de senha do Aluno:      
    while True:
      senha= input("Digite sua senha com 4 dígitos: ")
      self.__senha=(senha)
      if len(str(self.__senha))== 4:
        self._senha=senha
        break
      else:
        print("Senha inválida tente novamente com 4 dígitos:")
        continue
      finally:
        print("Finalizando o cadastro...")
    time.sleep(0.5)

#Função para printar os dados dos alunos
  def exibirDados_aluno(self):
    time.sleep(1)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\nMatricula: {self.__matricula}\nSenha:{self.__senha}\nTurma:{self.__turma}")

#Função para atualizar a turma do aluno set:
  def set_turma(self):
    while True:
        resposta = input(f"\n{self.__nome},deseja atualizar sua turma?\n\n[A] Sim\n[B] Não\nResposta: ")
        print("*=*="*6)
        if resposta.upper() == "A":
          nova_turma = input("Digite sua nova turma (máximo 30 caracteres):")
          if len(nova_turma) <= 30:
            self.__turma = nova_turma
            time.sleep(1)
            print("\nTurma atualizada com sucesso:)")
            print("*=*="*6)
            return
          else:
            print("Erro: A tuma deve ter no máximo 30 caracteres")
        elif resposta.upper() == "B":
          print(f"Ok, {self.__nome},você optou por não trocar de turma.")
          break
        else:
          print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")
