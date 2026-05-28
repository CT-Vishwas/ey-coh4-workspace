import csv
import tempfile
from pathlib import Path

from etl_app.config import ETLConfig
from etl_app.pipeline import run_etl


def test_run_etl_creates_output_files(tmp_path: Path) -> None:
    source_file = tmp_path / "source.csv"
    destination_file = tmp_path / "destination.csv"
    report_file = tmp_path / "summary_report.csv"

    rows = [
        {"id": "1", "name": "Alice", "status": "Active", "date": "2024-01-01"},
        {"id": "2", "name": "Bob", "status": "inactive", "date": "2024-01-02"},
    ]
    with source_file.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "name", "status", "date"])
        writer.writeheader()
        writer.writerows(rows)

    config = ETLConfig(
        source_path=source_file,
        destination_path=destination_file,
        report_path=report_file,
        source_type="csv",
        destination_type="csv",
        report_type="csv",
    )

    result = run_etl(config)

    assert destination_file.exists()
    assert report_file.exists()
    assert result["loaded_records"] == 1
    assert "report_path" in result
