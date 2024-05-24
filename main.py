import random

print("+-------------------------------------+")
print("+ Bem Vindo ao Jogo do Número Secreto +")
print("+-------------------------------------+")
numero_secreto = random.randint(1, 5)
tentativas_maximas = 3
tentativas = 1

while tentativas <= tentativas_maximas:
  print("Você está na tentativa", tentativas, "de", tentativas_maximas, ":")
  numero_usuario = int(input("Digite um Número "))
  
  if numero_secreto == numero_usuario:
    print("Você Acertou")
    break
  elif numero_usuario < numero_secreto:
    print("O Número secreto é maior")
  else:
    print("O Número secreto é menor")
  
  tentativas += 1