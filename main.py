from RDSDatabaseConnector import RDSDatabaseConnector
from DataFrameTransformNull import DataFrameTransformNull
from DataFrameInfo import DataFrameInfo
from NullPlotter import NullPlotter
from DataFrameTransformSkew import DataFrameTransformSkew
from CorrelationManager import CorrelationManager

if __name__ == "__main__":
    credentials_file_path = 'credentials.yaml'
    connector = RDSDatabaseConnector(credentials_file_path)
    data = connector.extract_data_to_dataframe('customer_activity')
    
    if data is not None:
        connector.save_to_csv(data, 'customer_activity.csv')
        loaded_data = connector.load_from_csv('customer_activity.csv')
        print(loaded_data.head())
    else:
        print("Data extraction failed. Please check the credentials.")

    # Create an instance of DataFrameInfo
    df_info = DataFrameInfo(loaded_data)

    # Describe all columns in the DataFrame
    print("Column Descriptions:")
    print(df_info.describe_columns())

    # Extract statistical values
    print("\nStatistics:")
    print(df_info.extract_statistics())

    # Count distinct values in categorical columns
    print("\nDistinct Values in Categorical Columns:")
    print(df_info.count_distinct_values())

    # Print out the shape of the DataFrame
    print("\nDataFrame Shape:")
    print(df_info.print_shape())

    # Generate count/percentage count of values in each column
    print("\nValue Counts with Percentages:")
    print(df_info.generate_value_counts())

    # Create an instance of DataFrameTransform for Null
    transformer = DataFrameTransformNull(loaded_data)

    # Determine the percentage of missing values in each column
    missing_percentage = transformer.missing_values_percentage()
    print("Percentage of missing values in each column:")
    print(missing_percentage)

    # Drop columns with missing values exceeding a threshold
    transformed_df = transformer.drop_rows_with_high_null_proportion(threshold=0.01)
    print("\nDataFrame after dropping columns with missing values exceeding threshold:")
    transformed_df.to_csv("drop_null_data.csv", index=False)
    print("Transformed data saved to 'transformed_data.csv'.")

    # Create an instance of Plotter
    plotter = NullPlotter(transformed_df)

    # Visualize the removal of missing values
    plotter.visualize_removal_of_values(loaded_data, transformed_df)

    #******************************************************************************************#
    # Skew analysis
    numeric_columns = transformed_df.columns[:9]  # Selecting the first 9 numeric columns

    # Step 1: Identify skewed columns
    transformer = DataFrameTransformSkew(transformed_df)
    transformer.identify_skewed_columns(threshold=0.3)
    transformer.log_transform()

    # Step 2: Visualize the skewness after transformation
    transformer.visualize_skew()

    # Step 3: Visualize the correlation matrix
    correlation_manager = CorrelationManager(transformed_df)
    correlation_manager.visualize_correlation_matrix()
    
    # Step 4: Drop highly correlated columns
    df_after_dropping, dropped_columns = correlation_manager.drop_highly_correlated_columns(threshold=0.8)
    print("Highly correlated columns removed:", dropped_columns)
    
    # Save the transformed data to a new CSV file
    df_after_dropping.to_csv("transformed_data.csv", index=False)
    print("Transformed data saved to 'transformed_data.csv'.")