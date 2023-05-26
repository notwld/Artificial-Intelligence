# Exercise 1
# Lab 7 Functions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def pso(fitness_func, swarm_size=50, max_iter=100, c1=2.0, c2=2.0, w=0.7):
    search_min = -5
    search_max = 5
    num_dims = 2
    swarm_pos = np.random.uniform(search_min, search_max, (swarm_size, num_dims))
    swarm_vel = np.zeros((swarm_size, num_dims))
    swarm_best_pos = np.copy(swarm_pos)
    swarm_best_fitness = np.full((swarm_size,), np.inf)
    global_best_pos = np.zeros((num_dims,))
    global_best_fitness = np.inf
    positions_history = []  # for animation
    for i in range(max_iter):
        fitness = fitness_func(swarm_pos[:, 0], swarm_pos[:, 1])
        better_fitness_mask = fitness < swarm_best_fitness
        swarm_best_pos[better_fitness_mask] = swarm_pos[better_fitness_mask]
        swarm_best_fitness[better_fitness_mask] = fitness[better_fitness_mask]
        best_particle_idx = np.argmin(swarm_best_fitness)
        if swarm_best_fitness[best_particle_idx] < global_best_fitness:
            global_best_pos = np.copy(swarm_best_pos[best_particle_idx])
            global_best_fitness = swarm_best_fitness[best_particle_idx]
        r1 = np.random.uniform(size=(swarm_size, num_dims))
        r2 = np.random.uniform(size=(swarm_size, num_dims))
        swarm_vel = w * swarm_vel + c1 * r1 * (swarm_best_pos - swarm_pos) + c2 * r2 * (global_best_pos - swarm_pos)
        swarm_pos += swarm_vel
        swarm_pos = np.clip(swarm_pos, search_min, search_max)
        positions_history.append(np.copy(swarm_pos))  # for animation
    return global_best_pos, global_best_fitness, positions_history

best_pos, best_fitness, positions_history = pso(f)

# Animation code
fig, ax = plt.subplots()
scat = ax.scatter([], [])
def init():
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    return scat,

def update(i):
    scat.set_offsets(positions_history[i])
    return scat,

ani = FuncAnimation(fig, update, frames=len(positions_history), init_func=init, blit=True)
ani.save("task1_2.gif", dpi=120, writer="imagemagick")
plt.show()
