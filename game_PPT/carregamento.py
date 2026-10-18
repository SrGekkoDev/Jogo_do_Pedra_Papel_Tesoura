import os
import random
import time

pedra = "🪨"
papel = "📄"
tesoura = "✂️"

imagens = [pedra, papel, tesoura]

# Dicionário para converter o texto da jogada no ícone visual
icones = {
    "pedra": "🪨 PEDRA",
    "papel": "📄 PAPEL",
    "tesoura": "✂️ TESOURA"
}

def carregamento(escolha_maquina, ciclos=15):
    print("Sorteando jogada da máquina...")
    time.sleep(0.5)

    for i in range(ciclos):
        quadro_atual = random.choice(imagens)

        # Limpa o terminal
        os.system("cls" if os.name == "nt" else "clear")

        print("🪨  📄  ✂️  🪨  📄  ✂️  🪨  📄  ✂️  🪨  📄  ✂️\n")
        print(f"      {quadro_atual}      \n")

        # Efeito de desaceleração gradual
        progresso = i / (ciclos - 1)
        atraso = 0.05 + (0.25 * progresso)
        time.sleep(atraso)

    # Exibe o resultado real que a máquina escolheu
    os.system("cls" if os.name == "nt" else "clear")
    print("✨ ESCOLHA DA MÁQUINA ✨\n")
    print(f"👉 {icones.get(escolha_maquina, escolha_maquina)}\n")
    time.sleep(1)