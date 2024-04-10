import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self, credentials_file_path):
        self._credentials = self._load_credentials(credentials_file_path)
        self._engine = self._create_database_engine()

    def _load_credentials(self, credentials_file_path):
        try:
            with open(credentials_file_path, 'r') as file:
                credentials = yaml.safe_load(file)
            return credentials
        except Exception as e:
            print(f"Error loading credentials from {credentials_file_path}: {e}")
            return None

    def _create_database_engine(self):
        if self._credentials:
            host = self._credentials.get('RDS_HOST')
            port = self._credentials.get('RDS_PORT')
            database = self._credentials.get('RDS_DATABASE')
            user = self._credentials.get('RDS_USER')
            password = self._credentials.get('RDS_PASSWORD')
            return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
        else:
            return None

    def extract_data_to_dataframe(self, table_name):
        if self._engine:
            query = f'SELECT * FROM {table_name}'
            df = pd.read_sql_query(query, self._engine)
            return df
        else:
            return None

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def load_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df
