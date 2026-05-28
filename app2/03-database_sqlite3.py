import sqlite3
from dataclasses import dataclass
from typing import Optional, List


DB_PATH = "app2.sqlite3"


@dataclass
class User:
    id: Optional[int]
    name: str
    email: str


def get_conn(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(path: str = DB_PATH) -> None:
    """Create users table if not exists."""
    with get_conn(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """
        )


def create_user(name: str, email: str, path: str = DB_PATH) -> int:
    """Insert a user and return the new id."""
    with get_conn(path) as conn:
        cur = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
        )
        return cur.lastrowid


def get_user(user_id: int, path: str = DB_PATH) -> Optional[User]:
    with get_conn(path) as conn:
        cur = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        if row:
            return User(id=row["id"], name=row["name"], email=row["email"])
        return None


def list_users(path: str = DB_PATH) -> List[User]:
    with get_conn(path) as conn:
        cur = conn.execute("SELECT id, name, email FROM users ORDER BY id")
        return [User(id=r["id"], name=r["name"], email=r["email"]) for r in cur.fetchall()]


def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None, path: str = DB_PATH) -> bool:
    """Update provided fields. Returns True if a row was updated."""
    fields = []
    params = []
    if name is not None:
        fields.append("name = ?")
        params.append(name)
    if email is not None:
        fields.append("email = ?")
        params.append(email)
    if not fields:
        return False
    params.append(user_id)
    with get_conn(path) as conn:
        cur = conn.execute(f"UPDATE users SET {', '.join(fields)} WHERE id = ?", params)
        return cur.rowcount > 0


def delete_user(user_id: int, path: str = DB_PATH) -> bool:
    with get_conn(path) as conn:
        cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return cur.rowcount > 0


if __name__ == "__main__":
    # simple demo
    init_db()
    print("Creating users...")
    alice_id = create_user("Alice", "alice@example.com")
    bob_id = create_user("Bob", "bob@example.com")
    print("Users:", list_users())
    print("Get Alice:", get_user(alice_id))
    update_user(bob_id, email="robert@example.com")
    print("After update:", list_users())
    delete_user(alice_id)
    print("Final:", list_users())
