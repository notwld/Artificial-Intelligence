# a single-based metaheuristic (S-metaheuristic) 

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def objective_function(x):
    return x ** 2 

def generate_candidates(current_solutions):
    candidates = []
    for solution in current_solutions:
        for _ in range(10):  # Generate 10 candidate solutions for each current solution
            candidate = random.uniform(-10, 10)  # Example: Generate random candidates within range [-10, 10]
            candidates.append(candidate)
    return candidates

def select_solution(candidates):
    selected_solution = min(candidates, key=objective_function)
    return selected_solution

def s_metaheuristic(initial_solutions, stopping_criteria):
    current_solutions = initial_solutions.copy()
    iteration = 0

    while True:
        candidates = generate_candidates(current_solutions)
        selected_solution = select_solution(candidates)
        current_solutions = [selected_solution] * len(current_solutions)
        iteration += 1

        stopping_criteria = True 
        if stopping_criteria:
            break

    best_solution = min(current_solutions, key=objective_function)
    return best_solution

def update_plot(solution):
    plt.cla()
    x = np.linspace(-10, 10, 100)
    y = objective_function(x)
    plt.plot(x, y, 'b-', label='Objective Function')
    plt.scatter(solution, objective_function(solution), c='r', label='Current Solutions')

    plt.xlim(-10, 10)
    plt.ylim(0, 100)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

initial_solutions = [0, 0]  
stopping_criteria = False  

fig, ax = plt.subplots()

def animate(frame):
    best_solution = s_metaheuristic(initial_solutions, stopping_criteria)
    update_plot(best_solution)
    if stopping_criteria:
        anim.event_source.stop() 

anim = FuncAnimation(fig, animate, frames=range(1), repeat=False)
anim.save('./task3_2.gif', writer='pillow')
plt.show()
