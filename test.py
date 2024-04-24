from RDSDatabaseConnector import RDSDatabaseConnector
from DataFrameTransformNull import DataFrameTransformNull
from DataFrameTransformSkew import DataFrameTransformSkew
from NullPlotter import NullPlotter


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

    numeric_columns = transformed_df.columns[:9]  # Selecting the first 9 numeric columns

    # Step 1: Identify skewed columns
    transformer = DataFrameTransformSkew(transformed_df)
    transformer.identify_skewed_columns(threshold=0.5)
    transformer.log_transform()

    # Step 2: Visualize the skewness after transformation
    transformer.visualize_skew()

    # Step 3: Save a Separate Copy of DataFrame
    transformer.to_csv('transformed_data.csv', index=False)