import pandas as pd
import sqlalchemy as sa
from .utils import get_credentials
from .DataConn import DataConn


def load_data(exec_date, path):
    
    timestamp = datetime.strftime(exec_date, '%Y-%m-%d %H')
    print(f"Cargando la data para la fecha: {timestamp}")
    
    processed_data_path = (
        f"{path}/processed_data/{timestamp.year}-{timestamp.month}-{timestamp.day}-{timestamp.hour}_processed_data.parquet"
    )
    
    df = pd.read_parquet(processed_data_path)
    
    print(df.sample(5))
    
    
    # Get engine connection
    credentials = get_credentials()
    
    engine = DataConn(credentials)
    
    table_name = f"{timestamp.year}-{timestamp.month}-{timestamp.day}-{timestamp.hour}_processed_data"
    
    # Load data on data warehouse Amazon Redshift
    try:
        df.reset_index(drop=True, inplace=True)
        
        with engine.connect() as connection:
            connection.execute(f"DROP TABLE IF EXISTS {table_name};")
        
        df.to_sql(
            table_name,
            engine,
            index=False,
            if_exists='replace',
        )
        
        print('Data loaded on Amazon Redshift')
        
    except sa.exc.SQLAlchemyError as e:
        print(f"Error occurred while loading the data: {e}")
        
    except Exception as e:
        print(e)
        
    finally:
        # Closing connection
        if hasattr(engine, 'dispose'):
            engine.dispose()
        elif hasattr(engine, 'close'):
            engine.close()
        print('Data warehouse connection closed successfully')