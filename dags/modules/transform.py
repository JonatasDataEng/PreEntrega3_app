import json
import pandas as pd
from datetime import datetime

def pre_processing_data(exec_date, path):
    
    ### 1. Convert raw_data .json to pd.DataFrame

    date = datetime.strptime(exec_date, '%Y-%m-%d %H')
    raw_data_path = (
        f"{path}/raw_data/{date.year}-{date.month}-{date.day}-{date.hour}_raw_data.json"
    )
    
    with open(raw_data_path, 'r') as f:
        raw_data = json.load(f)
    
    # Create Data List
    name = []
    symbol = []
    date_collected = []
    time_collected = []
    market_cap = []
    price = []
    volume_24h = []
    circulating_supply = []
    total_supply = []
    
    # Timestamp
    today_date = pd.Timestamp.today().strftime('%d/%m/%Y')
    current_time = pd.Timestamp.now().tz_localize('UTC').tz_convert('America/Argentina/Buenos_Aires').strftime('%H:%M:%S %Z')
        
    for coin in raw_data['data']:
        name.append(coin['name'])
        symbol.append(coin['symbol'])
        date_collected.append(today_date)
        time_collected.append(current_time)
        market_cap.append(coin['quote']['USD']['market_cap'])
        price.append(coin['quote']['USD']['price'])
        volume_24h.append(coin['quote']['USD']['volume_24h'])
        circulating_supply.append(coin['circulating_supply'])
        total_supply.append(coin['total_supply'])
            
        # Create dictionary to insert data
        coin_dict = {
            "name": name,
            "symbol": symbol,
            "date_collected": date_collected,
            "time_collected": time_collected,
            "market_cap": market_cap,
            "price": price,
            "volume_24h": volume_24h,
            "circulating_supply": circulating_supply,
            "total_supply": total_supply
        }
        
        # Convert dictionary to DataFrame
        df = pd.DataFrame(coin_dict, columns=["name", "symbol", "date_collected", "time_collected", "market_cap", "price", "volume_24h", "circulating_supply", "total_supply"])
        print("Data structured on dataframe")
        print(df.head())
        
        ### 2. Pre-Processing Data
        
        # 1. Check if DataFrame is empty
    if df.empty:
        print("\nDataFrame empty. Finishing execution")
        return False
    
    # 2. Check data type
    # Convert numerical columns to float
    numerical_columns = [
    "market_cap", "price", "volume_24h", "circulating_supply", 
    "total_supply"
]
    
    for col in numerical_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # Convert date columns to datetime
    df['date_collected'] = pd.to_datetime(df['date_collected'], errors='coerce', dayfirst=True).dt.strftime('%d/%m/%Y')
    df['time_collected'] = pd.to_datetime(df['time_collected'], errors='coerce').dt.tz_convert('America/Argentina/Buenos_Aires').dt.strftime('%H:%M:%S %Z')
        
        
    # 3. Remove Invalid data
    
    # Remove duplicated data
    df.drop_duplicates(inplace=True)
    
    # Remove negative values
    for col in ["market_cap", "price", "volume_24h", "circulating_supply", "total_supply"]:
        df = df[(df[col] >= 0)]
        
    # Remove invalid datetime
    df.dropna(subset=['date_collected', 'time_collected'], inplace=True)
    
    # Normalize strings
    # Remover espaços em branco extras e converter para caixa baixa
    df['name'] = df['name'].str.strip().str.lower()
    df['symbol'] = df['symbol'].str.strip().str.upper()
    
    # Remove null data
    df.dropna(inplace=True)
    
    # 4. Round numerical values
    for col in numerical_columns:
        df[col] = df[col].round(2)
        
    df_cleaned = df
        
    # Print cleaned data
    print("\nDataFrame checked and cleaned")
    print(df_cleaned.head())
    
    # Load processed data
    processed_data_path = (
        f"{path}/processed_data/{date.year}-{date.month}-{date.day}-{date.hour}_processed_data.parquet"
    )
    
    df_cleaned.to_parquet(processed_data_path, index=False)
    
    print(f"Data transformed and saved to {processed_data_path}")