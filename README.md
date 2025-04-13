
# MLMC Housing Price in Poland Forecast

This project uses the **Multilevel Monte Carlo (MLMC)** method to forecast residential real estate prices in Poland over a 3-year period. It compares MLMC with the traditional Monte Carlo (MC) method in terms of accuracy and computational efficiency.

---

## Goal

To simulate future prices of residential properties in Poland (both new and secondary market) using stochastic models and compare:

* Monte Carlo simulation
* Multilevel Monte Carlo (MLMC)

---

## Data Source

The data used in this project comes from official government statistics:

**Główny Urząd Statystyczny (GUS)** - Main Statistical Office of Poland

> File: `<span>obrot_nieruchomosciami_w_2023_r_003.xlsx</span>`

Key tables used:

* `<span>Tabl_8</span>`: Primary market (new flats) — transaction value & usable area
* `<span>Tabl_10</span>`: Secondary market (used flats) — transaction value & usable area

Based on this data, we computed the average price per square meter in 2023:

| Market           | Avg. Price (2023) |
| ---------------- | ----------------- |
| Primary market   | 8,154.72 PLN/m²  |
| Secondary market | 7,675.59 PLN/m²  |

---

## Methodology

I modeled future prices using **Geometric Brownian Motion (GBM)** and ran simulations with:

### Monte Carlo

* 10,000 simulations
* Monthly time steps over 3 years

### MLMC

* Levels 0 to 4
* Decreasing number of simulations at higher levels
* Combined estimates using level differences

---

## Results

### Forecasted average price in 3 years:

| Method      | Market    | Forecast Price   |
| ----------- | --------- | ---------------- |
| Monte Carlo | Primary   | 9,151.32 PLN/m² |
| MLMC        | Primary   | 9,221.77 PLN/m² |
| Monte Carlo | Secondary | 8,404.22 PLN/m² |
| MLMC        | Secondary | 8,301.14 PLN/m² |

---

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run simulations:

```
python src/monte_carlo.py
python src/mlmc.py
```

3. Explore interactive version in Jupyter:

```
jupyter notebook notebooks/mlmc_simulation.ipynb
```

---

## References

* [GUS - Main Statistical Office of Poland](https://stat.gov.pl/)
* Mike Giles: *Multilevel Monte Carlo methods* (2008)
* [Wikipedia: Geometric Brownian Motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)

---

## About

This project was created as a short 1-2 day portfolio demonstration combining real-world housing data with advanced simulation techniques.

> Author: Agata Dąbrowska
> License: MIT
>
