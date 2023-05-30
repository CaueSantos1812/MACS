import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

tempo = 30
fig, ax = plt.subplots()
t = np.arange(0, tempo)

line_suscetiveis, = ax.plot([], [], label='Suscetíveis')
line_infectados, = ax.plot([], [], label='Infectados')
line_recuperados, = ax.plot([], [], label='Recuperados')
line_mortos, = ax.plot([], [], label='Mortos')

def init():
    ax.set_xlim(0, tempo)
    ax.set_ylim(0, 100000)
    ax.set_xlabel('Tempo (dias)')
    ax.set_ylabel('Número de Pessoas')
    ax.set_title('Dinâmica do Vírus')
    ax.legend()
    return line_suscetiveis, line_infectados, line_recuperados, line_mortos

def update(frame):
    N = 100000
    I0 = 100
    S0 = N - I0
    R0 = 0
    D0 = 0
    taxa_de_infecção = 0.8
    taxa_de_recuperação = 0.01
    taxa_de_mortalidade = 0.02

    suscetiveis, S = [S0], S0
    infectados, I = [I0], I0
    recuperados, R = [R0], R0
    mortos, D = [D0], D0

    for i in range(1, frame + 1):
        S = S - (taxa_de_infecção * I * S / N)
        I = I + taxa_de_infecção * I * S / N - taxa_de_recuperação * I - taxa_de_mortalidade * I
        R = N - S - I - D
        D = D + taxa_de_mortalidade * I

        if S < 0:
            S = 0
        if I < 0:
            I = 0
        if R < 0:
            R = 0
        if D < 0:
            D = 0

        suscetiveis.append(S)
        infectados.append(I)
        recuperados.append(R)
        mortos.append(D)

    line_suscetiveis.set_data(t[:frame+1], suscetiveis)
    line_infectados.set_data(t[:frame+1], infectados)
    line_recuperados.set_data(t[:frame+1], recuperados)
    line_mortos.set_data(t[:frame+1], mortos)

    return line_suscetiveis, line_infectados, line_recuperados, line_mortos

ani = FuncAnimation(fig, update, frames=range(tempo), init_func=init, blit=True, interval=100)

#nome_arquivo = 'teste_projeto.gif'
#ani.save(nome_arquivo, writer='imagemagick')

plt.show()