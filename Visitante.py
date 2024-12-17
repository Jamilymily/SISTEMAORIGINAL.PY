import time

class Visitante:
  def __init__(self,nome,cpf, idade,documento):
    self.__nome= nome
    self.__cpf=cpf
    self.__idade= idade
    self.__documento=documento

  def get_nome(self):
    return self.__nome

  def get_cpf(self):
    return self.__cpf

  def get_idade(self):
    return self.__idade

  def get_documento(self):
    return self.__documento
    
  def cadastrar_visitante(self):
    self.__nome=input("Digite seu nome:")
    time.sleep(0.5)

    try:
      while True:
        cpf= input("Digite seu CPF com 11 dígitos:")
        self.__cpf=(cpf)
        if len(str(cpf)) == 11:
          self.__cpf=cpf
          break
        else:
          raise ValueError("CPF inválido.")
# O raise vai interromper o fluxo normal da função se a entrada for invalida.
   except ValueError as e:#O except Vai capturar a mensagem e imprime na tela
print(f"Valor inválido{e}. Tente novamente")

  try:
    while True:
      idade= int(input("Digite sua idade:"))
      self.__idade=(idade)
      if idade>=18:
        break
      else:
        entrada=input("Menor de 18 anos precisa estar acompanhado de um responsável legal Você está acompanhado?\n\n[A]Sim\n[B]Não\n\nResposta:")
        if entrada.upper()=="A":
          break
        elif entrada.upper()=="B":
          raise PermissionError('Acesso Negado, menor de idade')
        else:
          raise TypeError("Resposta Inválida. Escolha [A] ou [B]")
  except TypeError as e:#Direcionado para capturar erro de tipo de entrada errada.
    print(f"Erro, tente novamente{e}")
    time.sleep(1)
  except PermissionError as e:#Usado Para restringir acesso de menores de idade.
    print(f"{e}")
    time.sleep(1)
    exit()

    while True:
      documento = input("É necessário o documento de identificação (RG, IDENTIDADE, CNH, CARTEIRA DE HABILITAÇÃO): ").strip().upper()
      if documento in ["RG", "IDENTIDADE", "CNH", "CARTEIRA DE HABILITAÇÃO"]:
        self.__documento = documento
        print("Acesso liberado,agora você pode entrar na instituição:)")
        break
      else:
        print("Docuemnto inválido. Por favor, escolha um dos documentos listados")
        time.sleep(0.5)
        continue

  def exibirDados_Visitante(self):
    time.sleep(1)
    print("*=*"*6)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\n Idade:{self.__idade}\n Documento:{self.__documento}")
    print("*=*"*6)

