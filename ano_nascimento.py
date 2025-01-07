nome = input("Digite seu nome completo: ")
ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
ano = int(2022)

executando = True

while executando:
  if ano_nascimento >= 1922 and ano_nascimento <= 2021:
    executando = False
  else:
    print("Ano de nascimento inválido")
    ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
  print(f"Olá {nome}, sua idade é: ", ano - ano_nascimento)
