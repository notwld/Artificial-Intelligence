# Trajectory (S-metaheuristics)

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def objective_function(x):
    return x ** 2 

def generate_candidates(current_solution):
    candidates = []
    for _ in range(10):  
        candidate = random.uniform(-10, 10)  
        candidates.append(candidate)
    return candidates

def select_candidate(candidates):
    selected_candidate = min(candidates, key=objective_function)
    return selected_candidate

def s_metaheuristic(initial_solution, stopping_criteria):
    current_solution = initial_solution
    iteration = 0

    while True:
        candidates = generate_candidates(current_solution)
        selected_candidate = select_candidate(candidates)
        current_solution = selected_candidate
        iteration += 1
        stopping_criteria = True 
        if stopping_criteria:
            break

    best_solution = current_solution
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

initial_solution = 0  
stopping_criteria = False 

fig, ax = plt.subplots()

def animate(frame):
    best_solution = s_metaheuristic(initial_solution, stopping_criteria)
    update_plot(best_solution)
    if stopping_criteria:
        anim.event_source.stop() 
anim = FuncAnimation(fig, animate, frames=range(1), repeat=False)
anim.save('./task3.gif', writer='pillow')
plt.show()
