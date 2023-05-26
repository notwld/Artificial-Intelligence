# Exercise 4 
import numpy as np

def f1(x, y):
    return (x - 1) ** 2 + y ** 2

def f2(x, y):
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
    convergence_time = 0
    for i in range(max_iter):
        fitness = fitness_func(swarm_pos[:, 0], swarm_pos[:, 1])
        better_fitness_mask = fitness < swarm_best_fitness
        swarm_best_pos[better_fitness_mask] = swarm_pos[better_fitness_mask]
        swarm_best_fitness[better_fitness_mask] = fitness[better_fitness_mask]
        best_particle_idx = np.argmin(swarm_best_fitness)
        if swarm_best_fitness[best_particle_idx] < global_best_fitness:
            global_best_pos = np.copy(swarm_best_pos[best_particle_idx])
            global_best_fitness = swarm_best_fitness[best_particle_idx]
            convergence_time = i
        r1 = np.random.uniform(size=(swarm_size, num_dims))
        r2 = np.random.uniform(size=(swarm_size, num_dims))
        swarm_vel = w * swarm_vel + c1 * r1 * (swarm_best_pos - swarm_pos) + c2 * r2 * (global_best_pos - swarm_pos)
        swarm_pos += swarm_vel
        swarm_pos = np.clip(swarm_pos, search_min, search_max)
    return global_best_pos, global_best_fitness, convergence_time

# Run PSO multiple times to get the average convergence time
num_runs = 10
f1_convergence_times = []
f2_convergence_times = []
for i in range(num_runs):
    _, _, convergence_time = pso(f1)
    f1_convergence_times.append(convergence_time)
    _, _, convergence_time = pso(f2)
    f2_convergence_times.append(convergence_time)

# Print the average convergence time for each function
print("Average convergence time for f1:", np.mean(f1_convergence_times))
print("Average convergence time for f2:", np.mean(f2_convergence_times))
