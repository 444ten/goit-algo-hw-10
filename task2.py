import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  # Lower bound
b = 2  # Upper bound

# N = 100
# N = 1_000
N = 10_000
# N = 100_000

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

points_under_curve = y_rand <= f(x_rand)
count_under_curve = np.sum(points_under_curve)

rectangle_area = (b - a) * f(b)
monte_carlo_area = (count_under_curve / N) * rectangle_area

analytical_result, error = spi.quad(f, a, b)

print(f"Monte Carlo Result (N={N}): {monte_carlo_area}")
print(f"Analytical Result (SciPy): {analytical_result}")
print(f"Error: {abs(monte_carlo_area - analytical_result)}")

x_plot = np.linspace(a - 0.5, b + 0.5, 400)
y_plot = f(x_plot)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_plot, y_plot, 'r', linewidth=2, label='f(x) = x^2')

ax.scatter(x_rand[points_under_curve], y_rand[points_under_curve], color='green', s=1, alpha=0.3, label='Under Curve')
ax.scatter(x_rand[~points_under_curve], y_rand[~points_under_curve], color='blue', s=1, alpha=0.3, label='Above Curve')

ax.set_xlim([a - 0.5, b + 0.5])
ax.set_ylim([0, f(b) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Monte Carlo Integration (N={N})')
ax.legend()
ax.grid(True)

plt.show()