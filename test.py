from RDSDatabaseConnector import RDSDatabaseConnector
from DataFrameTransformNull import DataFrameTransformNull
from DataFrameTransformSkew import DataFrameTransformSkew
from NullPlotter import NullPlotter
from SkewPlotter import SkewPlotter


if __name__ == "__main__":
    credentials_file_path = 'credentials.yaml'
    connector = RDSDatabaseConnector(credentials_file_path)
    data = connector.extract_data_to_dataframe('customer_activity')
    
    if data is not None:
        connector.save_to_csv(data, 'customer_activity.csv')
        loaded_data = connector.load_from_csv('customer_activity.csv')
        print(loaded_data.head)
    else:
        print("Data extraction failed. Please check the credentials.")

    transformer = DataFrameTransformNull(loaded_data)
    transformed_df = transformer.drop_rows_with_high_null_proportion(threshold=0.01)
    print("\nDataFrame after dropping columns with missing values exceeding threshold:")

    numeric_columns = data.columns[:9]  # Selecting the first 9 numeric columns

    # Step 1: Identify skewed columns
    transformer = DataFrameTransformSkew(data)
    skewed_columns = transformer.identify_skewed_columns()
    print(transformer)
    # Step 2: Perform transformations on skewed columns
    transformed_data_log = data.copy()
    transformed_data_sqrt = data.copy()

    for column in skewed_columns:
        transformed_data_log = transformer.log_transform(column)
        transformed_data_sqrt = transformer.sqrt_transform(column)

    # Step 5: Save a Separate Copy of DataFrame
    data.to_csv('transformed_data.csv', index=False)