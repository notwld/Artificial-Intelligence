import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def objective(x, y):
    return (x - 3.14) ** 2 + (y - 2.72) ** 2 + np.sin(3 * x + 1.41) + np.sin(4 * y - 1.73)


x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x_range, y_range)

Z = objective(X, Y)


fig, ax = plt.subplots()
ax.contourf(X, Y, Z, levels=50, cmap='jet')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Objective Function')


def optimize(learning_rate, num_iterations):

    x = np.random.uniform(-5, 5)
    y = np.random.uniform(-5, 5)

    history = []

    for i in range(num_iterations):
        gradient_x = 2 * (x - 3.14) + 3 * np.cos(3 * x + 1.41)
        gradient_y = 2 * (y - 2.72) + 4 * np.cos(4 * y - 1.73)

        x -= learning_rate * gradient_x
        y -= learning_rate * gradient_y

        history.append((x, y))

    return (x, y), history


def animate(frame):
    learning_rate = 0.1
    num_iterations = frame + 1
    (x, y), history = optimize(learning_rate, num_iterations)
    path = np.array(history)
    ax.plot(path[:, 0], path[:, 1], color='black', alpha=0.1)
    ax.plot(x, y, 'o', color='black')
    ax.set_title(f'Optimization (Learning Rate = {learning_rate}, Iterations = {num_iterations})')
ani = FuncAnimation(fig, animate, frames=100, interval=100)
ani.save('./task2_1.gif', writer='pillow')
plt.show()
