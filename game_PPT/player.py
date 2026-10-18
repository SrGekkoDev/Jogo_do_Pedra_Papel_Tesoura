import questionary

def jogada_player():
    print("Bem Vindo ao jogo do 🪨 ​PEDRA🪨​\n                🗒️ ​PAPEL🗒️​\n        ✂️​ TESOURA✂️​")

    jogada = questionary.select(
        "Escolha uma das opções: Pedra, Papel ou Tesoura:",
        choices=["pedra", "papel", "tesoura"]
    ).ask()
    return jogada