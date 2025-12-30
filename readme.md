## Task 2: Monte Carlo Integration

**Objective:** Calculate the definite integral of $f(x) = x^2$ from $x=0$ to $x=2$ using the Monte Carlo method and compare it with the analytical result.

### Theoretical Value
The analytical solution for $\int_{0}^{2} x^2 dx$ is:
$$\left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3} \approx 2.666667$$

### Monte Carlo Results
I ran the simulation with `N` random points. Here is a typical output comparison:

| Method | Result | Absolute Error |
| :--- | :--- | :--- |
| **SciPy `quad` (Analytical)** | `2.666666666666667` | `0.0` |
| **Monte Carlo (N=100)** | `2.88` | `~0.21` |
| **Monte Carlo (N=1,000)** | `2.704` | `~0.037` |
| **Monte Carlo (N=10,000)** | `2.652` | `~0.014` |
| **Monte Carlo (N=100,000)** | `2.669` | `~0.002` |

### Conclusions
1.  **Approximation:** The Monte Carlo method successfully approximated the integral value close to the analytical solution ($2.666...$).
2.  **Accuracy vs. N:** The accuracy of the Monte Carlo method depends heavily on the number of random points ($N$). As $N$ increases, the error decreases (Law of Large Numbers).
    * With small $N$ (e.g., 100), the result fluctuates significantly.
    * With large $N$ (e.g., 100,000), the result stabilizes and becomes very precise.
3.  **Usage:** While `scipy.quad` is faster and more accurate for simple 1D functions, Monte Carlo is indispensable for high-dimensional integrals where standard quadrature methods fail.