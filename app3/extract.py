import pandas as pd
from pathlib import Path


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.
    Returns:
        pd.DataFrame: The extracted data as a DataFrame.
    """
    # Check if the file exists
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Read the CSV file into a DataFrame
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")