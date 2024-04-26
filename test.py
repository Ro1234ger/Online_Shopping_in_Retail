from RDSDatabaseConnector import RDSDatabaseConnector
from DataFrameTransformNull import DataFrameTransformNull
from DataFrameTransformSkew import DataFrameTransformSkew
from CorrelationManager import CorrelationManager


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
    transformed_df = transformer.drop_rows_with_high_null_proportion(threshold=0)
    print("\nDataFrame after dropping columns with missing values exceeding threshold:")

    # Step 1: Identify skewed columns
    transformer = DataFrameTransformSkew(transformed_df)
    skewed_columns = transformer.identify_skewed_columns(threshold=0.5)
    for column in skewed_columns:
        transformed_df = transformer.log_transform(transformed_df, column)

    # Step 2: Visualize the skewness after transformation
    # transformer.visualize_skew()

    # Step 3: Visulaise the correlation matrix
    correlation_manager = CorrelationManager(transformed_df)
    correlation_manager.visualize_correlation_matrix()
    
    # Step 4: Drop highly correlated columns
    df_after_dropping, dropped_columns = correlation_manager.drop_highly_correlated_columns(threshold=0.7)
    print("Highly correlated columns removed:", dropped_columns)