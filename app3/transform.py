import pandas as pd
def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the extracted data by performing necessary cleaning and formatting.

    Args:
        data (pd.DataFrame): The extracted data as a DataFrame.
    Returns:
        pd.DataFrame: The transformed data as a DataFrame.
    """
    # Example transformation: Remove rows with missing values
    transformed_data = data.dropna()
    
    # Example transformation: Convert column names to lowercase
    transformed_data.columns = [col.lower() for col in transformed_data.columns]
    
    return transformed_data