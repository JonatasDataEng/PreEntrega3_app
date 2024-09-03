import json
import os
import pandas as pd
from requests import Session
from requests.exceptions import RequestException
from datetime import datetime
from modules.config_api import config_api

def extract_data_from_api(exec_date, path):
    # Verifica se exec_date é um datetime, caso contrário, converte
    if not isinstance(exec_date, datetime):
        raise ValueError("exec_date deve ser um objeto datetime")

    # API Parameters
    parameters = {
        'start': config_api['start'],
        'limit': config_api['limit'],
        'convert': config_api['currency']
    }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config_api['api_key']
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
        response = session.get(config_api['api_url'], params=parameters)
        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP de erro
        data = response.json()
        
        date = datetime.strptime(exec_date, "%Y-%m-%d %H")
        raw_data_path = (
            f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.json"
        )

        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)

        with open(raw_data_path, 'w') as f:
            json.dump(data, f)

        print(f"Data extracted and saved to {raw_data_path}")
        
    except RequestException as e:
        print(f"Request error: {e}")
        raise
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        raise
    except Exception as e:
        print(f"Error during data extraction: {e}")
        raise