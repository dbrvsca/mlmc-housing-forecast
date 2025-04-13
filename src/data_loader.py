import pandas as pd

def load_and_clean_table(filepath, sheet_name, skiprows=4):
    df = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows)
    df.columns = ['Category', 'Number of Properties', 'Value (thousands PLN)', 'Usable Area (m2)']
    df = df.dropna(subset=['Value (thousands PLN)', 'Usable Area (m2)'])
    df['Value (thousands PLN)'] = pd.to_numeric(df['Value (thousands PLN)'], errors='coerce')
    df['Usable Area (m2)'] = pd.to_numeric(df['Usable Area (m2)'], errors='coerce')
    return df

def calculate_avg_price_per_m2(df):
    total_value_pln = df['Value (thousands PLN)'].sum() * 1000
    total_area = df['Usable Area (m2)'].sum()
    return total_value_pln / total_area

if __name__ == "__main__":
    filepath = "data/obrot_nieruchomosciami_w_2023_r_003.xlsx"

    # Load and clean primary market data
    df_primary = load_and_clean_table(filepath, sheet_name="Tabl_8")
    avg_primary = calculate_avg_price_per_m2(df_primary)
    print(f"Primary market average price per m²: {avg_primary:.2f} PLN")

    # Load and clean secondary market data
    df_secondary = load_and_clean_table(filepath, sheet_name="Tabl_10")
    avg_secondary = calculate_avg_price_per_m2(df_secondary)
    print(f"Secondary market average price per m²: {avg_secondary:.2f} PLN")