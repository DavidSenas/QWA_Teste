import Menu_Inicial
from CoresFonte import *
from Menu_Inicial import *
from datetime import time
from Cadastro import *


Lista_CPF = []
Cadastrando_Candidato = []
Candidatos_Cadastrados = [[], [], [], [], []]
Menu_Inicial.Linha_Margem()


print(FonteBranca())
print("Aguarde o Programa está sendo inicializado!")


for segundos in range(0, 11):
    print("-", end="")
    sleep(0.5)
print()


Menu_Inicial.Menu_de_Opções()
Linha_Divisória()


while True:

    try:
        FonteBranca()
        Flag = int(input("Escolha a opção que deseja executar: "))

        if Flag < 1 or Flag > 3:
            print(f"{FonteVermelha()}Opção inválida, escolha entre os número (1, 2 ou 3):{FonteBranca()} ")

        if Flag == 1:
            print("Aguarde, programa está sendo encerrado! ")

            for contador in range(0, 10):
                print(".", end=" ")
                sleep(1)
            print()
            break

        if Flag == 2:
            vaga = int(input("Informe qual vaga ira vincular o Candidato: "))
            Cadastrando_Candidato = [Cadastrar_Candidato(vaga)]

            for CPF in Lista_CPF:
                print()

                for candidatos in Cadastrando_Candidato:
                    print()

                    if candidatos.CPF in CPF.CPF:

                        print(f"{FonteVermelha()}O CPF consta na lista de cadastrados, Não foi possivel continuar o cadastro{FonteBranca()}")
                        exec()
                        print()
                        Linha_Divisória()

            Lista_CPF = Cadastrando_Candidato
            Linha_Divisória()
            print()
            print("Verifique  os dados do candidato cadastrado! ")
            print()

            for candidato in Cadastrando_Candidato:

                print(candidato)
            print()
            Flag = int(input(f"Digite [1] para vincular o canditado a uma das vaga {vaga}, ou [2] para Retornar Menu anterior! "))
            print()
            Linha_Divisória()

            if Flag == 1:

                if len(Candidatos_Cadastrados[vaga-1]) == 3:
                    print(f"{FonteVermelha()}O candidato não pode ser cadastrado por esceder o numero previsto por vaga!{FonteBranca()}")
                else:

                    Candidatos_Cadastrados[vaga-1].append(Cadastrando_Candidato)
                    print("Aguarde, estamos verificando a disponibilidade de vaga!")

                    for contador in range(0, 2):
                        sleep(1)
                    print()
                    print(f"{FonteVerde()}Candidatos Vinculado a Vaga {vaga} com Sucesso!{FonteBranca()}")
                    Linha_Divisória()

                Menu_de_Opções()

            if Flag == 2:

                continue
            Linha_Divisória()

        if Flag == 3:

            for cadastro in Candidatos_Cadastrados:
                for candidatos in cadastro:
                    for dados in candidatos:
                        print(f"{dados}", end=" ")
                        print()
                        Linha_Divisória()
                    print()

            Flag = int(input("Escolha [1] para salvar, ou [2] para Deletar Cadastrados(OBS: essa opção perderá todos os dados: "))
            if Flag == 1:
                print("A lista Foi Salva com sucesso")

            if Flag == 2:
                Candidatos_Cadastrados.clear()
                Lista_CPF.clear()
                print("Lista de Candidatos foi deletada! ")

    except:
        print(f"{FonteVermelha()}Reinicie o cadastro !{FonteBranca()}")
        Linha_Divisória()
        Menu_de_Opções()


print()
print(f"Programa Finalizado!{ResetFonte()}")
Linha_Margem()

