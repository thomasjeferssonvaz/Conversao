from time import sleep
import os
clear = lambda: os.system('cls')


def verifyoctal(num_str):
  octal = "01234567"[:8]
  for x in num_str:
    if x not in octal:
      octaltrue = False
      break
    else:
      octaltrue = True
  # print(octaltrue)
  return octaltrue

def verifydecimal(num_str):
  decimal = "0123456789"[:10] 
  for x in num_str:
    if x not in decimal:
        decimaltrue = False
        break
    else:
      decimaltrue = True  
  # print(decimaltrue)
  return decimaltrue

def verifyhexa(num_str):
  hexa = "0123456789abcdef"[:16] 
  for x in num_str:
    if x not in hexa:
        hexatrue = False
        break
    else:
      hexatrue = True  
  # print(hexatrue)
  return hexatrue

def verifybi(num_str):
  bi = "01"[:2] 
  for x in num_str:
    if x not in bi:
        bitrue = False
        break
    else:
      bitrue = True  
  # print(bitrue)
  return bitrue

def detecao():
  value = input("Coloque os valores a serem convertidos: ")
  print("Verificando sistema...")
  sleep(0.5)
  num_str = list(value)
  # print(num_str)
  resoctal = verifyoctal(num_str)
  resdecimal = verifydecimal(num_str)
  reshexa = verifyhexa(num_str)
  resbi = verifybi(num_str)
  print(f"O valor pode pertencer ao(s) sistema(s): ")
  if resoctal == True:
    print("Octal\n")

  if resdecimal == True:
    print("Decimal\n")
  
  if reshexa == True:
    print("Hexadecimal\n")

  if resbi == True:
    print("Binário\n")
  if not resoctal and not resdecimal and not reshexa and not resbi :
    print("Nenhum\n")

def menu():
  print("———> Menu <———\n")
  print("Escolha sua opção:\n")
  print("1. Verificar sistema")
  print("2. Converter número")
  print("3. Sair")
  switch = int(input("—>"))
  match switch:
    case 1:
      detecao()
    case 2:
      print("VAZIO")
    case 3:
      print("Saindo")
      sleep(1)
      print("Tchau")
    case _:
      print("Opção inválida selecionada")
      sleep(2)
      clear()
      menu()


def main():
  menu()

main()