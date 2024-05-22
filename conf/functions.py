import sqlite3
import conf.config as config

def db_connect():
    return sqlite3.connect(config.DATABASE_PATH)


def create_table():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        );
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                date DATE
            );
        """)

    conn.commit()
    conn.close()

create_table()


def get_categories():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    return cursor.fetchall()