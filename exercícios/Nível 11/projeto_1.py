import random

def game_start():
    print("\nBem-vindo(a) à Aventura: A Busca pelo Artefato Perdido!")
    print("Você é um aventureiro renomado, conhecido por sua coragem e astúcia. Rumores de um artefato antigo com poderes inimagináveis o levaram a uma floresta densa e misteriosa. A lenda diz que o artefato está escondido em um templo esquecido, guardado por criaturas místicas e armadilhas mortais.")
    print("\nVocê se encontra na Entrada da Floresta.")
    print("Uma trilha estreita se abre para uma floresta escura e silenciosa. O ar é pesado e a luz do sol mal penetra as copas das árvores.")
    choose_path('entrada_floresta')

def choose_path(location):
    if location == 'entrada_floresta':
        print("\nOpções:")
        print("A. Seguir a trilha principal.")
        print("B. Investigar um barulho estranho à direita.")
        print("C. Procurar por atalhos na mata fechada.")
        choice = input("Escolha A, B ou C: ").upper()
        if choice == 'A':
            clareira()
        elif choice == 'B':
            rio()
        elif choice == 'C':
            ruinas_antigas()
        else:
            print("Escolha inválida. Tente novamente.")
            choose_path('entrada_floresta')

def clareira():
    print("\nVocê chegou à Clareira.")
    print("Uma pequena clareira iluminada pelo sol, com flores exóticas e um silêncio perturbador. No centro, há uma estátua coberta de musgo.")
    print("\nOpções:")
    print("A. Examinar a estátua.")
    print("B. Continuar pela trilha.")
    choice = input("Escolha A ou B: ").upper()
    if choice == 'A':
        if random.random() < 0.7: # 70% chance of trap
            armadilha_espinhos()
        else:
            templo_escondido()
    elif choice == 'B':
        caverna_escura()
    else:
        print("Escolha inválida. Tente novamente.")
        clareira()

def rio():
    print("\nVocê chegou ao Rio.")
    print("Um rio de águas escuras e correnteza forte. Há uma ponte de madeira velha e bamba.")
    print("\nOpções:")
    print("A. Atravessar a ponte.")
    print("B. Seguir a margem do rio.")
    choice = input("Escolha A ou B: ").upper()
    if choice == 'A':
        if random.random() < 0.5: # 50% chance of bridge breaking
            queda_no_rio()
        else:
            outro_lado_rio()
    elif choice == 'B':
        caverna_escura()
    else:
        print("Escolha inválida. Tente novamente.")
        rio()

def ruinas_antigas():
    print("\nVocê chegou às Ruínas Antigas.")
    print("Restos de uma civilização esquecida, cobertos por vegetação. Há inscrições ilegíveis nas pedras.")
    print("\nOpções:")
    print("A. Tentar decifrar as inscrições.")
    print("B. Procurar por passagens secretas.")
    choice = input("Escolha A ou B: ").upper()
    if choice == 'A':
        if random.random() < 0.6: # 60% chance of ambush
            emboscada()
        else:
            templo_escondido()
    elif choice == 'B':
        caverna_escura()
    else:
        print("Escolha inválida. Tente novamente.")
        ruinas_antigas()

def caverna_escura():
    print("\nVocê entrou na Caverna Escura.")
    print("Uma caverna úmida e escura. Sons estranhos ecoam lá dentro.")
    print("\nOpções:")
    print("A. Entrar na caverna.")
    print("B. Voltar para a Clareira.")
    choice = input("Escolha A ou B: ").upper()
    if choice == 'A':
        if random.random() < 0.8: # 80% chance of spider nest
            ninho_aranhas()
        else:
            tesouro_escondido()
    elif choice == 'B':
        clareira()
    else:
        print("Escolha inválida. Tente novamente.")
        caverna_escura()

def outro_lado_rio():
    print("\nVocê atravessou o rio com segurança. Há uma trilha que leva a um local familiar.")
    print("\nOpções:")
    print("A. Seguir a trilha.")
    choice = input("Escolha A: ").upper()
    if choice == 'A':
        caverna_escura()
    else:
        print("Escolha inválida. Tente novamente.")
        outro_lado_rio()

def templo_escondido():
    game_win("Você encontrou o templo, e dentro dele, o artefato! A aventura termina com sucesso!")

def armadilha_espinhos():
    game_over("Você caiu em uma armadilha de espinhos. Fim de jogo.")

def queda_no_rio():
    game_over("A ponte quebrou e você foi levado pela correnteza. Fim de jogo.")

def emboscada():
    game_over("Você foi emboscado por criaturas. Fim de jogo.")

def ninho_aranhas():
    game_over("Você entrou em um ninho de aranhas gigantes. Fim de jogo.")

def tesouro_escondido():
    game_win("Você encontrou um tesouro valioso! A aventura termina com sucesso!")

def game_over(message):
    print("\n" + message)
    print("\nGAME OVER")

def game_win(message):
    print("\n" + message)
    print("\nPARABÉNS! VOCÊ VENCEU!")

if __name__ == "__main__":
    game_start()