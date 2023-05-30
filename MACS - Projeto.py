import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_virus_spread(N, I0, D0, R0, beta, gamma, mu, t_max):
    S = N - I0 - D0 - R0
    I = I0
    R = R0
    D = D0
    
    susceptible = [S]
    infected = [I]
    dead = [D]
    
    for t in range(1, t_max):
        # Certo grau de aleatorieadade
        new_infections = np.random.poisson(beta * S * I / N)
        new_recoveries = np.random.poisson(I * gamma)
        new_deaths = np.random.poisson(I * mu)
        
        S -= new_infections - new_deaths
        I += new_infections - new_recoveries - new_deaths
        D += new_deaths
        S += new_recoveries  # Pessoas que se recuperaram podem se reeinfectar novamente
        
        # População deve ficar sempre menor que a quantidade inicial de pessoas (sistema fechado)
        S = max(0, min(S, N))
        I = max(0, min(I, N))
        D = max(0, min(D, N))
        
        susceptible.append(S)
        infected.append(I)
        dead.append(D)
    
    return susceptible, infected, dead

N_pessoas = 50
Infectados, D0, R0 = 1, 0, 0
tax_infec, tax_rec, tax_mort = 0.17, 0.02, 0.001
t_max = 250

s, i, d = simulate_virus_spread(N_pessoas, Infectados, 0, 0, tax_infec, tax_rec, tax_mort, t_max)

fig, ax = plt.subplots()
susceptible_line, = ax.plot([], [], label='Susceptible')
infected_line, = ax.plot([], [], label='Infected')
dead_line, = ax.plot([], [], label='Dead')
ax.legend()


def init():
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, N_pessoas)
    susceptible_line.set_data([], [])
    infected_line.set_data([], [])
    dead_line.set_data([], [])
    return susceptible_line, infected_line, dead_line

def update(frame):
    susceptible_line.set_data(np.arange(frame+1), s[:frame+1])
    infected_line.set_data(np.arange(frame+1), i[:frame+1])
    dead_line.set_data(np.arange(frame+1), d[:frame+1])
    return susceptible_line, infected_line, dead_line

ani = animation.FuncAnimation(fig, update, frames=t_max, init_func=init, blit=True)
plt.show()
