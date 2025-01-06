print('''Bem-vindo a calculadora inteligente!

Menu principal:

1 - soma
2 - subtração
3 - multiplicação
4 - divisão
0 - sair

''')

codigo = input("Digite o código da operação desejada: ")
num1 = input("Digite um número inteiro: ")
num1 = int(num1)
num2 = input("Digite outro número inteiro: ")
num2 = int(num2)

programa_rodando = True

def somar_numeros(num1, num2):
  print (num1 + num2)
  return
def subtrair_numero(num1, num2):
  return num1 - num2

def multiplicar_numero(num1, num2):
  return num1 * num2

def dividir_numero(num1, num2):
  return num1 / num2

while programa_rodando:

  if codigo == "1":
    somar_numeros(num1, num2)
    programa_rodando = False
  elif codigo == "2":
    subtrair_numero()
  elif codigo == "3":
    multiplicar_numero()
  elif codigo == "4":
    dividir_numero()
  elif codigo == "0":
    print("Encerrando programa... Até logo!")
    programa_rodando = False
  else:
    print("Opção inválida")
