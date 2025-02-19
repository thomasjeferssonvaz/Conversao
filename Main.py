from time import sleep
import os
clear = lambda: os.system('cls')


def verify(num_str,base):
  match base:
    case 1:
      list = "01234567"[:8]
    case 2:
      list = "0123456789"[:10]
    case 3:
      list = "0123456789abcdef"[:16]
    case 4:
      list = "01"[:2]
  for x in num_str:
    if x not in list:
      res = False
      break
    else:
      res = True
  return res

def detecao():
  value = input("Coloque os valores a serem convertidos: ").lower()
  print("Verificando sistema...")
  sleep(0.5)
  num_str = list(value)
  # print(num_str)
  resoctal = verify(num_str, 1)
  resdecimal = verify(num_str, 2)
  reshexa = verify(num_str, 3)
  resbi = verify(num_str, 4)
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
  print("1. Sair    2. Verificar novamente")
  saida = int(input("—>"))
  match saida:
    case 1:
      menu()
    case 2:
      clear()
      detecao()
    case _:
      print("\nOpção indisponível! Redirecionando ao menu principal!")
      sleep(2)
      menu()
    
def converteDestino(value, base):
  list = []
  quociente = int(value)//base
  resto = int(value)%base
  list.append(resto)
  while quociente > base-1:
    resto = quociente%base
    list.append(resto)
    quociente = quociente//base
    if quociente < base:
      list.append(quociente)
      break
  list.reverse()
  i = 0
  for x in list:
    if list[i] > 9:
      list[i] = chr(list[i]+55)
    i += 1
  return str(list).strip("[]").replace(",","").replace(" ","").replace("'","")

def converteOrigem(value, base):
  valueList = []
  for x in value:
    valueList.append(x)
  #print(valueList)
  valueList.reverse()
  #print(valueList)
  res = []
  i = 0
  for x in valueList:
    if valueList[i].upper() in ("A","B","C","D","E","F"):
      valueList[i] = ord(valueList[i].upper())-55
      #print(valueList[i])
    a = int(valueList[i]) * int(base)**i
    i += 1
    res.append(a)
  i = 0
  soma = 0
  for x in res:
    soma = soma + int(res[i])
    i += 1
  #print(soma)
  return soma

def converte(value, sysOriginal, sysDestino):
  match sysOriginal:
    case 1:
      valueInterno = converteOrigem(value, 8)
    case 2:
      valueInterno = value
    case 3:
      valueInterno = converteOrigem(value, 16)
    case 4:
      valueInterno = converteOrigem(value, 2)

  match sysDestino:
    case 1:
      resposta = converteDestino(valueInterno, 8)
    case 2:
      resposta = converteDestino(valueInterno, 9)
    case 3: 
      resposta = converteDestino(valueInterno, 16)
    case 4:
      resposta = converteDestino(valueInterno, 2)
    
  return resposta

def conversao():
  clear()
  print("———> Conversão <———")
  print("Escolha o sistema original do valor:\n")
  print("1. Octal\n")
  print("2. Decimal\n")
  print("3. Hexadecimal\n")
  print("4. Binário\n")
  sysOriginal = int(input("—>"))
  if sysOriginal < 1 or sysOriginal > 4:
    print("\nOpção indisponível! Redirecionando ao menu principal!")
    conversao()

  print("\nEscolha para qual sistema converter:\n")
  print("1. Octal\n")
  print("2. Decimal\n")
  print("3. Hexadecimal\n")
  print("4. Binário\n")
  sysDestino = int(input("—>"))
  sysDestinoList = ["", "Octal", "Decimal", "Hexadecimal", "Binário"]
  if sysDestino < 1 or sysDestino > 4:
    print("\nOpção indisponível! Redirecionando ao menu principal!")
    conversao()

  print("\nEscreva o valor a ser convertido:\n")
  value = input("—>")
  if sysOriginal == sysDestino:
    print("sistema de origem é igual ao sistema de destino! Conversão desnecessária, redirencionando ao menu principal.")
    sleep(3)
    menu()
  else:
    resultado = converte(value, sysOriginal, sysDestino)
    print(f"\nO Valor convertido para {sysDestinoList[int(sysDestino)]} é: {resultado}")


    print("1. Sair    2. Converter novamente")
    saida = int(input("—>"))
    match saida:
      case 1:
        menu()
      case 2:
        clear()
        conversao()
      case _:
        print("\nOpção indisponível! Redirecionando ao menu principal!")
        sleep(2)
        menu()

def menu():
  clear()
  print("———> Menu <———\n")
  print("Escolha sua opção:\n")
  print("1. Verificar sistema")
  print("2. Converter número")
  print("3. Sair")
  switch = int(input("—>"))
  match switch:
    case 1:
      clear()
      detecao()
      menu()
    case 2:
      clear()
      conversao()
    case 3:
      print("Saindo")
      sleep(1)
      print("Tchau")
      sleep(1)
      clear()
      exit()
    case _:
      print("Opção inválida selecionada")
      sleep(2)
      clear()
      menu()

def main():
  menu()

main()