import time
from abc import ABC

class UsuarioIFRO(ABC):
    def __init__(self, nome, cpf, matricula, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__matricula = matricula
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_matricula(self):
        return self.__matricula

    def get_senha(self):
        return self.__senha

    def criar_senha(self):
        self.__senha = int(input("Digite sua senha: "))
        return self.__senha

    def set_senha(self, novasenha):
        self.__novasenha = ("Digite sua nova senha:")
        self.__novasenha = self.__senha
        print("Senha alterada com sucesso")


class CpfInvalidoError(Exception):
    pass


class MatriculaInvalidaError(Exception):
    pass


class SenhaInvalidaError(Exception):
    pass


class DepartamentoInvalidoError(Exception):
    pass


class Servidor(UsuarioIFRO):
    def __init__(self, nome, cpf, senha, matricula, departamento):
        super().__init__(nome, cpf, senha, matricula)
        self.__departamento = departamento

    def cadastrar_servidor(self):
        try:
            time.sleep(1)
            print("Cadastro Servidor, dados necessários:\n\n01-Nome\n02-Matricula\n03 Departamento\n04-CPF\n05-Senha\n\n")
            time.sleep(1)
            self.__nome = input("Digite seu nome: ")
            time.sleep(0.5)

            # Validação de Departamento:
            while True:
                try:
                    departamento = input("Digite seu departamento: ")
                    if len(departamento) > 30:
                        raise DepartamentoInvalidoError("Departamento deve ter no máximo 30 caracteres.")
                    self.__departamento = departamento
                    break
                except DepartamentoInvalidoError as e:
                    print(e)
                    time.sleep(0.5)
                    continue

            time.sleep(0.5)

            # Validação de CPF:
            while True:
                try:
                    cpf = input("Digite seu CPF com 11 dígitos: ")
                    if len(cpf) != 11 or not cpf.isdigit():
                        raise CpfInvalidoError("CPF inválido. Tente novamente com apenas 11 dígitos.")
                    self.__cpf = cpf
                    break
                except CpfInvalidoError as e:
                    print(e)
                    time.sleep(0.5)
                    continue

            time.sleep(0.5)

            # Validação de Matrícula:
            while True:
                try:
                    matricula = input("Digite sua Matrícula com 7 dígitos: ")
                    if len(str(matricula)) != 7:
                        raise MatriculaInvalidaError("Matrícula inválida. Deve ter exatamente 7 dígitos.")
                    self.__matricula = matricula
                    break
                except MatriculaInvalidaError as e:
                    print(e)
                    time.sleep(0.5)
                    continue

            time.sleep(0.5)

            # Validação de Senha:
            while True:
                try:
                    senha = input("Digite sua senha com 4 dígitos: ")
                    if len(senha) != 4 or not senha.isdigit():
                        raise SenhaInvalidaError("Senha inválida. Tente novamente com 4 dígitos.")
                    self.__senha = senha
                    break
                except SenhaInvalidaError as e:
                    print(e)
                    continue

        except Exception as e:
            print(f"Ocorreu um erro durante o cadastro: {e}")
        finally:
            print("Finalizando o cadastro...")

    def exibirDados_servidor(self):
        try:
            time.sleep(1)
            print("*=*" * 6)
            print(f"Nome: {self.__nome}\nCPF: {self.__cpf}\nMatrícula: {self.__matricula}\nSenha: {self.__senha}\nDepartamento: {self.__departamento}")
            print("*=*" * 6)
        except Exception as e:
            print(f"Ocorreu um erro ao mostrar os dados: {e}")
        finally:
            print("Fim da exibição")

    # Set escolha do usuário para troca de departamento
    def set_departamento(self):
        try:
            while True:
                atualiza = input(f"{self.__nome}, deseja atualizar seu departamento?\n\n[A] Sim\n[B] Não\n\nResposta: ")
                if atualiza.upper() == "A":
                    novo_departamento = input("Digite seu novo departamento (máximo 30 caracteres): ")
                    if len(novo_departamento) > 30:
                        raise DepartamentoInvalidoError("O departamento deve ter no máximo 30 caracteres. Por favor, digite novamente.")
                    self.__departamento = novo_departamento
                    print("Departamento atualizado com sucesso.")
                    return
                elif atualiza.upper() == "B":
                    print(f"Ok, {self.__nome}, você optou por não trocar de departamento.")
                    break
                else:
                    print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")
        except DepartamentoInvalidoError as e:
            print(e)
        except Exception as e:
            print(f"Ocorreu um erro de atualização: {e}")
        finally:
            print("Processo de atualização finalizado.")
