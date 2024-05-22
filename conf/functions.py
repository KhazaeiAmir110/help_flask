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
                image_url TEXT NOT NULL,
                description TEXT NOT NULL,
                category_id INTEGER NOT NULL,
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

def get_categories_by_id(id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM categories WHERE id = '{id}'")
    return cursor.fetchone()

def get_articles():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles ORDER BY date DESC")
    return cursor.fetchall()

def get_article_with_category_id(category_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM articles WHERE id = '{category_id}'")
    return cursor.fetchall()

def get_article_with_search(searched_word):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM articles WHERE name LIKE '%{searched_word}%' OR description LIKE '%{searched_word}%'"
    )
    results = cursor.fetchall()

    if not results:
        return None
    else:
        return results


def get_article_by_id(article_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM articles WHERE id = '{article_id}'"
    )
    result = cursor.fetchone()
    if not result:
        return None
    else:
        return result