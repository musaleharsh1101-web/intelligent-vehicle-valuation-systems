import sqlite3
from pathlib import Path

import pandas as pd


DATABASE_PATH = Path(__file__).resolve().parent / "autovalue.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialise_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS valuations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                customer_name TEXT NOT NULL,
                customer_mobile TEXT,
                customer_city TEXT,
                brand TEXT NOT NULL,
                year INTEGER,
                km_driven INTEGER,
                fuel TEXT,
                transmission TEXT,
                estimated_price REAL NOT NULL
            )
            """
        )


def save_valuation(details):
    initialise_database()
    columns = [
        "customer_name", "customer_mobile", "customer_city", "brand", "year",
        "km_driven", "fuel", "transmission", "estimated_price",
    ]
    with get_connection() as connection:
        cursor = connection.execute(
            f"INSERT INTO valuations ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})",
            [details.get(column) for column in columns],
        )
        return cursor.lastrowid


def get_valuations(limit=None):
    initialise_database()
    query = "SELECT * FROM valuations ORDER BY datetime(created_at) DESC, id DESC"
    if limit:
        query += " LIMIT ?"
        return pd.read_sql_query(query, get_connection(), params=[limit])
    return pd.read_sql_query(query, get_connection())
