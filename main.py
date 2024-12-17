#Alunas: Ádiles Naiandra, Alice Néry, Ana Andrade, Jamily Emanuelle
#Turma: 2º ano informática vespertino
#Disciplina: Programação Orientada a Objetos
 
import time
from Aluno import Aluno
from GerenciadorRelatorio import GerenciadorRelatorio
from Relatorio import  Relatorio
from Servidor import Servidor
from Visitante import Visitante
from datetime import datetime, timedelta



time.sleep(0.1)
print("*=*" * 16)
print("Olá,Seja bem-vindo(a) ao nosso Sistema IDCotrol.")
print("*=*"*16)
time.sleep(0.5)

while True:
  adicionar=input("\nVocê vai ser cadastrar na área aluno ou servidor?\n\n[A]Aluno\n[B]Servidor\n[C]Visitante\n\nResposta=")
  if adicionar.upper() == "A":
    print("*=*"*12)
    print("Você vai se cadastrar na área aluno")
    print("*=*"*12)
    aluno=Aluno(nome="", cpf="", matricula="", senha="", turma="")
    aluno.cadastrar_aluno()
    aluno.set_turma()
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
    servidor= Servidor(nome="", cpf="", matricula="", senha="",departamento="")
    servidor.cadastrar_servidor()
    servidor.set_departamento()
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
  else:
    print("Resposta inválida. Por favor, escolha [A], [B] ou [C].")
  
while True:  
  resposta = input("Você deseja ter acesso a área de relatório?\n[A]Sim\n[B]Não\nR:")
  if resposta.upper() == "A":
    print("===ÁREA RELATÓRIO===")
    relatorio1 = Relatorio(1, "Aluno", datetime.now(), visitantes=50)
    relatorio2 = Relatorio(2, "Servidor", datetime.now() - timedelta(days=1), visitantes=10)

    # Criando o gerenciador e adicionando os relatórios
    gerenciador = GerenciadorRelatorio()
    gerenciador.adicionar_relatorio(relatorio1)
    gerenciador.adicionar_relatorio(relatorio2)

   
    # Listando relatórios do tipo "Aluno"
    print("\n=== RELATÓRIOS DO TIPO 'ALUNO' ===")
    gerenciador.lista_relatorio("Aluno")

    # Registrando saída para o relatório 1
    print("\n=== REGISTRANDO SAÍDA PARA O RELATÓRIO 1 ===")
    relatorio1.registrar_saida(datetime.now())

    # Listando novamente para verificar a saída registrada
    print("\n=== RELATÓRIOS ATUALIZADOS ===")
    gerenciador.lista_relatorio()
    break
      
  elif resposta.upper()=="B":
    print("O relatório não será exibido")
    break
      
  else:
    print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")
    break
    
