import random


choice = [
    "pedra" , "papel" , "tesoura"
]
computer_choice = random.choice(choice)

player = input("Escolha uma das opções: Pedra, Papel ou Tesoura:").lower()

if (player == "tesoura" and computer_choice == "papel") or \
    (player == "pedra" and computer_choice == "tesoura") or \
    (player == "tesoura" and computer_choice == "papel") or \
    (player == "papel" and computer_choice == "pedra"):
    winner = "player"

elif player == computer_choice:
    winner = "empate"

else:
    winner = "computer"

print(winner)