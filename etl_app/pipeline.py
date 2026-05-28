import logging
from pathlib import Path
from typing import Iterable, List, Dict

from .config import ETLConfig
from .extract import extract_data, stream_csv
from .load import load_data
from .reporting import generate_summary_report
from .transform import transform_data
from .utils import setup_logging


def run_etl(config: ETLConfig) -> Dict[str, int]:
    setup_logging(config.log_level)
    logging.info("Starting ETL pipeline")

    if config.source_type.lower() == "csv":
        raw_data = stream_csv(config.source_path)
    else:
        raw_data = extract_data(config.source_path, config.source_type)

    transformed = transform_data(raw_data)
    transformed = list(transformed)

    if transformed:
        fieldnames = list(transformed[0].keys())
    else:
        fieldnames = []

    load_data(config.destination_path, transformed, config.destination_type)

    if config.report_type == "csv":
        generate_summary_report(transformed, config.report_path)
    else:
        generate_summary_report(transformed, config.report_path)

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
