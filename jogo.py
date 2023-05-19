# criar um programa que faça o computador jogar Jokenpô com vocÊ


import random as rd
import time

jogo = "JOKENPÔ"
print(f"{jogo:=^60}")

escolhas = ["[1] Pedra", "[2] Papel", "[3] Tesoura"]
escolha_pc = rd.choice(escolhas)
print("Escolha uma opção digitando um número de 1 a 3:")
for escolha in escolhas:
    print(escolha)

# Mensagem de erro para caso o input não seja uma das opções em número
while True:
    try:
        escolha_usuario = int(input("Qual é a sua jogada? "))
        if escolha_usuario < 1 or escolha_usuario > 3:
            print("Escolha uma opção válida")
        else:
            break
    except ValueError:
        print("Escolha uma opção válida")

# Mostrar o "carregamento" do resultado
print("JO")
time.sleep(0.7)
print("KEN")
time.sleep(0.7)
print("PÔ")
time.sleep(0.7)

# Condições com base na escolha do jogador
if escolha_usuario == 1:
    print("Você escolheu [1] Pedra")
elif escolha_usuario == 2:
    print("Você escolheu [2] Papel")
else:
    print("Você escolheu [3] Tesoura")

# Escolha do computador
if 1 <= escolha_usuario <= 3:
    print(f"O computador escolheu: {escolha_pc}")

# Dicionário de relações de vitória
relacoes_vitoria = {
    1: [3],  # Pedra vence Tesoura
    2: [1],  # Papel vence Pedra
    3: [2],  # Tesoura vence Papel
}

# Verificar o resultado do embate
if escolha_pc == escolhas[escolha_usuario - 1]:
    print("EMPATE")
elif escolha_pc in [escolhas[i - 1] for i in relacoes_vitoria[escolha_usuario]]:
    print("VOCÊ GANHOU")
else:
    print("VOCÊ PERDEU PARA O COMPUTADOR")