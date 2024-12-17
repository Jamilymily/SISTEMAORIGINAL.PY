#Alunas: Ádiles Naiandra, Alice Néry, Ana Andrade, Jamily Emanuelle
#Turma: 2º ano informática vespertino
 
import time
from Servidor import*
from catraca import *
from Aluno import *
from Recepcionista import *
from Relatorio import GerenciadorRelatorio, Relatorio
from UsuarioIFRO import *
from Visitante import *
from datetime import datetime, timedelta
time.sleep(0.1)
print("*=*" * 16)
print("Olá,Seja bem-vindo(a) ao nosso Sistema IDCotrol.")
print("*=*"*16)
time.sleep(0.5)
while True:
    acesso=int(input("Você deseja acessar cadastro ou relatório?\n [1]Cadastro\n[2]relatório"))
    if acesso()==1:
      adicionar=input("\nVocê vai ser cadastrar na área aluno ou servidor?\n\n[A]Aluno\n[B]Servidor\n[C]Visitante\n\nResposta=")
    if adicionar.upper() == "A":
      print("*=*"*12)
      print("Você vai se cadastrar na área aluno")
      print("*=*"*12)
      aluno=Aluno(nome="", cpf="", matricula="", senha="", turma="")
      aluno.cadastrar_aluno()
      aluno.atualizar_turma()
      aluno.exibirDados_aluno()
      print("."*15)
      print("\nCadastrado na área aluno com sucesso")
      print("Agora você tem acesso a todos os serviços da catraca")
      print("."*15)
      break

    elif adicionar.upper()=="B":
      print("*=*"*12)
      print("Você vai se cadastra na área do servidor")
      print("*=*"*12)
      servidor=Servidor(nome="", cpf="", matricula="", senha="",departamento="")
      servidor.cadastrar_servidor()
      servidor.atualizar_departamento()
      servidor.exibirDados_servidor()
      print("\nCadastro realizado com sucesso:)\n")
      print("Agora você tem acesso a todos os serviços da catraca.")
      break
    elif adicionar.upper()=="C":
      print("*=*"*12)
      visitante= Visitante(nome="", cpf="",idade="", documento="")
      visitante.cadastrar_visitante()
      visitante.exibirDados_Visitante()
      break
      
# Caso a pessoa escolher a opção errada
      
    if adicionar.upper() not in ["A", "B", "C"]:
      print("Resposta inválida, tente novamente")
      continue
    elif acesso==2:
      print("\n=== ÁREA DE RELATÓRIO ===")
      gerencia= GerenciadorRelatorio()
      rela1= Relatorio(1,"Aluno", datetime.now(), alunos=15)
      rela2=Relatorio(2,"Visitante", datetime.now - timedelta(hours=2))
      rela3= Relatorio(3,"Servidor", datetime.now() - timedelta(days=1), servidor=5)
      rela4=Relatorio(4,"Visitante", datetime.now() -  timedelta(days=2), visitantes=1)

      gerencia.adicionar_relatorio(rela1)
      gerencia.adicionar_relatorio(rela2)
      gerencia.adicionar_relatorio(rela3)
      gerencia.adicionar_relatorio(rela4)

      print("\n=== RELATÓRIOS ====")
      gerencia.lista_relatorio()

      print("\n=== SAÍDA ===")
      rela2.saida(datetime.now())
      rela2.exibirRelatorio()

      print("\n=== RELATÓRIO MODO 'VISITANTE'===")
      gerencia.lista_relatorio("Visitante")

      print("\n=== RELATÓRIO MODO 'SERVIDOR'===")
      gerencia.lista_relatorio("Servidor")

      print("\n=== RELATÓRIO MODO 'ALUNO'===")
      gerencia.lista_relatorio("Aluno")