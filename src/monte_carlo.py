import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_price = 8154.72  # average price from primary market (PLN/m2)
mu = 0.03  # expected annual return
sigma = 0.15  # annual volatility
T = 3  # years
n_simulations = 10000
n_steps = 12 * T

dt = T / n_steps

# Simulate paths
prices = np.zeros((n_simulations, n_steps + 1))
prices[:, 0] = initial_price

for t in range(1, n_steps + 1):
    Z = np.random.standard_normal(n_simulations)
    prices[:, t] = prices[:, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

# Final prices
final_prices = prices[:, -1]
mean_price = np.mean(final_prices)
median_price = np.median(final_prices)
std_dev = np.std(final_prices)

# Plot
plt.hist(final_prices, bins=50, color='skyblue', edgecolor='black')
plt.axvline(mean_price, color='red', linestyle='--', label=f'Mean: {mean_price:.2f} PLN/m²')
plt.axvline(median_price, color='green', linestyle='--', label=f'Median: {median_price:.2f} PLN/m²')
plt.title("Monte Carlo Simulation\nPrimary Market Housing Price (3-Year Forecast)")
plt.xlabel("Price per m² [PLN]")
plt.ylabel("Number of Scenarios")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
