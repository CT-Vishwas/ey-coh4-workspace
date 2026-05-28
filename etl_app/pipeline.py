import logging
from pathlib import Path
from typing import Dict
from .config import ETLConfig
from .utils import setup_logging
from .extract import extract_data


def run_etl(config: ETLConfig) -> Dict[str, int]:
    setup_logging(config.log_level)
    logging.info("Starting ETL pipeline")

    # Extract
    logging.info(f"Extracting data from {config.source_path} as {config.source_type}")
    app__inventory_data = extract_data(config.source_path, config.source_type)

    logging.info("ETL pipeline finished")
    return {
        "loaded_records": len(transformed),
        "report_path": str(config.report_path),
    }


def build_default_config() -> ETLConfig:
    root = Path.cwd()
    return ETLConfig(
        source_path=root / "etl_app" / "data" / "source.csv",
        destination_path=root / "etl_app" / "data" / "destination.csv",
        report_path=root / "etl_app" / "reports" / "summary_report.csv",
    )
