#  a population-based metaheuristic (P-metaheuristic) algorithm
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def objective_function(x):
    return x ** 2  

def generate_population(population_size):
    population = []
    for _ in range(population_size):
        solution = random.uniform(-10, 10)  # Example: Generate random solutions within range [-10, 10]
        population.append(solution)
    return population

def replace_population(population):
    # Generate a new population based on the current population
    new_population = population.copy()  
    return new_population

def preselect_population(population):
    new_population = population.copy() 
    return new_population

def p_metaheuristic(population_size, stopping_criteria):
    population = generate_population(population_size)
    iteration = 0

    while True:
        population = replace_population(population)
        population = preselect_population(population)
        iteration += 1

        stopping_criteria = True
        if stopping_criteria:
            break

    best_solution = min(population, key=objective_function)
    return best_solution

def update_plot(solution):
    plt.cla()
    x = np.linspace(-10, 10, 100)
    y = objective_function(x)
    plt.plot(x, y, 'b-', label='Objective Function')
    
    plt.scatter(solution, objective_function(solution), c='r', label='Current Solution')
    plt.xlim(-10, 10)
    plt.ylim(0, 100)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()


population_size = 10 
stopping_criteria = False  
fig, ax = plt.subplots()

def animate(frame):
    best_solution = p_metaheuristic(population_size, stopping_criteria)
    update_plot(best_solution)
    if stopping_criteria:
        anim.event_source.stop() 
anim = FuncAnimation(fig, animate, frames=range(1), repeat=False)
anim.save('./task3_1.gif', writer='pillow')
plt.show()
