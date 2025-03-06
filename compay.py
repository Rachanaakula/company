import pandas as pd
import matplotlib.pyplot as plt

# Load sales data (Assuming a CSV file with columns: Date, Product, Sales, Region)
def load_sales_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

# Calculate total sales
def total_sales(df):
    return df['Sales'].sum()

# Sales trend over time
def sales_trend(df):
    df['Month'] = df['Date'].dt.to_period('M')
    trend = df.groupby('Month')['Sales'].sum()
    trend.plot(title='Monthly Sales Trend', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()
    return trend

# Top-selling products
def top_selling_products(df, top_n=5):
    return df.groupby('Product')['Sales'].sum().nlargest(top_n)

# Sales by region
def sales_by_region(df):
    return df.groupby('Region')['Sales'].sum()

# Main function to run analysis
def analyze_sales(file_path):
    df = load_sales_data(file_path)
    print("Total Sales:", total_sales(df))
    print("\nTop Selling Products:\n", top_selling_products(df))
    print("\nSales by Region:\n", sales_by_region(df))
    print("\nSales Trend:")
    sales_trend(df)

# Example usage (update with actual file path)

# analyze_sales('sales_data.csv')
