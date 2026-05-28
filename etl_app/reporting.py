import csv
import logging
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List


def generate_summary_report(records: Iterable[Dict[str, Any]], report_path: Path) -> Dict[str, Any]:
    rows = list(records)
    summary = {
        "total_records": len(rows),
        "fields": list(rows[0].keys()) if rows else [],
        "status_counts": Counter(row.get("status", "unknown") for row in rows),
    }
    write_summary_csv(report_path, summary)
    logging.info("Report saved to %s", report_path)
    return summary


def write_summary_csv(report_path: Path, summary: Dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value"])
        writer.writerow(["total_records", summary["total_records"]])
        writer.writerow(["fields", ",".join(summary["fields"])])
        for status, count in summary["status_counts"].items():
            writer.writerow([f"status_{status}", count])


def generate_csv_report(records: Iterable[Dict[str, Any]], report_path: Path, fieldnames: List[str]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
