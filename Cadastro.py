from datetime import date
from CoresFonte import FonteBranca, FonteVermelha, ResetFonte


class Cadastrar_Candidato:
    def __init__(self, vaga=0):
        self.vaga = vaga
        mes_atual = date.today().month
        ano_atual = date.today().year
        self.capacidade_civil = " "

        try:
            while True:
                self.nome = str(input("Digite o nome do candidato: ")).upper().strip()
                self.sobrenome = str(input("Digite o sobrenome do candidato: ")).upper().strip()

                while True:

                    try:
                        self.CPF = str(input("Digite o númdero de CPF composto por 11 digitos (apenas números): "))

                    except:
                        print(f"{FonteVermelha()}Houve um erro ao digitar o CPF, tente novamente{FonteBranca()}")

                    else:
                        if not self.CPF.isnumeric():
                            print(f"{FonteVermelha()}Digite apenas números Apenas numeros{FonteBranca()}")

                        elif len(self.CPF) < 11 or len(self.CPF) > 11:
                            print(f"{FonteVermelha()}Verifique se o CPF digitado corresponde a 11 digitos! {FonteBranca()}")

                        elif len(self.CPF) == 11:
                            break

                while True:
                    mes_de_nascimento = str(input("Digite o mês de nascimento do candidato com 2 digitos: "))
                    mes_de_nascimento = int(mes_de_nascimento)
                    if mes_de_nascimento <= 0 or mes_de_nascimento > 12:
                        print(f"{FonteVermelha()}Verifique o Mês de nascimento, ele deve ser composto por 2 digitos!{FonteBranca()}")

                    else:
                        break

                while True:
                    ano_de_nascimento = str(input("Digite o Ano de nascimento do candidato com 4 Digitos: "))

                    if not ano_de_nascimento.isnumeric():
                        print(f"{FonteVermelha()}Digite apenas números{FonteBranca()}")

                    elif len(ano_de_nascimento) < 4:
                        print(f"{FonteVermelha()}O ano deve ser composto por 4 Digitos: {FonteBranca()}")

                    else:
                        ano_de_nascimento = int(ano_de_nascimento)
                        self.idade = (ano_atual - ano_de_nascimento)
                        break

                if self.idade < 18:
                    self.capacidade_civil = f"O danditado {self.nome} é menor de idade!"

                elif self.idade >= 18:
                    self.capacidade_civil = "maior de idade"


                else:
                    if mes_de_nascimento > mes_atual and self.idade == 18:
                        self.capacidade_civil = f" O canditado {self.nome} vai completar {self.idade}"
                break

        except Exception as erro:
            print(f"{FonteVermelha()}Houve um erro {erro}inesperado, faça o cadastro novamente!{FonteBranca()} ")

    def __repr__(self):
        return f"Vaga: {self.vaga} Nome:{self.nome} Sobrenome: {self.sobrenome}  CPF: {self.CPF} Idade: {self.idade} Observação: {self.capacidade_civil} "


