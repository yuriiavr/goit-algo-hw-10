import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# Метод Монте-Карло
num_samples = 10000
x_random = np.random.uniform(a, b, num_samples)
y_random = np.random.uniform(0, b**2, num_samples)

under_curve = y_random <= f(x_random)
monte_carlo_result = (under_curve.sum() / num_samples) * (b * b**2)

# Аналітичний розрахунок з використанням quad
quad_result, error = spi.quad(f, a, b)

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Інтеграл методом Монте-Карло: {monte_carlo_result:.4f}\nАналітичний інтеграл: {quad_result:.4f}')
plt.grid()
plt.show()

print(f'Інтеграл методом Монте-Карло: {monte_carlo_result:.6f}')
print(f'Аналітичний інтеграл: {quad_result:.6f}, похибка: {error:.6e}')
