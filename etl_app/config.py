import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ETLConfig:
    source_path: Path
    destination_path: Path
    report_path: Path
    log_level: str = "INFO"
    chunk_size: int = 500
    source_type: str = "csv"
    destination_type: str = "csv"
    report_type: str = "summary"


def load_config(config_path: Optional[str] = None) -> ETLConfig:
    """Load ETL configuration from environment variables or a config file."""
    root = Path(config_path or os.getcwd())
    source_path = Path(os.getenv("ETL_SOURCE_PATH", root / "data" / "source.csv"))
    destination_path = Path(os.getenv("ETL_DESTINATION_PATH", root / "data" / "destination.csv"))
    report_path = Path(os.getenv("ETL_REPORT_PATH", root / "reports" / "summary_report.csv"))
    log_level = os.getenv("ETL_LOG_LEVEL", "INFO")
    chunk_size = int(os.getenv("ETL_CHUNK_SIZE", "500"))
    source_type = os.getenv("ETL_SOURCE_TYPE", "csv")
    destination_type = os.getenv("ETL_DESTINATION_TYPE", "csv")
    report_type = os.getenv("ETL_REPORT_TYPE", "summary")

    return ETLConfig(
        source_path=source_path,
        destination_path=destination_path,
        report_path=report_path,
        log_level=log_level,
        chunk_size=chunk_size,
        source_type=source_type,
        destination_type=destination_type,
        report_type=report_type,
    )
