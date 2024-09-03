from dotenv import load_dotenv
from datetime import datetime, timedelta
import os


# Load enviroment variables from .env
load_dotenv()


def get_credentials() -> dict:
    
    host = os.getenv("REDSHIFT_HOST")
    user = os.getenv("REDSHIFT_USER")
    pwd = os.getenv("REDSHIFT_PASSWORD")
    port = os.getenv("REDSHIFT_PORT")
    database = os.getenv("REDSHIFT_DB")
    
    return {
        "host": host,
        "user": user,
        "pwd": pwd,
        "port": port,
        "database": database
    }
    
def get_defaultairflow_args():
    return {
        "owner": "jonatas_fg",
        "depends_on_past": False,
        "start_date": datetime(2024,8,1),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "catch"
        "retry_delay": timedelta(minutes=5)
    }