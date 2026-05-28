from datetime import datetime
from typing import Any, Dict, Iterable, List


def normalize_date(value: str, input_format: str = "%Y-%m-%d", output_format: str = "%Y-%m-%d") -> str:
    try:
        return datetime.strptime(value, input_format).strftime(output_format)
    except (TypeError, ValueError):
        return value


def clean_record(record: Dict[str, Any]) -> Dict[str, Any]:
    cleaned = {k: (v.strip() if isinstance(v, str) else v) for k, v in record.items()}
    if "date" in cleaned:
        cleaned["date"] = normalize_date(cleaned.get("date", ""))
    return cleaned


def apply_business_rules(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    transformed = []
    for record in records:
        cleaned = clean_record(record)
        if cleaned.get("status", "").lower() in {"active", "completed", "approved", "true"}:
            transformed.append(cleaned)
    return transformed


def transform_data(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return apply_business_rules(records)
