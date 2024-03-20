import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Обчислення інтеграла функції f на інтервалі [a, b] методом Монте-Карло
def monte_carlo_integration(f, a, b, samples=10000):
    x_random = np.random.uniform(a, b, samples)
    f_values = f(x_random)
    area = (b - a) / samples * np.sum(f_values)
    return area

# Порівняння результатів методу Монте-Карло та функції quad
def compare_with_quad(f, a, b):
    mc_result = monte_carlo_integration(f, a, b)
    quad_result, _ = spi.quad(f, a, b)
    print(f"Метод Монте-Карло: {mc_result}, Функція quad: {quad_result}")

# Візуалізація функції та області під кривою, що інтегрується
def plot_function(f, a, b):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()

# Параметри
a = 0
b = 2

# Виконання функцій
plot_function(f, a, b)
compare_with_quad(f, a, b)
