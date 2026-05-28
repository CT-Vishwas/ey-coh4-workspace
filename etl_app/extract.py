import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterator, List


def extract_csv(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [dict(row) for row in reader]


def extract_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_data(source_path: Path, source_type: str = "csv") -> Any:
    if source_type.lower() == "json":
        return extract_json(source_path)
    return extract_csv(source_path)


def stream_csv(path: Path) -> Iterator[Dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield dict(row)
