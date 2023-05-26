# Exercise 1
# Lab 8 Functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, y):
    return (x - 3.14) ** 2 + (y - 2.72) ** 2 + np.sin(3 * x + 1.41) + np.sin(4 * y - 1.73)

def pso_animation():
    search_min = -10
    search_max = 10
    num_dims = 2
    swarm_size = 50
    max_iter = 100
    c1 = 2.0
    c2 = 2.0
    w = 0.7

    swarm_pos = np.random.uniform(search_min, search_max, (swarm_size, num_dims))
    swarm_vel = np.zeros((swarm_size, num_dims))
    swarm_best_pos = np.copy(swarm_pos)
    swarm_best_fitness = np.full((swarm_size,), np.inf)
    global_best_pos = np.zeros((num_dims,))
    global_best_fitness = np.inf

    fig, ax = plt.subplots()
    x = np.linspace(search_min, search_max, 100)
    y = np.linspace(search_min, search_max, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.contour(X, Y, Z, levels=50, cmap='jet')
    ax.set_xlim([search_min, search_max])
    ax.set_ylim([search_min, search_max])
    sc = ax.scatter([], [])

    def animate(i):
        nonlocal swarm_pos, swarm_vel, swarm_best_pos, swarm_best_fitness, global_best_pos, global_best_fitness
        fitness = f(swarm_pos[:, 0], swarm_pos[:, 1])
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

        sc.set_offsets(swarm_pos)
        return sc,

    ani = animation.FuncAnimation(fig, animate, frames=max_iter, interval=50, blit=True)
    ani.save("Task1_1.gif", dpi=120, writer="imagemagick")
    plt.show()

pso_animation()
