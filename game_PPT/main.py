import random
from player import obter_jogada
import questionary


#pontuação
player_wins = 0
computer_wins = 0

#loop até alguem fazer mais que 3 pontos
while computer_wins < 2 and player_wins < 2:
#Aleatoriza oque a maquina vai jogar
    choice = ["pedra" , "papel" , "tesoura"]
    computer_choice = random.choice(choice)

    player = obter_jogada

    if (player == "tesoura" and computer_choice == "papel") or \
        (player == "pedra" and computer_choice == "tesoura") or \
        (player == "tesoura" and computer_choice == "papel") or \
        (player == "papel" and computer_choice == "pedra"):
        winner = "player"

    elif player == computer_choice:
        winner = "empate"
        player_wins += 1

    else:
        winner = "computer"
        computer_wins += 1
    
    if player_wins > computer_wins:
        print(f"Você ganhou!!")

    else:
        print(f"A maquina venceu!!")

    
continuar = questionary.select("deseja continuar?",["Continuar", "Parar"]).ask()

if continuar == "Continuar":
    print("a")
else:
    print("b")
