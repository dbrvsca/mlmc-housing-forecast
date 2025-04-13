import numpy as np

# Function to simulate Geometric Brownian Motion at a given level
def simulate_gbm(level, n_samples, T, initial_price, mu, sigma):
    n_steps = 2 ** level
    dt = T / n_steps
    prices = np.full(n_samples, initial_price)

    for _ in range(n_steps):
        Z = np.random.standard_normal(n_samples)
        prices *= np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

    return prices

# Multilevel Monte Carlo estimator
def mlmc_estimate(max_level, samples_per_level, T, initial_price, mu, sigma):
    estimate = 0.0

    for level in range(max_level + 1):
        n = samples_per_level[level]

        if level == 0:
            f_coarse = simulate_gbm(0, n, T, initial_price, mu, sigma)
            estimate += np.mean(f_coarse)
        else:
            f_fine = simulate_gbm(level, n, T, initial_price, mu, sigma)
            f_coarse = simulate_gbm(level - 1, n, T, initial_price, mu, sigma)
            diff = f_fine - f_coarse
            estimate += np.mean(diff)

    return estimate

# Parameters
initial_price = 8154.72  # average price from primary market (PLN/m2)
mu = 0.03
sigma = 0.15
T = 3
max_level = 4
samples_per_level = [10000, 5000, 2500, 1250, 625]

# Run MLMC
mlmc_result = mlmc_estimate(max_level, samples_per_level, T, initial_price, mu, sigma)
print(f"MLMC estimated average price in 3 years: {mlmc_result:.2f} PLN/m²")