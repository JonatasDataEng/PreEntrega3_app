import sqlalchemy as sa
import pandas as pd
import psycopg2


def DataConn(user_credentials):
    
    user = user_credentials['user']
    password = user_credentials['pwd']
    host = user_credentials['host']
    port = user_credentials['port']
    database = user_credentials['database']
    
    connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    
    try:
        engine = sa.create_engine(connection_url)
    except sa.exc.SQLAlchemyError as e:
        print(f"Failed to create connection: {e}")
        
    return engine