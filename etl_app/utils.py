import csv
import json
import logging
from pathlib import Path
from typing import Any, Dict


def setup_logging(log_level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )


def mkdir_p(path: Path) -> None:
    """Create directories recursively if they do not exist."""
    path.mkdir(parents=True, exist_ok=True)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_csv(path: Path, rows: Any, fieldnames: Any) -> None:
    mkdir_p(path.parent)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def safe_cast(value: Any, data_type: Any, default: Any = None) -> Any:
    try:
        return data_type(value)
    except (TypeError, ValueError):
        return default


def chunked(iterable, size: int):
    """Split an iterable into fixed-size chunks."""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) >= size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
