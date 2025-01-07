print('''Bem-vindo a calculadora inteligente!

Menu principal:

1 - soma
2 - subtração
3 - multiplicação
4 - divisão
0 - sair

''')

def somar_numeros(num1, num2):
  print("O resultado é: ", num1 + num2)

def subtrair_numero(num1, num2):
  print("O resultado é: ", num1 - num2)

def multiplicar_numero(num1, num2):
  print("O resultado é: ", num1 * num2)

def dividir_numero(num1, num2):
  print("O resultado é: ", num1 / num2)

programa_rodando = True

while programa_rodando:
  codigo = input("Digite o código da operação desejada: ")

  if codigo >= "5":
    print("Opção inválida")
    continue

  elif codigo in ["1", "2", "3", "4"]:

    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))

  if codigo == "1":
    somar_numeros(num1, num2)
  elif codigo == "2":
    subtrair_numero(num1, num2)
  elif codigo == "3":
    multiplicar_numero(num1, num2)
  elif codigo == "4":
    dividir_numero(num1, num2)
  elif codigo == "0":
    print("Encerrando programa... Até logo!")
    programa_rodando = False
  else:
    print("Opção inválida")
