from Servidor import Servidor

class Recepcionista(Servidor):
    def __init__ (self,nome,cpf,senha,matricula,departamento):
        super().__init__(nome,cpf,senha,matricula,departamento)
    def liberarVisitante(self):
        while True:
         try:
            liberar = input("Deseja liberar visitante? SIM [1] ou NÃO [2]")
            if liberar == 1:
                print("Acesso liberado!")
                break
            elif liberar == 2:
                print("Acesso negado!")
                break
                
         except Exception:
             print("""Algo deu errado. Tente novamente.
             """)
             while True:
            liberar = input("Deseja liberar visitante? SIM [1] ou NÃO [2]")
            if liberar == 1:
                print("Acesso liberado!")
                break
            elif liberar == 2:
                print("Acesso negado!")
                break
            else:
                print("Tente novamente")
