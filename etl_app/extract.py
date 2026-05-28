import pandas as pd
from pathlib import Path


def extract_data(source_path: Path, source_type: str = "csv") -> pd.DataFrame:
    """Extract data from the source path based on the specified type."""
    if source_type == "csv":
        return pd.read_csv(source_path)
    elif source_type == "json":
        return pd.read_json(source_path)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")