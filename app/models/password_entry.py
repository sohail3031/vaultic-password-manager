from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class PasswordEntry:
    site_name: str
    username: str
    password: str
    id: Optional[int] = None
    notes: Optional[str] = None
    category: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        return asdict(self)
