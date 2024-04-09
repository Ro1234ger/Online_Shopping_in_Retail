## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)

## Description
The RDSDatabaseConnector is a Python class that facilitates the extraction of data from an RDS database, saving it to a local CSV file, and loading it back into a DataFrame for analysis.

### Aim
The aim of this project is to provide a convenient way to interact with an RDS database, allowing users to easily extract and manipulate data for exploratory data analysis (EDA) tasks.

### What I Learned
- How to use SQLAlchemy to connect to a PostgreSQL database.
- How to use Pandas to extract data from a database into a DataFrame.
- How to save data to a CSV file and load it back into a DataFrame.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RDSDatabaseConnector.git

### Usage
from RDSDatabaseConnector import RDSDatabaseConnector
   ```bash
   # Load credentials from credentials.yaml
   credentials = RDSDatabaseConnector.load_credentials('credentials.yaml')

   # Create RDSDatabaseConnector instance
   connector = RDSDatabaseConnector(credentials)

   # Extract data from the 'customer_activity' table
   data = connector.extract_data_to_dataframe('customer_activity')

   # Save data to a CSV file
   connector.save_to_csv(data, 'customer_activity.csv')

   # Load data from the CSV file into a DataFrame
   loaded_data = connector.load_from_csv('customer_activity.csv')

   # Print the loaded data to check
   print(loaded_data.head())
   ```

### File Structure
1. README.md
2. db_utils.py
3. credentials.yaml
4. requirements.txt
