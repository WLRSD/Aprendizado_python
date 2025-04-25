# criação de função de tempo a ser iniciado e a ser calculado
import time

# Função para iniciar o tempo
def tempo_iniciar():
    start_time = time.time()
    return start_time

# Função para finalizar o tempo
def tempo_finalizar(start_time):
    end_time = time.time()
    return end_time - start_time