import sqlite3
from pathlib import Path


class Database:
    def __init__(self) -> None:
        self.DATA_FOLDER = Path(__file__).parent.parent.parent / "data"
        self.DB_PATH = self.DATA_FOLDER / "vault.db"

    def ensure_data_folder_exists(self) -> None:
        self.DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    def get_connection(self):
        self.ensure_data_folder_exists()

        return sqlite3.connect(self.DB_PATH)

    def initialize_database(self) -> None:
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
                    CREATE TABLE IF NOT EXISTS password_entries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        site_name TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        notes TEXT,
                        category TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """
        )

        connection.commit()
        connection.close()
