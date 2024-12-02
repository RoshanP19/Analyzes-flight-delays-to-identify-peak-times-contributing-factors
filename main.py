import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data(file_path):
    df = pd.read_csv(file_path)  # Assume CSV format for simplicity
    return df

# Preprocess Data
def preprocess_data(df):
    # Convert columns to appropriate types
    df['FlightDate'] = pd.to_datetime(df['FlightDate'], errors='coerce')  # Handle any errors in date
    df['Delay'] = pd.to_numeric(df['Delay'], errors='coerce')
    
    # Handle missing values, for example, removing rows with too many missing values
    df = df.dropna(subset=['FlightDate', 'Delay'])
    
    # Extract date components for analysis
    df['Year'] = df['FlightDate'].dt.year
    df['Month'] = df['FlightDate'].dt.month
    df['DayOfWeek'] = df['FlightDate'].dt.dayofweek  # Monday=0, Sunday=6
    df['HourOfDay'] = df['FlightDate'].dt.hour
    
    return df

# Analysis: Peak Times (Hourly and Daily Trends)
def analyze_peak_times(df):
    # Hourly delay analysis
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='HourOfDay', y='Delay', data=df)
    plt.title("Flight Delays by Hour of the Day")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Delay (Minutes)")
    plt.show()

    # Day of the week delay analysis
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='DayOfWeek', y='Delay', data=df)
    plt.title("Flight Delays by Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Delay (Minutes)")
    plt.show()

# Analysis: Factors Contributing to Delays (Weather, Distance, Airport Size, etc.)
def analyze_contributing_factors(df):
    # Let's assume we have columns for 'Weather', 'Distance', 'AirportSize'
    # For this example, we'll just visualize a few relations

    # Example: Weather vs Delay (Assuming 'Weather' is a categorical feature)
    if 'Weather' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Weather', y='Delay', data=df)
        plt.title("Flight Delays by Weather Conditions")
        plt.xlabel("Weather")
        plt.ylabel("Delay (Minutes)")
        plt.xticks(rotation=45)
        plt.show()

    # Example: Distance vs Delay
    if 'Distance' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Distance', y='Delay', data=df)
        plt.title("Flight Delays vs Distance")
        plt.xlabel("Distance (miles)")
        plt.ylabel("Delay (Minutes)")
        plt.show()

# Main function to run the analysis
def main():
    # Load and preprocess data
    file_path = 'flight_delay_data.csv'  # Replace with your dataset file path
    df = load_data(file_path)
    df = preprocess_data(df)
    
    # Analyze Peak Times (Hourly and Daily Trends)
    analyze_peak_times(df)
    
    # Analyze Contributing Factors (Weather, Distance, etc.)
    analyze_contributing_factors(df)

if __name__ == "__main__":
    main()

