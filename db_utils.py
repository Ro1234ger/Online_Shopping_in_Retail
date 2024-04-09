import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_credentials(credentials):
    with open(credentials, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.port = credentials['RDS_PORT']
        self.database = credentials['RDS_DATABASE']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.engine = self.create_engine()

    def create_engine(self):
        engine = create_engine(f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
        return engine

    def extract_data_to_dataframe(self, table_name):
        query = f'SELECT * FROM {table_name}'
        df = pd.read_sql_query(query, self.engine)
        return df

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def load_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df

# Load credentials from credentials.yaml
credentials = load_credentials('credentials.yaml')

# Create RDSDatabaseConnector instance
connector = RDSDatabaseConnector(credentials)

# Extract data from the 'customer_activity' table
data = connector.extract_data_to_dataframe('customer_activity')

# Save data to a CSV file
connector.save_to_csv(data, 'customer_activity.csv')

# Load data from the CSV file into a DataFrame
loaded_data = connector.load_from_csv('customer_activity.csv')

# Print the loaded data
print(loaded_data.head())