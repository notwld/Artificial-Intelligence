import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def fitness_function(x1, x2):
    f1 = x1 + 2 * -x2 + 3
    f2 = 2 * x1 + x2 - 8
    z = f1 ** 2 + f2 ** 2
    return z


def update_velocity(particle, velocity, pbest, gbest, w_min=0.5, max=1.0, c=0.1):
    num_particle = len(particle)
    new_velocity = np.array([0.0 for i in range(num_particle)])
    r1 = random.uniform(0, max)
    r2 = random.uniform(0, max)
    w = random.uniform(w_min, max)
    c1 = c
    c2 = c
    for i in range(num_particle):
        new_velocity[i] = w * velocity[i] + c1 * r1 * (pbest[i] - particle[i]) + c2 * r2 * (gbest[i] - particle[i])
    return new_velocity


def update_position(particle, velocity):
    new_particle = particle + velocity
    return new_particle


def pso_2d(population, dimension, position_min, position_max, generation, fitness_criterion):
    particles = [[random.uniform(position_min, position_max) for j in range(dimension)] for i in range(population)]
    pbest_position = particles
    pbest_fitness = [fitness_function(p[0], p[1]) for p in particles]
    gbest_index = np.argmin(pbest_fitness)
    gbest_position = pbest_position[gbest_index]
    velocity = [[0.0 for j in range(dimension)] for i in range(population)]
    for t in range(generation):
        if np.average(pbest_fitness) <= fitness_criterion:
            break
        else:
            for n in range(population):
                velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
                particles[n] = update_position(particles[n], velocity[n])
        pbest_fitness = [fitness_function(p[0], p[1]) for p in particles]
        pbest_position = [particles[i] if pbest_fitness[i] < fitness_function(pbest_position[i][0], pbest_position[i][1]) else pbest_position[i] for i in range(population)]
        gbest_index = np.argmin(pbest_fitness)
        gbest_position = pbest_position[gbest_index]
    print('Global Best Position: ', gbest_position)
    print('Best Fitness Value: ', min(pbest_fitness))
    print('Average Particle Best Fitness Value: ', np.average(pbest_fitness))
    print('Number of Generation: ', t)
    return particles, pbest_position, pbest_fitness
population = 100
dimension = 2
position_min = -100.0
position_max = 100.0
generation = 400
fitness_criterion = 10e-4

particles = [[random.uniform(position_min, position_max) for j in range(dimension)] for i in range(population)]
pbest_position = particles
pbest_fitness = [fitness_function(p[0],p[1]) for p in particles]
gbest_index = np.argmin(pbest_fitness)
gbest_position = pbest_position[gbest_index]
velocity = [[0.0 for j in range(dimension)] for i in range(population)]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
x = np.linspace(position_min, position_max, 80)
y = np.linspace(position_min, position_max, 80)
X, Y = np.meshgrid(x, y)
Z= fitness_function(X,Y)
ax.plot_wireframe(X, Y, Z, color='r', linewidth=0.2)
images = []

for t in range(generation):
    if np.average(pbest_fitness) <= fitness_criterion:
        break
    else:
        for n in range(population):
            velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
            particles[n] = update_position(particles[n], velocity[n])
        pbest_fitness = [fitness_function(p[0],p[1]) for p in particles]
        for i in range(population):
            if pbest_fitness[i] < fitness_function(pbest_position[i][0], pbest_position[i][1]):
                pbest_position[i] = particles[i]
        gbest_index = np.argmin(pbest_fitness)
        gbest_position = pbest_position[gbest_index]

    image = ax.scatter3D([particles[n][0] for n in range(population)],
                        [particles[n][1] for n in range(population)],
                        [fitness_function(particles[n][0],particles[n][1]) for n in range(population)], c='b')
    images.append([image])

animated_image = animation.ArtistAnimation(fig, images)
animated_image.save('./task2.gif', writer='pillow')

print('Global Best Position: ', gbest_position)
print('Best Fitness Value: ', min(pbest_fitness))
print('Average Particle Best Fitness Value: ', np.average(pbest_fitness))
print('Number of Generation: ', t+1)
