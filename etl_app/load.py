import csv
from pathlib import Path
from typing import Any, Dict, Iterable, List


def load_to_csv(path: Path, records: Iterable[Dict[str, Any]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def load_data(destination_path: Path, records: Iterable[Dict[str, Any]], destination_type: str = "csv") -> None:
    if destination_type.lower() == "csv":
        records = list(records)
        fieldnames = list(records[0].keys()) if records else []
        load_to_csv(destination_path, records, fieldnames)
    else:
        raise NotImplementedError(f"Destination type '{destination_type}' is not yet supported.")
