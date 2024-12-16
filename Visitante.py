import time

class Visitante:
    def __init__(self, nome, cpf, idade, documento):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_idade(self):
        return self.__idade

    def get_documento(self):
        return self.__documento
    
    def cadastrar_visitante(self):
        self.__nome = input("Digite seu nome: ")
        time.sleep(0.5)
        
        while True:
            try:
                cpf = input("Digite seu CPF com 11 dígitos: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("CPF inválido. Tente novamente com apenas 11 dígitos.")
                self.__cpf = cpf
                break
            except ValueError as e:
                print(e)
                time.sleep(0.5)
                continue
            finally:
                print("Tentativa de cadastro do CPF finalizada.")
        
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if idade < 18:
                    entrada = input("Menor de 18 anos precisa estar acompanhado de um responsável legal. Você está acompanhado?\n\n[A]Sim\n[B]Não\n\nResposta: ")
                    if entrada.upper() == "A":
                        break
                    else:
                        raise PermissionError("Acesso negado, você é menor de 18 anos!")
                else:
                    break
            except ValueError:
                print("Idade inválida. Por favor, digite um número válido para a idade.")
            except PermissionError as e:
                print(e)
                time.sleep(1)
                exit()
            finally:
                print("Tentativa de cadastro de idade finalizada.")
        
        while True:
            try:
                documento = input("É necessário o documento de identificação (RG, IDENTIDADE, CNH, CARTEIRA DE HABILITAÇÃO): ").strip().upper()
                if documento not in ["RG", "IDENTIDADE", "CNH", "CARTEIRA DE HABILITAÇÃO"]:
                    raise ValueError("Documento inválido. Por favor, escolha um dos documentos listados.")
                self.__documento = documento
                print("Acesso liberado, agora você pode entrar na instituição :)")
                break
            except ValueError as e:
                print(e)
                time.sleep(0.5)
                continue
            finally:
                print("Tentativa de cadastro de documento finalizada.")

    def exibirDados_Visitante(self):
        time.sleep(1)
        print("*=*"*6)
        print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\n Idade:{self.__idade}\n Documento:{self.__documento}")
        print("*=*"*6)
