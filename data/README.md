
# Real Estate Data

This folder contains raw real estate transaction data used in the MLMC housing price forecast project.

## Source

* **Institution**: GUS – Główny Urząd Statystyczny (Central Statistical Office of Poland)
* **Website**: [https://stat.gov.pl/]()
* **File name**: `obrot_nieruchomosciami_w_2023_r_003.xlsx`

## Relevant Sheets Used:

* `Tabl_8`– Primary market transactions (new flats)
* `Tabl_10` – Secondary market transactions (used flats)

These sheets contain:

* Total transaction values (in thousands PLN)
* Total usable area (in square meters)
* Number of properties sold

The average price per square meter is computed using:
`avg_price = total_value / total_area`

The file should be placed in this folder to be correctly accessed by the data loader script.
