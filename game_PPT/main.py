import random
import questionary
from player import jogada_player
from carregamento import carregamento

player_wins = 0
computer_wins = 0

# Loop até alguém fazer 2 pontos
while computer_wins < 2 and player_wins < 2:
    print(f"\n--- PLACAR: Você {player_wins} x {computer_wins} Máquina ---")
    
    # 1. Pega a jogada do jogador
    player = jogada_player()

    if not player:
        break

    # 2. A máquina sorteia a opção
    choices = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(choices)

   
    carregamento(computer_choice)

    
    if (player == "tesoura" and computer_choice == "papel") or \
       (player == "pedra" and computer_choice == "tesoura") or \
       (player == "papel" and computer_choice == "pedra"):
        print("🎉🎉 Você ganhou esta rodada!! 🎉🎉")
        player_wins += 1

    elif player == computer_choice:
        print("🤝 Empate nesta rodada!! 🤝")

    else:
        print("💻 A máquina venceu esta rodada!! 💻")
        computer_wins += 1

# Fim de jogo
print("\n============================================")
if player_wins > computer_wins:
    print("🏆 PARABÉNS! Você Venceu!!!!")
else:
    print("🤖 FIM DE JOGO! A máquina venceu!!")
print("==============================================\n")

# Pergunta se quer continuar
continuar = questionary.select("Deseja jogar novamente?", ["Continuar", "Parar"]).ask()

if continuar == "Continuar":
    print("Reiniciando...")
else:
    print("Obrigado por jogar!")