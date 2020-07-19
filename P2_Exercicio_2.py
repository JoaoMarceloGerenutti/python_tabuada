''' =======================================
ESAMC -  Faculdade de Sorocaba
Programa feito para P2 do Chico.
Disciplina 	: Lógica de Programação e Algoritmos
Professor	: Francisco Tesifom Munhoz
Data	: 1º semestre de 2020
===========================================
P2      : Exercício 02
Autor	: João Marcelo Gerenutti
Data	: 17/06/2020
Comentários	: "Implemente um programa que solicita ao usuário a entrada de dois valores numéricos e, em seguida,
 apresenta para ele o seguinte menu de opções:

========  MENU  =========

Digite + para adição.

Digite – para subtração.

Digite * para multiplicação.

Digite / para divisão.

Digite ^ para potenciação.

========================

Enquanto o usuário não digitar um destes caracteres (+, -, *, / ou ^), o programa deve reexibir o menu.
 Quando o usuário digitar um caracter válido, o programa deve exibir o resultado da operação e encerrar."
============================================
'''

# ENTRADA DE DADOS/DECLARAÇÂO DE VARIAVEL
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

opcao = ""

resultado = int

# SAIDA DE DADOS
print("---------------------------------------------")
print("========  MENU  =========\n" +
      "Digite + para adição.\n" +
      "Digite – para subtração.\n" +
      "Digite * para multiplicação.\n" +
      "Digite / para divisão.\n" +
      "Digite ^ para potenciação.\n" +
      "========================")
print("---------------------------------------------")

# ENTRADA DE DADOS/DECLARAÇÂO DE VARIAVEL
opcao = (input("Digite uma opção do menu acima: "))

# PROCESSAMENTO DE DADOS
if opcao != "":
    # PROCESSAMENTO DE DADOS
    while opcao == "+" or opcao == "-" or opcao == "*" or opcao == "/" or opcao == "^":
        # PROCESSAMENTO DE DADOS
        if opcao == "+":
            resultado = num_1 + num_2
        elif opcao == "-":
            resultado = num_1 - num_2
        elif opcao == "*":
            resultado = num_1 * num_2
        elif opcao == "/":
            if num_2 == 0:
                # SAIDA DE DADOS
                print("Impossivel dividir por 0")
            else:
                # PROCESSAMENTO DE DADOS
                resultado = num_1 / num_2
        else:
            resultado = num_1 ** num_2

        # SAIDA DE DADOS
        print("Resultado de:", num_1, opcao, num_2, "=", resultado)
        print("---------------------------------------------")
        break
    else:
        # SAIDA DE DADOS
        print("Opção inválida!")
        print("---------------------------------------------")
        print("========  MENU  =========\n" +
              "Digite + para adição.\n" +
              "Digite – para subtração.\n" +
              "Digite * para multiplicação.\n" +
              "Digite / para divisão.\n" +
              "Digite ^ para potenciação.\n" +
              "========================")
        print("---------------------------------------------")
        opcao = (input("Digite uma opção do menu acima: "))
        # PROCESSAMENTO DE DADOS
        if opcao == "+":
            resultado = num_1 + num_2
        elif opcao == "-":
            resultado = num_1 - num_2
        elif opcao == "*":
            resultado = num_1 * num_2
        elif opcao == "/":
            if num_2 == 0:
                # SAIDA DE DADOS
                print("Impossivel dividir por 0")
            else:
                # PROCESSAMENTO DE DADOS
                resultado = num_1 / num_2
        else:
            resultado = num_1 ** num_2

        # SAIDA DE DADOS
        print("Resultado de:", num_1, opcao, num_2, "=", resultado)
        print("---------------------------------------------")