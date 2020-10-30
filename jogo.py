import random
import time
import os
# pedra papel tesoura

items = ("Pedra", "Papel", "Tesoura")
placar_pc = 0
placar_player = 0
nome = str(input("Digite o nome do desafiante: ")).title()
mensagem_boas_vindas = "Seja bem vindo desafiante {}!".format(nome)
for palavra in mensagem_boas_vindas:
	print("{}".format(palavra), end='',flush=True)
	time.sleep(0.1)
print()
up1 = "No mundo da programação tudo vale a pena e tudo é possível!"
for palavra in up1:
	print("{}".format(palavra), end='',flush=True)
	time.sleep(0.1)
print()
up2 = "Chegou a hora de enfrente seu computador!"
for palavra in up2:
	print("{}".format(palavra), end='',flush=True)
	time.sleep(0.1)
print()
up3 = "{} se você está pronto, digite enter para iniciar seu desafio!".format(nome)
for palavra in up3:
	print("{}".format(palavra), end='',flush=True)
	time.sleep(0.1)
print()
input()
print("Entrando no universo do jogo...")
time.sleep(1)
while True:
	os.system("clear")
	pc = random.randint(0, 2)
	print("""

\033[1;96m||||||| J O G O :  P E D R A   P A P E L   T E S O U R A |||||||\033[m


PLACAR DO JOGO:

-------   -----------
\033[1;94mPc [\033[m\033[1;31m{}\033[m] | |[\033[1;31m{}\033[m] \033[1;94mPlayer\033[m
-------   -----------
		""".format(placar_pc,placar_player))
	print("""
\033[1;93m------------------------------\033[m
[0] - Pedra    [x] - Sair
[1] - Papel    [y] - Pause
[2] - Tesoura
\033[1;93m------------------------------\033[m
	""")
	player = input("Digite um número de 0 a 2: ")
	if player.isnumeric():
		player = int(player)
		print("Computador está jogando...")
		time.sleep(0.5)
		print("Batendo dados do usuário e o computador...\n")
		time.sleep(0.5)
		if pc == player:
		    print("Empate!")
		    time.sleep(1)
		    os.system("clear")
		elif pc == 0 and player == 1:
		    print("{} venceu!".format(nome))
		    placar_player += 1
		    time.sleep(1)
		    os.system("clear")
		elif pc == 1 and player == 0:
		    print("Pc venceu!")
		    time.sleep(1)
		    placar_pc += 1
		    os.system("clear")
		elif pc == 2 and player == 1:
		    print("Pc venceu!")
		    time.sleep(1)
		    placar_pc += 1
		    os.system("clear")
		elif pc == 2 and player == 2:
		    print("Empate!")
		    time.sleep(1)
		    os.system("clear")
		elif pc == 1 and player == 1:
		    print("Empate!")
		    time.sleep(1)
		    os.system("clear")
		elif pc == 0 and player == 0:
		    print("Empate!")
		    time.sleep(1)
		    os.system("clear")
		elif pc == 2 and player == 0:
		    print("{} venceu!".format(nome))
		    time.sleep(1)
		    placar_player += 1
		elif pc == 0 and player == 2:
		    print("Pc venceu")
		    time.sleep(1)
		    placar_pc += 1
		    os.system("clear")
		elif pc == 1 and player == 2:
		    print("{} venceu!".format(nome))
		    time.sleep(1)
		    placar_player += 1
		    os.system("clear")
		else:
			print("\033[1;91mJogada não disponível!\033[m")
			time.sleep(1)
			os.system("clear")
	elif player == "X" or player == "x":
		break

	elif player == "Y" or player == "y":
		os.system("clear")
		print("\033[1;91mJOGO   PAUSADO!\033[m")
		input("Dê enter para voltar a jogar, {}... ".format(nome))
		os.system("clear")
	else:
		os.system("clear")
