"""Data validation examples using Python dataclasses.

Run:
	python 01-datavalidations.py
"""

from dataclasses import dataclass, field
from typing import List, Any, Dict
import re


class ValidationError(ValueError):
	"""Raised when a dataclass fails validation."""


@dataclass
class Address:
	street: str
	city: str
	zip_code: str

	def __post_init__(self) -> None:
		if not isinstance(self.street, str) or not self.street.strip():
			raise ValidationError("street must be a non-empty string")
		if not isinstance(self.city, str) or not self.city.strip():
			raise ValidationError("city must be a non-empty string")
		if not isinstance(self.zip_code, str) or not re.fullmatch(r"\d{5}", self.zip_code):
			raise ValidationError("zip_code must be exactly 5 digits")


@dataclass
class User:
	name: str
	age: int
	email: str
	address: Address
	tags: List[str] = field(default_factory=list)

	def __post_init__(self) -> None:
		if not isinstance(self.name, str) or not self.name.strip():
			raise ValidationError("name must be a non-empty string")
		if not isinstance(self.age, int) or not (0 <= self.age <= 120):
			raise ValidationError("age must be int between 0 and 120")
		if not isinstance(self.email, str) or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", self.email):
			raise ValidationError("email must be a valid email address")
		if not isinstance(self.tags, list) or any(not isinstance(t, str) or not t.strip() for t in self.tags):
			raise ValidationError("tags must be a list of non-empty strings")

	@classmethod
	def from_dict(cls, data: Dict[str, Any]) -> "User":
		addr = data.get("address", {}) or {}
		address = Address(
			street=addr.get("street", ""),
			city=addr.get("city", ""),
			zip_code=addr.get("zip_code", ""),
		)
		return cls(
			name=data.get("name", ""),
			age=data.get("age", 0),
			email=data.get("email", ""),
			address=address,
			tags=data.get("tags", []),
		)


def main() -> None:
	good = {
		"name": "Alice",
		"age": 30,
		"email": "alice@example.com",
		"address": {"street": "123 Main St", "city": "Metropolis", "zip_code": "12345"},
		"tags": ["admin", "user"],
	}

	bad = {
		"name": "",
		"age": 200,
		"email": "not-an-email",
		"address": {"street": "", "city": "", "zip_code": "abc"},
		"tags": ["", 123],
	}

	print("Creating good user...")
	u = User.from_dict(good)
	print("Success:", u)

	print("\nCreating bad user (expected failures)...")
	try:
		User.from_dict(bad)
	except ValidationError as e:
		print("Validation failed:", e)


if __name__ == "__main__":
	main()

